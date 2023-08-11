# Fashion Review Summarization and Sentiment Analysis

This project addresses the challenge of making informed online fashion purchases by creating summaries of product reviews to provide quick insights. The study compares these summaries with official product descriptions and predicts sentiment based on text. The data is sourced from Amazon, comprising over 883,000 reviews and additional API-scraped reviews.

## Key Objectives

1. Summarize fashion item reviews for quick insights.
2. Compare review summaries to official product descriptions.
3. Predict sentiment from review text.
4. Utilize Airflow, GCP storage, MongoDB, and Databricks for data management and analysis.

## Datasets

- Amazon fashion reviews (883,636 reviews).
- Amazon API-scraped reviews for specific fashion items.

## Methods

- Aggregate data from two distinct datasets.
- Employ Airflow for data upload and GCP storage.
- Perform summarization and sentiment analysis using NLTK, TextRank, LSA, Logistic Regression, SVM, BERT, and SiBERT.
- Utilize PyTorch for logistic regression and mean absolute error (MAE) evaluation.
- Compare summaries with official product descriptions.
- Implement models on GPU cluster for efficiency.

## Results

- Effective summarization of product reviews using NLTK.
- Accurate sentiment analysis using spaCy and pretrained logistic regression.
- Positive and negative sentiment prediction based on review text.
- Deep learning models like BERT and SiBERT show promising performance.

## Tools and Libraries

- NLTK, TextRank, LSA, spaCy, BERT, SiBERT, pandas, pyspark, pymongo, transformers, vaderSentiment, engSpacySentiment, Airflow, GCP, MongoDB, Databricks.

This project aims to enhance online shopping experiences by providing concise summaries and sentiment insights from customer reviews, contributing to more informed purchasing decisions.
