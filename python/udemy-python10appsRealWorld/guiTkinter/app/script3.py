from tkinter import *

window = Tk()

def convert():
    #print(entryKg.get())
    ounces = float(entryKg.get())*350274
    pounds = float(entryKg.get())*2.20462
    grams = float(entryKg.get())*1000
    txtGrams.insert(END, grams)
    txtPounds.insert(END, pounds)
    txtOunces.insert(END, ounces)

LblKg = Label(window, text = "Kg")
LblKg.grid(row=1,column=1)

entryKg_value = StringVar()
entryKg = Entry(window,textvariable =entryKg_value)
entryKg.grid(row=1,column=2)

btnConvert = Button(window, text= "Convert", command = convert)
btnConvert.grid(row=1,column=3)

txtGrams = Text(window,width=15,height=1)
txtGrams.grid(row=2,column=1)

txtPounds = Text(window,width=15,height=1)
txtPounds.grid(row=2,column=2)

txtOunces = Text(window,width=15,height=1)
txtOunces.grid(row=2,column=3)

window.mainloop()