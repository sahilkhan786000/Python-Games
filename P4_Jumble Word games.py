import random
from tkinter import *
from tkinter import messagebox
from random import shuffle


answer = [ " sahil ", "khan", "sikandar", "ronak", "python", "anaconda"]
words = []
for i in answer:
    word=list(i)
    shuffle(word)
    words.append(word)
num = random.randint(0,len(words))


def initial():
    global words,num
    w= str(words[num])
    lbl.configure(text = w )

def ans():
    global words, answer,num
    user_input=e1.get()
    if user_input==answer[num]:
        messagebox.showinfo("Success", "yup this is right")
        Reset()
    else:
        messagebox.showinfo("Error", "nope this is not  right")
        e1.delete(0,END)


def Reset():
    global words, num, answer
    num=random.randint(0, len(words))
    lbl.configure(text=words[num])
    e1.delete(0,END)



root = Tk()
root.geometry("300x300")
lbl = Label(root, font ='times 20')
lbl.pack(pady=30, ipady=10,ipadx=10)

answ = StringVar()
e1 = Entry(root,textvariable = answ)
e1.pack(ipady=5, ipadx = 5)

button1 =Button(root, text="check", width=20, command = ans)
button1.pack(pady=40)

button2 =Button(root, text="Reset", width=20, command = Reset)
button2.pack()

root.mainloop()

