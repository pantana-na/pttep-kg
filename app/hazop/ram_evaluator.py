"""PTT GC 5x5 Risk Assessment Matrix (RAM) & LOPA Safeguard Evaluator.

Governed by PTT GC Corporate Standard W-(Q-MP)-002 R2 and SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE.
Supports 3-Risk-Block Lifecycle and 3 Human-in-the-Loop (HITL) gates.
"""

from typing import Tuple, List, Dict, Any, Optional

# PTT GC 5x5 RAM Lookup Grid: rows = Severity (1..5), cols = Likelihood (1..5)
# Severity: 1=Slight, 2=Minor, 3=Local, 4=Major, 5=Extensive
# Likelihood: 1=Improbable, 2=Remote, 3=Occasional, 4=Probable, 5=Frequent
RAM_GRID = {
    5: {1: "Medium", 2: "High",   3: "High",    4: "Extreme", 5: "Extreme"},
    4: {1: "Medium", 2: "Medium", 3: "High",    4: "High",    5: "Extreme"},
    3: {1: "Low",    2: "Medium", 3: "Medium",  4: "High",    5: "High"},
    2: {1: "Low",    2: "Low",    3: "Medium",  4: "Medium",  5: "High"},
    1: {1: "Very Low", 2: "Very Low", 3: "Low", 4: "Low",     5: "Medium"},
}

RISK_RANKS = {"Very Low": 0, "Low": 1, "Medium": 2, "High": 3, "Extreme": 4}


def calculate_overall_severity(people: int, env: int, econ: int, social: int) -> int:
    """Severity is the maximum across all 4 impact dimensions."""
    p = max(1, min(5, int(people)))
    en = max(1, min(5, int(env)))
    ec = max(1, min(5, int(econ)))
    s = max(1, min(5, int(social)))
    return max(p, en, ec, s)


def get_risk_rating(severity: int, likelihood: int) -> str:
    """Returns the qualitative risk rating (Very Low, Low, Medium, High, Extreme) from the 5x5 RAM."""
    s = max(1, min(5, int(severity)))
    l = max(1, min(5, int(likelihood)))
    return RAM_GRID[s][l]


def calculate_ipl_credit(safeguard: Dict[str, Any]) -> int:
    """Computes IPL Likelihood credit reduction based on SIL rating and independence."""
    sil = str(safeguard.get("sil_rating", "") or "").upper()
    sg_desc = str(safeguard.get("description", "") or "").upper()
    is_ipl = safeguard.get("is_ipl", False) or safeguard.get("is_interlock_esd", False) or (safeguard.get("il_esd", "") == "Yes")
    
    # Check text for SIL indicators
    if "SIL 3" in sil or "SIL 3" in sg_desc:
        return 3
    elif "SIL 2" in sil or "SIL 2" in sg_desc:
        return 2
    elif "SIL 1" in sil or "SIL 1" in sg_desc:
        return 1
    elif "DIERS" in sg_desc or "PSV" in sg_desc:
        return 2 if "DIERS" in sg_desc else 1
    elif "RELIABLE POWER" in sg_desc:
        return 1

    return 1 if is_ipl else 0


def evaluate_1st_risk(
    people: int,
    env: int,
    econ: int,
    social: int,
    initial_likelihood: int
) -> Dict[str, Any]:
    """Evaluates Block 1: Initial Risk (Without Safeguards) - HITL Gate 1."""
    severity = calculate_overall_severity(people, env, econ, social)
    l_init = max(1, min(5, int(initial_likelihood)))
    initial_risk = get_risk_rating(severity, l_init)

    return {
        "severity": severity,
        "overall_severity": severity,
        "initial_likelihood": l_init,
        "people": max(1, min(5, int(people))),
        "env": max(1, min(5, int(env))),
        "econ": max(1, min(5, int(econ))),
        "social": max(1, min(5, int(social))),
        "initial_risk_rating": initial_risk
    }


def evaluate_2nd_risk(
    first_risk: Dict[str, Any],
    safeguards: List[Dict[str, Any]],
    override_mitigated_likelihood: Optional[int] = None
) -> Dict[str, Any]:
    """Evaluates Block 2: Mitigated Risk (With Safeguards) - HITL Gate 3."""
    severity = first_risk.get("overall_severity", first_risk.get("severity", 5))
    l_init = first_risk.get("initial_likelihood", 4)

    total_credits = sum(calculate_ipl_credit(sg) for sg in safeguards)
    if override_mitigated_likelihood is not None:
        l_mit = max(1, min(5, int(override_mitigated_likelihood)))
    else:
        l_mit = max(1, l_init - total_credits)

    mitigated_risk = get_risk_rating(severity, l_mit)
    requires_action = RISK_RANKS.get(mitigated_risk, 0) >= RISK_RANKS["Medium"]

    return {
        "severity": severity,
        "overall_severity": severity,
        "initial_likelihood": l_init,
        "initial_risk_rating": first_risk.get("initial_risk_rating", get_risk_rating(severity, l_init)),
        "total_ipl_credits": total_credits,
        "mitigated_likelihood": l_mit,
        "mitigated_risk_rating": mitigated_risk,
        "action_required": requires_action,
        "requires_action": requires_action
    }


def evaluate_deviation_risk(
    people: int,
    env: int,
    econ: int,
    social: int,
    initial_likelihood: int,
    safeguards: List[Dict[str, Any]],
    override_mitigated_likelihood: Optional[int] = None
) -> Dict[str, Any]:
    """Unified 3-Risk-Block evaluation for backward compatibility and end-to-end testing."""
    first = evaluate_1st_risk(people, env, econ, social, initial_likelihood)
    second = evaluate_2nd_risk(first, safeguards, override_mitigated_likelihood)

    return {
        "severity": first["overall_severity"],
        "overall_severity": first["overall_severity"],
        "initial_likelihood": first["initial_likelihood"],
        "initial_risk_rating": first["initial_risk_rating"],
        "people": first["people"],
        "env": first["env"],
        "econ": first["econ"],
        "social": first["social"],
        "total_ipl_credits": second["total_ipl_credits"],
        "mitigated_likelihood": second["mitigated_likelihood"],
        "mitigated_risk_rating": second["mitigated_risk_rating"],
        "action_required": second["requires_action"],
        "requires_action": second["requires_action"],
        "safeguards_detail": [
            {
                "description": sg.get("description", ""),
                "il_esd": "Yes" if (sg.get("is_ipl") or sg.get("il_esd") == "Yes" or "SIL" in str(sg.get("sil_rating", "")).upper()) else "No",
                "ipl_credit": calculate_ipl_credit(sg)
            }
            for sg in safeguards
        ]
    }
