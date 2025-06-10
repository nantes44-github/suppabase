# Supabase Explorer

Supabase Explorer is a Streamlit application that allows users to connect to a Supabase database and explore its tables and records. This project provides a user-friendly interface to list tables and retrieve the first 10 records from each table.

## Features

- Connect to a Supabase database using the Supabase URL, API key, and optional authorization token.
- List all tables available in the connected Supabase database.
- Fetch and display the first 10 records from each table.

## Requirements

To run this project, you need to have the following dependencies installed:

- Streamlit
- Supabase client library
- Any other required libraries listed in `requirements.txt`

## Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/supabase-explorer.git
   cd supabase-explorer
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Supabase credentials. You can use the `.env.example` file as a reference.

5. Run the Streamlit application:

   ```
   streamlit run src/app.py
   ```

## Usage

- Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
- Enter your Supabase URL, API key, and optional authorization token in the input fields.
- Click on the button to connect and explore the database.
- View the list of tables and their first 10 records displayed in the application.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.