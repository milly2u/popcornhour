# MilisPopcornHour

Este es un proyecto web creado con **Flask**, **Flask-Login**, **Flask-SQLAlchemy** y conectado a **Supabase** como base de datos PostgreSQL.

### Funcionalidades principales:
- **Registro y autenticación de usuarios** utilizando Flask-Login.
- **Visualización de películas** desde la base de datos.
- **Comentarios de películas** donde los usuarios pueden añadir opiniones y calificaciones.

### Requisitos

1. **Python** 3.x
2. **Flask**
3. **Flask-Login**
4. **Flask-SQLAlchemy**
5. **psycopg2** para la conexión con PostgreSQL.

### Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Crea un entorno virtual y activa el entorno:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate  # En Windows
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

4. Crea las tablas en la base de datos ejecutando el siguiente comando:

    ```bash
    python app.py
    ```

5. Abre tu navegador y visita:

    ```bash
    http://localhost:5000
    ```

### Configuración de Supabase

Este proyecto utiliza **Supabase** como base de datos PostgreSQL. Para conectar tu aplicación a Supabase, asegúrate de configurar correctamente tu URI de base de datos en el archivo `app.py`.

### Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
