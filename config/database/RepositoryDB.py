from config.database.ConfigConexionDB import get_connection
from psycopg2 import sql
from model.Product import Product


def insert_db(data):
    conection = get_connection()
    cur = conection.cursor()
    insert_query = sql.SQL("insert into product (name, price, image, origin) values ({}, {}, {}, {})")
    cur.execute(insert_query.format(sql.Literal(data.name), sql.Literal(data.price), sql.Literal(data.image),
                                    sql.Literal(data.origin)))
    conection.commit()
    cur.close()



