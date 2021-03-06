from distutils.command.config import config
from tkinter import END, Image, Tk, Text, BOTH, W, N, E, S, Toplevel, font, messagebox
from PIL import ImageTk, Image  
from tkinter import Button, Frame, Label
from activity import activity
from event import event
from cpm import cpmCalculate
import re

def new_window():
    top = Toplevel()
    top.configure(background='#ffd6b3')
    top.title("Help")
    top.geometry("750x550")
    lab = Label(top, text="This is the program to calculate the CPM", background='#ffd6b3', font=("Arial", 14))
    lab.pack(pady=5)
    lab1 = Label(top, text="In order to perform a proper calculation you have to insert data in a right way", background='#ffd6b3', font=("Arial", 14))
    lab1.pack(pady=5)
    lab2 = Label(top, text="Example :", background='#ffd6b3', font=("Arial", 14))
    lab2.pack(pady=5)

    image1 = Image.open("example.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(top, image=test)
    label1.image = test
    label1.place(x=5, y=5)
    label1.pack()

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.master.title("CPM")
        self.pack(fill=BOTH, expand=True)
        self.configure(background='#ffd6b3')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(5, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        myFont = font.Font(family='Arial', size=15)

        lbl1 = Label(self, text="Activities", font=("Arial", 16), bg='#ffd6b3')
        lbl1.grid(column=0,row=0, pady=4, padx=5)

        lbl2 = Label(self, text="Duration", font=("Arial", 16), bg='#ffd6b3')
        lbl2.grid(column=1,row=0, pady=4, padx=5)

        lbl3 = Label(self, text="Chronology", font=("Arial", 16), bg='#ffd6b3')
        lbl3.grid(column=2,row=0, pady=4, padx=5)

        self.area1 = Text(self, font=("Arial", 16), bg='#ffe3cc')
        self.area1.grid(row=1, column=0, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        self.area2 = Text(self, font=("Arial", 16), bg='#ffe3cc')
        self.area2.grid(row=1, column=1, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        self.area3 = Text(self, font=("Arial", 16), bg='#ffe3cc')
        self.area3.grid(row=1, column=2, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        abtn = Button(self, text="Clear", command=self.clear_text_fields, bg='#cfaa8c')
        abtn['font'] = myFont
        abtn.grid(row=1, column=5)

        # cbtn = Button(self, text="Remove", bg='#cfaa8c')
        # cbtn['font'] = myFont
        # cbtn.grid(row=2, column=5, pady=4)

        hbtn = Button(self, text="Help", command=new_window, bg='#cfaa8c')
        hbtn['font'] = myFont
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="Calculate", command=self.calculate, bg='#cfaa8c')
        obtn['font'] = myFont
        obtn.grid(row=5, column=5)

    def retrieve_activites_names(self):
        input = self.area1.get("1.0",'end-1c')
        return input

    def retrieve_activites_duration(self):
        input = self.area2.get("1.0",'end-1c')
        return input

    def retrieve_activites_chronology(self):
        input = self.area3.get("1.0",'end-1c')
        return input

    def clear_text_fields(self):
        self.area1.delete('1.0', END)
        self.area2.delete('1.0', END)
        self.area3.delete('1.0', END)

    def calculate(self):

        actNames = self.retrieve_activites_names().splitlines()
        actDuration = self.retrieve_activites_duration().splitlines()
        actChronology = self.retrieve_activites_chronology().splitlines()

        testNames = True
        testDurations = True
        testChronology = True
        testColumnsSize = True
        errorMessage = "Fix the errors below :"

        if not(len(actNames) == len(actDuration) == len(actChronology)):
            errorMessage = errorMessage + "\nColumns souhld have the same size !"
            print("==================================================================")
            print("Columns souhld have the same size !")
            print("==================================================================")
            testColumnsSize = False

        for name in actNames:
            pattern = re.compile("^[A-Z]{1,1}$")
            if not pattern.match(name):
                errorMessage = errorMessage + "\nNames should be upper case signle letters !"
                print("==================================================================")
                print(" Activities should be upper case signle letters !")
                print("==================================================================")
                testNames = False
                break

        for duration in actDuration:
            pattern = re.compile("^[1-9][0-9]*$")
            if not pattern.match(duration):
                errorMessage = errorMessage + "\nDurations must be a positive number !"
                print("==================================================================")
                print("Durations must be a positive number !")
                print("==================================================================")
                testNames = False
                break

        for chronology in actChronology:
            pattern = re.compile("^[0-9]{0,5}[-][0-9]{0,5}$")
            if not pattern.match(chronology):
                errorMessage = errorMessage + "\nChronologies must be a \"*number* - *number*\" pattern ! "
                print("==================================================================")
                print("Chronologies must be a \"*number* - *number*\" pattern !")
                print("==================================================================")
                testNames = False
                break

        # print(actNames)
        # print(actDuration)
        # print(actChronology)

        if testNames and testChronology and testDurations and testColumnsSize:    
            activities = []
            for i in range(len(actNames)):
                activities.append(activity(actNames[i],actDuration[i],actChronology[i]))

            activities.append(activity('A',3,'1-2'))
            activities.append(activity('B',4,'2-3'))
            activities.append(activity('C',6,'2-4'))
            activities.append(activity('D',7,'3-5'))
            activities.append(activity('E',1,'5-7'))
            activities.append(activity('F',2,'4-7'))
            activities.append(activity('G',3,'4-6'))
            activities.append(activity('H',4,'6-7'))
            activities.append(activity('I',1,'7-8'))
            activities.append(activity('J',2,'8-9'))

            # activities.append(activity('A',6,'1-2'))
            # activities.append(activity('B',10,'1-3'))
            # activities.append(activity('C',6,'2-3'))
            # activities.append(activity('D',12,'2-5'))
            # activities.append(activity('E',5,'3-4'))
            # activities.append(activity('F',8,'3-5'))
            # activities.append(activity('G',8,'4-6'))
            # activities.append(activity('H',7,'5-6'))
            # activities.append(activity('I',8,'5-7'))
            # activities.append(activity('J',6,'6-7'))
            # activities.append(activity('J',7,'7-8'))

            cpmCalculate(activities)
        else:
            messagebox.showerror("Input error", errorMessage) 
