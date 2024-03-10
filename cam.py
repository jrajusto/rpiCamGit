from picamera.array import PiGRBArray
from picamera import PiCamera
import time 
import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as font
import datetime

camera = PiCamera()
camera.resolution(640,480)
camera.framerate = 32
rawCapture = PiGRBArray(camera,size=(640,480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

    image = frame.array
    cv2.imshow("Frame",image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break


def takePic():
    image = Image.fromarray(img2)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save("micro/"+time) #foldername
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
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    img = frame.array
   
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
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

cap.release()


