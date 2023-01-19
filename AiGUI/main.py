# Dependency :
'''
    tkinter --> pip install tkinter
    PIL --> pip install pillow
'''

from tkinter import *
from PIL import ImageTk, Image
import os

SIZE_PHOTO = (1920, 1080)


root = Tk()
root.geometry('1000x900')

# sshpass -p "bogdan" scp bogdan@192.168.22.118:/home/bogdan/Desktop/AI/tflite1/results/test1.jpg .

label = Label(root, text='My object detection Raspberry Pi4 project')
label.pack()

frame = Frame(root, width=1920, height=1080)
frame.place(anchor='center', relx=0.5, rely=0.5)
img = Image.open("istockphoto-1188686189-612x612.jpg")

img=img.resize(SIZE_PHOTO)
img = ImageTk.PhotoImage(img)

label_img = Label(frame, image=img)
label_img.pack()

def do_magic():
    print("here")
    os.system('sshpass -p "bogdan" scp bogdan@192.168.22.118:/home/bogdan/Desktop/AI/tflite1/results/test1.jpg .')
    for widget in frame.winfo_children():
        widget.destroy()

    img = Image.open("test1.jpg")
    img = img.resize(SIZE_PHOTO)
    img = ImageTk.PhotoImage(img)
    label_img = Label(frame, image=img)
    label_img.pack()
    frame.refresh()

button = Button(root, text="Do magic!", command=do_magic,highlightcolor="green")
button.pack()

frame.pack()

# Create an object of tkinter ImageTk

root.mainloop()
