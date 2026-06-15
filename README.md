# Voice of the Customer (VoC) Intelligence Pipeline: AI-Augmented Sentiment Audit

## Project Overview
This project demonstrates a hybrid approach to large-scale qualitative analysis. Using a dataset of Google Play Store reviews, I built a natural language processing (NLP) pipeline to automate sentiment scoring and conducted a "Human-in-the-Loop" audit to identify where automated models fail to capture user nuance.

## The Problem
Manual thematic coding of 10,000+ reviews is inefficient, yet pure AI sentiment analysis often misses sarcasm, negation (e.g., "not good"), and technical frustration, leading to skewed UX priorities.

## 🔬 Methodology & Tech Stack
* **Quantitative:** Sentiment Polarity Modeling using TextBlob (Lexicon-based NLP).
* **Qualitative Audit:** Statistical validation of AI scores against User Star Ratings to identify "Cognitive Dissonance."
* **Classification Engine:** Zero-shot Natural Language Inference via `facebook/bart-large-mnli`.
* **Tech Stack:** Python (Pandas, NLTK, TextBlob, Scikit-Learn, Matplotlib, Seaborn, Plotly).

## Key Technical Achievements
* **Custom NLP Preprocessing:** Built a regex-based cleaning pipeline to normalize "noisy" mobile review data.
* **Integrity Audit:** Discovered a 0.48 correlation between user ratings and AI sentiment, identifying 217 critical false positives where users expressed deep frustration that the AI categorized as positive.


# Voice of the Customer (VoC) Intelligence Pipeline: AI-Augmented Sentiment Audit

## Project Overview
This project demonstrates a hybrid approach to large-scale qualitative analysis. Using a dataset of Google Play Store reviews, I built a natural language processing (NLP) pipeline to automate sentiment scoring and conducted a "Human-in-the-Loop" audit to identify where automated models fail to capture user nuance.

### The Problem
Manual thematic coding of 10,000+ reviews is inefficient, yet pure AI sentiment analysis often misses sarcasm, negation (e.g., "not good"), and technical frustration, leading to skewed UX priorities.

---

## 🏗️ Repository Architecture
To maintain enterprise-level reproducibility, the directory namespace is strictly segmented:

```text
📁 sentiment-analysis-audit/
├── 📄 README.md
├── 📁 utils/
│   └── 📄 config.py                       # Centralized immutable path management
├── 📁 notebooks/
│   ├── 📄 01_text_preprocessing.ipynb     # Text normalization & regex cleaning
│   ├── 📄 02_sentiment_modeling.ipynb     # TextBlob sentiment calculation & audit
│   ├── 📄 03_positive_analysis.ipynb      # Value proposition frequency extraction
│   └── 📄 04_negative_analysis.ipynb      # Zero-shot classification & Pareto charts
├── 📁 data/
│   ├── 📁 raw/                            # Original unedited app reviews
│   ├── 📁 processed/                      # Normalized & sentiment-scored data
│   └── 📁 analysis/                       # Human gold-standards & 10k AI classified pools
└── 📁 reports/
    └── 📁 figures/                        # Automated reporting visualizations
        ├── 📁 00_sentiment_metrics/       # Correlation plots & mismatch logs
        ├── 📁 01_positive_analysis/       # Value prop frequency HTML tables
        └── 📁 02_negative_analysis/       # Pareto plots & interactive hierarchical treemaps
 ```       

---

## 🏆 Key Technical Achievements
* **Custom NLP Preprocessing:** Built a regex-based cleaning pipeline to normalize "noisy" mobile review data.
* **Integrity Audit:** Discovered a 0.48 correlation between user ratings and AI sentiment, identifying 217 critical false positives where users expressed deep frustration that the AI categorized as positive.
* **Mass Inference Scaling:** Successfully scaled expert qualitative analysis logic by over 6,000%, programmatically sorting **6,841 raw negative reviews** into localized feature problem surfaces.

---
## Project Roadmap & Status
I am currently executing this project in four distinct modules.

* [x] **Module 1: Data Infrastructure** * *Status:* ✅ Complete (Regex-based cleaning & normalization, and paths configured)
* [x] **Module 2: Sentiment Audit** * *Status:* ✅ Complete (Correlation charts generated, Statistical validation of AI vs. Human labels)
* [x] **Module 3: Positive Value Mapping**  * *Status:* ✅ Complete (Value proposition analysis, Extracting 'What Users Love')
* [ ] **Module 4: Negative Pain Point Stratification** * *Status:* ⚠️ **Active Sprint / Work in Progress (WIP)** (Pareto Analysis of 1-3 star reviews)
    * *Milestone:* Mass inference successfully completed. Current charts plot a raw baseline model.
    * *Calibration Target:* Initial validation audits indicated a low agreement score (**Cohen's Kappa: 0.22**) due to generalist AI defaulting heavily to broad "General Experience" tags. I am actively refactoring the classification layers into structured exclusionary definitions to sharpen accuracy margins.
    * *Next Update: Expected May 2026 *
* [ ] **Module 5: Executive Reporting** * *Status:* 🗺️ Planned (Final visualization dashboard for Product Stakeholders)
* [ ] Maintenance: Final repository cleanup and .gitignore optimization.
---

## 📊 Where to View Generated Reports
All visualizations are generated dynamically and saved directly inside the `reports/figures/` directories for quick cross-functional handoffs:

### 1. AI Misclassifications (`/reports/figures/00_sentiment_metrics/`)
* `sentiment_correlation.png`: Charts the operational gap between AI sentiment and actual human star ratings.
* `mismatch_table.html`: Logs exact rows where automated sentiment missed user sarcasm or explicit negations.

### 2. User Delight Drivers (`/reports/figures/01_positive_analysis/`)
* `comprehensive_value_prop_table.html`: Frequency distributions outlining why premium users remain active.

### 3. Pain Prioritization Matrix (`/reports/figures/02_negative_analysis/`)
* `pain_point_pareto.png`: Dual-axis Pareto chart separating core software issues from generalized feedback.
* `thematic_pain_hierarchy.html`: **Interactive Treemap.** Open this file inside any browser window to hover over and interactively filter proportional volumes of product friction.

---

## 🚀 How to Run and Reproduce
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/sentiment-analysis-audit.git](https://github.com/YOUR_USERNAME/sentiment-analysis-audit.git)
   
2. Install the production dependencies:
    ```bash
    pip install pandas transformers scikit-learn matplotlib seaborn plotly openpyxl

3. Run the Jupyter Notebook files sequentially from 01 to 04 to rebuild the pipeline matrices from scratch.
