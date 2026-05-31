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

