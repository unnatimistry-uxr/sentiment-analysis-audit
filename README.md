# Voice of the Customer (VoC) Intelligence Pipeline: AI-Augmented Sentiment Audit

## Project Overview
This project demonstrates a hybrid approach to large-scale qualitative analysis. Using a dataset of Google Play Store reviews, I built a natural language processing (NLP) pipeline to automate sentiment scoring and conducted a "Human-in-the-Loop" audit to identify where automated models fail to capture user nuance.

## The Problem
Manual thematic coding of 10,000+ reviews is inefficient, yet pure AI sentiment analysis often misses sarcasm, negation (e.g., "not good"), and technical frustration, leading to skewed UX priorities.

## Methodology
* **Quantitative:** Sentiment Polarity Modeling using TextBlob (Lexicon-based NLP).
* **Qualitative Audit:** Statistical validation of AI scores against User Star Ratings to identify "Cognitive Dissonance."
* **Tech Stack:** Python (Pandas, NLTK, TextBlob), Seaborn for statistical visualization.

## Key Technical Achievements
* **Custom NLP Preprocessing:** Built a regex-based cleaning pipeline to normalize "noisy" mobile review data.
* **Integrity Audit:** Discovered a 0.48 correlation between user ratings and AI sentiment, identifying 217 critical false positives where users expressed deep frustration that the AI categorized as positive.

## Project Roadmap & Status
I am currently executing this project in four distinct modules.

* [x] **Module 1: Data Infrastructure** (Regex-based cleaning & normalization)
* [x] **Module 2: Sentiment Audit** (Statistical validation of AI vs. Human labels)
* [x] **Module 3: Positive Value Mapping** (Extracting 'What Users Love')
* [ ] **Module 4: Negative Pain Point Stratification** (Pareto Analysis of 1-3 star reviews)
    * *Next Update: Manual coding of top 6 'Product Killers' (Expected May 2026)*
* [ ] **Module 5: Executive Reporting** (Final visualization dashboard for Product Stakeholders)
* [ ] Maintenance: Final repository cleanup and .gitignore optimization.