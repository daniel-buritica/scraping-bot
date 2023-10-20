import psycopg2


def get_connection():
    global conection
    try:
        conection = psycopg2.connect(
            host="localhost",
            database="webscraping",
            user="postgres",
            password="admin",
            port="5432"
        )
    except Exception as e:
        print(f"Fail Connection data base : {e}")

    return conection
