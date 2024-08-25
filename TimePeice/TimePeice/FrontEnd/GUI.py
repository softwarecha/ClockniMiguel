from tkinter import *
import TimePeice.BackEnd.BackEnd
import os

class Clock:
    def __init__(self):
        self.root = Tk()
        self.root.title('Clock')
        self.root.geometry('502x329')

        self.current_dir = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_dir, 'Bdnew.png')


        self.background = PhotoImage(file=self.image_path)
        self.background_label = Label(self.root, image=self.background)
        self.background_label.place(relwidth= 1, relheight=1)
        self.root.resizable(False, False)
        self.root.iconbitmap('C:\\Users\\softw\\OneDrive\\Documents\\Python Projects\\TimePeice\\TimePeice\\FrontEnd\\Icon.ico')
        self.label_time()
        self.Upate_Time()
        self.center_window()
    def label_time(self):
        self.label = Label(self.root, font=('Coda Caption', 60), foreground='cyan', background='black')
        self.label.place(relx= 0.5, rely=0.5, anchor='center')
    def Upate_Time(self):
        Current_Time = TimePeice.BackEnd.BackEnd.Stime()
        self.label.config(text=Current_Time)
        self.label.after(1000, self.Upate_Time)

    def center_window(self):

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()


        window_width = 502
        window_height = 329


        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2


        self.root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


