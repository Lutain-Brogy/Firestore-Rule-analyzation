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
                    "🌍 Public/logged in Access",
                    "🔐 Authentication",
                    "👤 User Identity",
                    "👥 Ownership & Membership",
                    "📅 Time-Based Rules",
                    "📄 Document-Based Rules",
                    "🔗 Cross-Document Checks",
                    "Open guider"
                ]
            )

        if read ==  "🌍 Public/logged in Access":
            face = st.selectbox('Choose type',
                                 ["Public","Logged in"])
            if face == 'Logged in':
              A = st.text_input('The collection')
              B = st.text_input("The document")
              C = st.text_input('The subcollection')
              D_choice = st.selectbox("type?",
                                 ["Any", "your own"])
              if D_choice == "Any":
                  D = "{any}"
              else:
                  D = st.text_input("Enter your wildcard")
                  st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{B}/{C}/{D} {{

      allow read: if request.auth != null;

    }}

  }}
}}
""")       
            if face == 'Public':
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
        
        
        if read == "🔐 Authentication":
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
                E = st.selectbox('Choose permission type',
                                 ["deny","allow"])
                if E == 'allow':
                    E = '!'
                else:
                    E = '='
               
                F_choice = st.selectbox('Choose permission',
    ["Logged in", "Owner only", "Admin", "Specific UID", "Role based"]
)

user_input = st.text_input("Enter value (UID or Role)")

mapping = {

    'Owner only' = "&& request.auth.uid == resource.data.ownerId",

    'Admin' = "&& request.auth.token.role == 'admin'",

    'Specific UID' = f"&& request.auth.uid == '{user_input}'",

    'Role based' = f"&& request.auth.token.role == '{user_input}'",

    "Logged in" = ""
}
mapping = F_choice


st.code(f"""
rules_version = '2';

service cloud.firestore {{
  match /databases/{{database}}/documents {{

    match /{A}/{B}/{C}/{D} {{

      allow read: if request.auth {E}= null
                  {F_choice}

    }}

  }}
}}
""")
            

        
            
