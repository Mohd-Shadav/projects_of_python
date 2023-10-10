import random as rn
import tkinter as tk
from time import sleep
a=tk.Tk()
comp_point=0
point=0
#a.configure(background="skyblue")

def stpsc():
        l=['s','p','sc']
        comp=rn.choice(l)
        u=e1.get()
        global comp_point
        global point
        
        if(u=='s'):
                if(comp=='s'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="Match Draw",fg="black",font=4)
                    d.grid(row=11,column=5)
                    
                if(comp=='p'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Lose--",fg="red",font=4)
                    d.grid(row=11,column=5)
                    comp_point=comp_point+1
                if(comp=='sc'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Win--",fg="blue",font=4)
                    d.grid(row=11,column=5)
                    point=point+1
        if(u=='p'):
                if(comp=='p'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="Match Draw",fg="black",font=4)
                    d.grid(row=11,column=5)
                if(comp=='sc'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Lose--",fg="red",font=4)
                    d.grid(row=11,column=5)
                    comp_point=comp_point+1
                if(comp=='s'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Win--",fg="blue",font=4)
                    d.grid(row=11,column=5)
                    point=point+1
                    
        if(u=='sc'):
                if(comp=='sc'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="Match Draw",fg="black",font=4)
                    d.grid(row=11,column=5)
                if(comp=='s'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Lose--",fg="red",font=4)
                    d.grid(row=11,column=5)
                    comp_point=comp_point+1
                if(comp=='p'):
                    d0=tk.Label(a,text=f"Your choice : {u}\ncomputer choice :{comp}",font=5,fg="white",bg="black")
                    d0.grid(row=8,column=5)
                    d=tk.Label(a,text="--You Win--",fg="blue",font=4)
                    d.grid(row=11,column=5)
                    point=point+1
        m=tk.Label(a,text=f"computer point : {comp_point}\nYour point : {point}")
        m.grid(row=13,column=5)
        if(comp_point==5):
                d2=tk.Label(a,text="YOU ARE A LOSER",font=10,fg="red")
                d2.grid(row=14,column=5)
                comp_point=0
                point=0
                d3=tk.Button(a,text="Exit",fg="white",bg="green",command=a.destroy)
                d3.grid(row=15,column=5)
        if(point==5):
                
                d2=tk.Label(a,text="YOU ARE A WINNER",font=10,fg="blue")
                d2.grid(row=14,column=5)
                point=0
                comp_point=0

                d3=tk.Button(a,text="Exit",fg="white",bg="green",command=a.destroy)
                d3.grid(row=15,column=5)
               
                
                
a.title("Stone paper scissor")
a.geometry('1000x1000')
l1=tk.Label(a,text="press s for stone\npress p for paper\ntype sc for scissor",fg="blue",bg="pink",font=5)
l1.grid(rows=1,column=5)
l2=tk.Label(a,text="--------------------------------------------",font=5)
l2.grid(row=2,column=5)
name=tk.Label(a,text="Enter Your Choice : ",width=20,font=10)
name.grid(row=5,column=5)
e1=tk.Entry(a,width=40,font=5)
e1.grid(row=6,column=5)
b1=tk.Button(a,text='Play',fg="white",bg="green",width=3,height=1,command=stpsc)
b1.grid(row=7,column=5)
l3=tk.Label(a,text="--------------------------------------------",font=5)
l3.grid(row=9,column=5)
l3=tk.Label(a,text="--------------------------------------------",font=5)
l3.grid(row=12,column=5)




           
a.mainloop()
            
        
