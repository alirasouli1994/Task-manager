import tkinter as tk
from tkinter import ttk
from s11 import User
from tkinter import messagebox
from task import Task

# main_window = tk.Tk()
# lbl_username = tk.Label(main_window,text="username")
# ent_username = tk.Entry(main_window)
# lbl_password = tk.Label(main_window,text="password")

# ent_password = tk.Entry(main_window)
# btn_login = tk.Button(main_window,text="login")

# lbl_username.pack()
# ent_username.pack()
# lbl_password.pack()
# ent_password.pack()
# btn_login.pack()
# main_window.mainloop()

class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.widgets ={
                       "login_page":{},
                       "register_page":{},
                       "main_page":{}
                       }
        self.set_mainwidow()
        self.login_page()
        
        
        

    def login_page(self):
        self.destroy_all()
        
        self.widgets["login_page"]["frm_login"] = tk.Frame(self)
        self.widgets["login_page"]["lbl_username"] = tk.Label(self.widgets["login_page"]["frm_login"],text="username")
        self.widgets["login_page"]["ent_username"] = tk.Entry(self.widgets["login_page"]["frm_login"])
        self.widgets["login_page"]["lbl_password"] = tk.Label(self.widgets["login_page"]["frm_login"],text="password")
        self.widgets["login_page"]["ent_password"] = tk.Entry(self.widgets["login_page"]["frm_login"])
        self.widgets["login_page"]["btn_login"] = tk.Button(self.widgets["login_page"]["frm_login"],text="login",command=self.login)
        self.widgets["login_page"]["btn_show_register_page"] = tk.Button(self.widgets["login_page"]["frm_login"],text="go to register page",command=self.register_page)
        self.set_positions()


    def register_page(self):
        self.destroy_all()
        self.widgets["register_page"]["frm_register"] = tk.Frame(master=self)
        self.widgets["register_page"]["lbl_username"] = tk.Label(self.widgets["register_page"]["frm_register"],text="username")
        self.widgets["register_page"]["ent_username"] = tk.Entry(self.widgets["register_page"]["frm_register"])
        self.widgets["register_page"]["lbl_password1"] = tk.Label(self.widgets["register_page"]["frm_register"],text="password")
        self.widgets["register_page"]["ent_password1"] = tk.Entry(self.widgets["register_page"]["frm_register"])
        self.widgets["register_page"]["lbl_password2"] = tk.Label(self.widgets["register_page"]["frm_register"],text="cofirm password")
        self.widgets["register_page"]["ent_password2"] = tk.Entry(self.widgets["register_page"]["frm_register"])
        self.widgets["register_page"]["btn_register"] = tk.Button(self.widgets["register_page"]["frm_register"],text="register",command=self.register_user)
        self.widgets["register_page"]["btn_show_login_page"] = tk.Button(self.widgets["register_page"]["frm_register"],text="go to login page",command=self.login_page)
        self.set_positions()

    def main_page(self):
        username = self.widgets["login_page"]["ent_username"].get()
        self.destroy_all()
        self.widgets["main_page"]["frm_main"] = tk.Frame(master=self)
        self.widgets["main_page"]["lbl_user"] = tk.Label(self.widgets["main_page"]["frm_main"],text=f"Welcome, {username}")
        
        self.widgets["main_page"]["lbl_task_name"] = tk.Label(self.widgets["main_page"]["frm_main"],text=f"Task Name")        
        self.widgets["main_page"]["ent_task_add"] = tk.Entry(self.widgets["main_page"]["frm_main"])
        self.widgets["main_page"]["btn_task_add"] = tk.Button(self.widgets["main_page"]["frm_main"], text="Add Task",command=lambda:self.add_task(username))
        self.widgets["main_page"]["btn_task_edit"] = tk.Button(self.widgets["main_page"]["frm_main"], text="    Edit    " , command=self.edit_selection_task)
        # dead line label 
        self.widgets["main_page"]["lbl_deadline"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Dead line ")
        self.widgets["main_page"]["lbl_deadline_year"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Year")
        self.widgets["main_page"]["lbl_deadline_month"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Month")
        self.widgets["main_page"]["lbl_deadline_day"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Day")
        self.widgets["main_page"]["lbl_deadline_hour"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Hour")
        self.widgets["main_page"]["lbl_deadline_minut"] = tk.Label(self.widgets["main_page"]["frm_main"],text="Minut")
        #deadline input field
        self.widgets["main_page"]["ent_deadline_year"] = tk.Entry(self.widgets["main_page"]["frm_main"])
        self.widgets["main_page"]["ent_deadline_month"] = tk.Entry(self.widgets["main_page"]["frm_main"])
        self.widgets["main_page"]["ent_deadline_day"] = tk.Entry(self.widgets["main_page"]["frm_main"])
        self.widgets["main_page"]["ent_deadline_hour"] = tk.Entry(self.widgets["main_page"]["frm_main"])
        self.widgets["main_page"]["ent_deadline_minut"] = tk.Entry(self.widgets["main_page"]["frm_main"])

        self.widgets["main_page"]["list_task"]=ttk.Treeview(self.widgets["main_page"]["frm_main"],columns=('Task','Dead line','Creat at','Last update','is done'),show= "headings",selectmode="browse")

        self.widgets["main_page"]["list_task"].heading("Task" , text="Task")
        self.widgets["main_page"]["list_task"].heading("Dead line" , text="Dead line")
        self.widgets["main_page"]["list_task"].heading("Creat at" , text="Creat at")
        self.widgets["main_page"]["list_task"].heading("Last update" , text="Last update")
        self.widgets["main_page"]["list_task"].heading("is done" , text="is done")
        # self.widgets["main_page"]["list_task"].column(anchor="center")
        self.widgets["main_page"]["btn_logout"] = tk.Button(self.widgets["main_page"]["frm_main"], text="Logout", command=self.login_page)

        self.widgets["main_page"]["frm_main"].place(x=0, y=0, width=790, height=600)
        self.widgets["main_page"]["lbl_user"].place(x=10 , y=10 )
        self.widgets["main_page"]["lbl_task_name"].place(x=10 , y=40 )
        self.widgets["main_page"]["ent_task_add"].place(x=80 , y=40 , width=300)
        self.widgets["main_page"]["btn_task_add"].place(x=80 , y=120 )
        self.widgets["main_page"]["list_task"].place(x=10 ,y=160, width=790)

        self.widgets["main_page"]["lbl_deadline"].place(x=10, y=90)
        self.widgets["main_page"]["lbl_deadline_year"] .place(x=85, y=70)
        self.widgets["main_page"]["lbl_deadline_month"].place(x=130, y=70)
        self.widgets["main_page"]["lbl_deadline_day"].place(x=188,y=70)
        self.widgets["main_page"]["lbl_deadline_hour"].place(x=235,y=70)
        self.widgets["main_page"]["lbl_deadline_minut"].place(x=282,y=70)
        self.widgets["main_page"]["ent_deadline_year"].place(x=80,y=90,width=40)
        self.widgets["main_page"]["ent_deadline_month"].place(x=130,y=90,width=40)
        self.widgets["main_page"]["ent_deadline_day"].place(x=180,y=90,width=40)
        self.widgets["main_page"]["ent_deadline_hour"] .place(x=230,y=90,width=40)
        self.widgets["main_page"]["ent_deadline_minut"].place(x=280,y=90,width=40)
        
        self.widgets["main_page"]["btn_task_edit"].place(x=65,y=400)
        self.widgets["main_page"]["btn_logout"].place(x=10,y=400)

        # show tasks in tree
        # tree = self.widgets["main_page"]["list_task"]
        # a = Task(None,username)
        # result= a.featch_task()
        # for i in tree.get_children():
        #     tree.delete(i)
        # for row in result:
        #     tree.insert("","end",values=row)
        self.refresh_tasks(username)
    
    def refresh_tasks(self,username):
        tree = self.widgets["main_page"]["list_task"]
        a = Task(None,username,None)
        result= a.featch_task()
        for i in tree.get_children():
            tree.delete(i)
        for row in result:
            tree.insert("","end",values=row)
        # the columns in the center
        columns=tree["columns"]
        for col in columns:
            tree.heading(col, anchor="center")
            tree.column(col, anchor="center")
                       

    def destroy_all(self):
        for v1 in self.widgets.values():
            for v2 in v1.values():
                v2.destroy()
        self.widgets = {"login_page":{},"register_page":{}, "main_page":{}}


    def set_mainwidow(self):
        root= tk.Frame(self)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() 
        app_width = 800
        app_height = 600
        x = (screen_width // 2) - (app_width // 2)
        y = (screen_height //2) - (app_height // 2)
        self.geometry(f'{app_width}x{app_height}+{x}+{y}')
        self.minsize(400, 300)
        self.maxsize(1000, 700)

    def set_positions(self):
        for v1 in self.widgets.values():
            for v2 in v1.values():
                v2.pack()
    
    def register_user(self):
        username = self.widgets["register_page"]["ent_username"].get()
        password1 = self.widgets["register_page"]["ent_password1"].get()
        password2 = self.widgets["register_page"]["ent_password2"].get()
        if password1==password2:
            u = User(username=username,password=password2)
            u.save()
            messagebox.showinfo("user created",f"user {username} created successfully!")
        else:
            messagebox.showerror("faild",f"passwords are not match!")
    # # login

    def login(self):
        username = self.widgets["login_page"]["ent_username"].get()
        password = self.widgets["login_page"]["ent_password"].get()
        l = User(username,password)
        a= l.user_login()
        if a :
            self.main_page()
        else:
            messagebox.showerror("faild",f"username or passwords are not match!")

    def add_task(self,username):
        description = self.widgets["main_page"]["ent_task_add"].get()
        Y= self.widgets["main_page"]["ent_deadline_year"].get()
        M= self.widgets["main_page"]["ent_deadline_month"].get()
        D= self.widgets["main_page"]["ent_deadline_day"].get()
        h= self.widgets["main_page"]["ent_deadline_hour"].get()
        m= self.widgets["main_page"]["ent_deadline_minut"].get()
        deadline= f'{Y}-{M}-{D}  {h}:{m}'
        # print(deadline)
        T = Task(description,username,deadline)
        T.save_task()
        self.refresh_tasks(username)
    
    def edit_selection_task(self):
        # selected_item = self.widgets["main_page"]["list_task"].focus()
        a= self.widgets["main_page"]["list_task"].focus()
        print(a)



my_app = App()
my_app.mainloop()





    