"""Check the published evidence digest and arithmetic, without private data."""
from pathlib import Path
import hashlib
import json
import math

root = Path(__file__).resolve().parents[1]
m = json.loads((root / "results/metrics.json").read_text(encoding="utf-8"))
e = json.loads((root / "results/evidence-manifest.json").read_text(encoding="utf-8"))
canonical = json.dumps(m, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
assert hashlib.sha256(canonical.encode()).hexdigest() == e["metrics_sha256_canonical_json"]
scores = {r["experiment"]: r["public_ba"] for r in m["public_scores"]}
assert math.isclose(scores["G07"]-scores["V3"], .005, abs_tol=1e-12)
assert max(scores.values()) == scores["G07"]
assert all(0 <= r["ba"] <= 1 for r in m["matched_development_oof"])
assert m["data"]["selection_per_class"] * m["task"]["classes"] == m["data"]["selection_rows"]
for branch, r in m["inference_180_rows"].items():
    assert math.isclose(1-r["after_forward_seconds"]/r["before_forward_seconds"], r["time_reduction"], abs_tol=1e-12)
print("Published evidence digest and arithmetic: passed")
print("G07 - V3: +0.005 BA = +0.5 percentage points")
print("Scope: aggregate consistency; does not rerun training, OOF or hidden scoring")
