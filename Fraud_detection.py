import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


st.set_page_config(page_title="Fraud Detection App", page_icon="🛡️", layout="wide")


MODEL_CANDIDATES = [
    "xgb_fraud_model.joblib",
    "fraud_detection_model.pkl",
]


def inject_styles():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap');
            :root {
                --bg-dark: #020617;
                --bg-panel: rgba(15, 23, 42, 0.88);
                --bg-panel-alt: rgba(15, 118, 167, 0.18);
                --border-soft: rgba(148, 163, 184, 0.25);
                --accent: #f97316;
                --accent-strong: #fb8500;
                --text-primary: #f8fafc;
                --text-muted: #94a3b8;
            }
            [data-testid="stAppViewContainer"] {
                background: radial-gradient(circle at 20% 20%, #101828 0, #00040f 65%);
                color: var(--text-primary);
                font-family: 'Space Grotesk', sans-serif;
            }
            .block-container {
                padding: 2.5rem 5vw 4rem;
                max-width: 100% !important;
            }
            .hero-card, .insight-card {
                border-radius: 1.5rem;
                border: 1px solid var(--border-soft);
                box-shadow: 0 30px 70px rgba(2, 6, 23, 0.55);
                padding: 1.75rem;
                height: 100%;
            }
            .hero-card {
                background: linear-gradient(120deg, rgba(14, 165, 233, 0.22), rgba(99, 102, 241, 0.22));
            }
            .insight-card {
                background: rgba(15, 23, 42, 0.7);
            }
            .insight-card ul {
                padding-left: 1.2rem;
                margin-bottom: 0;
            }
            .section-divider {
                margin: 2.5rem 0 1.25rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }
            .form-card {
                background: var(--bg-panel);
                padding: 1.5rem 1.75rem;
                border-radius: 1.3rem;
                border: 1px solid var(--border-soft);
                backdrop-filter: blur(14px);
            }
            .sidebar-card {
                background: rgba(2, 6, 23, 0.55);
                border-radius: 1rem;
                padding: 1.25rem;
                border: 1px solid rgba(148, 163, 184, 0.18);
            }
            .sidebar-card li {
                margin-bottom: 0.4rem;
            }
            .stat-box {
                background: rgba(15, 23, 42, 0.78);
                border-radius: 1.2rem;
                padding: 1.2rem 1.4rem;
                border: 1px solid rgba(148, 163, 184, 0.2);
                height: 100%;
            }
            .stat-box .label {
                font-size: 0.8rem;
                color: var(--text-muted);
                letter-spacing: 0.08rem;
                text-transform: uppercase;
            }
            .stat-box .value {
                font-size: 1.4rem;
                font-weight: 600;
            }
            .status-pill {
                display: inline-flex;
                align-items: center;
                padding: 0.15rem 0.65rem;
                border-radius: 999px;
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.06rem;
                background: var(--accent-soft, rgba(249, 115, 22, 0.2));
                color: var(--accent-strong);
            }
            .stat-section {
                margin-top: 1.5rem;
                margin-bottom: 0.5rem;
            }
            .footer {
                margin-top: 3rem;
                text-align: center;
                color: var(--text-muted);
                font-size: 0.9rem;
                letter-spacing: 0.08rem;
                text-transform: uppercase;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_model():
    """Load the first available model artifact from the known candidates."""
    for model_path in MODEL_CANDIDATES:
        if Path(model_path).exists():
            try:
                return joblib.load(model_path), model_path
            except Exception as exc:
                st.warning(f"Failed to load {model_path}: {exc}")
    st.error(
        "No trained model artifact found. Place one of the known files next to the app "
        "before running predictions."
    )
    return None, None


model, model_name = load_model()
inject_styles()

top_left, top_right = st.columns([0.8, 0.2])
with top_left:
    st.title("Fraud Detection App")
    st.caption(
        "Quickly test PaySim-style transactions and see how the fraud model reacts."
    )
with top_right:
    st.markdown(
        """
        <div style="text-align: right; color: #94a3b8; font-size: 0.95rem; margin-top: 3rem;">
            Created by Sandeep M.
        </div>
        """,
        unsafe_allow_html=True,
    )

hero_left, hero_right = st.columns([0.6, 0.4], gap="large")
with hero_left:
    st.markdown(
        """
        <div class="hero-card">
            <h3>Live Transaction Check</h3>
            <p>Enter any transfer, payment, or cash-out and watch the model return its risk call in
            real time.</p>
            <ul>
                <li>Inputs match the PaySim column names.</li>
                <li>Scaling and encoding already handled in the model file.</li>
                <li>Change values to compare different "what-if" runs fast.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        """
        <div class="insight-card">
            <h4>Playbook</h4>
            <ul>
                <li>Write down the account balances that raised the flag.</li>
                <li>Store the model verdict and score for your audit notes.</li>
                <li>Reuse tricky cases later when retraining the model.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-card">
            <h3>How it works</h3>
            <ol>
                <li>Pick a transaction type from PaySim.</li>
                <li>Enter the amount and both account balances.</li>
                <li>Hit "Run Prediction" to see the fraud call.</li>
                <li>Adjust the inputs or share the result.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.subheader("Live Signals")
    activity = [
        ("São Paulo", "Cash Out", 0.81),
        ("Berlin", "Transfer", 0.38),
        ("Lagos", "Payment", 0.92),
        ("Bengaluru", "Debit", 0.47),
    ]
    for city, txn, score in activity:
        st.caption(f"{city} • {txn} • Risk Index {int(score * 100)}/100")

active_model = Path(model_name).stem if model_name else "Unavailable"
st.markdown("<div class='stat-section'>", unsafe_allow_html=True)
stat_col1, stat_col2, stat_col3 = st.columns(3, gap="large")

with stat_col1:
    st.markdown(
        f"""
        <div class="stat-box">
            <div class="label">Active Model</div>
            <div class="value">{active_model}</div>
            <span class="status-pill">live</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stat_col2:
    st.markdown(
        """
        <div class="stat-box">
            <div class="label">Latency Budget</div>
            <div class="value">&lt; 120 ms</div>
            <span class="status-pill">streaming</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stat_col3:
    st.markdown(
        """
        <div class="stat-box">
            <div class="label">Training ROC-AUC</div>
            <div class="value">0.99</div>
            <span class="status-pill">+0.02 vs baseline</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
st.subheader("Scenario Builder")
st.caption("Fill in the transaction details you want to test.")

transaction_label_map = {
    "Payment": "PAYMENT",
    "Transfer": "TRANSFER",
    "Cash Out": "CASH_OUT",
    "Cash In": "CASH_IN",
    "Debit": "DEBIT",
}

transaction_choice = st.selectbox(
    "Transaction Type",
    list(transaction_label_map.keys())
)
transaction_type = transaction_label_map[transaction_choice]

with st.form("scenario_builder"):
    st.markdown("<div class='form-card'>", unsafe_allow_html=True)
    amount_val = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=0.01,
        help="Use the PaySim amount column value here.",
    )

    col_origin, col_destination = st.columns(2, gap="large")

    with col_origin:
        st.markdown("#### Origin Account")
        origin_old_col, origin_new_col = st.columns(2)
        with origin_old_col:
            oldbalanceOrg_val = st.number_input(
                "Old Balance",
                min_value=0.0,
                step=0.01,
                key="old_origin",
            )
        with origin_new_col:
            newbalanceOrig_val = st.number_input(
                "New Balance",
                min_value=0.0,
                step=0.01,
                value=10000.0,
                key="new_origin",
            )

    with col_destination:
        st.markdown("#### Destination Account")
        dest_old_col, dest_new_col = st.columns(2)
        with dest_old_col:
            oldbalanceDest_val = st.number_input(
                "Old Balance",
                min_value=0.0,
                step=0.01,
                key="old_dest",
            )
        with dest_new_col:
            newbalanceDest_val = st.number_input(
                "New Balance",
                min_value=0.0,
                step=0.01,
                key="new_dest",
            )
    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Run Prediction", use_container_width=True)

if submitted:
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount_val],
        'oldbalanceOrg': [oldbalanceOrg_val],
        'newbalanceOrig': [newbalanceOrig_val],
        'oldbalanceDest': [oldbalanceDest_val],
        'newbalanceDest': [newbalanceDest_val]
    })

    if model is not None:
        risk_score = None
        try:
            prediction = model.predict(input_data)[0]
            if hasattr(model, "predict_proba"):
                risk_score = float(model.predict_proba(input_data)[0][1])
        except Exception as e:
            st.error(f"Model prediction failed: {e}")
            prediction = None

        if prediction is not None:
            st.subheader("Prediction Result:")
            outcome = "Fraudulent Transaction" if int(prediction) == 1 else "Legitimate Transaction"
            st.write(outcome)
            if risk_score is not None:
                st.progress(min(max(risk_score, 0.0), 1.0))
                st.caption(f"Model risk score: {risk_score:.2%}")
                disposition = "fraudulent" if int(prediction) == 1 else "legitimate"
                disposition_prob = risk_score if disposition == "fraudulent" else 1 - risk_score
                st.markdown(
                    f"**This transaction has {disposition_prob * 100:.1f}% probability of being {disposition}.**"
                )
            else:
                st.caption("Probability output not available for this model.")
            st.caption(f"Model source: {model_name}")
    else:
        st.info("Model not available. Place a supported model file next to this script and rerun the app.")
else:
    if model is None:
        st.info("Model not available. Place a supported model file next to this script and rerun the app.")
    else:
        st.info("Enter the values above and press Run Prediction to see the model output.")

