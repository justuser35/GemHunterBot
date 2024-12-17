import mysql.connector
from config import host, user, password, db_name

db = mysql.connector.connect(
    host=host,
    user=user,
    password="password"
)