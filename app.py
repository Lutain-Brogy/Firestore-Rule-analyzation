import streamlit as st

st.title("Firestore Rule Analyzer")

user_line = st.text_input("Type the first Firestore rule line")

correct_first_line = "service cloud.firestore {"

if user_line:  # only run after user types something

    if user_line == correct_first_line:
        st.success("Correct first line.")
        st.code(user_line)
    else:
        st.error("The first line is wrong.")
        st.code(f"Expected: {correct_first_line}")
        st.code(f"Got: {user_line}")
