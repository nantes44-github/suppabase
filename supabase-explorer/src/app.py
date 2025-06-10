import streamlit as st
from supabase_connector import SupabaseConnector

def main():
    st.title("Supabase Explorer")

    # User input for Supabase credentials
    supabase_url = st.text_input("Supabase URL", placeholder="https://your-project.supabase.co")
    supabase_api_key = st.text_input("API Key", type="password", placeholder="your-api-key")
    supabase_auth_token = st.text_input("Authorization Token (optional)", type="password", placeholder="your-auth-token_without_bearer")

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
            st.write("Tables:")
            for table in tables:
                st.write(f"- {table}")
                records = connector.get_records(table)
                st.write("First record:")
                st.write(records)
        else:
            st.write("No tables found.")

if __name__ == "__main__":
    main()