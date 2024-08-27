import pymysql
import logging
from dotenv import load_dotenv
import os

def ConexionMobonet():
    try:
        conn = pymysql.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), db=os.getenv('DB_NAME'))
        return conn
    except pymysql.MySQLError as e:
        logging.error(f"Error conectando a la base de datos: {e}")
        raise