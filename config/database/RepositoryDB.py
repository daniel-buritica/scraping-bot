from ConfigConexionDB import get_connection
from psycopg2 import sql


def insert_db(data):
    conection = get_connection()
    cur = conection.cursor()
    insert_query = sql.SQL("insert into product (name, price, origin) values ({}, {}, {})")
    cur.execute(insert_query.format(sql.Literal(data.name), sql.Literal(data.price), sql.Literal(data.origin)))
    conection.commit()
    cur.close()
