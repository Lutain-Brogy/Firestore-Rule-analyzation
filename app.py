import streamlit as st

st.title("Firestore RuleSense")

mode = 'normal'
#else mode == 'teaching'

choice = st.selectbox(
"What type of rule do you want?", 
   [
        "An allow read only",
#        "Allow write only",
 #       "Allow read and write",
  #      "Deny all access",
   #     "Custom (one allowed, one denied)"
        
    ]
)

if choice == "An allow read only":
    edit_choice = st.selectbox(
        "Select the read rule typeyou want:",
       [
            "read public access",
            "read authenticated access",
          #  "read role-based access",
           # "read owner-based access",
            #"read shared list access",
            #"read time-based access",
            #"read field-based conditions"
        ]
    )







      
