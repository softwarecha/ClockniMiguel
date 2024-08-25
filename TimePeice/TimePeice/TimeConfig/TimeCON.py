from time  import strftime
from tkinter import *


class Time:
    def __init__(self):
        self.root = Tk()
        self.root.title('Clock')
        self.label1()
    def Display_Time(self):
        self.string = strftime('%H:%M:%S %p')
        self.label.config(text=self.string)
        self.label.after(1000, self.Display_Time)



    def label1(self):
        self.label = Label(self.root, font=('Arial', 80), background='black', foreground='cyan')
        self.label.pack(anchor= 'center')
Clock = Time()
Clock.Display_Time()
Clock.root.mainloop()