import tkinter as tk

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Calculator")
        self.wm_iconbitmap('myIcon.ico')
        self.geometry("710x600")
        self.grid()
        self.create_widgets()



    def create_widgets(self):    
        self.toolbar = tk.Frame(self, borderwidth=2, relief="groove")
        self.toolbar.pack(side="top")

        self.main_frame = tk.Frame(self, borderwidth=2, width=697, height=300)
        self.main_frame.pack(side="top")

        self.top_packing_frame = tk.Frame(self.main_frame, width=697, height=10)
        self.top_packing_frame.pack(side="top")
        self.entry_frame =tk.Frame(self.main_frame, width=697, height=100)
        self.entry_frame.pack(side="top")
        self.cal_frame = tk.Frame(self.main_frame, relief="groove", width=400, height=212, borderwidth=2)
        self.cal_frame.pack(side="top", fill=tk.X, expand=1)
        self.calculations_frame = tk.Frame(self.main_frame, relief="groove", width=400, height=100, borderwidth=2)
        self.calculations_frame.pack(side="bottom", fill=tk.X, expand=1)

        dec_button = tk.Button(self.toolbar, text="Decimal Calculator", width=20, command = self.dec_cal)
        bin_button = tk.Button(self.toolbar, text="Binary Calcualtor", width=20, command = self.bin_cal)
        hex_button = tk.Button(self.toolbar, text="Hexadecimal Calculator", width=20, command = self.hex_cal)
        dec_button.pack(side="left")
        bin_button.pack(side="left")
        hex_button.pack(side="left")

        self.button_clear1 = tk.Button(self.entry_frame, text="Clear", width=12, command=self.button_clear1_func)
        self.button_clear1.grid(row=0, column=1, columnspan=2)
        self.number_entry1 = tk.Entry(self.entry_frame, width=30)
        self.number_entry1.grid(row=2, column=1, columnspan=2)


        #Draws the Text box that will show the previous 10 calculations
        self.packing_frame1 = tk.Frame(self.calculations_frame, width=60, height=30)
        self.packing_frame1.grid(column=0, row=0)
        
        self.prev_calc_button1 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func1)
        self.prev_calc_button1.grid(column=2, row=0)
        self.prev_calc1 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc1.grid(column=1, columnspan=3, row=1)

        self.prev_calc_button2 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func2)
        self.prev_calc_button2.grid(column=2, row=2)
        self.prev_calc2 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc2.grid(column=1, columnspan=3, row=3)

        self.prev_calc_button3 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func3)
        self.prev_calc_button3.grid(column=2, row=4)
        self.prev_calc3 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc3.grid(column=1, columnspan=3, row=5)

        self.prev_calc_button4 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func4)
        self.prev_calc_button4.grid(column=2, row=6)
        self.prev_calc4 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc4.grid(column=1, columnspan=3, row=7)

        self.prev_calc_button5 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func5)
        self.prev_calc_button5.grid(column=2, row=8)
        self.prev_calc5 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc5.grid(column=1, columnspan=3, row=9)


        self.prev_calc_button6 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func6)
        self.prev_calc_button6.grid(column=6, row=0)
        self.prev_calc6 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc6.grid(column=5, columnspan=3, row=1)

        self.prev_calc_button7 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func7)
        self.prev_calc_button7.grid(column=6, row=2)
        self.prev_calc7 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc7.grid(column=5, columnspan=3, row=3)

        self.prev_calc_button8 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func8)
        self.prev_calc_button8.grid(column=6, row=4)
        self.prev_calc8 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc8.grid(column=5, columnspan=3, row=5)

        self.prev_calc_button9 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func9)
        self.prev_calc_button9.grid(column=6, row=6)
        self.prev_calc9 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc9.grid(column=5, columnspan=3, row=7)

        self.prev_calc_button10 = tk.Button(self.calculations_frame, text = "Use", width=10, command=self.use_func10)
        self.prev_calc_button10.grid(column=6, row=8)
        self.prev_calc10 = tk.Entry(self.calculations_frame, width=30)
        self.prev_calc10.grid(column=5, columnspan=3, row=9)





    def dec_cal(self):
        """The Function that handles the decimal calculator layout and button functions"""
        #Resetting the Calculator Frame area
        self.cal_frame.destroy()
        self.number_entry1.delete(0,tk.END)

        #Redrawing the Calculator Frame
        self.cal_frame = tk.Frame(self.main_frame, relief="groove", width=440, height=300, borderwidth=2)
        self.cal_frame.pack(side="left", fill=tk.BOTH, expand=1)

        #Drawing the frame that will hold the conversion buttons
        self.convert_frame = tk.Frame(self.cal_frame, relief = "groove", width=405, height = 50, borderwidth=2)
        self.convert_frame.pack(side="top")

        #Drawing the frame that will hold the calculators number buttons
        self.num_button_frame = tk.Frame(self.cal_frame, relief="groove", width = 400, height=200, borderwidth=2)
        self.num_button_frame.pack(side="left", expand=1)

        #Drawing the frame that will hold the calculators operational buttons
        self.op_button_frame = tk.Frame(self.cal_frame, relief="groove", width=400, height=200, borderwidth=2)
        self.op_button_frame.pack(side="right", expand=1)



        #Drawing all of the number related buttons
        self.packing_frame1 = tk.Frame(self.num_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)
        
        self.button7 = tk.Button(self.num_button_frame, text="7", width=5, height=1, command = self.button7_func)
        self.button7.grid(row=5, column=1)
        self.button8 = tk.Button(self.num_button_frame, text="8", width=5, height=1, command = self.button8_func)
        self.button8.grid(row=5, column=2)
        self.button9 = tk.Button(self.num_button_frame, text="9", width=5, height=1, command = self.button9_func)
        self.button9.grid(row=5, column=3)

        self.button4 = tk.Button(self.num_button_frame, text="4", width=5, height=1, command = self.button4_func)
        self.button4.grid(row=6, column=1)
        self.button5 = tk.Button(self.num_button_frame, text="5", width=5, height=1, command = self.button5_func)
        self.button5.grid(row=6, column=2)
        self.button6 = tk.Button(self.num_button_frame, text="6", width=5, height=1, command = self.button6_func)
        self.button6.grid(row=6, column=3)

        self.button1 = tk.Button(self.num_button_frame, text="1", width=5, height=1, command = self.button1_func)
        self.button1.grid(row=7, column=1)
        self.button2 = tk.Button(self.num_button_frame, text="2", width=5, height=1, command = self.button2_func)
        self.button2.grid(row=7, column=2)
        self.button3 = tk.Button(self.num_button_frame, text="3", width=5, height=1, command = self.button3_func)
        self.button3.grid(row=7, column=3)

        self.button0 = tk.Button(self.num_button_frame, text="0", width=15, height=1, command = self.button0_func)
        self.button0.grid(row=8, column=1, columnspan=3)

        self.packing_frame1 = tk.Frame(self.num_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)



        #Drawing all of the operational buttons
        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)
        
        self.button_plus1 = tk.Button(self.op_button_frame, text="+", width=5, height=1, command=self.dec_addition)
        self.button_plus1.grid(row=5, column=1)
        self.button_minus1 = tk.Button(self.op_button_frame, text="-", width=5, height=1, command=self.dec_minus)
        self.button_minus1.grid(row=5, column=2)

        self.button_mulitply1 = tk.Button(self.op_button_frame, text="*", width=5, height=1, command=self.dec_multiply)
        self.button_mulitply1.grid(row=6, column=1)
        self.button_divide1 = tk.Button(self.op_button_frame, text="/", width=5, height=1, command=self.dec_divide)
        self.button_divide1.grid(row=6, column=2)

        self.button_equals1 = tk.Button(self.op_button_frame, text="=", width=5, height=1, command=self.dec_equals)
        self.button_equals1.grid(row=7, column=1, columnspan=2)

        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)


        #Drawing conversion buttons
        self.convert_bin = tk.Button(self.convert_frame, text="Convert to Binary", width = 15, height = 1)
        self.convert_bin.grid(row=0, column = 0)

        self.convert_hex = tk.Button(self.convert_frame, text="Convert to Hex", width = 15, height = 1)
        self.convert_hex.grid(row=0, column = 1)





    def bin_cal(self):
        """The Function that handles the binary calculator layout and button functions"""
        self.cal_frame.destroy()
        self.number_entry1.delete(0,tk.END)

        #Redrawing the Calculator Frame
        self.cal_frame = tk.Frame(self.main_frame, relief="groove", width=440, height=300, borderwidth=2)
        self.cal_frame.pack(side="left", fill=tk.BOTH, expand=1)

        #Drawing the frame that will hold the calculators number buttons
        self.num_button_frame = tk.Frame(self.cal_frame, relief="groove", width = 400, height=200, borderwidth=2)
        self.num_button_frame.pack(side="left", expand=1)

        #Drawing the frame that will hold the calculators operational buttons
        self.op_button_frame = tk.Frame(self.cal_frame, relief="groove", width=400, height=200, borderwidth=2)
        self.op_button_frame.pack(side="right", expand=1)



        #Drawing all of the number related buttons
        self.packing_frame1 = tk.Frame(self.num_button_frame, width=150, height=57)
        self.packing_frame1.grid(rowspan=4, columnspan=5)

        self.button1 = tk.Button(self.num_button_frame, text="1", width=21, height=1, command = self.button1_func)
        self.button1.grid(row=5, column=1, columnspan=3)

        self.button0 = tk.Button(self.num_button_frame, text="0", width=21, height=1, command = self.button0_func)
        self.button0.grid(row=8, column=1, columnspan=3)

        self.packing_frame1 = tk.Frame(self.num_button_frame, width=100, height=57)
        self.packing_frame1.grid(rowspan=4, columnspan=5)



        #Drawing all of the operational buttons
        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)
        
        self.button_plus2 = tk.Button(self.op_button_frame, text="+", width=5, height=1)
        self.button_plus2.grid(row=5, column=1)
        self.button_minus2 = tk.Button(self.op_button_frame, text="-", width=5, height=1)
        self.button_minus2.grid(row=5, column=2)

        self.button_mulitply2 = tk.Button(self.op_button_frame, text="*", width=5, height=1)
        self.button_mulitply2.grid(row=6, column=1)
        self.button_divide2 = tk.Button(self.op_button_frame, text="/", width=5, height=1)
        self.button_divide2.grid(row=6, column=2)

        self.button_equals2 = tk.Button(self.op_button_frame, text="=", width=5, height=1)
        self.button_equals2.grid(row=7, column=1, columnspan=2)

        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)






        
    def hex_cal(self):
        """The function the handles the hex calculator layout and button functions"""
        self.cal_frame.destroy()
        self.number_entry1.delete(0,tk.END)

        #Redrawing the Calculator Frame
        self.cal_frame = tk.Frame(self.main_frame, relief="groove", width=440, height=300, borderwidth=2)
        self.cal_frame.pack(side="left", fill=tk.BOTH, expand=1)

        #Drawing the frame that will hold the calculators number buttons
        self.num_button_frame = tk.Frame(self.cal_frame, relief="groove", width = 400, height=200, borderwidth=2)
        self.num_button_frame.pack(side="left", expand=1)

        #Drawing the frame that will hold the calculators operational buttons
        self.op_button_frame = tk.Frame(self.cal_frame, relief="groove", width=400, height=200, borderwidth=2)
        self.op_button_frame.pack(side="right", expand=1)



        #Drawing all of the number related buttons

        #Number Buttons
        self.button7 = tk.Button(self.num_button_frame, text="7", width=5, height=1, command = self.button7_func)
        self.button7.grid(row=8, column=1)
        self.button8 = tk.Button(self.num_button_frame, text="8", width=5, height=1, command = self.button8_func)
        self.button8.grid(row=8, column=2)
        self.button9 = tk.Button(self.num_button_frame, text="9", width=5, height=1, command = self.button9_func)
        self.button9.grid(row=8, column=3)

        self.button4 = tk.Button(self.num_button_frame, text="4", width=5, height=1, command = self.button4_func)
        self.button4.grid(row=7, column=1)
        self.button5 = tk.Button(self.num_button_frame, text="5", width=5, height=1, command = self.button5_func)
        self.button5.grid(row=7, column=2)
        self.button6 = tk.Button(self.num_button_frame, text="6", width=5, height=1, command = self.button6_func)
        self.button6.grid(row=7, column=3)

        self.button1 = tk.Button(self.num_button_frame, text="1", width=5, height=1, command = self.button1_func)
        self.button1.grid(row=6, column=1)
        self.button2 = tk.Button(self.num_button_frame, text="2", width=5, height=1, command = self.button2_func)
        self.button2.grid(row=6, column=2)
        self.button3 = tk.Button(self.num_button_frame, text="3", width=5, height=1, command = self.button3_func)
        self.button3.grid(row=6, column=3)

        self.button0 = tk.Button(self.num_button_frame, text="0", width=15, height=1, command = self.button0_func)
        self.button0.grid(row=5, column=1, columnspan=3)

        #Letter Buttons
        self.buttonA = tk.Button(self.num_button_frame, text="A", width=5, height=1, command = self.buttonA_func)
        self.buttonA.grid(row=9, column=1)
        self.buttonB = tk.Button(self.num_button_frame, text="B", width=5, height=1, command = self.buttonB_func)
        self.buttonB.grid(row=9, column=2)
        self.buttonC = tk.Button(self.num_button_frame, text="C", width=5, height=1, command = self.buttonC_func)
        self.buttonC.grid(row=9, column=3)

        self.buttonD = tk.Button(self.num_button_frame, text="D", width=5, height=1, command = self.buttonD_func)
        self.buttonD.grid(row=10, column=1)
        self.buttonE = tk.Button(self.num_button_frame, text="E", width=5, height=1, command = self.buttonE_func)
        self.buttonE.grid(row=10, column=2)
        self.buttonF = tk.Button(self.num_button_frame, text="F", width=5, height=1, command = self.buttonF_func)
        self.buttonF.grid(row=10, column=3)


        #Drawing all of the operational buttons
        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)
        
        self.button_plus3 = tk.Button(self.op_button_frame, text="+", width=5, height=1)
        self.button_plus3.grid(row=5, column=1)
        self.button_minus3 = tk.Button(self.op_button_frame, text="-", width=5, height=1)
        self.button_minus3.grid(row=5, column=2)

        self.button_mulitply3 = tk.Button(self.op_button_frame, text="*", width=5, height=1)
        self.button_mulitply3.grid(row=6, column=1)
        self.button_divide3 = tk.Button(self.op_button_frame, text="/", width=5, height=1)
        self.button_divide3.grid(row=6, column=2)

        self.button_equals3 = tk.Button(self.op_button_frame, text="=", width=5, height=1)
        self.button_equals3.grid(row=7, column=1, columnspan=2)

        self.packing_frame1 = tk.Frame(self.op_button_frame, width=100, height=30)
        self.packing_frame1.grid(rowspan=4, columnspan=5)



    #Functions for the number buttons
    def button1_func(self):
        self.number_entry1.insert(tk.END, "1")

    def button2_func(self):
        self.number_entry1.insert(tk.END, "2")

    def button3_func(self):
        self.number_entry1.insert(tk.END, "3")

    def button4_func(self):
        self.number_entry1.insert(tk.END, "4")

    def button5_func(self):
        self.number_entry1.insert(tk.END, "5")

    def button6_func(self):
        self.number_entry1.insert(tk.END, "6")

    def button7_func(self):
        self.number_entry1.insert(tk.END, "7")

    def button8_func(self):
        self.number_entry1.insert(tk.END, "8")

    def button9_func(self):
        self.number_entry1.insert(tk.END, "9")

    def button0_func(self):
        self.number_entry1.insert(tk.END, "0")

    def buttonA_func(self):
        self.number_entry1.insert(tk.END, "A")

    def buttonB_func(self):
        self.number_entry1.insert(tk.END, "B")

    def buttonC_func(self):
        self.number_entry1.insert(tk.END, "C")

    def buttonD_func(self):
        self.number_entry1.insert(tk.END, "D")

    def buttonE_func(self):
        self.number_entry1.insert(tk.END, "E")

    def buttonF_func(self):
        self.number_entry1.insert(tk.END, "F")


    #Entry Box Button Functions
    def button_clear1_func(self):
        self.number_entry1.delete(0,tk.END)
        


    #Function Button functions
    def dec_addition(self):
        """Addition"""
        global var1
        var1 = 0
        var1 = self.number_entry1.get()
        if var1 == "":
            var1 = 0
        self.number_entry1.delete(0, tk.END)

        global func
        func = "+"

    def dec_minus(self):
        """Subtraction"""
        global var1
        var1 = 0
        var1 = self.number_entry1.get()
        if var1 == "":
            var1 = 0
        self.number_entry1.delete(0, tk.END)

        global func
        func = "-"

    def dec_multiply(self):
        """Multiplication"""
        global var1
        var1 = 0
        var1 = self.number_entry1.get()
        if var1 == "":
            var1 = 0
        self.number_entry1.delete(0, tk.END)

        global func
        func = "*"

    def dec_divide(self):
        """Division"""
        global var1
        var1 = 0
        var1 = self.number_entry1.get()
        if var1 == "":
            var1 = 0
        self.number_entry1.delete(0, tk.END)

        global func
        func = "/"

    def dec_equals(self):
        global var2
        var2 = 0
        var2 = self.number_entry1.get()
        if var2 == "":
            var2 ==0
        self.number_entry1.delete(0, tk.END)
        
        x = float(var1)
        y = float(var2)
        
        global result

        if func == "+":
            result = x + y
        elif func == "-":
            result = x - y
        elif func == "*":
            result = x * y
        elif func == "/":
            result = x / y
        
        self.number_entry1.insert(0, result)

        global cal1
        cal1 = 0
        global cal2
        cal2 = 0
        global cal3
        cal3 = 0
        global cal4
        cal4 = 0
        global cal5
        cal5 = 0
        global cal6
        cal6 = 0
        global cal7
        cal7 = 0
        global cal8
        cal8 = 0
        global cal9
        cal9 = 0
        global cal10
        cal10 = 0
        
        cal10 = self.prev_calc9.get()
        cal9 = self.prev_calc8.get()
        cal8 = self.prev_calc7.get()
        cal7 = self.prev_calc6.get()
        cal6 = self.prev_calc5.get()
        cal5 = self.prev_calc4.get()
        cal4 = self.prev_calc3.get()
        cal3 = self.prev_calc2.get()
        cal2 = self.prev_calc1.get()
        cal1 = self.number_entry1.get()
        
        self.prev_calc1.delete(0, tk.END)
        self.prev_calc2.delete(0, tk.END)
        self.prev_calc3.delete(0, tk.END)
        self.prev_calc4.delete(0, tk.END)
        self.prev_calc5.delete(0, tk.END)
        self.prev_calc6.delete(0, tk.END)
        self.prev_calc7.delete(0, tk.END)
        self.prev_calc8.delete(0, tk.END)
        self.prev_calc9.delete(0, tk.END)
        self.prev_calc10.delete(0, tk.END)


        self.prev_calc10.insert(0, cal10)        
        self.prev_calc9.insert(0, cal9)
        self.prev_calc8.insert(0, cal8)
        self.prev_calc7.insert(0, cal7)
        self.prev_calc6.insert(0, cal6)
        self.prev_calc5.insert(0, cal5)
        self.prev_calc4.insert(0, cal4)
        self.prev_calc3.insert(0, cal3)
        self.prev_calc2.insert(0, cal2)
        self.prev_calc1.insert(0, cal1)


    #The functions that handle each of the 'use' buttons
    def use_func1(self):
        x = self.prev_calc1.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func2(self):
        x = self.prev_calc2.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func3(self):
        x = self.prev_calc3.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func4(self):
        x = self.prev_calc4.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func5(self):
        x = self.prev_calc5.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func6(self):
        x = self.prev_calc6.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func7(self):
        x = self.prev_calc7.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func8(self):
        x = self.prev_calc8.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func9(self):
        x = self.prev_calc9.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)
    
    def use_func10(self):
        x = self.prev_calc10.get()
        self.number_entry1.delete(0, tk.END)
        self.number_entry1.insert(0, x)




    #Functions that handle the conversions from Decimal to Binary and Hex

    def BecToBin(self):
        x = self.number_entry1.get()
        




if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
