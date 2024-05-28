import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("main")

def reg():
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   

def login():
    print("log")
    from subprocess import call
    call(["python", "login.py"])   

def window():
    root.destroy()

# Load background image
image2 = Image.open('b9.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = tk.Label(root, text="Sickel Cell Detection", font=('times', 40,' bold '), height=1, width=50,bg="BLACK",fg="white")
lbl.place(x=0, y=0)

framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=400, height=300, bd=5, font=('times', 14, ' bold '),bg="seashell2")
framed.place(x=w//2 - 200, y=h//2 - 150)

button1 = tk.Button(framed, text='Login Now',width=15,height=2,bd=5,bg='#152238',font=('times', 15, ' bold '),fg='white',command=login)
button1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

button2 = tk.Button(framed, text='Register',width=15,height=2,bd=5,bg='#152238',font=('times', 15, ' bold '),fg='white',command=reg)
button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

exit_button = tk.Button(framed, text="Exit", command=window, width=15, height=2, bd=5,font=('times', 15, ' bold '),bg="red",fg="white")
exit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()
