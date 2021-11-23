//It is a small application in which you have to enter the data or link as input and, it will generate a QR code. It will save that image as well.

import pyqrcode
import os
import image
from tkinter import *
from tkinter import messagebox

qr = Tk()
qr.title("QR CODE GENERATOR")
qr.geometry("500x500+0+0") #wid,height,x-axis,y-axis
qr.config(bg= "#0C1E28")

def generate_QR():
    if len(user_input.get())!=0 :
        global qrinput,img
        qrinput = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qrinput.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())

def save_png():
    dir = path1 = os.getcwd()+ "//QR Code"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        #if if len(user_input.get())!=0 :
    
        saveimg = qr.png(os.path.join(dir.user_input+ ".png"), Scale=8)
        if len(user_input.get())!=0:
            messagebox.showinfo(message="error! file name cannot be empty.")
            
    except:
        messagebox.showinfo(message="error! generate qrcode first.")


lbl = Label(qr,  text="Enter message or URL",bg='#808080')
lbl.grid(row=2, column= 1, padx= 5,pady=10 )

user_input = StringVar()
entry = Entry(qr, textvariable = user_input)
entry.grid(row=2, column= 3,padx=5,pady=10)


button = Button(qr, text = "generate_QR", width=15, command = generate_QR )
button.grid(row=5, column= 1, padx= 5,pady=10)

button = Button(qr, text = "Save Image", width = 15 , command=save_png)
button.grid(row=5, column= 3,padx=5,pady=10)

img_lbl = Label(qr, bg='#F25252')
img_lbl.grid(row=6, column= 2,padx=5,pady=10)

output = Label(qr,text="",bg='#F25252')
output.grid(row=7, column= 2,padx=2,pady=10)
 
qr.mainloop()
