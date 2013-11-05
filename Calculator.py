from tkinter import *


class MainWindow(Frame):


    def _init_(self, master):
        super(MainWindow, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.decimalbutton = Button(self, text = "Decimal Calculator")
        self.decimalbutton.grid()
        self.binarybutton = Button(self, text = "Binary Calculator")
        self.binarybutton.grid()
        self.hexbutton = Button(self, text = "Hex Calculator")
        self.hexbutton.grid()





root = Tk()
root.title("Calculator")
root.geometry("200x100")
app = MainWindow(root)
root.mainloop()
