from TimePeice.FrontEnd.GUI import Clock
from tkinter import messagebox

messagebox.askquestion('Error!', 'System Memory Error!')
messagebox.showerror('Error', 'System will be formatted')



if __name__ == '__main__':
    app = Clock()
    app.root.mainloop()