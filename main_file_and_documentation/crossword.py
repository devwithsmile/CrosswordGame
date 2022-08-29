#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
from PIL import ImageTk,Image
     


# In[3]:


def welcomePage():
    # Create an instance of tkinter welcomedow
    welcome = Tk()
    welcome.config(bg="black")
    welcome.title("welcome")
    #root = Tk()

    # Define the geometry of the welcomedow
    welcome.geometry("600x600")

    frame = Frame(welcome, width=600, height=400)
    frame.pack()
    frame.config(bg="black")
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("crossword.jpeg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()


    button1 = Button(frame, text='Start' ,width = 8,bg = "#6CD300", fg = "black",command=lambda: [welcome.destroy(),option()])
    button1.pack(side=LEFT)
    button1.config(height=2,
    width=15)

    button2 = Button(frame, text='Quit' ,width = 8,
                 bg = "#6CD300", fg = "black" , command=welcome.destroy)
    button2.pack(side=RIGHT)
    button2. config(height=2,
    width=15)

    welcome.mainloop()


# In[4]:


def option():
    # Create an instance of tkinter window
    win = Tk()

    win.resizable(False,False)
    win.config(bg="black")
    #root = Tk()

    # Define the geometry of the window
    win.geometry("600x500")
    win.title("option page")

    frame = Frame(win, width=600, height=400)
    frame.config(bg="black")
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("level1.jfif"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()


    button1 = Button(frame, text='Easy' ,width = 8,bg = "#6CD300", fg = "black",command=lambda:[win.destroy(),level1()])
    button1.place(x=130, y=200)
    button1. config(height=3,
    width=15)

    button2 = Button(frame, text='Hard' ,width = 8,bg = "#6CD300", fg = "black",command=lambda:[win.destroy(),level5()] )
    button2.place(x=290, y=200)
    button2. config(height=3,
    width=15)

    win.mainloop()


# In[5]:


def level1():

    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)


    def submit():
        #inputvariables
        v1=b2.get()
        v2=b8.get()

        if v1.upper()=="E" and v2.upper()=="G":
            messagebox.showinfo("showinfo","U cleared the level !")
            root.destroy()
            level2()

        elif v1.upper()!="E":
            messagebox.showinfo("showinfo","First value is incorrect!")

        elif v2.upper()!="G":
            #l71=tk.Label(f3,text="\n HEY SECOND VALUE IS INCORRECT\n ",bg="red",fg="white")
            #l71.grid()
            
            messagebox.showinfo("showinfo","second value is incorrect!")

        else:
            #l71=tk.Label(f2,text="\n U failed\n ",bg="red",fg="white")
            #l71.grid()
            messagebox.showinfo("showinfo","U FAILED!")


    root=tk.Tk()
    root.geometry("800x600")
    root.resizable(False,False)
    root.title("crossword level 1 ")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(root,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1
    b1=tk.Label(f1,text="H",width="5")
    b1.grid()

    b2=tk.Entry(f1,width="5")
    b2.grid(row="0",column="1",padx="0")

    b3=tk.Label(f1,text="Y",width="5")
    b3.grid(row="0",column="2",padx="0")

      #row2
    b4=tk.Label(f1,width="5",bg="black")
    b4.grid(row="1",column="0",)

    b5=tk.Label(f1,text="G",width="5")
    b5.grid(row="1",column="1",padx="2",pady="2")

    b6=tk.Label(f1,width="5",bg="black")
    b6.grid(row="1",column="2",padx="0",pady="2")

     #row3

    b7=tk.Label(f1,text="N",width="5")
    b7.grid(row="2",column="0",)

    b8=tk.Entry(f1,width="5")
    b8.grid(row="2",column="1",padx="2",pady="1")

    b9=tk.Label(f1,width="5",text="O")
    b9.grid(row="2",column="2",padx="0",pady="1")



    #frame2
    f2=tk.Frame(root)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid()


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="1. Used to greet someomne \n")
    l3.grid()

    l4=tk.Label(f2,text="2. Group of people helping \n      others under a single name")
    l4.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()])
    button1.grid()

    #frame3
    f3=tk.Frame(root)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label2=tk.Label(f3,text="\n 1.  Protien source")
    label2.grid()


    label9=tk.Label(f3,text="\n\n\n\n\n\n")#using it like "\n"
    label9.grid()

    button2=tk.Button(f3,text="QUIT",command=root.destroy)
    button2.grid()


    #execution
    root.mainloop()


# In[6]:


def level2():

    def submit():
        #inputvariables
        v1=b1.get()
        v2=b3.get()
        v3=b5.get()
        v4=b7.get()
        v5=b9.get()

        if v1.upper()=="" and v2.upper()=="" and v3.upper()=="" and v4.upper()=="" and v5.upper()=="":
            messagebox.showinfo("showinfo", "Please enter value!!!")
            
            

        elif v1.upper()=="A" and v2.upper()=="E" and v3.upper()=="A" and v4.upper()=="E" and v5.upper()=="O":
            messagebox.showinfo("showinfo", "cleared the crossword")
            level2.destroy()
            level3()

        elif v1.upper()!="A":
            messagebox.askretrycancel("askretrycancel", " 1st row , 1st value is incorrect!")

        elif v2.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "1st row ,2nd value is incorrect!")  

        elif v3.upper()!="A":
            messagebox.askretrycancel("askretrycancel", "2nd row is incorrect!")  

        elif v4.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "3rd row, 1st value is incorrect!") 

        elif v5.upper()!="O":
            messagebox.askretrycancel("askretrycancel", "3rd row ,2nd value is incorrect!") 

        else:
            messagebox.showerror("showerror", "U failed")


    level2=tk.Tk()
    level2.geometry("800x600")
    level2.resizable(False,False)
    level2.title("Easy level 2")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(level2,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1
    b1=tk.Entry(f1,width="5")
    b1.grid()

    b2=tk.Label(f1,width="5",text="C")
    b2.grid(row="0",column="1",padx="0")

    b3=tk.Entry(f1,width="5")
    b3.grid(row="0",column="2",padx="0")

      #row2
    b4=tk.Label(f1,width="5",text="G")
    b4.grid(row="1",column="0",)

    b5=tk.Entry(f1,width="5")
    b5.grid(row="1",column="1",padx="2",pady="2")

    b6=tk.Label(f1,width="5",text="G")
    b6.grid(row="1",column="2",padx="0",pady="2")

     #row3

    b7=tk.Entry(f1,width="5")
    b7.grid(row="2",column="0",)

    b8=tk.Label(f1,width="5",text="P")
    b8.grid(row="2",column="1",padx="2",pady="1")

    b9=tk.Entry(f1,width="5")
    b9.grid(row="2",column="2",padx="0",pady="1")



    #frame2
    f2=tk.Frame(level2)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid()


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="1. A playing card with a single spot on it,\n ranked as the highest card in its suit in most card games. \n")
    l3.grid()

    l4=tk.Label(f2,text="2.a device for keeping the patient's mouth open during a \ndental or surgical operation. \n")
    l4.grid()

    l5=tk.Label(f2,text="3.A type of health plan that offers a local network of \ndoctors and hospitals for you to choose from   \n ")
    l5.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()])
    button1.grid()

    #frame3
    f3=tk.Frame(level2)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label2=tk.Label(f3,text="\n 1.  The length of time that a person has lived or a thing has existed.")
    label2.grid()


    label2=tk.Label(f3,text="\n 2. a protective lid or cover for an object such as a bottle. \n")
    label2.grid()


    #label10=tk.Label(f3,text="\n")#using it like "\n"
    #label10.grid()

    label4=tk.Label(f3,text="\n 3. a person's sense of self-esteem or self-importance..\n\n\n\n\n\n\n")
    label4.grid()

    button1=tk.Button(f3,text="QUIT",command=level2.destroy)
    button1.grid()


    #execution
    level2.mainloop()




# In[7]:


