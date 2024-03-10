from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as font
import datetime
def takePic():
    image = Image.fromarray(img2)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save("macro/"+time)
root = Tk()
root.geometry("800x480")
cap = cv2.VideoCapture(1) #change based on port
#root.attributes('-fullscreen',True)
root.tk.call('tk','scaling',1)#change scaling ratio
f1 = LabelFrame(root)
f1.pack()
L1 = Label(f1)
L1.pack()
frame1 = LabelFrame(f1)
frame1.pack()
Button(frame1,text= "Capture and Save",command = takePic,height=2,width=15,font=font.Font(size=15)).grid(row=0,column=0)

Button(frame1,text= "Cancel",command = takePic,height=2,width=15,font=font.Font(size=15)).grid(row=0,column=1)
image_size = 89 #change size
while True:
    img = cap.read()[1]
   
    dim = (0,0)

    width = int(img.shape[1] * image_size / 100)
    height = int(img.shape[0] * image_size / 100)
    dim = (width, height)
    
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img2))
    img3 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    img3 = ImageTk.PhotoImage(Image.fromarray(img3))
    L1['image'] = img3 

    root.update()

cap.release()