from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from configparser import ConfigParser
import test2
import test4
import test5
import test6


def everything(code,name):
    top = Toplevel()
    top.title(f'{code}+{name}+Prints')
    #top.iconbitmap('c:/gui/codemy.ico')

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

        # Create a database or connect to one that exists
        conn = sqlite3.connect('test2.db')

        # Create a cursor instance
        c = conn.cursor()
        try:
            c.execute(f"""SELECT rowid, * FROM "{code}+{name}+Prints" """)
            '''SELECT '''
        except sqlite3.OperationalError:
            messagebox.showerror(title="Error", message="Nema tabela za ta mashina")
        records = c.fetchall()

        # Add our data to the screen
        global count
        count = 0

        # for record in records:
        #	print(record)
        test2.record_something(name,records,my_tree,count)

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()


    def search_records():
        lookup_record = search_entry.get()
        # close the search box
        search.destroy()

        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('test2.db')

        # Create a cursor instance
        c = conn.cursor()

        c.execute(f"SELECT rowid, * FROM '{code}+{name}+Prints' WHERE Date like ?", (lookup_record,))
        records = c.fetchall()

        # Add our data to the screen
        global count
        count = 0

        # for record in records:
        #	print(record)

        test2.record_something(name,records,my_tree,count)
        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()


    def lookup_records():
        global search_entry, search

        search = Toplevel(top)
        search.title("Lookup Records")
        search.geometry("400x200")
        # search.iconbitmap('c:/gui/codemy.ico')

        # Create label frame
        search_frame = LabelFrame(search, text="Date")
        search_frame.pack(padx=10, pady=10)

        # Add entry box
        search_entry = Entry(search_frame, font=("Helvetica", 18))
        search_entry.pack(pady=20, padx=20)

        # Add button
        search_button = Button(search, text="Search Records", command=search_records)
        search_button.pack(padx=20, pady=20)


    # Add Menu
    my_menu = Menu(top)
    top.config(menu=my_menu)

    # Configure our menu
    tools_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Tools", menu=tools_menu)
    tools_menu.add_command(label="Search", command=lookup_records)
    # Add Some Style
    style = ttk.Style()

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
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll2 = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll2.pack(side=BOTTOM, fill=X)
    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll2.set, selectmode="extended")
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)
    tree_scroll2.config(command=my_tree.xview)

    # Define Our Column

    test2.unique_tree(name,my_tree)
    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background=saved_secondary_color)
    my_tree.tag_configure('evenrow', background=saved_primary_color)




    def select_record(e):

        # Grab record Number
        selected = my_tree.focus()
        # Grab record values
        values = my_tree.item(selected, 'values')

    # Add Buttons
    button_frame = LabelFrame(top, text="Commands")
    button_frame.pack(fill="x", expand="yes", padx=20)

    def remove_one():
        x = my_tree.selection()[0]
        my_tree.delete(x)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('test2.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete From Database
        c.execute(f"DELETE from '{code}+{name}+Prints' WHERE Code=" + code_entry.get())

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Add a little message box for fun
        messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")

    remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
    remove_one_button.grid(row=0, column=3, padx=10, pady=10)
    def calcopener():
        test4.everything(code, name)

    def priceopener():
        test5.everything(code, name)

    def prometopener():
        test6.opener(code, name)
    calc_button = Button(button_frame, text="Calculate", command=calcopener)
    calc_button.grid(row=0, column=8, padx=10, pady=10)
    price_button = Button(button_frame, text="Prices", command=priceopener)
    price_button.grid(row=0, column=9, padx=10, pady=10)
    promet_button = Button(button_frame, text="Promet", command=prometopener)
    promet_button.grid(row=0, column=10, padx=10, pady=10)
    # Bind the treeview
    my_tree.bind("<ButtonRelease-1>", select_record)

    # Run to pull data from database on start
    query_database()
    # root.mainloop()