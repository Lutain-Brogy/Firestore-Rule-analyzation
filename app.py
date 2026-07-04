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
                D = st.selectbox(
                   'type',
                    ["Any", "your own"]
                )
                E = st.selectbox(["deny", "allow"])

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

        
            
