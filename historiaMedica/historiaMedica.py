import tkinter as tk 
from paciente.gui import Frame

def main():
    root=tk.Tk()
    root.title("historia medica")
    root.resizable(0,0)

    frame=Frame(root)
    frame.mainloop() 

    root.mainloop()
if __name__=="__main__":
    main()