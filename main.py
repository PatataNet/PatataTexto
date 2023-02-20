from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.font as tkFont
import pyperclip as clip
import os
import webbrowser
root = Tk()
root.minsize(600,600)
root.maxsize(600,600)
root.configure(background="gray87")
open_img = ImageTk.PhotoImage(Image.open ("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open ("save_file.png"))
close_img = ImageTk.PhotoImage(Image.open ("close.png"))
delete_img = ImageTk.PhotoImage(Image.open ("delete_text.png"))
run_img = ImageTk.PhotoImage(Image.open ("run.png"))
my_text= Text(root,height=30,width=60)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)
name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title=" Open text File", filetypes=(("txt Files", "*.txt"),))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    html_file = open(name,'r')
    paragraph=html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    messagebox.showinfo("Update", "Success")
def run_html_file():
    global name
    webbrowser.open(name)
def delete():
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
def close():
    buttonNo.place(relx=0.36,rely=0.085,anchor= CENTER)
    buttonYes.place(relx=0.44,rely=0.085,anchor= CENTER)
    buttonCancel.place(relx=0.54,rely=0.085,anchor= CENTER)
    LabelClose.place(relx=0.28,rely=0.085,anchor= CENTER)
    root.mainloop()
def closeyes():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    root.destroy()
def closeno():
    root.destroy()
def closecancel():
    buttonNo.place(relx=0.36,rely=2.285,anchor= CENTER)
    buttonYes.place(relx=0.42,rely=2.285,anchor= CENTER)
    buttonCancel.place(relx=0.50,rely=2.285,anchor= CENTER)
    LabelClose.place(relx=0.20,rely=2.285,anchor= CENTER)




label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.32,rely=0.03,anchor= CENTER)
input_file_name = Entry(root)
input_file_name.place(relx=0.56,rely=0.03, anchor= CENTER)
open_button=Button(root,image=open_img,text="OpenFile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image=save_img,text="Save File", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
delete_button=Button(root,image=delete_img,text="Delete Text", command=delete)
delete_button.place(relx=0.17,rely=0.03,anchor= CENTER)
run_button=Button(root,image=run_img,text="Exit File", command=run_html_file)
run_button.place(relx=0.23,rely=0.03,anchor= CENTER)
close_button=Button(root,image=close_img,text="Exit Window", command=close)
close_button.place(relx=0.95,rely=0.03,anchor= CENTER)
buttonNo=Button(root,text="No", command=closeno)
buttonYes=Button(root,text="Yes", command=closeyes)
buttonCancel=Button(root,text="Cancel", command=closecancel)
LabelClose=Label(root, text ="Save?")





root.mainloop()