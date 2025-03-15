from flask import Flask
from extensions import db, cors
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = 'https://gjrylpzkgoohprwurzev.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdqcnlscHprZ29vaHByd3VyemV2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3ODMsImV4cCI6MjA1NzUwNDc4M30.DX0qc0_mO69L51A9vJE67Ui6jy2_FefbdlVnFsZ60AM'

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to create and configure the Flask app
def create_app():
    app = Flask(__name__)

    # Database configuration (PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mauro0811...M@db.gjrylpzkgoohprwurzev.supabase.co:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)

    # Import and register the routes
    from routes import routes_bp
    app.register_blueprint(routes_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
