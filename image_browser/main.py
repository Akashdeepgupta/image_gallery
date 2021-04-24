from tkinter import *
from PIL import ImageTk, Image


def forward(img_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=img_list[img_number-1])
    button_forward = Button(root, text ="next",command = lambda :forward(img_number+1))
    button_back = Button(root,text="previous",command=lambda :back(img_number-1))

    if img_number == 5:
        button_forward = Button(root,text="next",state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(img_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[img_number - 1])
    button_forward = Button(root, text="next", command=lambda: forward(img_number + 1))
    button_back = Button(root, text="previous", command=lambda: back(img_number - 1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

root = Tk()
root.title("akash")
root.iconbitmap("C:/Users/Akashdeep Gupta/PycharmProjects/image_browser/download.ico")
root.geometry("600x550")

img1 = ImageTk.PhotoImage(Image.open("Photo_Ibm/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("Photo_Ibm/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("Photo_Ibm/3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("Photo_Ibm/4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("Photo_Ibm/5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("Photo_Ibm/6.jpg"))

img_list = [img1, img2, img3, img4, img5, img6]

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="previous", command=back)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forward = Button(root, text="next", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
