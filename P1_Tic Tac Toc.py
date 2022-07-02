from tkinter import *
from tkinter.messagebox import showinfo

n1,n2,n3,n4,n5,n6,n7,n8,n9=1,1,1,1,1,1,1,1,1
z=1
y=""
x=2
player_1=[]
player_2=[]




def play(p,q):
 choose.destroy()


 def new (p):
     root.destroy()
     win = Tk()
     win.geometry("700x500")
     win.title("TIC TAC TOC")

     def Exit():
        win.destroy()

     lab=Label(win, text="Congratulation !  "+ p + "  You  Won ", font="stencil 20", fg="cyan")
     lab.place(x=50,y=50)
     btn2 = Button(win, text="Back", command=work, height=5, width=6, fg="red", bg="yellow")
     btn2.place(x=100, y=100)
     btn1 = Button(win, text="Exit", command=Exit, height=5, width=6, fg="red", bg="yellow")
     btn1.place(x=300, y=100)

     win.mainloop()


 def newO(q):
     root.destroy()
     win1 = Tk()
     win1.geometry("700x500")
     win1.title("New window")
     def Exit():
         win1.destroy()

     lab=Label(win1, text="Congratulation ! "  +  q + " You  Won ", font="stencil 20", fg="orange")
     lab.place(x=50, y=50)
     btn2=Button(win1, text="Back", command=work, height=5, width=6, fg="red",bg="yellow")
     btn2.place(x=100, y=100)
     btn1 = Button(win1, text="Exit", command=Exit, height=5, width=6, fg="red", bg="yellow")
     btn1.place(x=300, y=100)
     win1.mainloop()







 def compX(p) :
     if b1['text']=='X' and b2['text']=='X' and b3['text']=='X'  :
        new(p)


     elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        new(p)

     elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        new(p)

     elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        new(p)

     elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        new(p)

     elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        new(p)

     elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        new(p)

     elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        new(p)



 def compO(q):
     if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        newO(q)


     elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        newO(q)

     elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        newO(q)

     elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        newO(q)

     elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        newO(q)

     elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        newO(q)

     elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        newO(q)

     elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        newO(q)







 def define_sign(num,p,q):
     global x,y,z,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10
     global player_1, player_2


     if num ==1:
       if n1 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b1.configure(text=y)
         if y=='X':
             b1.configure(bg="cyan")
         elif y=='O':
             b1.configure(bg="orange")
         x=x+1
         compX(p)
         compO(q)


     if num ==2:
       if n2 ==1:
         if x%2==0:
             y='X'
             b2.configure(bg="cyan")
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b2.configure(text=y)
         if y == 'X':
             b2.configure(bg="cyan")
         elif y == 'O':
             b2.configure(bg="orange")
         x=x+1
         n2=n2+1
         compX(p)
         compO(q)



     if num ==3:
       if n3 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b3.configure(text=y)
         if y == 'X':
             b3.configure(bg="cyan")
         elif y == 'O':
             b3.configure(bg="orange")
         x=x+1
         n3=n3+1
         compX(p)
         compO(q)


     if num ==4:
       if n4 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b4.configure(text=y)
         if y == 'X':
             b4.configure(bg="cyan")
         elif y == 'O':
             b4.configure(bg="orange")
         x=x+1
         n4=n4+1
         compX(p)
         compO(q)



     if num ==5:
       if n5 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b5.configure(text=y)
         if y == 'X':
             b5.configure(bg="cyan")
         elif y == 'O':
             b5.configure(bg="orange")
         x=x+1
         n5=n5+1
         compX(p)
         compO(q)




     if num ==6:
       if n6 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b6.configure(text=y)
         if y == 'X':
             b6.configure(bg="cyan")
         elif y == 'O':
             b6.configure(bg="orange")
         x=x+1
         n6=n6+1
         compX(p)
         compO(q)



     if num ==7:
       if n7 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b7.configure(text=y)
         if y == 'X':
             b7.configure(bg="cyan")
         elif y == 'O':
             b7.configure(bg="orange")
         x=x+1
         n7=n7+1
         compX(p)
         compO(q)



     if num ==8:
       if n8 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b8.configure(text=y)
         if y == 'X':
             b8.configure(bg="cyan")
         elif y == 'O':
             b8.configure(bg="orange")
         x=x+1
         n8=n8+1
         compX(p)
         compO(q)




     if num ==9:
       if n9 ==1:
         if x%2==0:
             y='X'
             player_1.append(num)
             print(player_1)

         elif x%2!=0:
             y='O'
             player_2.append(num)
             print(player_2)

         b9.configure(text=y)
         if y == 'X':
             b9.configure(bg="cyan")
         elif y == 'O':
             b9.configure(bg="orange")
         x=x+1
         n9=n9+1
         compX(p)
         compO(q)




 root=Tk()
 root.geometry("700x600")
 root.title("Tic Tac Toc ")

 l1=Label(root,text="Player_1 : "+p, font="times 15")
 l1.grid(row=0,column=1)


 l2=Label(root,text="Player_2 : "+q, font="times 15")
 l2.grid(row=0,column=3)

 b1=Button(root, width=20,height=8,command=lambda:define_sign(1,p,q))
 b1.grid(row=1, column=1)

 b2=Button(root, width=20,height=8,command=lambda:define_sign(2,p,q))
 b2.grid(row=1, column=2)

 b3=Button(root, width=20,height=8,command=lambda:define_sign(3,p,q))
 b3.grid(row=1, column=3)

 b4=Button(root, width=20,height=8,command=lambda:define_sign(4,p,q))
 b4.grid(row=5, column=1)

 b5=Button(root, width=20,height=8,command=lambda:define_sign(5,p,q))
 b5.grid(row=5, column=2)

 b6=Button(root, width=20,height=8,command=lambda:define_sign(6,p,q))
 b6.grid(row=5, column=3)

 b7=Button(root, width=20,height=8,command=lambda:define_sign(7,p,q))
 b7.grid(row=9, column=1)

 b8=Button(root, width=20,height=8,command=lambda:define_sign(8,p,q))
 b8.grid(row=9, column=2)

 b9=Button(root, width=20,height=8,command=lambda:define_sign(9,p,q))
 b9.grid(row=9, column=3)

 root.mainloop()



