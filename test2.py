from tkinter import Tk, ttk
root_ = Tk()
tree1 = ttk.Treeview(root_, height = 10, selectmode = 'browse')
tree1.insert('', 'end', text = 'item 0')
tree1.insert('', 'end', text = 'item 1')
tree1.insert('', 'end', text = 'item 2')
tree1.insert('', 'end', text = 'item 3')
 
tree1.selection_get()