import streamlit as st

st.title("Firestore RuleSense")

choice = st.selectbox(
    "Choose a mode",
    ["Standard operation", "Learning mode"]
)