def level3():
    def submit():
        #inputvariables
        v1=b1.get()
        v2=b3.get()
        v3=b6.get()
        v4=b7.get()
        v5=b9.get()
        v6=b12.get()
        
        

        if v1.upper()=="A" and v2.upper()=="L" and v3.upper()=="A" and v4.upper()=="A" and v5.upper()=="T" and v6.upper()=="I":
            messagebox.showinfo("showinfo","U cleared the level !")
            level3.destroy()
            level4()

        elif (v2.upper()=="L" and v3.upper()=="A" and v4.upper()=="A" and v6.upper()=="I") and (v1.upper()!="A" or v5.upper()=="T"):
            messagebox.showinfo("showinfo","First value is incorrect! (Down)")

        elif v3.upper()!="A":
            messagebox.showinfo("showinfo","second value is incorrect!(Down)")
       
        elif v2.upper()!="L" or v4.upper()!="A":
            messagebox.showinfo("showinfo","Third value is incorrect!(Down)")

        elif v6.upper()!="I":
            messagebox.showinfo("showinfo","Third value is incorrect!(Across)")
            
        elif v5.upper()!="T":
            messagebox.showinfo("showinfo","Third value is incorrect (Across)")

        else:
            #l71=tk.Label(f2,text="\n U failed\n ",bg="red",fg="white")
            #l71.grid()
            messagebox.showinfo("showinfo","U FAILED!")


    level3 =tk.Tk()
    level3.geometry("800x600")
    level3.resizable(False,False)
    level3.title("level 3")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(level3,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1
    b1=tk.Entry(f1,width="5")
    b1.grid()

    b2=tk.Label(f1,text="B",width="5")
    b2.grid(row="0",column="1",padx="0")

    b3=tk.Entry(f1,width="5")
    b3.grid(row="0",column="2",padx="0")
    
    b4=tk.Label(f1,text="E",width="5")
    b4.grid(row="0",column="3",padx="0")

      #row2
    
    b5=tk.Label(f1,text="C",width="5")
    b5.grid(row="1",column="0",padx="2",pady="2")

    b6=tk.Entry(f1,width="5")
    b6.grid(row="1",column="1",padx="0")
    
    b7=tk.Entry(f1,width="5")
    b7.grid(row="1",column="2",padx="0")

    b8=tk.Label(f1,text="",width="5")
    b8.grid(row="1",column="3",padx="2",pady="2")

     #row3

    b9=tk.Entry(f1,width="5")
    b9.grid(row="2",column="0",padx="2",pady="1")

    b10=tk.Label(f1,text="Y",width="5")
    b10.grid(row="2",column="1",padx="2",pady="1")

    b11=tk.Label(f1,text="B",width="5")
    b11.grid(row="2",column="2",padx="2",pady="1")
    
    b12=tk.Entry(f1,width="5")
    b12.grid(row="2",column="3",)


    #frame2
    f2=tk.Frame(level3)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid()


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="\n 1. To have the ability, power, opportunity,\n time, etc. to do something \n")
    l3.grid()

    l4=tk.Label(f2,text="\n 2. A bill that became popular with \n NRC in INDIA")
    l4.grid()

    l5=tk.Label(f2,text="\n 3. The fifth month of the later \n ancient Egyptian civil calendar")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()])
    button1.grid()

    #frame3
    f3=tk.Frame(level3)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label2=tk.Label(f3,text="\n\n\n 1. To perform a particular function")
    label2.grid()
    
    label3=tk.Label(f3,text="\n\n 2. A part of the coast where the land \n goes in to form a curve \n")
    label3.grid()

    label4=tk.Label(f3,text="\n 3. Short form of laboratory.")
    label4.grid()
    
    
    


    label9=tk.Label(f3,text="\n\n")#using it like "\n"
    label9.grid()

    button1=tk.Button(f3,text="QUIT",command=level3.destroy)
    button1.grid()


    #execution
    level3.mainloop()


# In[8]:


def level4():
    def submit():
        #inputvariables
        v1=b2.get()
        v2=b4.get()
        v3=b6.get()
        v4=b8.get()
        v5=b9.get()
        v6=b10.get()
        
        
        

        if v1.upper()=="A" and v2.upper()=="A" and v3.upper()=="C" and v4.upper()=="H" and v5.upper()=="I" and v6.upper()=="E":
            messagebox.showinfo("showinfo","U cleared the level !")
            level4.destroy()
            level5()

        elif (v1.upper()=="A" and v3.upper()=="C" and v4.upper()=="H" and v5.upper()=="I") and (v2.upper()!="A" or v6.upper()!="E"):
            messagebox.showinfo("askretrycancel","First value is incorrect! (Down)")

        elif v1.upper()!="A" or v4.upper()!="H":
            messagebox.showinfo("showinfo","second value is incorrect!(Down)")
       
        elif v3.upper()!="C":
            messagebox.showinfo("showinfo","second value is incorrect!(Across)")

        elif v5.upper()!="I":
            messagebox.showinfo("showinfo","Third value is incorrect!(Across)")
            
    
        else:
            #l71=tk.Label(f2,text="\n U failed\n ",bg="red",fg="white")
            #l71.grid()
            messagebox.showinfo("showinfo","U FAILED!")


    level4 =tk.Tk()
    level4.geometry("800x600")
    level4.resizable(False,False)
    level4.title("level 4")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(level4,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      
        #row1
        
    b1=tk.Label(f1,text="C",width="5")
    b1.grid()

    b2=tk.Entry(f1,width="5")
    b2.grid(row="0",column="1",padx="0")

    b3=tk.Label(f1,text="T",width="5")
    b3.grid(row="0",column="2",padx="0")
    
   

      #row2
    
    b4=tk.Entry(f1,width="5")
    b4.grid(row="1",column="0",padx="0")
    
    b5=tk.Label(f1,text="C",width="5")
    b5.grid(row="1",column="1",padx="2",pady="2")

    b6=tk.Entry(f1,width="5")
    b6.grid(row="1",column="2",padx="0")
    
     #row3

    
    b7=tk.Label(f1,text="G",width="5")
    b7.grid(row="2",column="0",padx="0")

    b8=tk.Entry(f1,width="5")
    b8.grid(row="2",column="1",padx="2",pady="2")

    b9=tk.Entry(f1,width="5")
    b9.grid(row="2",column="2",padx="2",pady="1")
    
    #row4

    b10=tk.Entry(f1,width="5")
    b10.grid(row="3",column="0",padx="2",pady="1")

    b11=tk.Label(f1,text="E",width="5")
    b11.grid(row="3",column="1",padx="2",pady="1")
    
    b12=tk.Label(f1,text="",width="5")
    b12.grid(row="3",column="2",)


    #frame2
    f2=tk.Frame(level4)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid()


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="\n 1. Pet animal which is of same family \n\n in which lion and tiger belong \n")
    l3.grid()

    l4=tk.Label(f2,text="\n 2. A well known cement brand")
    l4.grid()

    l5=tk.Label(f2,text="\n 3.Made using milk \n\n\n\n\n ")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()])
    button1.grid()

    #frame3
    f3=tk.Frame(level4)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label2=tk.Label(f3,text="\n\n\n 1.A  box made of bars or wire \n, in which a bird or animal is kept \n so that it cannot escape")
    label2.grid()
    
    label3=tk.Label(f3,text="\n\n 2. A Pain that lasts a for long time \n")
    label3.grid()

    label4=tk.Label(f3,text="\n 3. Abrrivation of a system aims \n that  to get a target plasma \n concentration chosen by the user.")
    label4.grid()
    
    
    


    label9=tk.Label(f3,text="\n\n")#using it like "\n"
    label9.grid()

    button2=tk.Button(f3,text="QUIT",command=level4.destroy)
    button2.grid()


    #execution
    level4.mainloop()


# In[9]:


