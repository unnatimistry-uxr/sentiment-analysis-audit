{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cd55777b-d0dc-4fb3-8793-27e42cbae84b",
   "metadata": {},
   "source": [
    "# Voice of the Customer (VoC) Intelligence Pipeline: AI-Augmented Sentiment Audit\n",
    "\n",
    "## Project Overview\n",
    "This project demonstrates a hybrid approach to large-scale qualitative analysis. Using a dataset of Google Play Store reviews, I built a natural language processing (NLP) pipeline to automate sentiment scoring and conducted a \"Human-in-the-Loop\" audit to identify where automated models fail to capture user nuance.\n",
    "\n",
    "## The Problem\n",
    "Manual thematic coding of 10,000+ reviews is inefficient, yet pure AI sentiment analysis often misses sarcasm, negation (e.g., \"not good\"), and technical frustration, leading to skewed UX priorities.\n",
    "\n",
    "## Methodology\n",
    "* **Quantitative:** Sentiment Polarity Modeling using TextBlob (Lexicon-based NLP).\n",
    "* **Qualitative Audit:** Statistical validation of AI scores against User Star Ratings to identify 'Cognitive Dissonance.'\n",
    "* **Tech Stack:** Python (Pandas, NLTK, TextBlob), Seaborn for statistical visualization.\n",
    "\n",
    "## Key Technical Achievements\n",
    "* **Custom NLP Preprocessing:** Built a regex-based cleaning pipeline to normalize \"noisy\" mobile review data.\n",
    "* **Integrity Audit:** Discovered a **0.48 correlation** between user ratings and AI sentiment, identifying **217 critical false positives** where users expressed deep frustration that the AI categorized as positive."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd84d799-9a69-45b8-8780-2beeca911659",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
