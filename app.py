import streamlit as st

st.title("Firestore RuleSense")

mode = 'normal'
#else mode == 'teaching'

choice = st.selectbox(
    "What rule would you like to write?",
    [
        "Allow read only",
        "Create role",
#        "Allow write only",
 #       "Allow read and write",
  #      "Deny all access",
   #     "Custom (one allowed, one denied)"
        
    ]
)

#if choice == "create role":
 #   A = st.text_input("Create your role(s)")

  #  st.code(f"""
#admin.auth().setCustomUserClaims(uid, {{
 # role: "{A}"
#}});
#""")

if choice == "Allow read only":

    edit_choice = st.selectbox(
        "Select read rule type:",
        [
            "read public access",
            "read authenticated access",
        ]
    )
    if edit_choice == "read public access":
       st.write(f"Write all values then copy rule")

       A = st.text_input("A, the collection")
       B = st.text_input("B, the document")
       C = st.text_input("C, the subcollection")
       D = st.text_input("D value")

    
       B = A if B == "any" else B
       C = B if C == "any" else C
       D = C if D == "any" else D

       st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{{{B}}}/{C}/{{{D}}} {{

      allow read: if true;

    }}
  }}
}}
""")
        
    elif edit_choice == "read authenticated access":

          auth_choice = st.selectbox(
          "Select your authentication type of rule",
        [
            "logged in users",
            "only admin can read",
            "role-based",
            "custom based",
            "time based"
        ]
    )
          if auth_choice == "only admin can read":
              st.write("Write all values then copy rule")

              A = st.text_input("A, the collection")
              B = st.text_input("B, the document")
              C = st.text_input("C, the subcollection")
              D = st.text_input("D value")

              B = A if B == "any" else B
              C = B if C == "any" else C
              D = C if D == "any" else D
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
          elif auth_choice == 'custom based':
              st.write("Talk to Lutzet for this one, don’t worry he doesn’t charge.")

        
          elif auth_choice == 'logged in users':
               st.write("Write all values then copy rule")

               A = st.text_input("A, the collection")
               B = st.text_input("B, the document")
               C = st.text_input("C, the subcollection")
               D = st.text_input("D value")

               B = A if B == "any" else B
               C = B if C == "any" else C
               D = C if D == "any" else D

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

          elif auth_choice == 'role-based':
               st.write("Write all values then copy rule")
               A = st.text_input("A, the collection")
               B = st.text_input("B, the document")
               C = st.text_input("C, the subcollection")
               D = st.text_input("D value")
               E = st.text_input("Roles that can read, sapce by using ',' ") 

               B = A if B == "any" else B
               C = B if C == "any" else C
               D = C if D == "any" else D
              
               st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{{{B}}}/{C}/{{{D}}} {{

      allow read: if request.auth != null
                  && (
                    request.auth.token.role in [{E}]
                  );

      allow write: if request.auth != null
                   && request.auth.token.role == "admin";

    }}
  }}
}}
""")

          elif auth_choice == 'time based':
               st.write("Write all values then copy rule")
               A = st.text_input("A, the collection")
               B = st.text_input("B, the document")
               C = st.text_input("C, the subcollection")
               D = st.text_input("D value")
               E = st.text_input('From whem?')
               F = st.text_input('To when?')
        
               B = A if B == "any" else B
               C = B if C == "any" else C
               D = C if D == "any" else D
               st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{{{B}}}/{C}/{{{D}}} {{

      allow read: if request.auth != null
                  && request.time.hours >= {E}
                  && request.time.hours < {F};

      allow write: if false;

    }}
  }}
}}
""")
              
