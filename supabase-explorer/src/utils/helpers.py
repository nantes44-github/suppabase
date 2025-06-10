def validate_supabase_url(url):
    if not url.startswith("https://"):
        raise ValueError("The Supabase URL must start with 'https://'")
    return url

def validate_api_key(api_key):
    if not api_key:
        raise ValueError("API key cannot be empty")
    return api_key

def format_table_data(table_name, records):
    formatted_data = f"Table: {table_name}\n"
    for record in records:
        formatted_data += f"{record}\n"
    return formatted_data.strip()