import streamlit as st
import joblib
import pandas as pd
from auth import login, signup

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Fake Profile Detector", page_icon="🕵️")

# ---------------- BACKGROUND STYLE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #00BFFF);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = ""

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- AUTH SECTION ----------------
if not st.session_state["logged_in"]:

    st.title("🔐 Authentication System")

    choice = st.radio("Choose", ["Login", "Signup"])

    if choice == "Login":
        login()
    else:
        signup()

# ---------------- MAIN APP ----------------
else:
    st.title(f"🕵️ Welcome {st.session_state['user']}")

    if st.button("🚪 Logout"):
        logout()

    st.subheader("Fake Profile Detection AI")

    # ---------------- INPUTS ----------------
    followers = st.number_input("👥 Followers", 0)
    following = st.number_input("➡️ Following", 0)
    posts = st.number_input("📝 Posts", 0)
    bio_length = st.number_input("📄 Bio Length", 0)
    profile_pic = st.selectbox("🖼️ Profile Pic (1=Yes, 0=No)", [0, 1])

    # ---------------- PREDICTION ----------------
    if st.button("🚀 Predict"):

        # ✅ FIX: DataFrame with correct feature names
        input_data = pd.DataFrame([{
            "followers": followers,
            "following": following,
            "posts": posts,
            "bio_length": bio_length,
            "profile_pic": profile_pic
        }])

        pred = model.predict(input_data)
        prob = model.predict_proba(input_data)

        # ---------------- CLASS HANDLING (SAFE) ----------------
        real_prob = prob[0][list(model.classes_).index(0)]
        fake_prob = prob[0][list(model.classes_).index(1)]

        # ---------------- RESULT ----------------
        if pred[0] == 1:
            st.error("⚠️ FAKE PROFILE")
        else:
            st.success("✅ REAL PROFILE")

        # ---------------- PROBABILITIES ----------------
        st.write("Real probability:", real_prob)
        st.write("Fake probability:", fake_prob)
