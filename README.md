# Diabetes Prediction — End-to-End Logistic Regression

A small end-to-end project that trains a logistic regression model to predict diabetes and exposes a Streamlit app for interactive predictions.

## Project Structure

- `app.py` — Streamlit web app that loads `model.pkl` and `scaler.pkl` and performs predictions.
- `model_training.ipynb` — Notebook used to explore data, train the model, and create `model.pkl` and `scaler.pkl`.
- `diabetes_prediction_dataset.csv` — Original dataset used for training and experimentation.

## Dataset features

The dataset contains the following columns (features):

- `gender`
- `age`
- `hypertension`
- `heart_disease`
- `smoking_history`
- `bmi`
- `HbA1c_level` (average sugar level over ~2–3 months)
- `blood_glucose_level`
- `diabetes` (target label: 1 = diabetes, 0 = no diabetes)

## Requirements

- Python 3.8+
- Packages: `streamlit`, `numpy`, `pandas`, `scikit-learn`, `joblib`

Install dependencies with:

```bash
pip install streamlit numpy pandas scikit-learn joblib
```

### Setup (recommended)

- Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or
source .venv/bin/activate       # macOS / Linux
```

- Install from `requirements.txt` (preferred):

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, the project uses at minimum: `streamlit`, `numpy`, `pandas`, `scikit-learn`, and `joblib`.

## Running the Streamlit App

Make sure `model.pkl` and `scaler.pkl` are in the same directory as `app.py`.

Start the app:

```bash
streamlit run app.py
```

Open the URL for Web App for model (https://diabetes-prediction-using-logistic-regression-eauxyndbvdegrsfn.streamlit.app/).

### Run examples

- Run the Streamlit UI (quick prediction):

```bash
streamlit run app.py
```

- Open the training notebook to reproduce or retrain the model:

```bash
jupyter notebook model_training.ipynb
# or
jupyter lab model_training.ipynb
```

Make sure `model.pkl` and `scaler.pkl` produced by the notebook are next to `app.py` before running the Streamlit app.

## Training the Model

Use `model_training.ipynb` to reproduce data preprocessing, training, and serialization steps. The notebook will show how to generate `model.pkl` and `scaler.pkl` using `joblib`.

## Notes

- The app expects input features in the same order/format used during training: gender, age, hypertension, heart_disease, smoke, bmi, sugar_level, blood_glucose_level.
- If you need to regenerate the model, run the notebook and save `model.pkl` and `scaler.pkl` next to `app.py`.



