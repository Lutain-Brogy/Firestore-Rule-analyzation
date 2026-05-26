import streamlit as st
st.title("Firestore rule Analyzer")

user_line = st.text_input("Type the first Firestore rule line")

correct_first_line = "service cloud.firestore {"

user_line = "service cloud.firestore {"

if user_line == correct_first_line:
    st.write("Correct first line.")
    st.code(f"{user_line}")
else:
    st.write("The first line is wrong.")
