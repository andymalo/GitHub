from tkinter import *

window = Tk()

b1 = Button(window, text="Execute")
# b1.pack()
b1.grid(row=0,column=0)

l1 = Label(window, text="text")
l1.grid(row=0,column=5)

e1 = Entry(window)
e1.grid(row=0,column=1)

t1= Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()