from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
import bcrypt
from supabase import create_client

# Import supabase client
SUPABASE_URL = 'https://gjrylpzkgoohprwurzev.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdqcnlscHprZ29vaHByd3VyemV2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5Mjg3ODMsImV4cCI6MjA1NzUwNDc4M30.DX0qc0_mO69L51A9vJE67Ui6jy2_FefbdlVnFsZ60AM'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create a Blueprint for routes
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def home():
    return render_template('index.html')

# Route to display the registration form
@routes_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Verifica que las contraseñas coincidan
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return render_template('register.html')

        # Hashear la contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Verifica si el email ya está registrado
        response = supabase.table('user').select('*').eq('email', email).execute()
        if response.data:
            flash('El correo ya está registrado', 'error')
            return render_template('register_error.html')

        # Inserta el nuevo usuario en Supabase
        supabase.table('user').insert({'email': email, 'password': hashed_password}).execute()

        flash('Registro exitoso', 'success')
        return render_template('register_success.html')

    return render_template('register.html')

# Route to display the login form
@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Verifica si el usuario existe en la base de datos
        response = supabase.table('user').select('*').eq('email', email).execute()
        user = response.data[0] if response.data else None

        if user:
            # Verifica la contraseña
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                flash('Inicio de sesión exitoso', 'success')
                return render_template('success_login.html')
            else:
                flash('Contraseña incorrecta', 'error')
                return render_template('error_login.html')
        else:
            flash('El correo no está registrado', 'error')
            return render_template('error_login.html')

    return render_template('login.html')
