import json
import os
import sys
import argparse
from datetime import datetime, timedelta

# Rule 11.5: Use script-relative absolute path to prevent CWD-dependent failures on Windows.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # .../scripts
_AGENTS_DIR = os.path.dirname(_SCRIPT_DIR)                 # .../.agents
_WORKSPACE_ROOT = os.path.dirname(_AGENTS_DIR)             # workspace root
METRICS_FILE = os.path.join(_AGENTS_DIR, "logs", "metrics.json")

def init_metrics():
    logs_dir = os.path.dirname(METRICS_FILE)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    if not os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, "w") as f:
            json.dump({"history": [], "total_interventions": 0, "total_wins": 0}, f)

def log_session(wins, interventions, chain="U"):
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)

    session = {
        "timestamp": datetime.now().isoformat(),
        "wins": wins,
        "interventions": interventions,
        "uplift": (wins / (wins + interventions) * 100) if (wins + interventions) > 0 else 0,
        "chain": chain
    }

    data["history"].append(session)
    data["total_wins"] += wins
    data["total_interventions"] += interventions

    with open(METRICS_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Session Logged: Wins={wins}, Interventions={interventions}, Uplift={session['uplift']:.2f}%, Chain={chain}")

def get_total_uplift():
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)

    total = data["total_wins"] + data["total_interventions"]
    if total == 0:
        return 0, data
    return (data["total_wins"] / total) * 100, data

def get_30day_uplift():
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)

    cutoff = datetime.now() - timedelta(days=30)
    recent = [s for s in data["history"] if datetime.fromisoformat(s["timestamp"]) >= cutoff]
    wins = sum(s["wins"] for s in recent)
    interventions = sum(s["interventions"] for s in recent)
    total = wins + interventions
    uplift = (wins / total * 100) if total > 0 else 0
    return uplift, wins, interventions, len(recent)

def get_chain_breakdown():
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)
    
    breakdown = {}
    for s in data["history"]:
        c = s.get("chain", "U")
        if c not in breakdown:
            breakdown[c] = {"wins": 0, "interventions": 0, "sessions": 0}
        breakdown[c]["wins"] += s["wins"]
        breakdown[c]["interventions"] += s["interventions"]
        breakdown[c]["sessions"] += 1
    
    return breakdown

def print_dashboard():
    agg_uplift, data = get_total_uplift()
    w30_uplift, w30_wins, w30_interventions, w30_sessions = get_30day_uplift()
    breakdown = get_chain_breakdown()

    print("=" * 60)
    print("  AUTONOMY UPLIFT DASHBOARD (Rule 09.6)")
    print("=" * 60)
    print(f"  Aggregate Uplift%:      {agg_uplift:.2f}%")
    print(f"  Total Wins:             {data['total_wins']}")
    print(f"  Total Interventions:    {data['total_interventions']}")
    print(f"  Total Sessions:         {len(data['history'])}")
    print("-" * 60)
    print(f"  30-Day Window Uplift%:  {w30_uplift:.2f}%")
    print(f"  30-Day Sessions:        {w30_sessions}")
    print("-" * 60)
    
    print("  POWER-CHAIN BREAKDOWN:")
    print(f"  {'Chain':<10} | {'Sessions':<10} | {'Uplift%':<10}")
    print("-" * 35)
    for c in sorted(breakdown.keys()):
        stats = breakdown[c]
        total = stats["wins"] + stats["interventions"]
        u = (stats["wins"] / total * 100) if total > 0 else 0
        print(f"  {c:<10} | {stats['sessions']:<10} | {u:>7.2f}%")
    
    print("-" * 60)
    if agg_uplift < 40:
        print("  [WARN] Uplift% < 40%. Trigger /para-knowledge audit.")
    elif agg_uplift < 60:
        print("  [NOTE] Uplift% below 60% target. Monitor closely.")
    elif agg_uplift < 95:
        print("  [OK]   Uplift% within range. RC Gate: PENDING (Target 95%).")
    else:
        print("  [PASS] Uplift% >= 95%. RC Gate: CONFORMS.")
    print("=" * 60)

    if data["history"]:
        print("\n  Recent Session History (last 5):")
        for s in data["history"][-5:]:
            ts = s["timestamp"][:10]
            c = s.get("chain", "U")
            print(f"  [{ts}] [{c}] Wins={s['wins']} Interventions={s['interventions']} Uplift={s['uplift']:.1f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antigravity Crystallization Tracker")
    parser.add_argument("wins", type=int, nargs="?", help="Number of successful autonomous operations")
    parser.add_argument("interventions", type=int, nargs="?", help="Number of human interventions")
    parser.add_argument("--chain", type=str, default="U", help="Power-Chain identifier (A-G)")
    parser.add_argument("--dashboard", action="store_true", help="Show full metrics dashboard")

    args = parser.parse_args()

    if args.dashboard:
        print_dashboard()
    elif args.wins is not None and args.interventions is not None:
        log_session(args.wins, args.interventions, args.chain)
    else:
        uplift, _ = get_total_uplift()
        print(f"Current Aggregate Autonomy Uplift: {uplift:.2f}%")
        print("Tip: Run with --dashboard for full report, or [wins] [interventions] to log a session.")