def level5():
    def submit():
        #inputvariables
        v1=b3.get()
        v2=b5.get()
        v3=b6.get()
        v4=b14.get()
        v5=b17.get()
        v6=b27.get()
        v7=b28.get()
        v8=b29.get()
        v9=b30.get()
        v10=b38.get()
        v11=b40.get()
        v12=b51.get()
        v13=b52.get()
        v14=b63.get()
        v15=b65.get()


        if v1.upper()=="" and v2.upper()=="" and v3.upper()=="" and v4.upper()=="" and v5.upper()=="" and v6.upper()=="" and v7.upper()=="" and v8.upper()=="" and v9.upper()=="" and v10.upper()=="" and v11.upper()=="" and v12.upper()=="" and v13.upper()=="" and v14.upper()=="" and v15.upper()=="" :
            messagebox.showinfo("showinfo", "Please enter value!!!")


        elif v1.upper()=="B" and v2.upper()=="L" and v3.upper()=="E" and v4.upper()=="R" and v5.upper()=="E" and v6.upper()=="E" and v7.upper()=="A" and v8.upper()=="R" and v9.upper()=="L" and v10.upper()=="H" and v11.upper()=="G" and v12.upper()=="T" and v13.upper()=="E" and v14.upper()=="Y" and v15.upper()=="E":
            messagebox.showinfo("showinfo", "cleared the crossword")
            root.destroy()
            level6()

        elif v1.upper()!="B":
            messagebox.askretrycancel("askretrycancel", "1st row, 1st value is incorrect!")

        elif v2.upper()!="L":
            messagebox.askretrycancel("askretrycancel", "1st row, 2nd value is incorrect!")  

        elif v3.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "1st row, 3rd value is incorrect!")  

        elif v4.upper()!="R":
            messagebox.askretrycancel("askretrycancel", "2nd row, 1st value is incorrect!")  

        elif v5.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd row, 2nd value is incorrect!")

        elif v6.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "3rd row ,1st value is incorrect!")  

        elif v7.upper()!="A":
            messagebox.askretrycancel("askretrycancel", "3rd row ,2nd value is incorrect!")  

        elif v8.upper()!="R":
            messagebox.askretrycancel("askretrycancel", "3rd row ,3rd value is incorrect!")  

        elif v9.upper()!="L":
            messagebox.askretrycancel("askretrycancel", "3rd row ,4th value is incorrect!")  

        elif v10.upper()!="H":
            messagebox.askretrycancel("askretrycancel", "4th row, 1st value is incorrect!")  

        elif v11.upper()!="G":
            messagebox.askretrycancel("askretrycancel", "4th row, 2nd value is incorrect!")  

        elif v12.upper()!="T":
            messagebox.askretrycancel("askretrycancel", "5th row, 1st value is incorrect!")  

        elif v13.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "5th row, 2nd value is incorrect!")  

        elif v14.upper()!="Y":
            messagebox.askretrycancel("askretrycancel", "6th row,1st value is incorrect")  

        elif v15.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "6th row, 2nd value is incorrect")  


        else:
            messagebox.showerror("showerror", "U failed")


    root=tk.Tk()
    root.geometry("800x800")
    root.resizable(False,False)
    root.title("hard level 1")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(root,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1

    b1=tk.Label(f1,width="5",text="M")
    b1.grid(row="0",column="0")

    b2=tk.Label(f1,width="5",text="O")
    b2.grid(row="0",column="1")

    b3=tk.Entry(f1,width="5")
    b3.grid(row="0",column="2")

    b4=tk.Label(f1,width="5",text="I")
    b4.grid(row="0",column="3")

    b5=tk.Entry(f1,width="5")
    b5.grid(row="0",column="4")

    b6=tk.Entry(f1,width="5")
    b6.grid(row="0",column="5")





      #row2
    b13=tk.Label(f1,width="5",text="",bg="black")
    b13.grid(row="1",column="0")

    b14=tk.Entry(f1,width="5")
    b14.grid(row="1",column="1")

    b15=tk.Label(f1,width="5",text="",bg="black")
    b15.grid(row="1",column="2")

    b16=tk.Label(f1,width="5",text="M")
    b16.grid(row="1",column="3")

    b17=tk.Entry(f1,width="5")
    b17.grid(row="1",column="4")

    b18=tk.Label(f1,width="5",text="N")
    b18.grid(row="1",column="5")



     #row3
    b25=tk.Label(f1,width="5",text="",bg="black")
    b25.grid(row="2",column="0")

    b26=tk.Label(f1,width="5",text="P")
    b26.grid(row="2",column="1")

    b27=tk.Entry(f1,width="5")
    b27.grid(row="2",column="2")

    b28=tk.Entry(f1,width="5")
    b28.grid(row="2",column="3")

    b29=tk.Entry(f1,width="5")
    b29.grid(row="2",column="4")

    b30=tk.Entry(f1,width="5")
    b30.grid(row="2",column="5")



    #row4
    b37=tk.Label(f1,width="5",text="P")
    b37.grid(row="3",column="0")

    b38=tk.Entry(f1,width="5")
    b38.grid(row="3",column="1")

    b39=tk.Label(f1,width="5",text="",bg="black")
    b39.grid(row="3",column="2")

    b40=tk.Entry(f1,width="5")
    b40.grid(row="3",column="3")

    b41=tk.Label(f1,width="5",text="",bg="black")
    b41.grid(row="3",column="4")

    b42=tk.Label(f1,width="5",text="",bg="black")
    b42.grid(row="3",column="5")


    #row5
    b49=tk.Label(f1,width="5",text="",bg="black")
    b49.grid(row="4",column="0")

    b50=tk.Label(f1,width="5",text="A")
    b50.grid(row="4",column="1")

    b51=tk.Entry(f1,width="5")
    b51.grid(row="4",column="2")

    b52=tk.Entry(f1,width="5")
    b52.grid(row="4",column="3",padx="0")

    b53=tk.Label(f1,width="5",text="",bg="black")
    b53.grid(row="4",column="4")

    b54=tk.Label(f1,width="5",text="",bg="black")
    b54.grid(row="4",column="5")



    #row6
    b61=tk.Label(f1,width="5",text="",bg="black")
    b61.grid(row="5",column="0")

    b62=tk.Label(f1,width="5",text="N")
    b62.grid(row="5",column="1")

    b63=tk.Entry(f1,width="5",bg="white")
    b63.grid(row="5",column="2")

    b64=tk.Label(f1,text="S",width="5")
    b64.grid(row="5",column="3")

    b65=tk.Entry(f1,width="5",bg="white")
    b65.grid(row="5",column="4")

    b66=tk.Label(f1,width="5",text="",bg="black")
    b66.grid(row="5",column="5")



    #frame2
    f2=tk.Frame(root)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid(row="0",column="0")


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="1.  a telephone with access to a cellular radio\n system so it can be used\n over a wide area, without \na physical connection to a network. \n")
    l3.grid()

    l8=tk.Label(f2,text="2. plural of man. \n ")
    l8.grid()

    l4=tk.Label(f2,text="3.  something resembling this, as various\n synthetic substances \nfor use in costume jewelry. \n")
    l4.grid()

    l5=tk.Label(f2,text="4.  a figure expressing the acidity or alkalinity of\n a solution on a logarithmic scale on which 7 is \nneutral, lower values are more acid and higher\n values more alkaline.  \n ")
    l5.grid()

    l6=tk.Label(f2,text="5. Past of eat \n ")
    l6.grid()

    l7=tk.Label(f2,text="6. What is stock exchange of NEW YORK called  \n ")
    l7.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()



    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()] ,bg='white')
    button1.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()


    #button10=tk.Button(f2,text="Show",command=show ,bg='white')
    #button10.grid()

    #frame3
    f3=tk.Frame(root)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label3=tk.Label(f3,text="\n 1.Child who does not have parents  (R)")
    label3.grid()

    #label9=tk.Label(f3,text="\n")#using it like "\n"
    #label9.grid()


    label2=tk.Label(f3,text="\n 2. ---- is an acronym meaning Thank You.")
    label2.grid()


    #label10=tk.Label(f3,text="\n")#using it like "\n"
    #label10.grid()

    label4=tk.Label(f3,text="\n 3. A representation of the external form of \na person or thing in art.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    label4.grid()



    button10=tk.Button(f3,text="QUIT",command=root.destroy ,bg='white')
    button10.grid()

    label4=tk.Label(f3,text="")#using it like "\n"
    label4.grid()

    label5=tk.Label(f3,text="")#using it like "\n"
    label5.grid()

    #button15=tk.Button(f3,text="cancel",command=cancel ,bg='white')
    #button15.grid()



    #execution
    root.mainloop()


# In[10]:


def level6():
    def submit():
        #inputvariables
        v1=b3.get()
        v2=b5.get()
        v3=b14.get()
        v4=b16.get()
        v5=b18.get()
        v6=b27.get()
        v7=b28.get()
        v8=b29.get()
        v9=b30.get()
        v10=b38.get()
        v11=b40.get()
        v12=b50.get()
        v13=b53.get()
        v14=b54.get()



        if v1.upper()=="" and v2.upper()=="" and v3.upper()=="" and v4.upper()=="" and v5.upper()=="" and v6.upper()=="" and v7.upper()=="" and v8.upper()=="" and v9.upper()=="" and v10.upper()=="" and v11.upper()=="" and v12.upper()=="" and v13.upper()=="" and v14.upper()=="" :
            messagebox.showinfo("showinfo", "Please enter value!!!")
            

        elif v1.upper()=="P" and v2.upper()=="O" and v3.upper()=="P" and v4.upper()=="I" and v5.upper()=="O" and v6.upper()=="I" and v7.upper()=="L" and v8.upper()=="O" and v9.upper()=="T" and v10.upper()=="L" and v11.upper()=="E" and v12.upper()=="E" and v13.upper()=="A" and v14.upper()=="Y":
            messagebox.showinfo("showinfo", "cleared the crossword")
            root.destroy()
            hardlevel3()


        elif v1.upper()!="P":
            messagebox.askretrycancel("askretrycancel", "1st row, 1st value is incorrect!")

        elif v2.upper()!="O":
            messagebox.askretrycancel("askretrycancel", "1st row, 2nd value is incorrect!")  

        elif v3.upper()!="P":
            messagebox.askretrycancel("askretrycancel", "2nd row, 1st value is incorrect!")  

        elif v4.upper()!="I":
            messagebox.askretrycancel("askretrycancel", "2nd row, 2nd value is incorrect!")  

        elif v5.upper()!="O":
            messagebox.askretrycancel("askretrycancel", "2nd row, 3rd is incorrect!")

        elif v6.upper()!="I":
            messagebox.askretrycancel("askretrycancel", "3rd row ,1st value is incorrect!")  

        elif v7.upper()!="L":
            messagebox.askretrycancel("askretrycancel", "3rd row,2nd value is incorrect!")  

        elif v8.upper()!="O":
            messagebox.askretrycancel("askretrycancel", "3rd row,3rd value is incorrect!")  

        elif v9.upper()!="T":
            messagebox.askretrycancel("askretrycancel", "3rd row,4th value is incorrect!")  

        elif v10.upper()!="L":
            messagebox.askretrycancel("askretrycancel", "4th row, 1st value is incorrect!")  

        elif v11.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "4th row, 2nd value is incorrect!")  

        elif v12.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "5th row,1st value is incorrect!")  

        elif v13.upper()!="A":
            messagebox.askretrycancel("askretrycancel", "5th row,  2nd value is incorrect!")  

        elif v14.upper()!="Y":
            messagebox.askretrycancel("askretrycancel", "5th row , 3rd value is incorrect!")  


        else:
            messagebox.showerror("showerror", "U failed")


    root=tk.Tk()
    root.geometry("800x800")
    root.resizable(False,False)
    root.title("hard level 2")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(root,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1

    b1=tk.Label(f1,width="5",text="L")
    b1.grid(row="0",column="0")

    b2=tk.Label(f1,width="5",text="A")
    b2.grid(row="0",column="1")

    b3=tk.Entry(f1,width="5")
    b3.grid(row="0",column="2")

    b4=tk.Label(f1,width="5",text="T")
    b4.grid(row="0",column="3")

    b5=tk.Entry(f1,width="5")
    b5.grid(row="0",column="4")

    b6=tk.Label(f1,width="5",text="P")
    b6.grid(row="0",column="5")





      #row2
    b13=tk.Label(f1,width="5",text="",bg="black")
    b13.grid(row="1",column="0")

    b14=tk.Entry(f1,width="5")
    b14.grid(row="1",column="1")

    b15=tk.Label(f1,width="5",text="",bg="black")
    b15.grid(row="1",column="2")

    b16=tk.Entry(f1,width="5")
    b16.grid(row="1",column="3")

    b17=tk.Label(f1,width="5",text="",bg="black")
    b17.grid(row="1",column="4")

    b18=tk.Entry(f1,width="5")
    b18.grid(row="1",column="5")



     #row3
    b25=tk.Label(f1,width="5",text="",bg="black")
    b25.grid(row="2",column="0")

    b26=tk.Label(f1,width="5",text="P")
    b26.grid(row="2",column="1")

    b27=tk.Entry(f1,width="5")
    b27.grid(row="2",column="2")

    b28=tk.Entry(f1,width="5")
    b28.grid(row="2",column="3")

    b29=tk.Entry(f1,width="5")
    b29.grid(row="2",column="4")

    b30=tk.Entry(f1,width="5")
    b30.grid(row="2",column="5")



    #row4
    b37=tk.Label(f1,width="5",text="",bg="black")
    b37.grid(row="3",column="0")

    b38=tk.Entry(f1,width="5")
    b38.grid(row="3",column="1")

    b39=tk.Label(f1,width="5",text="",bg="black")
    b39.grid(row="3",column="2")

    b40=tk.Entry(f1,width="5")
    b40.grid(row="3",column="3")

    b41=tk.Label(f1,width="5",text="",bg="black")
    b41.grid(row="3",column="4")

    b42=tk.Label(f1,width="5",text="",bg="black")
    b42.grid(row="3",column="5")


    #row5
    b49=tk.Label(f1,width="5",text="",bg="black")
    b49.grid(row="4",column="0")

    b50=tk.Entry(f1,width="5")
    b50.grid(row="4",column="1")

    b51=tk.Label(f1,width="5",text="S")
    b51.grid(row="4",column="2")

    b52=tk.Label(f1,width="5",text="S")
    b52.grid(row="4",column="3",padx="0")

    b53=tk.Entry(f1,width="5")
    b53.grid(row="4",column="4")

    b54=tk.Entry(f1,width="5")
    b54.grid(row="4",column="5")







    #frame2
    f2=tk.Frame(root)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid(row="0",column="0")


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="1. a computer that is portable and suitable \nfor use while travelling.  \n")
    l3.grid()

    l8=tk.Label(f2,text="2. a person who operates the flying controls \nof an aircraft. \n ")
    l8.grid()

    l4=tk.Label(f2,text="3.  a short piece of writing on a particular subject. \n\n")
    l4.grid()




    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()
    
    
    
    



    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()],bg='white')
    button1.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()


    #button10=tk.Button(f2,text="Show",command=show ,bg='white')
    #button10.grid()

    #frame3
    f3=tk.Frame(root)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label3=tk.Label(f3,text="\n 1.the round fruit of a tree of the rose family,\n which typically has thin green or red skin and crisp flesh.")
    label3.grid()

    #label9=tk.Label(f3,text="\n")#using it like "\n"
    #label9.grid()


    label2=tk.Label(f3,text="\n 2. a thin rectangular slab of baked clay or other material,\n used in overlapping rows for covering roofs.")
    label2.grid()


    #label10=tk.Label(f3,text="\n")#using it like "\n"
    #label10.grid()

    label4=tk.Label(f3,text="\n 3.a rounded or cylindrical container, typically of \nmetal, used for cooking..\n\n")
    label4.grid()



    button10=tk.Button(f3,text="QUIT",command=root.destroy ,bg='white')
    button10.grid()

    label4=tk.Label(f3,text="")#using it like "\n"
    label4.grid()

    label5=tk.Label(f3,text="")#using it like "\n"
    label5.grid()

    #button15=tk.Button(f3,text="cancel",command=cancel ,bg='white')
    #button15.grid()



    #execution
    root.mainloop()


