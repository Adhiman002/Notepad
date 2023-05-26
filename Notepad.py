from tkinter import *
import os 
from tkinter.filedialog import askopenfilename,asksaveasfilename 

root=Tk()
root.geometry('700x500')
root.title('Notepad')

root.iconbitmap("notepad.ico")
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)

def New():
    global  file
    root.title("Untitled - Notepad")
    entry.delete(1.0,END)

def Open(): 
    global file
    file=askopenfilename(filetypes=[('Text files','*.txt')])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file))
        f=open(file,'r')
        entry.insert(1.0,f.read())
        f.close()
    

def Save():
    global file
    file=asksaveasfilename(filetype=[('text files','*.txt')])
    if file=="":
        file=None
    else:
        f=open(file,'w')
        f.write(entry.get(1.0,END))
        root.title(os.path.basename(file))

def Cut():
    entry.event_generate(("<<Cut>>"))

def Copy():
    entry.event_generate(("<<Copy>>"))


def Paste():
    entry.event_generate(("<<Paste>>"))



# create the file_menu
file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label='New',command=New)
file_menu.add_command(label='Open',command=Open)
file_menu.add_command(label='Save',command=Save)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)

menubar.add_cascade(label="File",menu=file_menu)

# EditMenu Bar
edit_menu = Menu(menubar,tearoff=0)

edit_menu.add_command(label='Cut', command=Cut)
edit_menu.add_command(label='Copy',command=Copy)
edit_menu.add_command(label='Paste',command=Paste)

menubar.add_cascade(label="Edit",menu=edit_menu)


#HelpMenu Bar
help_menu=Menu(menubar,tearoff=0)

help_menu.add_command(label='About Notepad')
menubar.add_cascade(label='Help',menu=help_menu)

#Scroll and Entry box
scrollbar=Scrollbar(root).pack(side=RIGHT,fill=Y)

entry=Text(root,wrap=WORD,bg='#fff',font=('vardana 20'))
entry.pack(padx=10,pady=5,expand=True,fill=BOTH)



root.mainloop()