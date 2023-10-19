import psycopg2

def get_conexion_db():

    conexion = psycopg2.connect(
        host="tu_host",
        database="tu_base_de_datos",
        user="tu_usuario",
        password="tu_contraseña"
    )
    return conexion
