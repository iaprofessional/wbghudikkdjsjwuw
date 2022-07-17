from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("GUI SYSTEM")

gui_elements = ["Label","Button","Dropdown"]
dropdown = ttk.Combobox(root, state="readonly", values = gui_elements)
dropdown.pack()

class CreateElements():
    
    def __init__(self):
        print("This is CreateElements Class")
        
    def newLabel(self):
        label = Label(root,text='SOME GUY MADE ME', fg="red")
        label.pack()
        
    def newButton(self):
        button = Button(root,text="Button", command=self.message)
        button.pack(padx=20,pady=10)
    
    def newDropdown(self):
        value = [1,2,3,4]
        newDropdown = ttk.Combobox(root, state="readonly", values = value)
        newDropdown.pack()
        
    def choose(self):
        elements = dropdown.get()
        if(elements=="Label"):
            self.newLabel()
        elif(elements=="Button"):
            self.newButton()
        else:
            self.newDropdown()

    def message(self):
        messagebox.showinfo("WHAT ARE YOU DOING HERE?","What? You just clicked me so WHAT?")
        
obj = CreateElements()
btn = Button(root,text="Click", command=obj.choose)
btn.pack(padx=20,pady=10)

root.mainloop()
