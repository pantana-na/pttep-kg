#!/usr/bin/env python3
"""Vertex AI Semantic Re-embedding for Cloud Spanner Equipment.

Generates authentic 768-dimensional semantic embeddings using Vertex AI text-embedding-004
via Application Default Credentials (ADC) and updates all equipment rows in Cloud Spanner.
SPEC-20260918-ZERO-MOCK-CLOUD-NATIVE-MIGRATION Section 3.3.
"""

import os
import sys
import time
from typing import List, Dict, Any
from google import genai
from google.cloud import spanner
from google.cloud.spanner_v1.param_types import Array, FLOAT64, STRING

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
REGION = os.getenv("GCP_REGION", "asia-southeast1")
INSTANCE_ID = os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
DATABASE_ID = os.getenv("SPANNER_DATABASE", "safety-db")
EMBEDDING_MODEL = "text-embedding-004"


def get_genai_client():
    return genai.Client(vertexai=True, project=PROJECT_ID, location=REGION)


def generate_embedding(client, text: str) -> List[float]:
    """Generates 768-dim embedding via Vertex AI text-embedding-004."""
    resp = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    if hasattr(resp, "embeddings") and resp.embeddings:
        return resp.embeddings[0].values
    elif hasattr(resp, "embedding") and resp.embedding:
        return resp.embedding.values
    raise ValueError(f"Unexpected response structure from embed_content: {resp}")


def reembed_all_equipment():
    print(f"=== Re-embedding Cloud Spanner Equipment with Vertex AI {EMBEDDING_MODEL} ===")
    print(f"GCP Project:  {PROJECT_ID}")
    print(f"Region:       {REGION}")
    print(f"Spanner:      {INSTANCE_ID} / {DATABASE_ID}\n")

    # 1. Initialize Clients
    genai_client = get_genai_client()
    spanner_client = spanner.Client(project=PROJECT_ID)
    instance = spanner_client.instance(INSTANCE_ID)
    database = instance.database(DATABASE_ID)

    # 2. Fetch all equipment from Cloud Spanner
    with database.snapshot() as snapshot:
        query = """
        SELECT EquipmentTag, Name, Type, DescriptionSummary
        FROM Equipment
        WHERE IsDeleted = false
        ORDER BY EquipmentTag
        """
        rows = list(snapshot.execute_sql(query))

    print(f"[FETCH] Found {len(rows)} active equipment items in Cloud Spanner.")
    if not rows:
        print("[WARNING] No equipment records found in Spanner. Aborting.")
        return

    # 3. Generate Embeddings via Vertex AI
    embedded_data = []
    t0 = time.time()
    for idx, (tag, name, eq_type, desc) in enumerate(rows, 1):
        clean_text = f"{tag} {name or ''} ({eq_type or 'Equipment'}): {desc or ''}".strip()
        print(f"  [{idx}/{len(rows)}] Generating embedding for {tag} ({name})...", end="", flush=True)
        try:
            vec = generate_embedding(genai_client, clean_text)
            embedded_data.append((tag, vec))
            print(f" OK (dim={len(vec)})")
        except Exception as e:
            print(f" FAILED: {e}")
            raise e

    elapsed = time.time() - t0
    print(f"\n[VERTEX AI] Successfully generated {len(embedded_data)} embeddings in {elapsed:.2f}s.")

    # 4. Update Spanner in batches
    print("\n[SPANNER UPDATE] Committing new 768-dim embeddings to Cloud Spanner...")

    def update_embeddings_tx(transaction):
        columns = ["EquipmentTag", "Embedding", "UpdatedAt"]
        values = [
            (tag, vec, spanner.COMMIT_TIMESTAMP)
            for tag, vec in embedded_data
        ]
        transaction.update(
            table="Equipment",
            columns=columns,
            values=values
        )

    database.run_in_transaction(update_embeddings_tx)
    print(f"[SPANNER UPDATE] Committed {len(embedded_data)} embeddings successfully.")

    # 5. Verify via live Vector Cosine Distance Query
    print("\n[VERIFICATION] Executing live Spanner vector cosine similarity query...")
    test_query = "cumene hydroperoxide decomposition reactor thermal runaway"
    test_vec = generate_embedding(genai_client, test_query)

    with database.snapshot() as snapshot:
        sql = """
        SELECT EquipmentTag, Name, Type,
               1.0 - COSINE_DISTANCE(Embedding, @query_vec) AS cosine_sim
        FROM Equipment
        WHERE Embedding IS NOT NULL AND IsDeleted = false
        ORDER BY cosine_sim DESC
        LIMIT 5
        """
        params = {"query_vec": test_vec}
        param_types = {"query_vec": Array(FLOAT64)}
        results = list(snapshot.execute_sql(sql, params=params, param_types=param_types))

    print(f"Vector search results for query: '{test_query}':")
    for r in results:
        print(f"  - Tag: {r[0]:<10} Name: {r[1]:<30} Sim: {r[3]:.4f}")

    print("\n=== Cloud Spanner Semantic Re-embedding Completed Successfully! ===")


if __name__ == "__main__":
    reembed_all_equipment()
