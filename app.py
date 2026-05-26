import streamlit as st

st.title("Your database is exposed checker")

mode = "normal"  # later you can change this to selectbox

correct_first_line = "service cloud.firestore {"

user_line = st.text_input("Type the first Firestore rule line")

if user_line:

    if user_line == correct_first_line:
        st.write('Correct first line') 
        st.code(f'user_line')

    else:
        st.error("The first line is wrong.")

        min_len = min(len(user_line), len(correct_first_line))

        for i in range(min_len):

            if user_line[i] != correct_first_line[i]:

                st.write(
                    f"Error at position {i+1}: "
                    f"expected '{correct_first_line[i]}' but got '{user_line[i]}'"
                )

        if len(user_line) != len(correct_first_line):
            st.warning("Length mismatch between input and expected rule.")

b = user_line

correct_second_line = f"match /database/{b} {{"

user_line = st.text_input("Type second line")

if user_line:

    if user_line == correct_second_line:
        st.write("Correct second line")
        st.code(user_line)

    else:
        st.write("The second line is wrong")

        min_len = min(len(user_line), len(correct_second_line))

        for i in range(min_len):

            if user_line[i] != correct_second_line[i]:

                st.write(
                    f"Error at position {i+1}: "
                    f"Expected '{correct_second_line[i]}' but got '{user_line[i]}'"
                )

        if len(user_line) != len(correct_second_line):
            st.warning("Length mismatch between input and expected rule.")
