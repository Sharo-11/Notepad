from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", 
                                        filetypes = [("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        name=os.path.basename(file)
        name=name.replace(".txt","")
        root.title(name + " - Hackerzz Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", 
                                        filetypes = [("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            
            name=os.path.basename(file)
            name=name.replace(".txt","")
            root.title(name + " - Hackerzz Notepad")
            print("File Saved")
    else:
         #Save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

def quitApp():
    ask=messagebox.askyesno("Exit","Are you sure?",icon="warning")
    if ask==1:
        root.destroy()
    else:
        return

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Hackerzz Notepad", "Notepad by Sharo")

def popup_menu(event):
    quick.tk_popup(event.x_root,event.y_root)

def black():
    TextArea.config(bg="Black",foreground="green")
    root.update

def white():
    TextArea.config(bg="white",foreground="black",insertbackground="black")
    root.update

def dark():
    TextArea.config(bg="#272727",foreground="#ffffff",insertbackground="#ffffff")
    root.update

def lucida():
    TextArea.config(font="Lucida 13")
    root.update

def garamond():
    TextArea.config(font="Garamond")
    root.update

def courier():
    TextArea.config(font="Courier 13")
    root.update

if __name__ == '__main__':
    #Basic Setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("images/HACKERZZ.ico")
    root.geometry("644x780")
    root.config(bg = "white")

    #TextArea
    TextArea = Text(root, font = "Courier 13", background = 'black', foreground = "light green", insertbackground = "#0af20a")
    file = None
    TextArea.pack(expand = True, fill = BOTH)
   
    
    #MenuBar
    MenuBar = Menu(root)
    
    #FILE MENU
    FileMenu = Menu(MenuBar, tearoff = 0)
    
    #To open new file
    FileMenu.add_command(label = "New", command = newFile)
    
    #To open already existing file
    FileMenu.add_command(label = "Open", command = openFile)
    
    #To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu = FileMenu)
    
    #EDIT MENU
    EditMenu = Menu(MenuBar, tearoff = 0)
    
    #Adding functions - Cut, Copy, Paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)
    MenuBar.add_cascade(label = "Edit", menu = EditMenu)
    
    #HELP MENU
    
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Hackerzz Notepad", command = about)
    MenuBar.add_cascade(label = "Help", menu = HelpMenu)
    
    root.config(menu = MenuBar)

    #Settings menu
    Setting=Menu(MenuBar,tearoff=0)
    background=Menu(Setting,tearoff=0)
    f_ont=Menu(Setting,tearoff=0)

    background.add_radiobutton(label="Default",command=black)
    background.add_radiobutton(label="Dark",command=dark)
    background.add_radiobutton(label="light",command=white)

    f_ont.add_radiobutton(label="lucida",command=lucida)
    f_ont.add_radiobutton(label="Courier 13",command=courier)
    f_ont.add_radiobutton(label="Garamond",command=garamond)

    Setting.add_cascade(label="Background",menu=background)
    Setting.add_cascade(label="font",menu=f_ont)
    MenuBar.add_cascade(label="Setting",menu=Setting)
    
    # quick access menu (right click menu)
    quick=Menu(MenuBar,tearoff=0)
    quick.add_command(label="Cut",command=cut)
    quick.add_command(label="Copy",command=copy)
    quick.add_command(label="Paste",command=paste)
    quick.add_separator
    quick.add_command(label="Exit",command=quitApp)
    
    root.bind("<Button-3>",popup_menu)
    #SCROLLBAR
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)
    
    root.mainloop()
