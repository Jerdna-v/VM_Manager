import csv
from configparser import ConfigParser
from tkinter import *
from tkinter import ttk

import tkcalendar
from datetime import timedelta
import sqlite3

import test2


def everything(code, name):
    top = Toplevel()
    top.title(f'{code}+{name}+Prices')
    date1 = tkcalendar.DateEntry(top)
    date1.pack(padx=0, pady=0)

    date2 = tkcalendar.DateEntry(top)
    date2.pack(padx=0, pady=0)
    def create_records():
        final = []
        for row in rows:
            print("row",row)
            row = list(row)
            row.insert(0,1)
            final.append(tuple(row))
        # final.append(())
        difference.insert(0,2)
        final.append(tuple(difference))
        # final.append(())
        multiplied.insert(0,3)
        final.append(tuple(multiplied))
        return final
    def multiply(dif):
        global multiplied
        con = sqlite3.connect('test2.db')
        cur = con.cursor()

        multiplied = [] #initialization of result list.
        cur.execute(f'''SELECT * from "{code}+{name}+Prices" ''')
        multiplier = list(cur.fetchall()[0])
        # try:
        print(len(multiplier))
        zip_object = zip(dif, multiplier)
        # except IndexError:
            # try:
            #     zip_object = zip(dif, multiplier)
            # except IndexError:
            #     pass
        if name == "Canto" or name == "Astro40" or name =="Astro40(s)" or name == "Astro40(1e)" or name == "Astro35":
            zip_object = zip(dif[5:], multiplier)
            multiplied.append(dif[0])
            multiplied.append(dif[1])
            multiplied.append(dif[2])
            multiplied.append(dif[3])
            multiplied.append(dif[4])
        else:
            zip_object = zip(dif[2:], multiplier)
            multiplied.append(dif[0])
            multiplied.append(dif[1])
        for list1_i, list2_i in zip_object:
            if type(list1_i) and type(list2_i) == int:
                print(list1_i,list2_i)
                multiplied.append(list1_i*list2_i)
        for i in dif[len(multiplied):]:
            multiplied.append(i)
        print("multipliead",multiplied)
        query_database()
    def subtraction():
        global difference
        difference = [] #initialization of result list.
        try:
            zip_object = zip(rows[-1],rows[0])
        except IndexError:
            try:
                zip_object = zip(rows[0], rows[0])
            except IndexError:
                pass
        for list1_i, list2_i in zip_object:
            if type(list1_i) and type(list2_i) == int:
                difference.append(list1_i-list2_i) #append each difference to list.
            else:
                difference.append(list1_i)
        print("diff",len(difference),difference)
        multiply(difference)

    def removeDuplicates(lst):
        return [t for t in (set(tuple(i) for i in lst))]

    def search():
        global rows
        con = sqlite3.connect('test2.db')
        cur = con.cursor()
        rows = []
        for date in dates:
            cur.execute(f"""SELECT * FROM '{code}+{name}+Prints' WHERE Date='{date}'""")
            rows = rows+cur.fetchall()
        rows = removeDuplicates(rows)
        rows.sort(key=lambda x: x[2])
        con.commit()
        con.close()
        subtraction()


    def date_range(start, stop):
        global dates  # If you want to use this outside of functions

        dates = []
        diff = (stop - start).days
        for i in range(diff + 1):
            day = start + timedelta(days=i)
            dates.append(day)
        if dates:
            dates = [x.strftime('%d %b %Y') for x in dates]
            # print(dates)  # Print it, or even make it global to access it outside this
            search()
        else:
            print('Make sure the end date is later than start date')
    Button(top, text='Find range', command=lambda: date_range(date1.get_date(), date2.get_date())).pack()
    def query_database():
        # Clear the Treeview
        global records
        for record in my_tree.get_children():
            my_tree.delete(record)
        records=create_records()
        # records.append(tuple(result))
        print(len(records[0]),len(records[1]),len(records[2]), records)

        # Add our data to the screen
        global count
        count = 0

        # for record in records:
        #	print(record)
        test2.record_something(name,records,my_tree,count)
    def export():
        with open(f'{code}+{name}+{records[0][1]}.csv', 'a', newline='') as f:
            w = csv.writer(f, dialect='excel')
            for record in records:
                record = list(record)
                if record[0] == 1:
                    record[0] = 'Pechatenje'
                if record[0] == 2:
                    record[0] = 'Razlika Pijachki'
                if record[0] == 3:
                    record[0] = 'Razlika Pari'
                    record[-1] = '\n'
                w.writerow(record)
    def treeview():
        global my_tree
        # Read our config file and get colors
        parser = ConfigParser()
        parser.read("treebase.ini")
        saved_primary_color = parser.get('colors', 'primary_color')
        saved_secondary_color = parser.get('colors', 'secondary_color')
        saved_highlight_color = parser.get('colors', 'highlight_color')
        # Add Some Style
        # Add Menu
        my_menu = Menu(top)
        top.config(menu=my_menu)

        # Configure our menu
        tools_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Export", command=export)
        tools_menu.add_separator()
        def reset_database():
            for record in my_tree.get_children():
                my_tree.delete(record)
        tools_menu.add_command(label="Reset", command=reset_database)
        tools_menu.add_separator()
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
        tree_frame.pack()

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        tree_scroll2 = Scrollbar(tree_frame, orient=HORIZONTAL)
        tree_scroll2.pack(side=BOTTOM, fill=X)
        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll2.set,
                               selectmode="extended")
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)
        tree_scroll2.config(command=my_tree.xview)

        # Define Our Column

        test2.unique_tree(name, my_tree)
        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background=saved_secondary_color)
        my_tree.tag_configure('evenrow', background=saved_primary_color)

        # Remove Many records

        def select_record(e):
            # Grab record Number
            selected = my_tree.focus()
            # Grab record values
            values = my_tree.item(selected, 'values')

        # Bind the treeview
        my_tree.bind("<ButtonRelease-1>", select_record)
    treeview()









        # Run to pull data from database on start
    # root.mainloop()
    # date1 = tkcalendar.DateEntry(top)
    # date1.pack(padx=0, pady=0)
    #
    # date2 = tkcalendar.DateEntry(top)
    # date2.pack(padx=0, pady=0)
    #
    # Button(top, text='Find range', command=lambda: date_range(date1.get_date(), date2.get_date())).pack()

    # top.mainloop()