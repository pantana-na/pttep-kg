"""PTT GC 5x5 Risk Assessment Matrix (RAM) & LOPA Safeguard Evaluator.

Governed by PTT GC Corporate Standard W-(Q-MP)-002 R2 and SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE.
"""

from typing import Tuple, List, Dict, Any

# PTT GC 5x5 RAM Lookup Grid: rows = Severity (1..5), cols = Likelihood (1..5)
# Severity: 1=Slight, 2=Minor, 3=Local, 4=Major, 5=Extensive
# Likelihood: 1=Improbable, 2=Remote, 3=Occasional, 4=Probable, 5=Frequent
RAM_GRID = {
    5: {1: "Medium", 2: "High",   3: "High",    4: "Extreme", 5: "Extreme"},
    4: {1: "Medium", 2: "Medium", 3: "High",    4: "High",    5: "Extreme"},
    3: {1: "Low",    2: "Medium", 3: "Medium",  4: "High",    5: "High"},
    2: {1: "Low",    2: "Low",    3: "Medium",  4: "Medium",  5: "High"},
    1: {1: "Low",    2: "Low",    3: "Low",     4: "Low",     5: "Medium"},
}

RISK_RANKS = {"Low": 1, "Medium": 2, "High": 3, "Extreme": 4}


def calculate_overall_severity(people: int, env: int, econ: int, social: int) -> int:
    """Severity is the maximum across all 4 impact dimensions."""
    p = max(1, min(5, people))
    en = max(1, min(5, env))
    ec = max(1, min(5, econ))
    s = max(1, min(5, social))
    return max(p, en, ec, s)


def get_risk_rating(severity: int, likelihood: int) -> str:
    """Returns the qualitative risk rating (Low, Medium, High, Extreme) from the 5x5 RAM."""
    s = max(1, min(5, severity))
    l = max(1, min(5, likelihood))
    return RAM_GRID[s][l]


def calculate_ipl_credit(safeguard: Dict[str, Any]) -> int:
    """Computes IPL Likelihood credit reduction based on SIL rating and independence."""
    sil = safeguard.get("sil_rating", "").upper()
    is_ipl = safeguard.get("is_ipl", False) or safeguard.get("is_interlock_esd", False) or "SIL" in sil
    
    if not is_ipl:
        return 0  # Non-IPL, basic BPCS or procedural safeguards get 0 credit
        
    if "SIL 3" in sil:
        return 3
    elif "SIL 2" in sil:
        return 2
    elif "SIL 1" in sil:
        return 1
    return 1 if is_ipl else 0


def evaluate_deviation_risk(
    people: int,
    env: int,
    econ: int,
    social: int,
    initial_likelihood: int,
    safeguards: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Evaluates the 3-risk-block lifecycle for a HAZOP consequence."""
    # 1. Initial Risk Block
    severity = calculate_overall_severity(people, env, econ, social)
    l_init = max(1, min(5, initial_likelihood))
    initial_risk = get_risk_rating(severity, l_init)

    # 2. Mitigated Risk Block
    total_credits = sum(calculate_ipl_credit(sg) for sg in safeguards)
    l_mitigated = max(1, l_init - total_credits)
    mitigated_risk = get_risk_rating(severity, l_mitigated)

    # 3. Recommendation requirement
    action_required = RISK_RANKS[mitigated_risk] >= RISK_RANKS["Medium"]

    return {
        "severity": severity,
        "initial_likelihood": l_init,
        "initial_risk_rating": initial_risk,
        "total_ipl_credits": total_credits,
        "mitigated_likelihood": l_mitigated,
        "mitigated_risk_rating": mitigated_risk,
        "action_required": action_required,
        "severity_breakdown": {
            "people": people,
            "environment": env,
            "economic": econ,
            "social": social
        }
    }
