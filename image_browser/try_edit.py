from tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()
root.geometry("600x440")
root.configure(bg="grey")


def resize_image(root,copy_of_image,label1):
    new_height=400
    new_width=400
    image=copy_of_image.resize((new_width,new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image=photo
    root.configure(bg="gold")

def next():
    global n
    global items_list
    n=(n+1)%len(items_list)
    img1=items_list[n]
    print(img1)
    image = Image.open("./Photo_Ibm/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.bind('<configure>', resize_image(root, copy_of_image, label1))
    label.grid(row=0,column=0,columnspan=3)



def previous():
    global n
    global items_list
    n=(n-1)%len(items_list)
    img1=items_list[n]
    print(img1)
    image = Image.open("./Photo_Ibm/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label2 = Label(root, image=photo)
    label2.bind('<configure>', resize_image(root, copy_of_image, label1))
    label2.grid(row=0, column=0, columnspan=3)



n=0
items_list=os.listdir("Photo_Ibm")
img1=items_list[n]


image = Image.open("./Photo_Ibm/"+img1)
copy_of_image=image.copy()
photo=ImageTk.PhotoImage(image)
label1=Label(root,image=photo)
label1.bind('<configure>',resize_image(root,copy_of_image,label1))
label1.pack()
b1=Button(root,text=">>",width=5,height=12,bg="gray30",fg="red",command=next)
b1.place(x=500,y=100)

b2=Button(root,text="<<",width=5,height=12,bg="gray30",fg="red",command=previous)
b2.place(x=55,y=100)

b3=Button(root,text="EXIT",width=56,height=2,bg="gray30",fg="red",command=root.quit)
b3.place(x=100,y=400)



root.mainloop()

