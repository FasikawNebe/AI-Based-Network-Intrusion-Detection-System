
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "nsl_kdd_random_forest_pipeline.joblib"

# NSL-KDD features
FEATURES = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "land", "wrong_fragment",
    "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells",
    "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
    "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
]

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

st.title("🛡️ AI-Based Network Intrusion Detection System")
st.write(
    "Upload network traffic records to identify normal "
    "traffic and potential security anomalies."
)

st.info(
    "This is an educational decision-support prototype. "
    "It does not automatically block network traffic."
)

try:
    model = load_model()
    st.success("Random Forest model loaded successfully.")
except Exception as error:
    st.error(f"Could not load model: {error}")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload network traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        missing = [col for col in FEATURES if col not in data.columns]

        if missing:
            st.error(
                "Your CSV is missing required features: "
                + ", ".join(missing)
            )
            st.stop()

        X = data[FEATURES].copy()

        st.subheader("Uploaded data")
        st.write(f"Records uploaded: {len(X)}")
        st.dataframe(X.head())

        if st.button("Analyze Network Traffic", type="primary"):
            predictions = model.predict(X)
            probabilities = model.predict_proba(X)[:, 1]

            results = pd.DataFrame({
                "Prediction": [
                    "Anomaly" if value == 1 else "Normal"
                    for value in predictions
                ],
                "Anomaly Probability (%)": (
                    probabilities * 100
                ).round(2)
            })

            final_results = pd.concat(
                [data.reset_index(drop=True), results],
                axis=1
            )

            st.subheader("Detection Results")

            total = len(predictions)
            anomalies = int((predictions == 1).sum())
            normal = total - anomalies

            col1, col2, col3 = st.columns(3)
            col1.metric("Total records", total)
            col2.metric("Normal records", normal)
            col3.metric("Potential anomalies", anomalies)

            st.dataframe(final_results)

            st.download_button(
                "Download prediction results",
                data=final_results.to_csv(index=False).encode("utf-8"),
                file_name="intrusion_detection_results.csv",
                mime="text/csv"
            )

    except Exception as error:
        st.error(f"Unable to process the CSV file: {error}")
