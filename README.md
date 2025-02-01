# Quantitative Analysis of RSI, PCA, and Machine Learning

This repository contains a student project for algorithmic trading that utilizes the Relative Strength Index (RSI) computed over multiple periods, Principal Component Analysis (PCA) for dimensionality reduction, and a linear machine learning model to generate trading signals.

**Disclaimer:** This project is for educational purposes only. The strategies implemented here should not be considered as financial advice.

## Overview

The core idea behind this project is:
- **Multi-Period RSI Calculation:**  
  Instead of relying on a single RSI, the project computes the RSI over a range of periods (e.g., from 2 to 24). This provides a richer view of market momentum across different time scales.
  
- **Dimensionality Reduction with PCA:**  
  The multiple RSI indicators, which may be correlated, are processed using PCA to extract the principal components that capture most of the variance in the data.
  
- **Linear Model for Prediction:**  
  The principal components serve as inputs to a linear regression model that predicts future price movements.  
  Based on the predictions and statistically derived thresholds (e.g., the 99th and 1st quantiles), trading signals (long/short) are generated.

## Repository Structure

- **model_in_sample.py**  
  Computes multiple RSIs, applies PCA, trains a linear regression model on historical data, and generates a scatter plot comparing the model's predictions with the actual target values.

- **Pca.py**  
  Computes and visualizes the principal components of the RSI indicators. This script displays the eigenvectors, illustrating the contribution of each RSI (for different periods) to the principal components.

- **rsi_behavior.py**  
  Analyzes the behavior of the RSI indicators by generating histograms, time-series plots, and a correlation heatmap. This helps in understanding the distribution and relationships among the various RSIs.

- **Walkforward.py**  
  Implements a walk-forward analysis, which:
  - Dynamically re-trains the model on a moving window of data.
  - Generates trading signals based on the model’s predictions.
  - Outputs key performance metrics such as:
    - **Mean Target Above Long Threshold:** Average target return when a long signal is generated.
    - **Mean Target Below Short Threshold:** Average target return when a short signal is generated.
    - **Profit Factor:** Ratio of the sum of positive returns to the absolute sum of negative returns.
    
- **input.csv**  
  A generic data file containing historical price data. The file must include at least:
  - `date`: Timestamp (e.g., in a format recognized by `pd.to_datetime`).
  - `close`: The closing price of the asset.

## Requirements

Make sure you have Python 3 installed. The project depends on the following libraries:

- pandas
- pandas_ta
- numpy
- seaborn
- matplotlib
- scipy

You can install these dependencies using `pip3`:

```bash
pip3 install pandas pandas_ta numpy seaborn matplotlib scipy