
# Longevity Analysis: Cross-Country Indicators (2000–2015)
**WORK IN PROGRESS**

## Overview
This project explores country-level indicators associated with life expectancy between 2000 and 2015.  
The goal is to identify patterns and predictors of longevity across countries.

## Data
This dataset was obtained from Kaggle. It contains annual country-level indicators related to health, economics, demographics, and public policy for 193 countries between 2000 and 2015 compiled from WHO and World Bank sources.
Raw data is stored in data/raw and should not be modified.

The target variable is **Life Expectancy at Birth**.

A full description of all 22 variables is available in [`docs/data_dictionary.md`](docs/data_dictionary.md).

## Experiment Log

| Version | Model | Change Description | R² | RMSE | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **v1.0** | Linear | Baseline: basic cleaning + all features | 0.842 | 124.5 | Fixed |
| **v1.1** | Linear | Added Log Transforms to `01_data_cleaning` | -- | -- | In Progress |

## Project Structure
### Notebooks
* `01_data_cleaning.ipynb`: Handles missing data imputation, outlier detection, and feature engineering (log-scaling/selection).
* `02_modelling.ipynb`: Current best model training and evaluation.

### Data
- `raw/`: Original WHO dataset as downloaded.
- `processed/`:
    - `life_expectancy_cleaned.csv`: Cleaned data with handled missing values and corrected types (post-imputation).
    - `life_expectancy_engineered.csv`: Version with log-transformed features and removed multicollinearity; optimized for linear modeling.

### Utilities
- `evaluation.py`: functions for evaluating model performance
- `notebook_setup.py`: common notebook setup routines
- `preprocessing.py`: functions for preprocessing data

### Models
Archive of model weights and performance metrics for every version.

## Setup & Requirements
This project uses `pyproject.toml` for dependency management.

* **Python:** 3.9+
* **Environment Setup:** ```bash
  pip install .

## Project Status 
**Done**
- Baseline Establishment (v1.0)
- Multi-model Benchmarking (Initial Search)

**To-Do**
- Feature Refinement (encoding 'country' etc)
- Optimization (Hyperparameter tuning)
- Interpretation/visuals
- completing README