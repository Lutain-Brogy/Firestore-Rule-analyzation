import streamlit as st

st.title("Firestore RuleSense")

choice = st.selectbox(
    "Choose a mode",
    ["Standard operation", "Learning mode"]
)

if choice == 'Standard operation':
   rule1, rule2, rule3, rule4 = st.tabs(["read type", "write type" , "create role", "read and write type"])

with rule1:
st.write('hey')
