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

    if edit_choice == "read public access":
       st.write('Write  all values then copy rule') 

    user_input = st.text_input("A, the collection")
    A = user_input

    B_input = st.text_input("B, the document")
    C_input = st.text_input("C, the subcollection")
    D_input = st.text_input("D value")

    B = A if B_input == "any" else B_input
    C = B if C_input == "any" else C_input
    D = C if D_input == "any" else D_input

    st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{{{B}}}/{C}/{{{D}}} {{

      allow read: if request.auth != null;

    }}
  }}
}}
""")

if edit_choice == 'read authenticated access':

    auth_choice = st.selectbox(
        'Select your authentication type of rule',
        ["only creater can read",
         "role-based",
         "custorm based",
         "time based"]
    )
        if auth_choice == 'only creater can read':
           st.write('Write  all values then copy rule') 

           user_input = st.text_input("A, the collection")
           A = user_input

           B_input = st.text_input("B, the document")
           C_input = st.text_input("C, the subcollection")
           D_input = st.text_input("D value")

           B = A if B_input == "any" else B_input
           C = B if C_input == "any" else C_input
           D = C if D_input == "any" else D_input

        st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{{{B}}}/{C}/{{{D}}} {{

      allow read: if request.auth != null
                  && request.auth.token.admin == true;

    }}
  }}
}}
""")
