from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
#--------------VARIABLES--------------#
DATABASE = "vehicles"
DATABASE_PASSWORD = "<PASSWORD>"
TABLE = "cars"
HOST = "127.0.0.1"
USER = "root"
# --------------DATABASE_CONNECTION--------------#
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=DATABASE_PASSWORD,
    database=DATABASE
)
mycursor = mydb.cursor(dictionary=True)
mycursor.execute(f"SELECT * FROM {TABLE}")
myresult = mycursor.fetchall()

db_data = []
for value in myresult:
    tupla = tuple(value.values())
    db_data.append(tupla)
columns = []
for object in myresult[0]:
    if object not in columns:
        columns.append(object)

root = Tk()
root.title("CRUD")
root.geometry("700x550")
# -------------------------TABLE_TREEVIEW------------------#
frame1 = Frame(root, width=100, highlightbackground="gray", highlightthickness=3)
frame1.grid(row=0, column=0, padx=10, pady=10)

tree = ttk.Treeview(frame1, columns=columns, padding="bottom", selectmode="browse", show="headings", height=10)

for column in columns:
    tree.heading(column, text=column)
    tree.column(column, width=120, stretch=False, anchor="c")

for data in db_data:
    tree.insert('', END, values=data)
tree.grid(row=1, column=1, padx=20, pady=20)

# Vertical
scroll_bar_y = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll_bar_y.set)
scroll_bar_y.grid(row=1, column=2, sticky="ns")


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        entry_text_1.delete(0, END)
        entry_text_1.insert(END, record[0])
        entry_text_2.delete(0, END)
        entry_text_2.insert(END, record[1])
        entry_text_3.delete(0, END)
        entry_text_3.insert(END, record[2])
        entry_text_4.delete(0, END)
        entry_text_4.insert(END, record[3])
        entry_text_5.delete(0, END)
        entry_text_5.insert(END, record[4])


tree.bind('<<TreeviewSelect>>', item_selected)
# ---------------------BUTTONS----------------#
frame2 = Frame(root, width=150, highlightbackground="gray", highlightthickness=3)
frame2.grid(row=1, column=0, padx=20, pady=20)


def create_record():
    try:
        sql = f"INSERT INTO {TABLE} (ID, Brand, Model , ProductionYear, Color) VALUES (%s, %s,%s, %s, %s)"
        values = (entry_text_1.get(), entry_text_2.get(), entry_text_3.get(), entry_text_4.get(), entry_text_5.get())
        mycursor.execute(sql, values)
        mydb.commit()
        messagebox.showinfo(title="Record Created", message="New record has been inserted")
        refresh()
    except mysql.connector.errors.IntegrityError:
        messagebox.showinfo(title="Warning", message="Bad index number")
    except mysql.connector.errors.DatabaseError as error:
        error_message = str(error)
        error_message_cuted = error_message[13:]
        messagebox.showinfo(title="Warning", message=f"{error_message_cuted}")


create_button = Button(frame2, text="Create", command=create_record, width=20, bg="green")
create_button.grid(row=0, column=0, sticky="ew")


def update_record():
    record = None
    try:
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
        if int(record[0]) == int(entry_text_1.get()):
            sql = f"UPDATE {TABLE} SET Brand = '{entry_text_2.get()}',Model = '{entry_text_3.get()}'," \
                  f"ProductionYear = {entry_text_4.get()},Color = '{entry_text_5.get()}'  WHERE ID = {record[0]} " \
                  f"AND Brand = '{record[1]}' AND Model = '{record[2]}' AND ProductionYear= {record[3]} " \
                  f"AND Color = '{record[4]}'"
            mycursor.execute(sql)
            mydb.commit()
            messagebox.showinfo(title="Record Updated", message="Record has been updated.")
            refresh()
        else:
            messagebox.showinfo(title="Warning", message="Different ID")
    except mysql.connector.errors.IntegrityError:
        messagebox.showinfo(title="Warning", message="Bad Index number")
    except mysql.connector.errors.DatabaseError as error:
        error_message = str(error)
        error_message_cutted = error_message[13:]
        messagebox.showinfo(title="Warning", message=f"{error_message_cutted}")
    except ValueError:
        messagebox.showinfo(title="Warning", message="ID should be a number.")


update_button = Button(frame2, text="Update", command=update_record, width=20, bg="yellow")
update_button.grid(row=0, column=1)


def delete():
    values = (entry_text_1.get(), entry_text_2.get(), entry_text_3.get(), entry_text_4.get(), entry_text_5.get())
    sql = f"DELETE FROM {TABLE} WHERE ID = {values[0]} " \
                  f"AND Brand = '{values[1]}' AND Model = '{values[2]}' AND ProductionYear= {values[3]} " \
                  f"AND Color = '{values[4]}'"
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo(title="Record Deleted", message="Record has been deleted.")
    refresh()


delete_button = Button(frame2, text="Delete", command=delete, width=20, bg="red")
delete_button.grid(row=0, column=2)


def refresh():
    global myresult
    tree.delete(*tree.get_children())
    mycursor.execute(f"SELECT * FROM {TABLE}")
    myresult = mycursor.fetchall()
    db_data = []
    for value in myresult:
        tupla = tuple(value.values())
        db_data.append(tupla)
    columns = []
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=120, stretch=False, anchor="c")
    for data in db_data:
        tree.insert('', END, values=data)
    tree.grid(row=1, column=1, padx=20, pady=20)


refresh_button = Button(frame2, text="Refresh", command=refresh, width=20, bg="blue")
refresh_button.grid(row=0, column=3)

# ------------------Data_Frame---------------------#
frame3 = Frame(root, width=100, highlightbackground="gray", highlightthickness=3)
frame3.grid(row=2, column=0, padx=20, pady=20, ipadx=5, ipady=5)

label_1 = ttk.Label(frame3, text="ID")
label_1.grid(row=0, column=0, padx=5, pady=5)
entry_text_1 = ttk.Entry(frame3)
entry_text_1.insert(END, "ID")
entry_text_1.grid(row=0, column=1)

label_2 = ttk.Label(frame3, text="Brand ")
label_2.grid(row=1, column=0)
entry_text_2 = ttk.Entry(frame3)
entry_text_2.insert(END, "Brand")
entry_text_2.grid(row=1, column=1)

label_3 = ttk.Label(frame3, text="Model ")
label_3.grid(row=2, column=0)
entry_text_3 = ttk.Entry(frame3)
entry_text_3.insert(END, "Model")
entry_text_3.grid(row=2, column=1)

label_4 = ttk.Label(frame3, text="ProductionYear ")
label_4.grid(row=3, column=0)
entry_text_4 = ttk.Entry(frame3)
entry_text_4.insert(END, "ProductionYear")
entry_text_4.grid(row=3, column=1)

label_5 = ttk.Label(frame3, text="Color ")
label_5.grid(row=4, column=0)
entry_text_5 = ttk.Entry(frame3)
entry_text_5.insert(END, "Color")
entry_text_5.grid(row=4, column=1)


root.mainloop()
