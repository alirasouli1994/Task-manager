import sqlite3
from pathlib import Path
import hashlib
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

db_path = Path()
db_path = db_path / "db.sqlite3"
#salam
def execute_db(f):
    def wrapper(*args,**kwargs):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(f(*args,**kwargs))
            connection.commit()
            result= cursor.fetchone()
        return result
    return wrapper

# create_table = execute_db(create_table)


class User:

    is_table_created = False
    db_path = None

    def __init__(self,username,password) -> None:
        if not User.is_table_created:
            db_path = Path()
            db_path = db_path / "db.sqlite3"
            self.create_table()

        self.username=username
        self.password = self.hash_password(password.encode())
        self.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.last_login=None

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password).hexdigest()

    #regesteruser
    @execute_db
    def save(self):
        return f"""insert into user (username,password,create_at,last_login) values
            ('{self.username}',
            '{self.password}',
            '{self.create_at}',
            '{self.last_login}');"""
    
    # user login
    @execute_db
    def user_login(self):
        #T = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        #(f"update user set last_login = '{T}' where username = '{self.username}' and password = '{self.password}' ;") 
        return (f"select username from user where username = '{self.username}' and password = '{self.password}';")                                                                                                                 

       
    

    @classmethod
    def create_table(cls):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            connection.commit()
            cursor.execute("""create table if not exists user(
                user_id integer primary key,
                username text,
                password text,
                create_at text,
                last_login text);""")
            connection.commit()
        cls.is_table_created = True


# def create_table_user():
#     with sqlite3.connect(db_path) as connection:
#         cursor = connection.cursor()
#         cursor.execute("""create table user(
#             id integer primary key,
#             username text,
#             password text,
#             create_at text,
#             last_login text);""")
#         connection.commit()

# if __name__ == "__main__":
#     a = User('mohammad',b'123')
#     a.save()




