
# Longevity Analysis: Cross-Country Indicators (2000–2015)

## Overview
This project explores country-level indicators associated with life expectancy between 2000 and 2015.  
The goal is to identify patterns and predictors of longevity across countries.

## Data
This dataset was obtained from Kaggle. It contains annual country-level indicators related to health, economics, demographics, and public policy for 193 countries between 2000 and 2015 compiled from WHO and World Bank sources.
Raw data is stored in data/raw and should not be modified.

The target variable is **Life Expectancy at Birth**.

A full description of all 22 variables is available in [`docs/data_dictionary.md`](docs/data_dictionary.md).

## Experiment Log

| Phase | Model | Key Activity | R²  | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline | Linear | Baseline: basic cleaning + all features | 0.842 | Completed |
| Benchmarking | Random Forest | First multi-model test; RF best but unstable | 0.969 | Completed |
| Refinement | All | Added Log Transforms to `01_preprocessing_and_eda`; re-evaluated models | -- | -- | Current |

## Project Structure
### Notebooks
* `01_preprocessing_and_eda.ipynb`: Handles missing data imputation, outlier detection, and feature engineering (log-scaling/selection).
* `02_modelling.ipynb`: Current best model training and evaluation.

### Data
- `raw/`: Original WHO dataset as downloaded.
- `processed/`:
    - `life_expectancy_cleaned.csv`: Cleaned data with handled missing values and corrected types (post-imputation).
    - `life_expectancy_engineered.csv`: Version with log-transformed features and removed multicollinearity; optimized for linear modeling.

### ml-core-utils (Submodule): Shared logic abstracted into a reusable package.
- `config.py`: global settings and notebook environment setup
- `data_io.py`: standardize model serialization and experiment tracking, ensuring every model run is documented with metadata.
- `evaluation.py`: functions for evaluating model performance
- `preprocessing.py`: functions for preprocessing data
- `persistence.py`: Handles model serialization (saving/loading) and versioning.

### Models
Archive of model weights and performance metrics for the baseline version and the current best model.

## Setup & Requirements
This project uses `pyproject.toml` for dependency management.

* **Python:** 3.12+
* **Environment Setup:** ```bash
  pip install .

**Note:** This repository uses a submodule for shared utilities. To clone including the submodule:
```bash
git clone --recursive https://github.com/MermonGData/longevity-prediction
pip install .

## Project Status 
**Done**
- Baseline establishment 
- Multi-model Benchmarking: identified Random Forest as top performer.
- Feature Engineering: Implemented log-transforms for skewed indicators in 01_eda_and_preprocessing.ipynb.
- Architecture Refactor: Abstracted core logic into ml-core-utils submodule and implemented persistence.py for model tracking.

**To-Do**
- Feature Refinement (encoding 'country' etc)
- Optimization (Hyperparameter tuning)
- Interpretation/visuals