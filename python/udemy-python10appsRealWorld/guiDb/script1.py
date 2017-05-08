
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
import backend

from tkinter import *
window = Tk()

LblTitle = Label(window, text = "Titre : ")
LblTitle.grid(row=1,column=1)

LblYear = Label(window, text = "Année : ")
LblYear.grid(row=2,column =1)

LblAuth = Label(window, text = "Auteur : ")
LblAuth.grid(row=1,column = 3)

LblISBN = Label(window,text = "ISBN : ")
LblISBN.grid(row=2,column =3)

eTitle_v = StringVar()
entryTitle = Entry(window,textvariable = eTitle_v)
entryTitle.grid(row=1, column =2)

eYear_v = StringVar()
entryYear = Entry(window,textvariable = eYear_v)
entryYear.grid(row=2, column =2)

eAuth_v = StringVar()
entryAuthor = Entry(window,textvariable = eAuth_v)
entryAuthor.grid(row=1, column =4)

eISBN_v = StringVar()
entryISBN = Entry(window,textvariable = eISBN_v)
entryISBN.grid(row=2, column =4)

lst = Listbox(window, height=6, width =35)
lst.grid(row = 3, column =1, rowspan=6,columnspan=2)

sb = Scrollbar(window,)
sb.grid(row= 3, column = 3,rowspan = 6)

lst.configure(yscrollcommand = sb.set)
sb.configure(command = lst.yview)

btnViewAll = Button(window, text = "View All",width = 12, command =viewAll)
btnViewAll.grid(row=3,column=4)

btnSearchE = Button(window, text = "Search Entry",width = 12, command =searchE)
btnSearchE.grid(row=4,column=4)

btnAddE = Button(window, text = "Add Entry",width = 12, command =addE)
btnAddE.grid(row=5,column=4)

btnUpdate = Button(window, text = "Update",width = 12, command =updtE)
btnUpdate.grid(row=6,column=4)

btnDelete = Button(window, text = "Delete",width = 12, command =delE)
btnDelete.grid(row=7,column=4)

btnViewAll = Button(window, text = "Close",width = 12, command =close)
btnViewAll.grid(row=8,column=4)

window.mainloop()