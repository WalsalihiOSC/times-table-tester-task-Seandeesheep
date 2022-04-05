# 05/04/22

# modules
from tkinter import *
from random import *


class TimeTableGenerator:
    def __init__(self, min=0, max=10):
        self.min = min
        self.max = max

    def generate(self):
        b = randint(self.min, self.max)
        a = randint(self.min, self.max)
        ans = a*b
        return a, b, ans

    @staticmethod
    def str_format(n1, n2):
        return f'{n1} * {n2}'


class TimesTableGUI:
    def __init__(self, parent):
        # initialising TimesTableGenerator instance and times table variables
        self.times_table = TimeTableGenerator()
        self.a = 0
        self.b = 0
        self.ans = 0

        # initialising main frame
        main = Frame(parent)

        # times table variable
        self.var = StringVar()

        # initialising widgets
        self.q = Label(main, text='')
        self.q.columnconfigure(0, weight=1)
        self.q.rowconfigure(0, weight=1)

        self.check_label = Label(main, text="")

        self.next_button = Button(main, text="Next", command=self.new_q)

        entry_box = Entry(main, width=10, textvariable=self.var)
        entry_box.columnconfigure(1, weight=1)
        entry_box.rowconfigure(0, weight=1)

        check_button = Button(main, text="Check Answer", command=self.check_answer)


        # widget grid
        main.grid(row=0, column=0)
        self.q.grid(row=0, column=0, padx=15, pady=5)
        entry_box.grid(row=0, column=1, padx=15, pady=5)
        check_button.grid(row=1, column=0, padx=15, pady=5)
        self.next_button.grid(row=1, column=1)
        self.check_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.new_q()

    def new_q(self):
        self.a, self.b, self.ans = self.times_table.generate()
        self.q.configure(text=self.times_table.str_format(self.a, self.b))
        self.next_button.configure(state=DISABLED)

    def check_answer(self):
        try:
            if int(self.var.get()) == self.ans:
                self.check_label.configure(text="Correct")
                self.next_button.configure(state=ACTIVE)
            else:
                self.check_label.configure(text="Wrong")
        except ValueError:
            self.check_label.configure(text="Invalid input")


# main routine
root = Tk()
TimesTableGUI(root)
root.mainloop()
