import requests

class SupabaseConnector:
    def __init__(self, url, api_key, auth_token=None):
        self.url = url
        self.api_key = api_key
        self.auth_token = auth_token
        self.headers = {
            "apikey": self.api_key,
            "Authorization": f"Bearer {self.auth_token}" if self.auth_token else None
        }

    def connect(self):
        # Here you would typically use a library like requests to establish a connection
        # For example, you could test the connection by making a simple request
        response = requests.get(f"{self.url}/rest/v1/", headers=self.headers)
        if response.status_code == 200:
            return True
        else:
            raise Exception("Connection failed: " + response.text)

    def list_tables(self):
        response = requests.get(f"{self.url}/rest/v1/", headers=self.headers)
        if response.status_code == 200:
            return response.json()["paths"]  # Assuming the response is a JSON list of tables
        else:
            raise Exception("Failed to list tables: " + response.text)

    def get_records(self, table_name):
        response = requests.get(f"{self.url}/rest/v1/{table_name}?limit=1", headers=self.headers)
        if response.status_code == 200:
            return response.json()  # Assuming the response is a JSON list of records
        #else:
            #raise Exception(f"Failed to get records from {table_name}: " + response.text)