global work

def work():
    global choose
    main.destroy()
    choose=Tk()
    choose.title("TIC TAC TOC")
    choose.geometry("500x500")

    l=Label(choose, text="NAME YOUR PLAYER : ", font="times,bolditalic,30")
    l.place(x=30, y=40)

    var1=StringVar()
    var2=StringVar()

    def Select():

        global name1, name2
        name1=var1.get()
        name2=var2.get()

        var1.set("")
        var2.set("")
        global B2
        B2=Button(choose,text="Lets Play :", command=lambda:play(name1,name2),font="times,24,bold", fg="white", bg='orange')
        B2.place(x=120,y=240)




    l = Label(choose, text="PLAYER_1 : ", font="time,italic,24")
    l.place(x=30, y=100)

    l = Label(choose, text="PLAYER_2 : ", font="time,italic,24")
    l.place(x=30, y=130)

    e1=Entry(choose,textvariable=var1)
    e1.place(x=150,y=100)

    e2 = Entry(choose, textvariable=var2)
    e2.place(x=150,y=130)


    b=Button(choose,text="PLAY", command=Select,height=3,border=6, width=6, fg="orange", bg="black")
    b.place(x=120, y=200)

    choose.mainloop()











main = Tk()
main.geometry("700x600")
main.title("TIC TAC TOC")
main.configure(bg="white")

def s():
    main.destroy()


L2 = Label(main, text="                                                            "
                      "                                                            "
                      "                                                            "
                      "                                                            ", bg="black", height=8)
L2.place(x=0, y=500)
L1= Label(main, text="WELCOME ! ", font="Stencil 40 bold italic")
L1.place(x=150, y=200)
B1 = Button(main, text="START", command=work, height=5, width=25 ,border=5, fg="violet", bg="black")
B1.place(x=60, y=350)
B2 = Button(main, text="EXIT", command=s, border=5, height=5, width=15, bg="black", fg="violet")
B2.place(x=470, y=380)
main.mainloop()
