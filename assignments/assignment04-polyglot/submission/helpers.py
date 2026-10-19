from pathlib import Path

import pandas as pd


def summarize_by_groups(df, value_col, group1_col, group2_col):
    """Return a grouped summary with n, mean, and SD for the chosen value and groups."""
    summary = (
        df.dropna(subset=[value_col, group1_col, group2_col])
        .groupby([group1_col, group2_col], as_index=False)
        .agg(
            n=(value_col, "size"),
            mean_value=(value_col, "mean"),
            sd_value=(value_col, "std"),
        )
        .sort_values([group1_col, group2_col])
        .reset_index(drop=True)
    )
    summary["mean_value"] = summary["mean_value"].round(2)
    summary["sd_value"] = summary["sd_value"].round(2)
    return summary


def load_nhanes(path: str | None = None):
    if path is None:
        candidate_paths = [
            Path("../../../examples/nhanes-equity/data/nhanes_equity_v6.csv"),
            Path("examples/nhanes-equity/data/nhanes_equity_v6.csv"),
        ]
        path = next((str(p) for p in candidate_paths if p.exists()), str(candidate_paths[0]))
    return pd.read_csv(path)
