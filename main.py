from tkinter import *
from tkinter import font
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
        root.title(os.path.basename(file) + " - Hackerzz Notepad")
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
            
            root.title(os.path.basename(file) + " - Hackerzz Notepad")
            print("File Saved")
    else:
         #Save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Hackerzz Notepad", "Notepad by Zacker")

if __name__ == '__main__':
    #Basic Setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("images/HACKERZZ.ico")
    root.geometry("644x780+0+0")
    root.config(bg = "black")
    
    #TextArea
    TextArea = Text(root, font = "Courier 13", background = "black", foreground = "#0af20a", cursor = "xterm green", insertbackground = "#0af20a")
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
    
    #SCROLLBAR
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)
    
    root.mainloop()