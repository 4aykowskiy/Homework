import sqlite3
with sqlite3.connect("Homework.db") as db:
    cursor=db.cursor()
    query="""CREATE TABLE IF NOT EXISTS users(
    PRIMARI KEY,
    name TEXT,
    login TEXT,
    password INTEGER
    )"""
    cursor.execute(query)
db.commit()