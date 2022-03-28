from cProfile import label
from hashlib import new
from tkinter import Image, Tk, Text, BOTH, W, N, E, S, Toplevel
from PIL import ImageTk, Image  
from tkinter.ttk import Frame, Button, Label, Style
from activity import activity
from event import event
import os
from cpm import cpmCalculate

def new_window():
    top = Toplevel()
    top.title("Second window")
    top.geometry("700x500")    # By default, it is kept as the geometry of the main window, but you can change it.
    lab = Label(top, text="This is the program to calculate the CPM")
    lab.pack(pady=5)
    lab1 = Label(top, text="In order to perform a proper calculation you have to insert data in a right way")
    lab1.pack(pady=5)
    lab2 = Label(top, text="Example :")
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

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(5, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl1 = Label(self, text="Activities")
        lbl1.grid(column=0,row=0, pady=4, padx=5)

        lbl2 = Label(self, text="Duration")
        lbl2.grid(column=1,row=0, pady=4, padx=5)

        lbl3 = Label(self, text="Chronology")
        lbl3.grid(column=2,row=0, pady=4, padx=5)

        self.area1 = Text(self)
        self.area1.grid(row=1, column=0, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        self.area2 = Text(self)
        self.area2.grid(row=1, column=1, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        self.area3 = Text(self)
        self.area3.grid(row=1, column=2, columnspan=1, rowspan=4,padx=1, sticky=E+W+S+N)

        abtn = Button(self, text="Add")
        abtn.grid(row=1, column=5)

        cbtn = Button(self, text="Remove")
        cbtn.grid(row=2, column=5, pady=4)

        hbtn = Button(self, text="Help", command=new_window)
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="Calculate", command=self.calculate)
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

    def calculate(self):

        actNames = self.retrieve_activites_names().splitlines()
        actDuration = self.retrieve_activites_duration().splitlines()
        actChronology = self.retrieve_activites_chronology().splitlines()

        print(actNames)
        print(actDuration)
        print(actChronology)

        if len(actNames) == len(actDuration) == len(actChronology):
            
            activities = []
            for i in range(len(actNames)):

                activities.append(activity(actNames[i],actDuration[i],actChronology[i]))
                # activities.append(activity('B',4,'2-3'))
                # activities.append(activity('C',6,'2-4'))
                # activities.append(activity('D',7,'3-5'))
                # activities.append(activity('E',1,'5-7'))
                # activities.append(activity('F',2,'4-7'))
                # activities.append(activity('G',3,'4-6'))
                # activities.append(activity('H',4,'6-7'))
                # activities.append(activity('I',1,'7-8'))
                # activities.append(activity('J',2,'8-9'))
            
            cpmCalculate(activities)

    
        else:
            print("Wrong input")