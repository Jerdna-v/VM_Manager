from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import colorchooser
from configparser import ConfigParser
import main
import tkinteredit2

root = Tk()
root.title('App')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x550")

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
        c.execute("SELECT rowid, * FROM machines")
        records = c.fetchall()
    except sqlite3.OperationalError:
        conn.execute('''CREATE TABLE IF NOT EXISTS "machines" (
                                "Code"	INTEGER UNIQUE,
                                "Name"	TEXT,
                                "Location"	TEXT,
                                "Description"	TEXT,
                                PRIMARY KEY("Code")
                                                    );''')
        conn.commit()
        main.everything()
    c.execute("SELECT rowid, * FROM machines")
    records = c.fetchall()
    # Add our data to the screen
    global count
    count = 0

    # for record in records:
    #	print(record)

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[3], record[4]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[3], record[4]),
                           tags=('oddrow',))
        # increment counter
        count += 1

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

    c.execute("SELECT rowid, * FROM machines WHERE Name like ?", (lookup_record,))

    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    # for record in records:
    #	print(record)

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[3], record[4]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2], record[3], record[4]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def lookup_records():
    global search_entry, search

    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    # search.iconbitmap('c:/gui/codemy.ico')

    # Create label frame
    search_frame = LabelFrame(search, text="Name")
    search_frame.pack(padx=10, pady=10)

    # Add entry box
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)

    # Add button
    search_button = Button(search, text="Search Records", command=search_records)
    search_button.pack(padx=20, pady=20)


def primary_color():
    # Pick Color
    primary_color = colorchooser.askcolor()[1]

    # Update Treeview Color
    if primary_color:
        # Create Striped Row Tags
        my_tree.tag_configure('evenrow', background=primary_color)

        # Config file
        parser = ConfigParser()
        parser.read("treebase.ini")
        # Set the color change
        parser.set('colors', 'primary_color', primary_color)
        # Save the config file
        with open('treebase.ini', 'w') as configfile:
            parser.write(configfile)


def secondary_color():
    # Pick Color
    secondary_color = colorchooser.askcolor()[1]

    # Update Treeview Color
    if secondary_color:
        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background=secondary_color)

        # Config file
        parser = ConfigParser()
        parser.read("treebase.ini")
        # Set the color change
        parser.set('colors', 'secondary_color', secondary_color)
        # Save the config file
        with open('treebase.ini', 'w') as configfile:
            parser.write(configfile)


def highlight_color():
    # Pick Color
    highlight_color = colorchooser.askcolor()[1]

    # Update Treeview Color
    # Change Selected Color
    if highlight_color:
        style.map('Treeview',
                  background=[('selected', highlight_color)])

        # Config file
        parser = ConfigParser()
        parser.read("treebase.ini")
        # Set the color change
        parser.set('colors', 'highlight_color', highlight_color)
        # Save the config file
        with open('treebase.ini', 'w') as configfile:
            parser.write(configfile)


def reset_colors():
    # Save original colors to config file
    parser = ConfigParser()
    parser.read('treebase.ini')
    parser.set('colors', 'primary_color', 'lightblue')
    parser.set('colors', 'secondary_color', 'white')
    parser.set('colors', 'highlight_color', '#347083')
    with open('treebase.ini', 'w') as configfile:
        parser.write(configfile)
    # Reset the colors
    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')
    style.map('Treeview',
              background=[('selected', '#347083')])


# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Configure our menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)
# Drop down menu
option_menu.add_command(label="Primary Color", command=primary_color)
option_menu.add_command(label="Secondary Color", command=secondary_color)
option_menu.add_command(label="Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Reset Colors", command=reset_colors)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)

# Search Menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
# Drop down menu
search_menu.add_command(label="Search", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Reset", command=query_database)

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
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Code", "Name", "Location", "Description")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Code", anchor=W, width=140)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("Location", anchor=CENTER, width=100)
my_tree.column("Description", anchor=CENTER, width=140)


# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Code", text="Code", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Location", text="Location", anchor=CENTER)
my_tree.heading("Description", text="Description", anchor=CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background=saved_secondary_color)
my_tree.tag_configure('evenrow', background=saved_primary_color)

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

code_label = Label(data_frame, text="Code")
code_label.grid(row=0, column=0, padx=10, pady=10)
code_entry = Entry(data_frame)
code_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(data_frame, text="Name")
name_label.grid(row=0, column=2, padx=10, pady=10)
name_entry = Entry(data_frame)
name_entry.grid(row=0, column=3, padx=10, pady=10)

location_label = Label(data_frame, text="Location")
location_label.grid(row=0, column=4, padx=10, pady=10)
location_entry = Entry(data_frame)
location_entry.grid(row=0, column=5, padx=10, pady=10)

description_label = Label(data_frame, text="Description")
description_label.grid(row=1, column=0, padx=10, pady=10)
description_entry = Entry(data_frame)
description_entry.grid(row=1, column=1, padx=10, pady=10)




# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Rown Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


# Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('test2.db')

    # Create a cursor instance
    c = conn.cursor()

    # Delete From Database
    c.execute("DELETE from machines WHERE Code=" + code_entry.get())

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear The Entry Boxes
    clear_entries()

    # Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")





# Clear entry boxes
def clear_entries():
    # Clear entry boxes
    code_entry.delete(0, END)
    name_entry.delete(0, END)
    location_entry.delete(0, END)
    description_entry.delete(0, END)


# Select Record
def select_record(e):
    # Clear entry boxes
    code_entry.delete(0, END)
    name_entry.delete(0, END)
    location_entry.delete(0, END)
    description_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outpus to entry boxes
    code_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    location_entry.insert(0, values[2])
    description_entry.insert(0, values[3])

def open_machine(e):
    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outpus to entry boxes
    tkinteredit2.everything(values[0], values[1])

# Update record
def update_record():
    # Grab the record number
    selected = my_tree.focus()
    # Update record
    my_tree.item(selected, text="", values=(
        code_entry.get(), name_entry.get(), location_entry.get(), description_entry.get(),))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('test2.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("""UPDATE "machines" SET
		Name = :name,
		Location = :loc,
		Description = :desc
		WHERE Code = :code""",
              {
                  'name': name_entry.get(),
                  'loc': location_entry.get(),
                  'desc': description_entry.get(),
                  'code': code_entry.get()
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    code_entry.delete(0, END)
    name_entry.delete(0, END)
    location_entry.delete(0, END)
    description_entry.delete(0, END)


# add new record to database
def add_record():
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('test2.db')

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO machines VALUES (:code, :name, :loc, :desc)",
              {
                  'code': code_entry.get(),
                  'name': name_entry.get(),
                  'loc': location_entry.get(),
                  'desc': description_entry.get(),
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    code_entry.delete(0, END)
    name_entry.delete(0, END)
    location_entry.delete(0, END)
    description_entry.delete(0, END)

    # Clear The Treeview Table
    my_tree.delete(*my_tree.get_children())

    # Run to pull data from database on start
    query_database()


# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

# remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
# remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

# remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
# remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)


def refresh():
    main.everything()
    query_database()

refresh_button = Button(button_frame, text="Refresh", command=refresh)
refresh_button.grid(row=0, column=8, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)
my_tree.bind("<Double-Button-1>", open_machine)

# Run to pull data from database on start
query_database()

root.mainloop()