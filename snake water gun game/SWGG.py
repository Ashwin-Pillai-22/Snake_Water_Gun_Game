from tkinter import *
from PIL import ImageTk ,Image
import random
from tkinter import messagebox
from pyttsx3 import speak
# def again():
def restart():
    root=Tk()
    root.geometry("700x600")
    root.maxsize(700,600)
    root.title("*Snake Water Gun* Game")
    img = PhotoImage(file="SWGGicon.png")	
    root.iconphoto(False,img)

    # background
    my=Image.open("img.png")
    resized=my.resize((700,600),Image.Resampling.LANCZOS)
    photo=ImageTk.PhotoImage(resized)
    Label(image=photo).place(x=0,y=0)

    def check(comp_choice,choice):
        if comp_choice==choice:
            return 0
        elif comp_choice==1 and choice==2:
            return -1
        elif comp_choice==2 and choice==3:
            return -1
        elif comp_choice==3 and choice==1:
            return -1
        return 1

    choice=-1
    def snakenew():
        
        
        choice=0
        ans=check(comp_choice,choice) 
        
        if ans==0:
            
            a=Image.open("snake.png")
            a_resized=a.resize((140,129),Image.Resampling.LANCZOS)
            a_photo=ImageTk.PhotoImage(a_resized)
            Label(image=a_photo,borderwidth=5).place(x=300,y=100)
            yon=messagebox.askretrycancel("DRAW","You and computer had same choices")
            if yon==True:
                root.destroy()
                restart()
            else:
                root.destroy()

        elif ans==1:
            
            b=Image.open("water.png")
            b_resized=b.resize((140,129),Image.Resampling.LANCZOS)
            b_photo=ImageTk.PhotoImage(b_resized)
            Label(image=b_photo,borderwidth=5).place(x=300,y=100)
            yon1=messagebox.askretrycancel("WON","You are Invincible!!")
            if yon1==True:
                root.destroy()
                restart()
            else:
                root.destroy()
        else:
            
            c=Image.open("gun.png")
            c_resized=c.resize((140,129),Image.Resampling.LANCZOS)
            c_photo=ImageTk.PhotoImage(c_resized)
            Label(image=c_photo,borderwidth=5).place(x=300,y=100)
            yon2=messagebox.askretrycancel("LOSE","Better luck next time")
            if yon2==True:
                root.destroy()
                restart()
            else:
                root.destroy()
                            

    def waternew():
        
        choice=1
        ans=check(comp_choice,choice)
        # if comp_choice==2:

        if ans==0:
           
            d=Image.open("water.png")
            d_resized=d.resize((140,129),Image.Resampling.LANCZOS)
            d_photo=ImageTk.PhotoImage(d_resized)
            Label(image=d_photo,borderwidth=5).place(x=300,y=100)
            yon3=messagebox.askretrycancel("DRAW","You and computer had same choices")
            if yon3==True:
                root.destroy()
                restart()
            else:
                root.destroy()
            
        elif ans==1:
            
            e=Image.open("gun.png")
            e_resized=e.resize((140,129),Image.Resampling.LANCZOS)
            e_photo=ImageTk.PhotoImage(e_resized)
            Label(image=e_photo,borderwidth=5).place(x=300,y=100)
            yon4=messagebox.askretrycancel("WON","You are Invincible!!")
            if yon4==True:
                root.destroy()
                restart()
            else:
                root.destroy()
        else:
            
            f=Image.open("snake.png")
            f_resized=f.resize((140,129),Image.Resampling.LANCZOS)
            f_photo=ImageTk.PhotoImage(f_resized)
            Label(image=f_photo,borderwidth=5).place(x=300,y=100)
            yon5=messagebox.askretrycancel("LOSE","Better luck next time")
            if yon5==True:
                root.destroy()
                restart()
            else:
                root.destroy()
        
    def gunnew():
       
        choice=2
        ans=check(comp_choice,choice)
        if ans==0:
            g=Image.open("gun.png")
            g_resized=g.resize((140,129),Image.Resampling.LANCZOS)
            g_photo=ImageTk.PhotoImage(g_resized)
            Label(image=g_photo,borderwidth=5).place(x=300,y=100)
            yon6=messagebox.askretrycancel("DRAW","You and computer had same choices")
            if yon6==True:
                root.destroy()
                restart()
            else:
                root.destroy()
        elif ans==1:
           
            h=Image.open("snake.png")
            h_resized=h.resize((140,129),Image.Resampling.LANCZOS)
            h_photo=ImageTk.PhotoImage(h_resized)
            Label(image=h_photo,borderwidth=5).place(x=300,y=100)
            yon7=messagebox.askretrycancel("WON","You are Invincible!!")
            if yon7==True:
                root.destroy()
                restart()
            else:
                root.destroy()
        else:
           
            i=Image.open("water.png")
            i_resized=i.resize((140,129),Image.Resampling.LANCZOS)
            i_photo=ImageTk.PhotoImage(i_resized)
            Label(image=i_photo,borderwidth=5).place(x=300,y=100)
            yon8=messagebox.askretrycancel("LOSE","Better luck next time")
            if yon8==True:
                root.destroy()
                restart()
            else:
                root.destroy()
            
        
    Label(root,text="COMPUTER",font=("arial" ,19," bold"),fg="red",relief=SOLID,borderwidth=3).place(x=300,y=20)
    
    
    global comp_choice
    comp_choice=random.randint(0,2) 

    
    Label(root,bg="black",padx=73,pady=60).place(x=300,y=100)
    
    Label(root,text="USER",font=("arial" ,19," bold"),fg="red",relief=SOLID,borderwidth=3,padx=38).place(x=300,y=300)

    snake=Image.open("snake.png")
    snake_resized=snake.resize((125,125),Image.Resampling.LANCZOS)
    snake_photo=ImageTk.PhotoImage(snake_resized)
    Button(image=snake_photo,borderwidth=5,command=snakenew).place(x=110,y=400)

    water=Image.open("water.png")
    water_resized=water.resize((125,125),Image.Resampling.LANCZOS)
    water_photo=ImageTk.PhotoImage(water_resized)
    Button(image=water_photo,borderwidth=5,command=waternew).place(x=310,y=400)

    gun=Image.open("gun.png")
    gun_resized=gun.resize((125,125),Image.Resampling.LANCZOS)
    gun_photo=ImageTk.PhotoImage(gun_resized)
    Button(image=gun_photo,borderwidth=5,command=gunnew).place(x=510,y=400)

    
    mainloop()
restart()    

    
