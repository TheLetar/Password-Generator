from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

window = Tk()
window.title("RPG (Random Password Generator)")
window.config(background='#4E6FE2')
window.minsize(500,180)
window.maxsize(500,180)
window.geometry('500x180+600+350')

tkletters = IntVar()
tknumbers = IntVar()
tksymbols = IntVar()
tkcharacter= IntVar()

def done():
    messagebox.showinfo("Sucess","Your password was copied to the clipboard")
def value(value):
    global scalevalue
    scalevalue = int(value)
    return scalevalue
def generate(length):
    letter = string.ascii_lowercase + string.ascii_uppercase
    number = string.digits
    symbols = string.punctuation

    if tkletters.get() == 1 and tknumbers.get() == 0 and tksymbols.get() == 0:
        result = ''.join(random.choice(letter) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tknumbers.get() == 1 and tkletters.get() == 0 and tksymbols.get() == 0:
        result = ''.join(random.choice(number) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tksymbols.get() == 1 and tkletters.get() == 0 and tknumbers.get() == 0:
        result = ''.join(random.choice(symbols) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tkletters.get() == 1 and tknumbers.get() == 1 and tksymbols.get() == 0:
        result = ''.join(random.choice(letter+number) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tksymbols.get() == 1 and tkletters.get() == 1 and tknumbers.get() == 0:
        result = ''.join(random.choice(symbols+letter) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tksymbols.get() == 1 and tkletters.get() == 0 and tknumbers.get() == 1:
        result = ''.join(random.choice(symbols+number) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()
    if tkletters.get() == 1 and tknumbers.get() == 1 and tksymbols.get() == 1:
        result = ''.join(random.choice(letter+number+symbols) for i in range(length))
        pyperclip.copy(result)
        entrytxt.delete(0, END)
        entrytxt.insert(0, result)
        done()

numbers_check = Checkbutton(window, text='Number',font=("Courrier", 10), bg="#00C9A6", variable=tknumbers)
letters_check = Checkbutton(window, text='Letter',font=("Courrier", 10), bg="#00C9A6", variable=tkletters)
symbols_check = Checkbutton(window, text='Symbol',font=("Courrier", 10), bg="#00C9A6", variable=tksymbols)
txt = Label(window, text ='Password :',font=("Courrier", 10), bg="#4E6FE2")
entrytxt = Entry(window)
character_scale = Scale(window, from_=1, to=150,length=150, orient=HORIZONTAL,label='numbers of chars :',font=("Courrier", 10), bg="#00C9A6", command = value)
character_scale.set(15)
generate_btn = Button(window, text='Generate',font=("Courrier", 10), bg="#F09D39", command= lambda: generate(scalevalue))
generate_btn.grid(row=4, column=2,padx = 10,pady = 5,columnspan=2)
character_scale.grid(row=5, column=1,padx = 0)
letters_check.grid(row=5, column=2,padx = 10,sticky =E)
numbers_check.grid(row=5, column=3,padx = 10,sticky =E)
symbols_check.grid(row=5, column=4,padx = 10,sticky =E)
txt.grid(row=1,column=2,padx = 10,pady = 15,columnspan=2)
entrytxt.grid(row=2,column=2,padx = 10,pady = 0,columnspan=2)

window.mainloop()




