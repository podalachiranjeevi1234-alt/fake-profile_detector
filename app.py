import streamlit as st
import joblib
import numpy as np
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
from auth import login, signup

st.set_page_config(page_title="Fake Profile Detector", page_icon="🕵️")

# INIT SESSION
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ---------------- LOGOUT ----------------
def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = ""

# ---------------- ML MODEL ----------------
model = joblib.load("model.pkl")

# ---------------- AUTH PAGE ----------------
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

    followers = st.number_input("👥 Followers", 0)
    following = st.number_input("➡️ Following", 0)
    posts = st.number_input("📝 Posts", 0)
    bio_length = st.number_input("📄 Bio Length", 0)
    profile_pic = st.selectbox("🖼️ Profile Pic (1=Yes, 0=No)", [0, 1])

    if st.button("🚀 Predict"):

        data = np.array([[followers, following, posts, bio_length, profile_pic]])

        pred = model.predict(data)
        prob = model.predict_proba(data)

        if pred[0] == 1:
            st.error("⚠️ FAKE PROFILE")
        else:
            st.success("✅ REAL PROFILE")

        st.write("Fake:", prob[0][1])
        st.write("Real:", prob[0][0])