import sqlite3
import s11
from pathlib import Path
import hashlib
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

db_path = Path()
db_path = db_path / "db.sqlite3"

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


class Task:

    is_table_created = False
    db_path = None

    def __init__(self,description,username,deadline) -> None:
        if not Task.is_table_created:
            db_path = Path()
            db_path = db_path / "db.sqlite3"
            self.create_table()

        self.description= description
        self.is_done= 0
        self.dead_line= deadline
        self.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.last_update=0
        self.username= username
        
    
    #save task
    @execute_db
    def save_task(self):
        user_id=self.featch_user_id()
        user_id=user_id[0]
        print(user_id)
        return f"""insert into task (description,create_at,user_id,dead_line) values
            ('{self.description}',
            '{self.create_at}',
            '{user_id}',
            '{self.dead_line}'
            );"""
    
    @execute_db
    def featch_user_id(self):
        return  f"select user_id from user where username = '{self.username}';"
    
    # @execute_db
    def featch_task(self):
        user_id = self.featch_user_id()
        # return f"select description,dead_line,create_at,last_update from task where user_id='{user_id}';"
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        # اجرای یک کوئری
        cursor.execute(f"select description,dead_line,create_at,last_update from task where user_id='{user_id[0]}';")

        # گرفتن همه ردیف‌ها از نتیجه کوئری
        rows = cursor.fetchall()

        # بستن اتصال به پایگاه داده
        conn.close()

        return rows
        

    @classmethod
    def create_table(cls):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            connection.commit()
            cursor.execute("""create table if not exists task(
                           task_id integer primary key,
                           user_id integer,
                           description text,
                           create_at string,
                           is_done integer DEFAULT 0 ,
                           last_update string,
                           dead_line string,
                           FOREIGN KEY (user_id) REFERENCES user(user_id)
                              );
                           """)
            connection.commit()

        cls.is_table_created = True