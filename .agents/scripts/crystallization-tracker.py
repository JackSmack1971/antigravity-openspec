import json
import os
import sys
from datetime import datetime, timedelta

# Rule 11.5: Use script-relative absolute path to prevent CWD-dependent failures on Windows.
# Path: workspace/.agents/scripts/this_script.py
# So: __file__ -> scripts/ -> .agents/ -> workspace root
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

def log_session(wins, interventions):
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)

    session = {
        "timestamp": datetime.now().isoformat(),
        "wins": wins,
        "interventions": interventions,
        "uplift": (wins / (wins + interventions) * 100) if (wins + interventions) > 0 else 0
    }

    data["history"].append(session)
    data["total_wins"] += wins
    data["total_interventions"] += interventions

    with open(METRICS_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Session Logged: Wins={wins}, Interventions={interventions}, Uplift={session['uplift']:.2f}%")

def get_total_uplift():
    init_metrics()
    with open(METRICS_FILE, "r") as f:
        data = json.load(f)

    total = data["total_wins"] + data["total_interventions"]
    if total == 0:
        return 0, data
    return (data["total_wins"] / total) * 100, data

def get_30day_uplift():
    """Calculate uplift within the 30-day crystallization window."""
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

def print_dashboard():
    """Print full Autonomy Uplift Dashboard (Rule 09.6 format)."""
    agg_uplift, data = get_total_uplift()
    w30_uplift, w30_wins, w30_interventions, w30_sessions = get_30day_uplift()

    print("=" * 50)
    print("  AUTONOMY UPLIFT DASHBOARD (Rule 09.6)")
    print("=" * 50)
    print(f"  Aggregate Uplift%:      {agg_uplift:.2f}%")
    print(f"  Total Wins:             {data['total_wins']}")
    print(f"  Total Interventions:    {data['total_interventions']}")
    print(f"  Total Sessions:         {len(data['history'])}")
    print()
    print(f"  30-Day Window Uplift%:  {w30_uplift:.2f}%")
    print(f"  30-Day Sessions:        {w30_sessions}")
    print(f"  30-Day Wins:            {w30_wins}")
    print(f"  30-Day Interventions:   {w30_interventions}")
    print()
    if agg_uplift < 40:
        print("  [WARN] Uplift% < 40%. Trigger /para-knowledge audit.")
    elif agg_uplift < 60:
        print("  [NOTE] Uplift% below 60% target. Monitor closely.")
    else:
        print("  [OK]   Uplift% is within acceptable range.")
    print("=" * 50)

    # Print last 5 sessions
    if data["history"]:
        print("\n  Recent Session History (last 5):")
        for s in data["history"][-5:]:
            ts = s["timestamp"][:10]
            print(f"  [{ts}] Wins={s['wins']} Interventions={s['interventions']} Uplift={s['uplift']:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        log_session(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 2 and sys.argv[1] == "--dashboard":
        print_dashboard()
    else:
        # Default: show aggregate uplift (backward compatible)
        uplift, _ = get_total_uplift()
        print(f"Current Aggregate Autonomy Uplift: {uplift:.2f}%")
        print("Tip: Run with --dashboard for full report, or [wins] [interventions] to log a session.")
