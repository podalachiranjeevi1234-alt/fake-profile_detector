import streamlit as st
from db import add_user, login_user

def signup():
    st.subheader("📝 Signup")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        try:
            add_user(username, password)
            st.success("Account created successfully ✅")
        except:
            st.error("Username already exists ❌")


def login():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
        else:
            st.error("Invalid credentials ❌")