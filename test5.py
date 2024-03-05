from configparser import ConfigParser
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Style, Treeview

import test2
def everything(code, name, numEnt=0):
    top = Toplevel()
    top.title(f"{str(code)}+{name}+Prices")
    # top.geometry("700x500")


    global con, cur, table_name
    con = sqlite3.connect('test2.db')
    cur = con.cursor()
    table_name = str(code)+'+'+name+'+Prices'
    def listtoStr(s):
        str1 = ""
        for el in s:
            str1 += el
            if el is not s[-1]:
                str1 += ', '
        return str1
    def fetch():
        cur.execute(f'''SELECT name FROM pragma_table_info("{table_name}") ORDER BY cid;''')
        col = cur.fetchall()
        return col
    def update(data, col):
        iterator = 0
        for tupl in col:
            if iterator == len(data):
                break
            data[iterator] = col[iterator][0] + '=' + data[iterator]
            iterator += 1
        cur.execute(f'''UPDATE "{table_name}" SET {listtoStr(data)}''')
        con.commit()
        con.close()

    def Convert():
        result = textarea.get(1.0, 'end')
        li = list(result.split("\n"))
        while '' in li:
            li.remove('')
        Check(li, fetch())

    def Check(li, col):
        if (len(li) == numEnt and len(col) == numEnt) or len(li) == len(col):
            update(li, col)
            top.destroy()
        else:
            messagebox.showerror(title="Error", message='Brojkata na ceni ne e tochna ili brojkata na produkti')
    def database():
        # Read our config file and get colors
        parser = ConfigParser()
        parser.read("treebase.ini")
        saved_primary_color = parser.get('colors', 'primary_color')
        saved_secondary_color = parser.get('colors', 'secondary_color')
        saved_highlight_color = parser.get('colors', 'highlight_color')


        def query_database():
            # Clear the Treeview
            for record in my_tree.get_children():
                my_tree.delete(record)
            cur.execute(f'''SELECT rowid, * FROM "{table_name}" ''')
            records = cur.fetchall()
            # records.append(tuple(result))
            print(records)

            # Add our data to the screen
            global count
            count = 0

            # for record in records:
            #	print(record)
            test2.record_something2(name,records,my_tree,count)
        def reset_database():
            for record in my_tree.get_children():
                my_tree.delete(record)

        # Add Menu
        my_menu = Menu(top)
        top.config(menu=my_menu)

        # Configure our menu
        tools_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_separator()
        tools_menu.add_command(label="Reset", command=reset_database)
        tools_menu.add_separator()
        # Add Some Style
        style = Style()

        # Pick A Theme
        style.theme_use('default')

        # Configure the Treeview Colors
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")

        # Change Selected Color #347083
        style.map('Treeview',
                  background=[('selected', saved_highlight_color)])

        # Create a Treeview Frame
        tree_frame = Frame(top)
        tree_frame.pack()

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        tree_scroll2 = Scrollbar(tree_frame, orient=HORIZONTAL)
        tree_scroll2.pack(side=BOTTOM, fill=X)
        # Create The Treeview
        my_tree = Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll2.set, selectmode="extended")
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)
        tree_scroll2.config(command=my_tree.xview)

        # Define Our Column

        test2.unique_tree2(name,my_tree)
        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background=saved_secondary_color)
        my_tree.tag_configure('evenrow', background=saved_primary_color)

        # Remove Many records


        # Run to pull data from database on start
        query_database()
    database()
    textarea=Text(top)
    textarea.pack()

    mybutton = Button(top, text="Update", command=Convert)
    mybutton.pack()