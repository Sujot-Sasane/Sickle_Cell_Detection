import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
#from subprocess import call
import cv2

# Initialize the main window
root = tk.Tk()
root.configure(background="seashell2")

# Get screen width and height and set the window size
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("MAIN PAGE")



# Load video and display on label
cap = cv2.VideoCapture('blood2.mp4')  # Replace with your video file

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (w, h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        background_label.imgtk = imgtk
        background_label.configure(image=imgtk)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop the video
    background_label.after(10, update_frame)

background_label = Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load and place logo image
image2 = Image.open('logo10.jpg')
image2 = image2.resize((140, 150), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(image=image2)
logo_label = tk.Label(root, image=logo_photo, bg="seashell2")
logo_label.image = logo_photo
logo_label.place(x=700, y=30)

# Add text below the logo image
text_label = tk.Label(root, text="Sickel Cell Anemia Detection System", font=('times', 25, 'bold'), bg="seashell2")
text_label.place(x=525, y=250)

text_label = tk.Label(root, text="Blood Smear Microscopic Pictures Are Required To Proceed \n Press START To Enter", font=('times', 25, 'bold'), bg="seashell2")
text_label.place(x=330, y=360)

def login():

    from subprocess import call
    call(["python", "GUI_main.py"]) 
    
# Add START button
button_start = tk.Button(root, text="START", command=login, width=15, height=1, font=('times', 15, 'bold'), bg="aqua", fg="black")
button_start.place(x=680, y=550)  # Center the button

# Start updating frames
update_frame()

# Run the main event loop
root.mainloop()

# Release video capture object
cap.release()
