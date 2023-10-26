from config.database.ConfigConexionDB import get_connection
from psycopg2 import sql
from model.Product import Product

def insert_db(data):
    data.name = "title"
    data.price = 134
    conection = get_connection()
    cur = conection.cursor()
    insert_query = sql.SQL("insert into product (name, price, image, origin) values ({}, {}, {}, {})")
    cur.execute(insert_query.format(sql.Literal(data.name), sql.Literal(data.price), sql.Literal(data.origin),
                                    sql.Literal(data.image)))
    conection.commit()
    cur.close()
