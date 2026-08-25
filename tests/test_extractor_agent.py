"""Unit and Property-Based Tests for Extractor Agent Engine (Step 2.0).

Verifies PSI classification, frontmatter schema compliance, and YAML round-trip invariants.
"""

import pytest
import yaml
from hypothesis import given, strategies as st
from agents.extractor.classifier import DocumentClassifier
from agents.extractor.agent import ExtractorAgent


# ==============================================================================
# 1. Deterministic Unit Tests
# ==============================================================================

def test_ut_ext_01_datasheet_classification(tmp_path):
    """UT-EXT-01: Ingest PDF named 14780-8120-PS-0010_CONTROL VALVE.pdf."""
    agent = ExtractorAgent(output_dir=str(tmp_path))
    res = agent.process_document("14780-8120-PS-0010_CONTROL VALVE.pdf")
    assert res["status"] == "SUCCESS"
    assert res["category"] == "data_sheets"
    assert res["confidence"] >= 0.90
    assert "equipment" in res["wiki_path"] or "instruments" in res["wiki_path"]


def test_ut_ext_02_pfd_and_pid_classification(tmp_path):
    """UT-EXT-02: Test classification across PFD, P&ID, standards, and manuals."""
    classifier = DocumentClassifier()
    
    # PFD
    pfd_res = classifier.classify_document("14780-8120-25-01-0001_PFD.pdf")
    assert pfd_res.category == "pfd"
    
    # PID
    pid_res = classifier.classify_document("14780-8120-25-23-0005_PID.pdf")
    assert pid_res.category == "pid"
    
    # HAZOP Report
    haz_res = classifier.classify_document("Phenol_Unit_2016_HAZOP_Report.pdf")
    assert haz_res.category == "hazop"


def test_frontmatter_schema_validation(tmp_path):
    """Verify generated markdown contains valid, parseable YAML frontmatter."""
    agent = ExtractorAgent(output_dir=str(tmp_path))
    res = agent.process_document("14780-8120-25-23-0005_PID.pdf")
    file_path = tmp_path / res["wiki_path"]
    assert file_path.exists()
    
    content = file_path.read_text(encoding="utf-8")
    assert content.startswith("---")
    parts = content.split("---", 2)
    assert len(parts) >= 3
    fm = yaml.safe_load(parts[1])
    assert isinstance(fm, dict)
    assert "sources" in fm
    assert "tags" in fm


# ==============================================================================
# 2. Property-Based Invariant Tests (Hypothesis)
# ==============================================================================

@given(
    st.dictionaries(
        keys=st.text(alphabet="abcdefghijklmnopqrstuvwxyz_", min_size=1, max_size=16),
        values=st.one_of(
            st.text(min_size=0, max_size=32),
            st.integers(min_value=-1000, max_value=1000),
            st.floats(min_value=-1000.0, max_value=1000.0, allow_nan=False),
            st.booleans(),
            st.lists(st.text(min_size=1, max_size=16), max_size=5)
        ),
        min_size=1,
        max_size=10
    )
)
def test_pbt_fmt_01_frontmatter_roundtrip(fm_dict):
    """PBT-FMT-01: Frontmatter Round-trip Invariant: deserialize(serialize(dict)) == dict."""
    dumped = yaml.safe_dump(fm_dict, sort_keys=True)
    loaded = yaml.safe_load(dumped)
    assert loaded == fm_dict
