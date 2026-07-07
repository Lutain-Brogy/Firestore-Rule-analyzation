import streamlit as st

st.title("Firestore RuleSense")

choice = st.selectbox(
    "Choose a mode",
    ["Standard operation", "Learning mode"]
)

if choice == 'Standard operation':
    rule1, rule2, rule3, rule4 = st.tabs(
        ["read type", "write type", "create role", "read and write type"]
    )

    with rule1:
        read = st.selectbox(
                'Select the read type of your choice',
                [
                    "🌍 Public",
                    "🔐 Authentication",
                    "👥 Ownership & Membership",
                    "📅 Time-Based Rules",
                    "📄 Document-Based Rules",
                    "🔗 Cross-Document Checks",
                    "Open guider"
                ]
            )

        if read ==  "🌍 Public":
                A = st.text_input('The collection')
                B = st.text_input("The document")     
                D_choice = st.selectbox("type?",
                                        ["Any", "your own"])
                if D_choice == "Any":
                     D = "{any}"
                else:
                     user_input = st.text_input("Enter your wildcard")
                     D = user_input 
                     
                E = st.selectbox('Choose permission',
                    ["deny", "allow"])
                if E == "allow":
                     E = "true"
                else:
                     E = "false"

                st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{B}/{D} {{
      allow read: if {E};
    }}

  }}
}}
""")
        
        
        if read == "🔐 Authentication":
                A = st.text_input('The collection')
                B = st.text_input("The document")
                D_choice = st.selectbox("type?",
                                        ["Any", "your own"])
                if D_choice == "Any":
                     D = "{any}"
                else:
                     user_input = st.text_input("Enter your wildcard")
                     D = user_input 
                E = st.selectbox('Choose permission type',
                                 ["deny","allow"])
                if E == 'allow':
                    E = '!'
                else:
                    E = '='
               
                F_choice = st.selectbox('Choose permission',
    ["Logged in", "Owner only", "Admin", "Specific UID", "Role based"]
)


                if F_choice == "Owner only":
                    rule = "&& request.auth.uid == resource.data.ownerId"

                elif F_choice == "Admin":
                    rule = "&& request.auth.token.role == 'admin'"

                elif F_choice == "Specific UID":
                    G = st.text_input('UID')
                    rule = f"&& request.auth.uid == '{G}'"

                elif F_choice == "Role based":
                    G = st.text_input('Selected role')
                    rule = f"&& request.auth.token.role == '{G}'"
                else:  # Logged in
                    rule = ""
                    
                st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{B}/{D} {{

      allow read: if request.auth {E}= null
                  {rule}

    }}

  }}
}}
""")
                if read == '📅 Time-Based Rules':
                   st.write('hello')
            

        
            
