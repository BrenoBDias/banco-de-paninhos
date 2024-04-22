import tkinter as tk
from tkinter.messagebox import showinfo

#will be used to show interface later in the project


root = tk.Tk()

def show_message():
    showinfo("Some title!","Hello, World!")

btn = tk.Button(root, text="click me!", command=show_message)
btn.pack()

root.mainloop()
