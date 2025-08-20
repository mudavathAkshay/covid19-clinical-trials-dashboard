from pathlib import Path

DATA_PATH = "covid_trials.csv"

TEXT_COLS = [
    "brief_title",
    "official_title",
    "brief_summary",
    "detailed_description",
    "condition",
    "intervention",
]

ID_COL = "nct_id"
DATE_COLS = {"start": "start_date", "complete": "completion_date"}
TARGET_COL = "status"
COUNTRY_COL = "country"
PHASE_COL = "phase"
STUDY_TYPE_COL = "study_type"
ENROLL_COL = "enrollment"
SPONSOR_COL = "sponsor"

BINARY_TARGET_MAP = {
    "Completed": 1,
    "Terminated": 0,
    "Withdrawn": 0,
    "Suspended": 0,
}

DEFAULT_EMBEDDER = "sentence-transformers/all-MiniLM-L6-v2"
MLFLOW_TRACKING_URI = "experiments/mlruns"
SEED = 42
