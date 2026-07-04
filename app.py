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
                    "Open guider",
                    "🌍 Public Access",
                    "🔐 Authentication",
                    "👤 User Identity",
                    "👥 Ownership & Membership",
                    "🛡️ Roles & Permissions",
                    "📅 Time-Based Rules",
                    "📄 Document-Based Rules",
                    "🔗 Cross-Document Checks"
                ]
            )

        if read == '🌍 Public Access':
                A = st.text_input('The collection')
                B = st.text_input("The document")
                C = st.text_input('The subcollection')
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

    match /{A}/{B}/{C}/{D} {{
      allow read: if {E};
    }}

  }}
}}
""")
            

        
            
