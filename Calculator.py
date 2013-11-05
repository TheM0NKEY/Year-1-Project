from tkinter import *

frame_index = 0

class MainWindow(Frame):

    def __init__(self, master):
        super(MainWindow, self).__init__(master)
        self.grid()
        self.create_widgets()



    def create_widgets(self):
        global frame_index
        self.decimalbutton = Button(self, text = "Decimal Calculator", command = self.dec_cal)
        self.decimalbutton.grid(row = 0, column = 0)
        self.binarybutton = Button(self, text = "Binary Calculator", command = self.bin_cal)
        self.binarybutton.grid(row = 0, column = 2)
        self.hexbutton = Button(self, text = "Hex Calculator", command = self.hex_cal)
        self.hexbutton.grid(row = 0, column = 4)

        if frame_index == 1:
            self.inputbox = Entry(self)
            self.inputbox.grid(row = 2, column = 2)
        elif frame_index == 2:
            self.inputbox = Entry(self)
            self.inputbox.grid(row = 2, column = 2)
        elif frame_index == 3:
            self.inputbox = Entry(self)
            self.inputbox.grid(row = 2, column = 2)


    def dec_cal(self):
        global frame_index
        frame_index = 1
        return frame_index

    def bin_cal(self):
        global frame_index
        frame_index = 2
        return frame_index

    def hex_cal(self):
        global frame_index
        frame_index = 3
        return frame_index



root = Tk()
root.title("Calculator")
root.geometry("404x300")
app = MainWindow(root)
root.mainloop()
