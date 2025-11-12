import json
from datetime import datetime
from pathlib import Path
import pandas as pd
from pydantic import BaseModel, Field

# --- Paths ---
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_IN   = REPO_ROOT / "data/input"
DATA_OUT = REPO_ROOT / "data/output"

# --- Schemas ---
class PageProfile(BaseModel):
    page_handle: str
    theme: str
    timezone: str
    never_post_raw: list[str]
    core_goal: str
    focus: str
    audience: str

# --- Helpers ---
#Map CSV column names to PageProfile field
COLMAP = {
    "Page Handle (e.g. @johndoe)": "page_handle",
    "Theme (e.g. pets, parenting)": "theme",
    "Timezone": "timezone",
    "What should NEVER be posted? (e.g. politics)" : "never_post_raw",
    "Core Goal (e.g. celebrate grandkids, nostalgia, tell jokes)": "core_goal",
    "Content Focus (e.g. relatable quotes, family life)": "focus",
    "Audience (e.g. pet owners, grandparents, new parents)": "audience"
}

def convert_all_csv(in_dir=DATA_IN, out_file=DATA_OUT / "profiles.json"):
    in_path  = Path(in_dir)
    out_path = Path(out_file)

    # Discover CSV and order them
    files = sorted(
        p for p in in_path.rglob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {in_dir.resolve()}")

    # Read and combine into DataFrames
    dfs = [pd.read_csv(p, encoding="utf-8-sig") for p in files]
    combined = dfs[0] if len(dfs) == 1 else pd.concat(dfs, ignore_index=True)

    if "Timestamp" in combined.columns:
        combined = combined.drop(columns=["Timestamp"])

    # Make sure the out dir exists
    out_path.parent.mkdir(parents=True, exist_ok=True)

    records = combined.to_dict(orient="records")
    formatted_json = json.dumps(records, ensure_ascii=False, indent=2)

    # Write to disk
    out_path.write_text(formatted_json, encoding="utf-8")

    print(formatted_json)

def main():
    convert_all_csv()

if __name__ == "__main__":
    main()