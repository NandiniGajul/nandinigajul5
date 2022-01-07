#widget -button,canvas,checkbutton,entry,frame,label,listbox,menu,menubutton,
 #          message,radiobutton,scale,scrolbar,text,toplevel,labelframe,messagebox

#geometry managers : --> pack(), grid(), place()

#place()
import tkinter as tk

win=tk.Tk()
win.geometry("500x400")

#add frame1
frame1=tk.Frame(master=win,width=100,height=100,bg="black")
frame1.pack(fill=tk.X) #fill=tk.X,tk.Y,tk.BOTH

#add frame2
frame2=tk.Frame(master=win,width=50,height=50,bg="yellow")
frame2.pack(side=tk.LEFT)

#add frame3
frame3=tk.Frame(master=win,width=25,height=25,bg="red")
frame3.pack(expand=True)

win.mainloop