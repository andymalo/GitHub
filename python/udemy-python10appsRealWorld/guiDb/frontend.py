
"""
A program that storres this book information :
Title, Author
Year, ISBN

User can :
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
import backend

def view_command():
    lst.delete(0, END)
    for row in backend.viewAll():
        lst.insert(END, row)

def search_command():
    lst.delete(0, END)
    for row in backend.searchEntry(entryTitle.get(),
                                   entryAuthor.get(), entryYear.get(), entryISBN.get()):
        lst.insert(END, row)

def add_command():
    backend.addEntry(entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get())
    lst.delete(0, END)
    lst.insert(END, (entryTitle.get(), entryAuthor.get(), entryYear.get(), entryISBN.get()))
    #view_command()

def get_selected_row(event):
    global selected_tuple
    index = lst.curselection()[0]
    selected_tuple = lst.get(index)
    entryAuthor.delete(0, END)
    entryAuthor.insert(END, selected_tuple[2])
    entryISBN.delete(0, END)
    entryISBN.insert(END, selected_tuple[4])
    entryTitle.delete(0, END)
    entryTitle.insert(END, selected_tuple[1])
    entryYear.delete(0, END)
    entryYear.insert(END, selected_tuple[3])

def delete_command():
    backend.delEntry(selected_tuple[0])

def update_command():
    backend.updateEntry(selected_tuple[0], entryTitle.get(),
                        entryAuthor.get(), entryYear.get(), entryISBN.get())

window = Tk()

window.wm_title = ("BookStore")

LblTitle = Label(window, text = "Titre : ")
LblTitle.grid(row = 1,column = 1)

LblYear = Label(window, text = "Année : ")
LblYear.grid(row= 2,column = 1)

LblAuth = Label(window, text = "Auteur : ")
LblAuth.grid(row= 1,column = 3)

LblISBN = Label(window,text = "ISBN : ")
LblISBN.grid(row = 2,column = 3)

eTitle_v = StringVar()
entryTitle = Entry(window,textvariable = eTitle_v)
entryTitle.grid(row = 1, column = 2)

eYear_v = StringVar()
entryYear = Entry(window,textvariable = eYear_v)
entryYear.grid(row = 2, column = 2)

eAuth_v = StringVar()
entryAuthor = Entry(window,textvariable = eAuth_v)
entryAuthor.grid(row = 1, column = 4)

eISBN_v = StringVar()
entryISBN = Entry(window,textvariable = eISBN_v)
entryISBN.grid(row=2, column = 4)

lst = Listbox(window, height = 6, width = 35)
lst.grid(row = 3, column = 1, rowspan=6,columnspan=2)

sb = Scrollbar(window,)
sb.grid(row = 3, column = 3,rowspan = 6)

lst.configure(yscrollcommand = sb.set)
sb.configure(command = lst.yview)

lst.bind('<<ListboxSelect>>', get_selected_row)

btnViewAll = Button(window, text = "View All",width = 12, command = view_command)
btnViewAll.grid(row=3,column=4)

btnSearchE = Button(window, text = "Search Entry",width = 12, command = search_command)
btnSearchE.grid(row=4,column=4)

btnAddE = Button(window, text = "Add Entry",width = 12, command = add_command)
btnAddE.grid(row=5,column=4)

btnUpdate = Button(window, text = "Update",width = 12, command = update_command)
btnUpdate.grid(row=6,column=4)

btnDelete = Button(window, text = "Delete",width = 12, command = delete_command)
btnDelete.grid(row=7,column=4)

btnViewAll = Button(window, text = "Close",width = 12, command = window.destroy)
btnViewAll.grid(row=8,column=4)

window.mainloop()