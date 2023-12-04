import sqlite3
import tkinter as tk
from tkinter import ttk

def query_database():
    # اتصال به پایگاه داده SQLite
    conn = sqlite3.connect("sqlite3.db")
    cursor = conn.cursor()

    # اجرای یک کوئری
    cursor.execute("SELECT * FROM task")

    # گرفتن همه ردیف‌ها از نتیجه کوئری
    rows = cursor.fetchall()

    # بستن اتصال به پایگاه داده
    conn.close()

    return rows

def display_result_in_treeview(tree, results):
    # پاک کردن محتویات قبلی در treeview
    for i in tree.get_children():
        tree.delete(i)

    # نمایش نتایج در treeview
    for row in results:
        tree.insert("", "end", values=row)

def main():
    # ساخت یک پنجره
    window = tk.Tk()
    window.title("نمایش داده‌ها از SQLite در Treeview")

    # ایجاد یک treeview
    tree = ttk.Treeview(window)
    tree["columns"] = ("نام ستون 1", "نام ستون 2", "و ...")

    # تنظیم نام ستون‌ها
    tree.column("#0", width=0, stretch=tk.NO)  # ستون خالی
    tree.column("نام ستون 1", anchor=tk.W, width=100)
    tree.column("نام ستون 2", anchor=tk.W, width=100)
    # ...

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("نام ستون 1", text="نام ستون 1", anchor=tk.W)
    tree.heading("نام ستون 2", text="نام ستون 2", anchor=tk.W)
    # ...

    # نمایش treeview
    tree.pack()

    # گرفتن نتایج از پایگاه داده و نمایش در treeview
    results = query_database()
    display_result_in_treeview(tree, results)

    # اجرای حلقه اصلی
    window.mainloop()

if __name__ == "__main__":
    main()
