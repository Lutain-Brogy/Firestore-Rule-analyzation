import streamlit as st

st.title("Firestore RuleSense")

mode = 'normal'
#else mode == 'teaching'

choice = st.selectbox(
    "What rule would you like to write?",
    [
        "Allow read only",
#        "Allow write only",
 #       "Allow read and write",
  #      "Deny all access",
   #     "Custom (one allowed, one denied)"
        
    ]
)

if choice == "Allow read only":

    edit_choice = st.selectbox(
        "Select read rule type:",
        [
            "read public access",
            "read authenticated access",
        ]
    )