# In[28]:


def hardlevel3():
    def submit():
        #inputvariables
        v1=b3.get()
        v2=b5.get()
        v3=b7.get()
        v4=b10.get()
        v5=b15.get()
        v6=b19.get()
        v7=b21.get()
        v8=b28.get()
        v9=b31.get()
        v10=b33.get()
        
        
        

        if v1.upper()=="T" and v2.upper()=="M" and v3.upper()=="C" and v4.upper()=="R" and v5.upper()=="S" and v6.upper()=="V" and v7.upper()=="D" and v8.upper()=="E" and v9.upper()=="S"and v10.upper()=="E":
            messagebox.showinfo("showinfo","U cleared the level !")
            hardlevel3.destroy()
            hardlevel4()

        elif v5.upper()!="S":
            messagebox.showinfo("showinfo","First value is incorrect! (Down)")

        elif v1.upper()!="T" or v4.upper()!="R" or v5.upper()!="S":
            messagebox.showinfo("showinfo","Third value is incorrect!(Down)")
       
        elif v2.upper()!="M" or v6.upper()!="V" or v10.upper()!="E":
            messagebox.showinfo("showinfo","FIFTH value is incorrect!(DOWN)")

        elif v3.upper()!="C" or v7.upper()!="D" or v8.upper()!="E" :
            messagebox.showinfo("showinfo","Seventh value is incorrect!(Down)")
            
        #elif v5.upper()!="S":
           # messagebox.showinfo("showinfo","THIRD value is incorrect (ACROSS)")

        else:
            #l71=tk.Label(f2,text="\n U failed\n ",bg="red",fg="white")
            #l71.grid()
            messagebox.showinfo("showinfo","U FAILED!")


    hardlevel3 =tk.Tk()
    hardlevel3.geometry("800x600")
    hardlevel3.resizable(False,False)
    hardlevel3.title("hard level 3")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(hardlevel3,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      
        #row1
        
    b1=tk.Label(f1,text="",width="5",bg="black")
    b1.grid()

    b2=tk.Label(f1,text="A",width="5")
    b2.grid(row="0",column="1",padx="0")

    b3=tk.Entry(f1,width="5")
    b3.grid(row="0",column="2",padx="0")
    
    
    b4=tk.Label(f1,text="O",width="5")
    b4.grid(row="0",column="3",padx="0")
    
    b5=tk.Entry(f1,width="5")
    b5.grid(row="0",column="4",padx="0")
    
    b6=tk.Label(f1,text="I",width="5")
    b6.grid(row="0",column="5",padx="0")
    
    b7=tk.Entry(f1,width="5")
    b7.grid(row="0",column="6",padx="0")
    
    #ROW2
    b8=tk.Label(f1,text="U",width="5")
    b8.grid(row="1",column="0",padx="0")
    
    b9=tk.Label(f1,text="",width="5",bg="black")
    b9.grid(row="1",column="1",padx="0")
    
    b10=tk.Entry(f1,width="5")
    b10.grid(row="1",column="2",padx="0")
    
    b11=tk.Label(f1,text="",width="5",bg="black")
    b11.grid(row="1",column="3",padx="0")
    
    b12=tk.Label(f1,text="O",width="5")
    b12.grid(row="1",column="4",padx="0")
    
    b13=tk.Label(f1,text="",width="5",bg="black")
    b13.grid(row="1",column="5",padx="0")
    
    b14=tk.Label(f1,text="A",width="5")
    b14.grid(row="1",column="6",padx="0")
    
    #ROW3
    
    b15=tk.Entry(f1,width="5")
    b15.grid(row="2",column="0",padx="0")
    
    b16=tk.Label(f1,text="L",width="5")
    b16.grid(row="2",column="1",padx="0")
    
    b17=tk.Label(f1,text="E",width="5")
    b17.grid(row="2",column="2",padx="0")
    
    b18=tk.Label(f1,text="E",width="5")
    b18.grid(row="2",column="3",padx="0")
    
    b19=tk.Entry(f1,width="5")
    b19.grid(row="2",column="4",padx="0")
    
    b20=tk.Label(f1,text="E",width="5")
    b20.grid(row="2",column="5",padx="0")
    
    b21=tk.Entry(f1,width="5")
    b21.grid(row="2",column="6",padx="0")
    
    
    #ROW4
    
    b22=tk.Label(f1,text="E",width="5")
    b22.grid(row="3",column="0",padx="0")
    
    b23=tk.Label(f1,text="",width="5",bg="black")
    b23.grid(row="3",column="1",padx="0")
    
    b24=tk.Label(f1,text="E",width="5")
    b24.grid(row="3",column="2",padx="0")
    
    b25=tk.Label(f1,text="",width="5",bg="black")
    b25.grid(row="3",column="3",padx="0")
    
    b26=tk.Label(f1,text="I",width="5")
    b26.grid(row="3",column="4",padx="0")
    
    b27=tk.Label(f1,text="",width="5",bg="black")
    b27.grid(row="3",column="5",padx="0")
    
    b28=tk.Entry(f1,width="5")
    b28.grid(row="3",column="6",padx="0")

    #ROW5
    
    b29=tk.Label(f1,text="D",width="5")
    b29.grid(row="4",column="0",padx="0")
    
    b30=tk.Label(f1,text="",width="5",bg="black")
    b30.grid(row="4",column="1",padx="0")
    
    b31=tk.Entry(f1,width="5")
    b31.grid(row="4",column="2",padx="0")
    
    b32=tk.Label(f1,text="H",width="5")
    b32.grid(row="4",column="3",padx="0")
    
    b33=tk.Entry(f1,width="5")
    b33.grid(row="4",column="4",padx="0")
    
    b34=tk.Label(f1,text="E",width="5")
    b34.grid(row="4",column="5",padx="0")
    
    b35=tk.Label(f1,text="T",width="5")
    b35.grid(row="4",column="6",padx="0")
    






    #frame2
    f2=tk.Frame(hardlevel3)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid()


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="\n 1.of or concerning an atom or atoms\n")
    l3.grid()

    l4=tk.Label(f2,text="\n 3. If u wear a sleeve u will be ??\n")
    l4.grid()

    l5=tk.Label(f2,text="\n 5. A peice of cloth used to cover your bed !\n\n\n\n")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    l8=tk.Label(f2,text="")#using it like "\n"
    l8.grid()

    
    
    
    
    
    
    
    
    
    
    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()])
    button1.grid()

    #frame3
    f3=tk.Frame(hardlevel3)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label2=tk.Label(f3,text="\n\n\n 1. past tense of use is ....")
    label2.grid()
    
    label3=tk.Label(f3,text="\n\n 3. Gives oxygen and essential for the nature \n")
    label3.grid()

    label4=tk.Label(f3,text="\n 5. shown in theaters .")
    label4.grid()

    label5=tk.Label(f3,text="\n 7. a young person who is training to be in \n the army, navy, air force or police.")
    label5.grid()
    
    
    


    label9=tk.Label(f3,text="\n\n")#using it like "\n"
    label9.grid()

    button1=tk.Button(f3,text="QUIT",command=hardlevel3.destroy)
    button1.grid()


    #execution
    hardlevel3.mainloop()


