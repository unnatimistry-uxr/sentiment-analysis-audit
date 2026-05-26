import os
from pathlib import Path
from dataclasses import dataclass

# 1. Define the Base Directory (The project root)
BASE_DIR = Path(__file__).resolve().parent.parent

@dataclass(frozen=True)
class ProjectPaths:
    """
    Centralized path management with Namespaced Variable Names.
    Format: FOLDER_SUBFOLDER_FILENAME_EXT
    """
    
    # --- DIRECTORIES ---manual work files
    DIR_DATA_RAW = BASE_DIR / "data" / "raw"
    DIR_DATA_PROCESSED = BASE_DIR / "data" / "processed"
    DIR_DATA_ANALYSIS = BASE_DIR / "data" / "analysis"
    DIR_DATA_ARCHIVE = BASE_DIR / "data" / "archive"
    
    DIR_REPORTS_SENTIMENT = BASE_DIR / "reports" / "figures" / "00_sentiment_metrics"
    DIR_REPORTS_POSITIVE = BASE_DIR / "reports" / "figures" / "01_positive_analysis"
    
    # --- NEW: DIRECTORIES FOR PHASE 2 ---
    DIR_REPORTS_NEGATIVE = BASE_DIR / "reports" / "figures" / "02_negative_analysis"

    # --- DATA FILES ---
    # Raw
    DATA_RAW_GOOGLE_REVIEWS_CSV = DIR_DATA_RAW / "google_play_reviews.csv"
    
    # Processed
    DATA_PROCESSED_CLEANED_CSV = DIR_DATA_PROCESSED / "cleaned_reviews.csv"
    DATA_PROCESSED_WITH_SENTIMENT_CSV = DIR_DATA_PROCESSED / "cleaned_reviews_with_sentiment.csv"
    DATA_PROCESSED_NEGATIVE_POOL_CSV = DIR_DATA_PROCESSED / "negative_review_pool.csv"
    
    # Analysis
    DATA_ANALYSIS_MANUAL_SAMPLE_HTML = DIR_DATA_ANALYSIS / "manual_reading_sample.html"
    DATA_ANALYSIS_MANUAL_SAMPLE_XLSX = DIR_DATA_ANALYSIS / "manual_reading_sample.xlsx"
    DATA_ANALYSIS_FULL_5STAR_CSV = DIR_DATA_ANALYSIS / "full_categorized_5_star_reviews.csv"
    DATA_ANALYSIS_NEG_MANUAL_SAMPLE_XLSX = DIR_DATA_ANALYSIS / "negative_manual_sample.xlsx"
    DATA_ANALYSIS_NEG_THEMATIC_XLSX = DIR_DATA_ANALYSIS / "negative_Thematic_Analysis.xlsx"
    DATA_ANALYSIS_MASS_INFERENCE_CLASSIFIED_XLSX = DIR_DATA_ANALYSIS / "final_mass_inference_classified.xlsx"
    
    # --- REPORT FILES (Sentiment Metrics) ---
    REPORTS_SENTIMENT_SCORES_HTML = DIR_REPORTS_SENTIMENT / "sentiment_score_table.html"
    REPORTS_SENTIMENT_METRICS_JSON = DIR_REPORTS_SENTIMENT / "summary_metrics.json"
    REPORTS_SENTIMENT_MISMATCH_HTML = DIR_REPORTS_SENTIMENT / "mismatch_table.html"
    REPORTS_SENTIMENT_CORRELATION_PNG = DIR_REPORTS_SENTIMENT / "sentiment_correlation.png"

    # --- REPORT FILES (Positive Analysis) ---
    REPORTS_POS_FREQ_VALIDATION_HTML = DIR_REPORTS_POSITIVE / "frequency_validation.html"
    REPORTS_POS_VALUE_PROP_COMP_HTML = DIR_REPORTS_POSITIVE / "comprehensive_value_prop_table.html"
    
     # --- REPORT FILES (Negative Analysis) ---
    REPORTS_NEG_PARETO_PNG = DIR_REPORTS_NEGATIVE / "pain_point_pareto.png"
    REPORTS_NEG_TREEMAP_HTML = DIR_REPORTS_NEGATIVE / "thematic_pain_hierarchy.html"

# Instantiate for use in notebooks
paths = ProjectPaths()

def initialize_folders():
    """
    Safely creates the project structure if it doesn't exist.
    """
    required_folders = [
        paths.DIR_DATA_RAW, 
        paths.DIR_DATA_PROCESSED, 
        paths.DIR_DATA_ANALYSIS, 
        paths.DIR_DATA_ARCHIVE,
        paths.DIR_REPORTS_SENTIMENT,
        paths.DIR_REPORTS_POSITIVE,
        paths.DIR_REPORTS_NEGATIVE
    ]
    
    print("--- Project Structure Audit ---")
    for folder in required_folders:
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created: {folder.relative_to(BASE_DIR)}")
        else:
            print(f"✅ Exists:  {folder.relative_to(BASE_DIR)}")