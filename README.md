# AI-Based Network Intrusion Detection System Using Machine Learning

## Project Overview

This project demonstrates a machine-learning approach to detecting potentially anomalous network traffic using the NSL-KDD dataset.

It uses two classification models:

- **Logistic Regression:** Baseline model.
- **Random Forest:** Candidate model selected for the prototype.

The system classifies network traffic into two categories:

- `0` — Normal traffic
- `1` — Anomalous traffic

The intended users are security analysts and network administrators. The prototype provides decision support by identifying potentially suspicious traffic.

## Model Evaluation

Evaluation results from the latest experiment:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 69.02% | 78.43% |
| Precision | 88.42% | 96.87% |
| Recall | 52.44% | 64.18% |
| F1-score | 65.84% | 77.21% |

The Random Forest model achieved better results across all four reported metrics and was selected for the prototype.

## Project Structure

```text
C:\data\
│
├── app.py
├── requirements.txt
├── README.md
├── NSL_KDD_Intrusion_Detection_Implementation-1 (1).ipynb
├── prepare_sample.py
│
├── data\
│   ├── KDDTrain+.txt
│   ├── KDDTest+.txt
│   └── sample_network_traffic.csv
│
├── models\
│   └── nsl_kdd_random_forest_pipeline.joblib
│
├── reports\
│   ├── evaluation_results.json
│   ├── model_comparison.png
│   └── confusion_matrix.png
│
└── src\
    └── predict.py
```

## Requirements

- Python 3.10 or later
- pip
- Required packages listed in `requirements.txt`

## Installation

Open a terminal in the project directory and create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Web Application

Start the Streamlit application:

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal. Upload a CSV containing the required 41 NSL-KDD input features and analyze the records.

## Run Command-Line Predictions

Run the prediction script:

```powershell
python src\predict.py data\sample_network_traffic.csv
```

The script saves the predictions to `prediction_results.csv` in the project directory.

You can specify another output path:

```powershell
python src\predict.py data\sample_network_traffic.csv --output reports\my_predictions.csv
```

## Dataset

The project uses the NSL-KDD network intrusion detection dataset, with separate training and testing files.

The model uses 41 network traffic features. The target label is converted into a binary classification:

- Normal traffic: `0`
- Anomalous traffic: `1`

## Limitations and Responsible Use

This project is an educational machine-learning prototype, not a production-ready intrusion prevention system.

- Predictions may contain false positives and false negatives.
- The model should be independently tested and validated before real-world deployment.
- It does not automatically block network traffic.
- Human security analysts should review predictions before taking action.
- Dataset performance does not guarantee performance on modern real-world network traffic.

## Project Purpose

The goal is to demonstrate how machine learning can support network intrusion detection through data preprocessing, model training, evaluation, prediction, and a simple user interface.
