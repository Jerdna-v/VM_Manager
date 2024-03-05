from configparser import ConfigParser
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Style, Treeview

import test2
def opener(code, name):
    top = Toplevel()
    top.title("Temporary")
    # Add Record Entry Boxes
    data_frame = LabelFrame(top, text="Date")
    data_frame.pack(fill="x", expand="yes", padx=20)
    OPTIONS = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]
    day_label = Label(data_frame, text="Month")
    day_label.grid(row=0, column=0, padx=10, pady=10)
    variable = StringVar(top)
    variable.set(OPTIONS[0])  # default value
    w = OptionMenu(data_frame, variable, *OPTIONS)
    w.grid(row=0, column=1, padx=10, pady=10)

    promet_label = Label(data_frame, text="Year")
    promet_label.grid(row=0, column=2, padx=10, pady=10)
    promet_entry = Entry(data_frame)
    promet_entry.grid(row=0, column=3, padx=10, pady=10)

    def open():
        date = variable.get()+" "+promet_entry.get()
        top.destroy()
        everything(code, name, date)
    mybutton = Button(top, text="Next", command=open)
    mybutton.pack()

def everything(code, name, year, numEnt=0):
    top = Toplevel()
    top.title(f"{str(code)}+{name}+Promet+{year}")
    # top.geometry("700x500")


    global con, cur, table_name
    con = sqlite3.connect('test2.db')
    cur = con.cursor()
    table_name = str(code)+'+'+name+'+Promet+'+year
    # def listtoStr(s):
    #     str1 = ""
    #     for el in s:
    #         str1 += el
    #         if el is not s[-1]:
    #             str1 += ', '
    #     return str1
    # def fetch():
    #     cur.execute(f'''SELECT name FROM pragma_table_info("{table_name}") ORDER BY cid;''')
    #     col = cur.fetchall()
    #     return col
    # def update(data, col):
    #     iterator = 0
    #     for tupl in col:
    #         if iterator == len(data):
    #             break
    #         data[iterator] = col[iterator][0] + '=' + data[iterator]
    #         iterator += 1
    #     cur.execute(f'''UPDATE "{table_name}" SET {listtoStr(data)}''')
    #     con.commit()
    #     con.close()
    #
    # def Convert():
    #     result = textarea.get(1.0, 'end')
    #     li = list(result.split("\n"))
    #     while '' in li:
    #         li.remove('')
    #     Check(li, fetch())
    #
    # def Check(li, col):
    #     if (len(li) == numEnt and len(col) == numEnt) or len(li) == len(col):
    #         update(li, col)
    #         top.destroy()
    #     else:
    #         messagebox.showerror(title="Error", message='Brojkata na ceni ne e tochna ili brojkata na produkti')
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
            try:
                cur.execute(f'''SELECT rowid, * FROM "{table_name}" ''')
            except sqlite3.OperationalError:
                messagebox.showerror(title="Error", message="Nema tabela za toj mesec")
                top.destroy()
            records = cur.fetchall()
            # records.append(tuple(result))
            print(records)

            # Add our data to the screen
            global count
            count = 0

            # for record in records:
            #	print(record)
            test2.record_something3(records,my_tree,count)
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

        test2.unique_tree3(my_tree)
        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background=saved_secondary_color)
        my_tree.tag_configure('evenrow', background=saved_primary_color)

        # Remove Many records
        # Add Record Entry Boxes
        data_frame = LabelFrame(top, text="Record")
        data_frame.pack(fill="x", expand="yes", padx=20)

        day_label = Label(data_frame, text="Day")
        day_label.grid(row=0, column=0, padx=10, pady=10)
        day_entry = Entry(data_frame)
        day_entry.grid(row=0, column=1, padx=10, pady=10)

        promet_label = Label(data_frame, text="Promet")
        promet_label.grid(row=0, column=2, padx=10, pady=10)
        promet_entry = Entry(data_frame)
        promet_entry.grid(row=0, column=3, padx=10, pady=10)

        # Clear entry boxes
        def clear_entries():
            # Clear entry boxes
            day_entry.delete(0, END)
            promet_entry.delete(0, END)

        def remove_one():
            x = my_tree.selection()[0]
            my_tree.delete(x)

            # Create a database or connect to one that exists
            conn = sqlite3.connect('test2.db')

            # Create a cursor instance
            c = conn.cursor()

            # Delete From Database
            c.execute(f"""DELETE from "{table_name}" WHERE Day=""" + day_entry.get())

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear The Entry Boxes
            clear_entries()

            # Add a little message box for fun
            messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")
        # Update record
        def select_record(e):
            # Clear entry boxes
            day_entry.delete(0, END)
            promet_entry.delete(0, END)


            # Grab record Number
            selected = my_tree.focus()
            # Grab record values
            values = my_tree.item(selected, 'values')

            # outpus to entry boxes
            day_entry.insert(0, values[0])
            promet_entry.insert(0, values[1])

        def update_record():
            # Grab the record number
            selected = my_tree.focus()
            # Update record
            my_tree.item(selected, text="", values=(
                day_entry.get(), promet_entry.get(), ))

            # Update the database
            # Create a database or connect to one that exists
            conn = sqlite3.connect('test2.db')

            # Create a cursor instance
            c = conn.cursor()

            c.execute(f"""UPDATE "{table_name}" SET
        		Promet = :Promet,
        		WHERE Day = :Day""",
                      {
                          'Promet': promet_entry.get(),
                          'Day': day_entry.get()
                      })

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear entry boxes
            day_entry.delete(0, END)
            promet_entry.delete(0, END)

        # add new record to database
        def add_record():
            # Update the database
            # Create a database or connect to one that exists
            conn = sqlite3.connect('test2.db')

            # Create a cursor instance
            c = conn.cursor()

            # Add New Record
            c.execute(f"""INSERT INTO "{table_name}" VALUES (:Day, :Promet)""",
                      {
                          'Day': day_entry.get(),
                          'Promet': promet_entry.get(),
                      })

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear entry boxes
            day_entry.delete(0, END)
            promet_entry.delete(0, END)

            # Clear The Treeview Table
            my_tree.delete(*my_tree.get_children())

            # Run to pull data from database on start
            query_database()

        # Add Buttons
        button_frame = LabelFrame(top, text="Commands")
        button_frame.pack(fill="x", expand="yes", padx=20)

        update_button = Button(button_frame, text="Update Record", command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = Button(button_frame, text="Add Record", command=add_record)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
        # remove_all_button.grid(row=0, column=2, padx=10, pady=10)

        remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
        remove_one_button.grid(row=0, column=2, padx=10, pady=10)
        # Run to pull data from database on start
        my_tree.bind("<ButtonRelease-1>", select_record)

        query_database()
    database()
