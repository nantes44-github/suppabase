import streamlit as st
import json
from supabase_connector import SupabaseConnector

def main():
    st.title("Supabase Explorer")
    
    # Initialiser le stockage des profils dans session_state
    if 'profiles' not in st.session_state:
        st.session_state.profiles = {}
    if 'current_profile' not in st.session_state:
        st.session_state.current_profile = "Default"
    
    # Sélection ou création de profil
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Ajouter "New profile" à la liste des profils existants
        profile_options = list(st.session_state.profiles.keys())
        if "New profile" not in profile_options:
            profile_options.append("New profile")
        
        selected_profile = st.selectbox(
            "Select or create a profile", 
            options=profile_options,
            index=profile_options.index(st.session_state.current_profile) if st.session_state.current_profile in profile_options else 0
        )
    
    with col2:
        # Champ pour le nom du nouveau profil
        if selected_profile == "New profile":
            new_profile_name = st.text_input("New profile name", key="new_profile_name")
    
    # Utiliser les valeurs du profil sélectionné si disponibles
    if selected_profile != "New profile" and selected_profile in st.session_state.profiles:
        profile_data = st.session_state.profiles[selected_profile]
        default_url = profile_data.get('url', '')
        default_api_key = profile_data.get('api_key', '')
        default_auth_token = profile_data.get('auth_token', '')
        default_limit = profile_data.get('limit', 10)
    else:
        default_url = ''
        default_api_key = ''
        default_auth_token = ''
        default_limit = 10
    
    # User input for Supabase credentials
    supabase_url = st.text_input("Supabase URL", value=default_url, placeholder="https://your-project.supabase.co")
    supabase_api_key = st.text_input("API Key", value=default_api_key, type="password", placeholder="your-api-key")
    supabase_auth_token = st.text_input("Authorization Token (optional)", value=default_auth_token, type="password", placeholder="your-auth-token_without_bearer")
    
    # Add a number input for record limit
    records_limit = st.number_input("Number of records to retrieve per table", min_value=1, max_value=100, value=default_limit)
    
    # Save button
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Save profile"):
            profile_name = selected_profile
            if selected_profile == "New profile":
                if not st.session_state.get("new_profile_name"):
                    st.error("Please enter a name for the new profile")
                    return
                profile_name = st.session_state.new_profile_name
            
            # Sauvegarder le profil
            st.session_state.profiles[profile_name] = {
                'url': supabase_url,
                'api_key': supabase_api_key,
                'auth_token': supabase_auth_token,
                'limit': records_limit
            }
            st.session_state.current_profile = profile_name
            st.success(f"Profile '{profile_name}' saved!")
            st.rerun()  # Remplacé experimental_rerun par rerun
    
    with col2:
        if st.button("Connect"):
            if not supabase_url or not supabase_api_key:
                st.error("Please provide both Supabase URL and API Key.")
                return

            # Connect to Supabase
            connector = SupabaseConnector(supabase_url, supabase_api_key, supabase_auth_token)
            connector.connect()

            # List tables
            tables = connector.list_tables()
            if tables:
                st.write("### Tables:")
                for table in tables:
                    with st.expander(f"Table: {table}", expanded=False):
                        records = connector.get_records(table, limit=records_limit)
                        st.write(f"First {records_limit} records:")
                        st.write(records)
            else:
                st.write("No tables found.")
    
    # Pour le débogage - afficher les profils sauvegardés
    if st.checkbox("Show saved profiles"):
        st.json(st.session_state.profiles)

if __name__ == "__main__":
    main()