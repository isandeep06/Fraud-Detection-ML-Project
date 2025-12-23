## Fraud Detection App

Interactive Streamlit dashboard for stress-testing PaySim-style ledgers against trained fraud models. Operators can plug in transaction narratives, inspect model calls, and share audit-ready evidence without touching notebooks.

### Highlights
- Scenario builder mirrors the PaySim schema (`type`, `amount`, `oldbalanceOrg`, etc.) so CSV rows can be pasted in directly.
- Model loader auto-detects bundled artifacts (logistic regression, XGBoost, generic pickle). Drop your latest pipeline next to `Fraud_dectection.py` and the UI picks it up on boot.
- Probability call-outs, progress bars, and helper text translate every prediction into plain language for fraud analysts.

### Repo Layout
| Path | Purpose |
| --- | --- |
| `Fraud_dectection.py` | Streamlit UI + inference workflow. |
| `Fraud_Detection.ipynb` | Notebook used to explore PaySim data and train/export models. |
| `AIML Dataset.csv` | Sample ledger sourced from PaySim. |
| `xgb_fraud_model.pxl`, `fraud_detection_model.pkl`, `logistic_fraud_model.joblib` | Candidate model artifacts searched at runtime. |

### Requirements
- Windows/macOS/Linux with Python 3.10+ (tested on 3.13).
- Packages: `streamlit`, `pandas`, `joblib`, plus the libraries baked into your serialized model (e.g., `xgboost`, `scikit-learn`).

Install the basics:
```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas joblib
```

### Running the Dashboard
1. Clone or copy this folder locally.
2. Place at least one supported model file in the project root (`fraud_detection_model.pkl` is the default fallback).
3. Start Streamlit from the project directory using the same interpreter that has Streamlit installed:
	```bash
	python -m streamlit run Fraud_dectection.py
	```
4. Open the provided `http://localhost:8502` link in your browser.

> **Tip:** On Windows Store versions of Python you may need the fully qualified interpreter path, e.g., `C:/Users/<user>/AppData/.../python3.13.exe -m streamlit run Fraud_dectection.py`.

### Using the Scenario Builder
1. Pick a transaction `type` (Payment, Transfer, Cash Out, Cash In, Debit).
2. Enter the PaySim `amount` value and both origin/destination balances before/after the move.
3. Click **Run Prediction**. The app renders:
	- Model verdict (Fraudulent vs Legitimate).
	- Probability sentence ("This transaction has XX.X% probability of being …").
	- Progress bar + reference to the loaded model artifact.
4. Tweak any field and submit again to run what-if checks.

### Replacing / Updating Models
1. Export your estimator with `joblib.dump()` or `pickle.dump()`.
2. Name it to match an entry in `MODEL_CANDIDATES` inside `Fraud_dectection.py`, or edit that list to include your filename.
3. Restart the Streamlit app—`load_model()` selects the first existing file.

### Extending the Project
- **Feature engineering:** Update the notebook, retrain, and ensure preprocessing steps are encapsulated in the serialized pipeline.
- **Batch scoring:** Convert `Fraud_dectection.py` logic into a function and map across CSV rows or integrate with an API.
- **Audit logging:** Capture predictions plus user-entered metadata and send them to a database or CSV.

### Troubleshooting
- `streamlit : The term 'streamlit' is not recognized` → install Streamlit in the active environment or call it via `python -m streamlit`.
- `Model prediction failed: ...` → verify the artifact expects the exact PaySim columns and that preprocessing is bundled inside the pipeline.
- Blank probability text → your estimator lacks `predict_proba`; consider exporting a probabilistic model or handle decision functions manually.

### License & Credits
Created by Sandeep M. for rapid, analyst-friendly experimentation on PaySim-like fraud scenarios. Use responsibly when testing with real customer data.
