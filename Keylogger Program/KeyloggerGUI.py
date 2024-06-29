import Keylogger
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Keylogger using Python")
root.geometry("500x600")
wallpaper = Image.open(r"Keylogger Program\bg.jpg")
wallpaper = wallpaper.resize((600, 600), Image.ANTIALIAS)  # Resize to fit the window
background_image = ImageTk.PhotoImage(wallpaper)

canvas = Canvas(root, width=600, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

def guifunction2(values):
    Keylogger.function2(values)

a = Label(canvas, text="Keylogger Application", font=("Arial", 24, "bold"), bg='white')
b = Button(canvas, text="Capture Keystrokes", font=("Arial", 12), width=20, height=2, command=lambda:guifunction2(1))
c = Button(canvas, text="Stop Capture", font=("Arial", 12), width=20, height=2, command=lambda:guifunction2(0))
d = Button(canvas, text="View log file", font=("Arial", 12), width=20, height=2, command=Keylogger.function3)
e = Button(canvas, text="Close", font=("Arial", 12), width=20, height=2, command=root.destroy)

a_window = canvas.create_window(250, 100, window=a)
b_window = canvas.create_window(250, 200, window=b)
c_window = canvas.create_window(250, 300, window=c)
d_window = canvas.create_window(250, 400, window=d)
e_window = canvas.create_window(250, 500, window=e)

root.mainloop()
