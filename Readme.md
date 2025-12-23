<h1 align="center">🛡️ Fraud Detection Project — Streamlit + ML</h1>

<p align="center">
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-blue?logo=python"></a>
	<a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/Framework-Scikit--learn-orange?logo=scikitlearn"></a>
	<a href="https://xgboost.readthedocs.io/"><img src="https://img.shields.io/badge/Model-XGBoost-2b6cb0"></a>
	<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/UI-Streamlit-ff4b4b?logo=streamlit"></a>
	<img src="https://img.shields.io/badge/Status-Completed-success">
</p>

<p align="center">
	<img src="img.png" alt="Fraud Detection App" width="900" />
</p>

> 🧠 An end-to-end fraud detection system: train a model on PaySim-style transactions, export deployable artifacts, and use a Streamlit dashboard to test transactions in seconds.

---

## 📘 Project Overview

This repository contains:

- A full training notebook (EDA → preprocessing → training → evaluation → export)
- Saved model artifacts for reuse in apps/APIs
- A Streamlit UI to enter transaction details and instantly see the fraud verdict + probability

---

## 🎯 Key Features

- End-to-end ML workflow with clean, reproducible steps
- **99.99% accuracy** reported for the trained model
- Exported models (`.pkl` / `.joblib`) for easy deployment
- Streamlit “Scenario Builder” UI for interactive fraud checks
- Displays a simple result message: verdict + probability

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `Fraud_Detection.ipynb` | Full notebook workflow: preprocessing → modeling → evaluation → export. |
| `Fraud_detection.py` | Streamlit app for live transaction scoring. |
| `fraud_detection_model.pkl` | Saved model (pickle). |
| `xgb_fraud_model.joblib` | Saved model (joblib). |

---

## 🔗 Dataset

Dataset used (not uploaded to this repo):

- Kaggle: https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset/data

---

## 🌐 Live Project Link 

   Live Demo: https://frauds-detection-ml-project.streamlit.app/


---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Joblib / Pickle
- Streamlit
- Jupyter Notebook

---

## ⚙️ How to Run the Streamlit App

```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas joblib scikit-learn xgboost
python -m streamlit run Fraud_detection.py
```

---

## ⚙️ How to Load the Model

```python
import joblib

model = joblib.load("fraud_detection_model.pkl")

# Example prediction
pred = model.predict(X_new)

if hasattr(model, "predict_proba"):
		prob = model.predict_proba(X_new)[:, 1]
```

---

## 👨‍💻 Author

**Sandeep Maurya**

📧 [isandeeep06@gmail.com](mailto:isandeeep06@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/sandeepmaurya-datascientist)
🌐 [Portfolio](https://isandeep06.github.io/)

---

## 🌟 Support

If this project helped you:

⭐ Star this repo  
📢 Share it with others  
💬 Open an issue for suggestions or improvements

---

> _“Good ML isn’t only about accuracy — it’s about reliability, clarity, and real-world usability.”_