# In[12]:


def hardlevel4():    
    def submit():
        #inputvariables
        v1=b20.get()
        v2=b32.get()
        v3=b44.get()
        v4=b52.get()
        v5=b56.get()
        v6=b62.get()
        v7=b63.get()
        v8=b64.get()
        v9=b68.get()
        v10=b71.get()
        v11=b76.get()
        v12=b80.get()
        v13=b83.get()
        v14=b88.get()
        v15=b92.get()
        v16=b95.get()
        v17=b100.get()
        v18=b101.get()
        v19=b102.get()
        v20=b103.get()
        v21=b104.get()
        v22=b105.get()
        v23=b106.get()
        v24=b107.get()
        v25=b108.get()
        v26=b112.get()
        v27=b116.get()
        v28=b129.get()
        v29=b130.get()
        v30=b131.get()
        v31=b140.get()

        if v1.upper()=="" and v2.upper()=="" and v3.upper()=="" and v4.upper()=="" and v5.upper()=="" and v6.upper()=="" and v7.upper()=="" and v8.upper()=="" and v9.upper()=="" and v10.upper()=="" and v11.upper()=="" and v12.upper()=="" and v13.upper()=="" and v14.upper()=="" and v15.upper()=="" and v16.upper()=="" and v17.upper()=="" and v18.upper()=="" and v19.upper()=="" and v20.upper()=="" and v21.upper()=="" and v22.upper()=="" and v23.upper()=="" and v24.upper()=="" and v25.upper()=="" and v26.upper()=="" and v27.upper()=="" and v28.upper()=="" and v29.upper()=="" and v30.upper()=="" and v31.upper()=="":
            messagebox.showinfo("showinfo", "Please enter value!!!")
            root.destroy()
            lastPage()


        elif v1.upper()=="E" and v2.upper()=="F" and v3.upper()=="R" and v4.upper()=="I" and v5.upper()=="I" and v6.upper()=="E" and v7.upper()=="A" and v8.upper()=="T" and v9.upper()=="G" and v10.upper()=="N" and v11.upper()=="C" and v12.upper()=="E" and v13.upper()=="I" and v14.upper()=="H" and v15.upper()=="R" and v16.upper()=="F" and v17.upper()=="E" and v18.upper()=="G" and v19.upper()=="E" and v20.upper()=="T" and v21.upper()=="A" and v22.upper()=="B" and v23.upper()=="L" and v24.upper()=="E" and v25.upper()=="S" and v26.upper()=="N" and v27.upper()=="T" and v28.upper()=="V" and v29.upper()=="E" and v30.upper()=="N" and v31.upper()=="R":
            messagebox.showinfo("showinfo", "cleared the crossword")

        elif v1.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd column , 1st value is incorrect!")

        elif v2.upper()!="F":
            messagebox.askretrycancel("askretrycancel", "2nd column, 2nd value is incorrect!")  

        elif v3.upper()!="R":
            messagebox.askretrycancel("askretrycancel", "2nd column , 3rd value is incorrect!")  

        elif v4.upper()!="I":
            messagebox.askretrycancel("askretrycancel", "1st column, 1st value is incorrect!")  

        elif v5.upper()!="I":
            messagebox.askretrycancel("askretrycancel", "2nd column , 4th value is incorrect!")

        elif v6.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "1st row, 1st value is incorrect!")  

        elif v7.upper()!="A":
            messagebox.askretrycancel("askretrycancel", "1st row, 2nd value is incorrect!")  

        elif v8.upper()!="T":
            messagebox.askretrycancel("askretrycancel", "1st row, 3rd value is incorrect!")  

        elif v9.upper()!="G":
            messagebox.askretrycancel("askretrycancel", "2nd column ,5th value is incorrect!")  

        elif v10.upper()!="N":
            messagebox.askretrycancel("askretrycancel", "3rd column ,1st value is incorrect!")  

        elif v11.upper()!="C":
            messagebox.askretrycancel("askretrycancel", "1st column, 3rd value is incorrect!")  

        elif v12.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd column, 6hth value is incorrect!")  

        elif v13.upper()!="I":
            messagebox.askretrycancel("askretrycancel", "3rd column, 2nd value is incorrect!")  

        elif v14.upper()!="H":
            messagebox.askretrycancel("askretrycancel", "1st column, 4th value is incorrect!")  

        elif v15.upper()!="R":
            messagebox.askretrycancel("askretrycancel", "2nd column, 7th value is incorrect!")  

        elif v16.upper()!="F":
            messagebox.askretrycancel("askretrycancel", "3rd column, 3rd value is incorrect!")  

        elif v17.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd row, 1st value is incorrect!")  

        elif v18.upper()!="G":
            messagebox.askretrycancel("askretrycancel", "2nd row, 2nd value is incorrect!")  

        elif v19.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd row, 3rd value is incorrect!")  

        elif v20.upper()!="T":
            messagebox.askretrycancel("askretrycancel", "2nd row, 4th value is incorrect!")  

        elif v21.upper()!="A":
            messagebox.askretrycancel("askretrycancel", "2nd row, 5th value is incorrect!")  

        elif v22.upper()!="B":
            messagebox.askretrycancel("askretrycancel", "2nd row, 6th value is incorrect!")  

        elif v23.upper()!="L":
            messagebox.askretrycancel("askretrycancel", "2nd row, 7th value is incorrect!")  

        elif v24.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "2nd row, 8th value is incorrect!")  

        elif v25.upper()!="S":
            messagebox.askretrycancel("askretrycancel", "2nd row, 9th value is incorrect!")  

        elif v26.upper()!="N":
            messagebox.askretrycancel("askretrycancel", "1st column, 6th value is incorrect!")  

        elif v27.upper()!="T":
            messagebox.askretrycancel("askretrycancel", "2nd column, 9th value is incorrect!")  

        elif v28.upper()!="V":
            messagebox.askretrycancel("askretrycancel", "3rd row, 1st value is incorrect!")  

        elif v29.upper()!="E":
            messagebox.askretrycancel("askretrycancel", "3rd row, 2nd value is incorrect!")  

        elif v30.upper()!="N":
            messagebox.askretrycancel("askretrycancel", "3rd row, 3rd value is incorrect!")  

        elif v31.upper()!="R":
            messagebox.askretrycancel("askretrycancel", "2nd column, 10th value is incorrect!")  

        else:
            messagebox.showerror("showerror", "U failed")




    root=tk.Tk()
    root.geometry("800x800")
    root.resizable(False,False)
    root.title("Hard Level 4")

    #frame4 jo frame1 ko hold karega

    f4=tk.Frame(root,bg="black")
    f4.pack(side="top",expand="True",fill="both")

    #frame1

    f1=tk.Frame(f4,padx=(30),bg="black")
    f1.place(in_=f4, anchor="c",relx=.5, rely=.5)
      #row1

    b1=tk.Label(f1,width="5",bg="black")
    b1.grid(row="0",column="0")

    b2=tk.Label(f1,width="5",bg="black")
    b2.grid(row="0",column="1")

    b3=tk.Label(f1,width="5",bg="black")
    b3.grid(row="0",column="2")

    b4=tk.Label(f1,width="5",bg="black")
    b4.grid(row="0",column="3")

    b5=tk.Label(f1,width="5",bg="black")
    b5.grid(row="0",column="4")

    b6=tk.Label(f1,width="5",bg="black")
    b6.grid(row="0",column="5")

    b7=tk.Label(f1,width="5",bg="black")
    b7.grid(row="0",column="6")

    b8=tk.Label(f1,text="R",width="5")
    b8.grid(row="0",column="7")

    b9=tk.Label(f1,width="5",bg="black")
    b9.grid(row="0",column="8")

    b10=tk.Label(f1,width="5",bg="black")
    b10.grid(row="0",column="9")

    b11=tk.Label(f1,width="5",bg="black")
    b11.grid(row="0",column="10")

    b12=tk.Label(f1,width="5",bg="black")
    b12.grid(row="0",column="11")



      #row2
    b13=tk.Label(f1,width="5",bg="black")
    b13.grid(row="1",column="0")

    b14=tk.Label(f1,width="5",bg="black")
    b14.grid(row="1",column="1")

    b15=tk.Label(f1,width="5",bg="black")
    b15.grid(row="1",column="2")

    b16=tk.Label(f1,width="5",bg="black")
    b16.grid(row="1",column="3")

    b17=tk.Label(f1,width="5",bg="black")
    b17.grid(row="1",column="4")

    b18=tk.Label(f1,width="5",bg="black")
    b18.grid(row="1",column="5")

    b19=tk.Label(f1,width="5",bg="black")
    b19.grid(row="1",column="6")

    b20=tk.Entry(f1,width="5")
    b20.grid(row="1",column="7",padx="0")

    b21=tk.Label(f1,width="5",bg="black")
    b21.grid(row="1",column="8")

    b22=tk.Label(f1,width="5",bg="black")
    b22.grid(row="1",column="9")

    b23=tk.Label(f1,width="5",bg="black")
    b23.grid(row="1",column="10")

    b24=tk.Label(f1,width="5",bg="black")
    b24.grid(row="1",column="11")



     #row3
    b25=tk.Label(f1,width="5",bg="black")
    b25.grid(row="2",column="0")

    b26=tk.Label(f1,width="5",bg="black")
    b26.grid(row="2",column="1")

    b27=tk.Label(f1,width="5",bg="black")
    b27.grid(row="2",column="2")

    b28=tk.Label(f1,width="5",bg="black")
    b28.grid(row="2",column="3")

    b29=tk.Label(f1,width="5",bg="black")
    b29.grid(row="2",column="4")

    b30=tk.Label(f1,width="5",bg="black")
    b30.grid(row="2",column="5")

    b31=tk.Label(f1,width="5",bg="black")
    b31.grid(row="2",column="6")

    b32=tk.Entry(f1,width="5")
    b32.grid(row="2",column="7",padx="0")

    b33=tk.Label(f1,width="5",bg="black")
    b33.grid(row="2",column="8")

    b34=tk.Label(f1,width="5",bg="black")
    b34.grid(row="2",column="9")

    b35=tk.Label(f1,width="5",bg="black")
    b35.grid(row="2",column="10")

    b36=tk.Label(f1,width="5",bg="black")
    b36.grid(row="2",column="11")

    #row4
    b37=tk.Label(f1,width="5",bg="black")
    b37.grid(row="3",column="0")

    b38=tk.Label(f1,width="5",bg="black")
    b38.grid(row="3",column="1")

    b39=tk.Label(f1,width="5",bg="black")
    b39.grid(row="3",column="2")

    b40=tk.Label(f1,text="K",width="5")
    b40.grid(row="3",column="3")

    b41=tk.Label(f1,width="5",bg="black")
    b41.grid(row="3",column="4")

    b42=tk.Label(f1,width="5",bg="black")
    b42.grid(row="3",column="5")

    b43=tk.Label(f1,width="5",bg="black")
    b43.grid(row="3",column="6")

    b44=tk.Entry(f1,width="5")
    b44.grid(row="3",column="7",padx="0")

    b45=tk.Label(f1,width="5",bg="black")
    b45.grid(row="3",column="8")

    b46=tk.Label(f1,width="5",bg="black")
    b46.grid(row="3",column="9")

    b47=tk.Label(f1,width="5",bg="black")
    b47.grid(row="3",column="10")

    b48=tk.Label(f1,width="5",bg="black")
    b48.grid(row="3",column="11")

    #row5
    b49=tk.Label(f1,width="5",bg="black")
    b49.grid(row="4",column="0")

    b50=tk.Label(f1,width="5",bg="black")
    b50.grid(row="4",column="1")

    b51=tk.Label(f1,width="5",bg="black")
    b51.grid(row="4",column="2")

    b52=tk.Entry(f1,width="5")
    b52.grid(row="4",column="3",padx="0")

    b53=tk.Label(f1,width="5",bg="black")
    b53.grid(row="4",column="4")

    b54=tk.Label(f1,width="5",bg="black")
    b54.grid(row="4",column="5")

    b55=tk.Label(f1,width="5",bg="black")
    b55.grid(row="4",column="6")

    b56=tk.Entry(f1,width="5", fg="Black")
    b56.grid(row="4",column="7",padx="0")

    b57=tk.Label(f1,width="5",bg="black")
    b57.grid(row="4",column="8")

    b58=tk.Label(f1,width="5",bg="black")
    b58.grid(row="4",column="9")

    b59=tk.Label(f1,width="5",text="K")
    b59.grid(row="4",column="10")

    b60=tk.Label(f1,width="5",bg="black")
    b60.grid(row="4",column="11")

    #row6
    b61=tk.Label(f1,width="5", text="H")
    b61.grid(row="5",column="0")

    b62=tk.Entry(f1,width="5")
    b62.grid(row="5",column="1")

    b63=tk.Entry(f1,width="5")
    b63.grid(row="5",column="2")

    b64=tk.Entry(f1,text="K",width="5")
    b64.grid(row="5",column="3")

    b65=tk.Label(f1,width="5",bg="black")
    b65.grid(row="5",column="4")

    b66=tk.Label(f1,width="5",bg="black")
    b66.grid(row="5",column="5")

    b67=tk.Label(f1,width="5",bg="black")
    b67.grid(row="5",column="6")

    b68=tk.Entry(f1,width="5")
    b68.grid(row="5",column="7",padx="0")

    b69=tk.Label(f1,width="5",bg="black")
    b69.grid(row="5",column="8")

    b70=tk.Label(f1,width="5",bg="black")
    b70.grid(row="5",column="9")

    b71=tk.Entry(f1,width="5")
    b71.grid(row="5",column="10")

    b72=tk.Label(f1,width="5",bg="black")
    b72.grid(row="5",column="11")


    #row7
    b73=tk.Label(f1,width="5",bg="black")
    b73.grid(row="6",column="0")

    b74=tk.Label(f1,width="5",bg="black")
    b74.grid(row="6",column="1")

    b75=tk.Label(f1,width="5",bg="black")
    b75.grid(row="6",column="2")

    b76=tk.Entry(f1,width="5")
    b76.grid(row="6",column="3")

    b77=tk.Label(f1,width="5",bg="black")
    b77.grid(row="6",column="4")

    b78=tk.Label(f1,width="5",bg="black")
    b78.grid(row="6",column="5")

    b79=tk.Label(f1,width="5",bg="black")
    b79.grid(row="6",column="6")

    b80=tk.Entry(f1,width="5")
    b80.grid(row="6",column="7",padx="0")

    b81=tk.Label(f1,width="5",bg="black")
    b81.grid(row="6",column="8")

    b82=tk.Label(f1,width="5",bg="black")
    b82.grid(row="6",column="9")

    b83=tk.Entry(f1,width="5")
    b83.grid(row="6",column="10")

    b84=tk.Label(f1,width="5",bg="black")
    b84.grid(row="6",column="11")

    #row8
    b85=tk.Label(f1,width="5",bg="black")
    b85.grid(row="7",column="0")

    b86=tk.Label(f1,width="5",bg="black")
    b86.grid(row="7",column="1")

    b87=tk.Label(f1,width="5",bg="black")
    b87.grid(row="7",column="2")

    b88=tk.Entry(f1,width="5")
    b88.grid(row="7",column="3")

    b89=tk.Label(f1,width="5",bg="black")
    b89.grid(row="7",column="4")

    b90=tk.Label(f1,width="5",bg="black")
    b90.grid(row="7",column="5")

    b91=tk.Label(f1,width="5",bg="black")
    b91.grid(row="7",column="6")

    b92=tk.Entry(f1,width="5")
    b92.grid(row="7",column="7",padx="0")

    b93=tk.Label(f1,width="5",bg="black")
    b93.grid(row="7",column="8")

    b94=tk.Label(f1,width="5",bg="black")
    b94.grid(row="7",column="9")

    b95=tk.Entry(f1,width="5")
    b95.grid(row="7",column="10")

    b96=tk.Label(f1,width="5",bg="black")
    b96.grid(row="7",column="11")

    #row9

    b97=tk.Label(f1,width="5",bg="black")
    b97.grid(row="8",column="0")

    b98=tk.Label(f1,width="5",bg="black")
    b98.grid(row="8",column="1")

    b99=tk.Label(f1,width="5",text="v")
    b99.grid(row="8",column="2")

    b100=tk.Entry(f1,width="5")
    b100.grid(row="8",column="3")

    b101=tk.Entry(f1,width="5")
    b101.grid(row="8",column="4")

    b102=tk.Entry(f1,width="5")
    b102.grid(row="8",column="5")

    b103=tk.Entry(f1,width="5")
    b103.grid(row="8",column="6")

    b104=tk.Entry(f1,width="5")
    b104.grid(row="8",column="7",padx="0")

    b105=tk.Entry(f1,width="5")
    b105.grid(row="8",column="8")

    b106=tk.Entry(f1,width="5")
    b106.grid(row="8",column="9")

    b107=tk.Entry(f1,width="5")
    b107.grid(row="8",column="10")

    b108=tk.Entry(f1,width="5")
    b108.grid(row="8",column="11")

    #row10
    b109=tk.Label(f1,width="5",bg="black")
    b109.grid(row="9",column="0")

    b110=tk.Label(f1,width="5",bg="black")
    b110.grid(row="9",column="1")

    b111=tk.Label(f1,width="5",bg="black")
    b111.grid(row="9",column="2")

    b112=tk.Entry(f1,width="5")
    b112.grid(row="9",column="3")

    b113=tk.Label(f1,width="5",bg="black")
    b113.grid(row="9",column="4")

    b114=tk.Label(f1,width="5",bg="black")
    b114.grid(row="9",column="5")

    b115=tk.Label(f1,width="5",bg="black")
    b115.grid(row="9",column="6")

    b116=tk.Entry(f1,width="5")
    b116.grid(row="9",column="7",padx="0")

    b117=tk.Label(f1,width="5",bg="black")
    b117.grid(row="9",column="8")

    b118=tk.Label(f1,width="5",bg="black")
    b118.grid(row="9",column="9")

    b119=tk.Label(f1,width="5",bg="black")
    b119.grid(row="9",column="10")

    b120=tk.Label(f1,width="5",bg="black")
    b120.grid(row="9",column="11")

    #row11
    b121=tk.Label(f1,width="5",bg="black")
    b121.grid(row="10",column="0")

    b122=tk.Label(f1,width="5",bg="black")
    b122.grid(row="10",column="1")

    b123=tk.Label(f1,width="5",bg="black")
    b123.grid(row="10",column="2")

    b124=tk.Label(f1,width="5",bg="black")
    b124.grid(row="10",column="3")

    b125=tk.Label(f1,width="5",bg="black")
    b125.grid(row="10",column="4")

    b126=tk.Label(f1,width="5",bg="black")
    b126.grid(row="10",column="5")

    b127=tk.Label(f1,width="5",bg="black")
    b127.grid(row="10",column="6")

    b128=tk.Label(f1,width="5",text="O")
    b128.grid(row="10",column="7",padx="0")

    b129=tk.Entry(f1,width="5")
    b129.grid(row="10",column="8")

    b130=tk.Entry(f1,width="5")
    b130.grid(row="10",column="9")

    b131=tk.Entry(f1,width="5")
    b131.grid(row="10",column="10")

    b132=tk.Label(f1,width="5",bg="black")
    b132.grid(row="10",column="11")


    #row12
      #row2
    b133=tk.Label(f1,width="5",bg="black")
    b133.grid(row="11",column="0")

    b135=tk.Label(f1,width="5",bg="black")
    b135.grid(row="11",column="1")

    b136=tk.Label(f1,width="5",bg="black")
    b136.grid(row="11",column="2")

    b136=tk.Label(f1,width="5",bg="black")
    b136.grid(row="11",column="3")

    b137=tk.Label(f1,width="5",bg="black")
    b137.grid(row="11",column="4")

    b138=tk.Label(f1,width="5",bg="black")
    b138.grid(row="11",column="5")

    b139=tk.Label(f1,width="5",bg="black")
    b139.grid(row="11",column="6")

    b140=tk.Entry(f1,width="5")
    b140.grid(row="11",column="7",padx="0")

    b141=tk.Label(f1,width="5",bg="black")
    b141.grid(row="11",column="8")

    b142=tk.Label(f1,width="5",bg="black")
    b142.grid(row="11",column="9")

    b143=tk.Label(f1,width="5",bg="black")
    b143.grid(row="11",column="10")

    b144=tk.Label(f1,width="5",bg="black")
    b144.grid(row="11",column="11")



    #frame2
    f2=tk.Frame(root)
    f2.pack(side="left",expand="True",fill="both")

    l1=tk.Label(f2,text="ACROSS",bg="black",fg="white")
    l1.grid(row="0",column="0")


    l2=tk.Label(f2,text="")#using it like "\n"
    l2.grid()

    l3=tk.Label(f2,text="1.  Energy that is transferred from one body to another \nas the result of a difference in temperature (H) \n")
    l3.grid()

    l4=tk.Label(f2,text="2.  The fresh edible portions of certain herbaceous\n plants—roots, stems, leaves, flowers, fruit, or seeds. (V) \n")
    l4.grid()

    l5=tk.Label(f2,text="3.  A tool which is used to expose materials\n to a hot environment  \n (O) ")
    l5.grid()


    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()

    l7=tk.Label(f2,text="")#using it like "\n"
    l7.grid()

    button1=tk.Button(f2,text="SUBMIT",command=lambda: [submit()],bg='white')
    button1.grid()

    l5=tk.Label(f2,text="")#using it like "\n"
    l5.grid()

    l6=tk.Label(f2,text="")#using it like "\n"
    l6.grid()



    #frame3
    f3=tk.Frame(root)
    f3.pack(side="left",expand="True",fill="y")

    label1=tk.Label(f3,text="DOWN",bg="black",fg="white")
    label1.grid()

    label3=tk.Label(f3,text="\n 1. a machine used for keeping things cold.  (R)")
    label3.grid()

    #label9=tk.Label(f3,text="\n")#using it like "\n"
    #label9.grid()


    label2=tk.Label(f3,text="\n 2. A room or area where food is prepared and cooked. \n(K left of R)")
    label2.grid()


    #label10=tk.Label(f3,text="\n")#using it like "\n"
    #label10.grid()

    label4=tk.Label(f3,text="\n 3. is a tool or weapon with a cutting edge or blade.\n(K right of R)\n\n\n\n\n\n")
    label4.grid()



    button10=tk.Button(f3,text="QUIT",command=root.destroy)
    button10.grid()

    label4=tk.Label(f3,text="")#using it like "\n"
    label4.grid()

    label5=tk.Label(f3,text="")#using it like "\n"
    label5.grid()





    #execution
    root.mainloop()


# In[13]:


def lastPage():   
    
   

    # Create an instance of tkinter window
    win = Tk()
    #root = Tk()

    # Define the geometry of the window
    win.geometry("700x500")
    win.title("Thank You ")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("end.jpeg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()


    button1 = Button(frame, text='Play Again' ,width = 8,bg = "#6CD300", fg = "black",command=lambda: [win.destroy(),level1()])
    button1.place(x=150, y=320)

    button2 = Button(frame, text='Quit' ,width = 8,bg = "#6CD300", fg = "black" , command=win.destroy)
    button2.place(x=500, y=320)

    win.mainloop()


# In[13]:


welcomePage()


