from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


class BoxingSalary:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("930x500")
        self.root.title("BoxingSalary")
        self.root.maxsize(930, 500)
        self.root.minsize(930, 500)
        self.root['bg'] = ['white']
        self.icon = ImageTk.PhotoImage(Image.open(r"C:\Users\kneno\OneDrive\Desktop\boxer-icon-man-boxing-gloves-helmet-fighter-sign_53562-14834.jpg"))
        self.label = Label(image=self.icon)
        self.label.place(x=215, y=45)

        # Header
        self.heading = Label(self.root, text="Boxing Salary Calculation", font=('verdana', 20, 'bold'), fg="#52595D")
        self.heading.place(y=1, x=260)
        self.frame1 = LabelFrame(self.root, text="Fill up your information", width=195, height=300, font=('verdana', 10, 'bold'),
                                 borderwidth=3, relief=RIDGE, highlightthickness=4, bg="white", highlightcolor="white",
                                 highlightbackground="white", fg="#52595D")
        self.frame2 = LabelFrame(self.root, text="Total match earnings", width=175, height=300,
                                 font=('verdana', 10, 'bold'),
                                 borderwidth=3, relief=RIDGE, highlightthickness=4, bg="white", highlightcolor="white",
                                 highlightbackground="white", fg="#52595D")
        self.frame2.place(y=45, x=720)
        self.frame1.place(y=45, x=15)

        # CheckButtons
        self.var_max_rounds = IntVar()
        self.var_ko_win = IntVar()
        self.var_full_hall = IntVar()
        self.var_venom_equipment = IntVar()
        self.var_main_event = IntVar()
        self.var_match_lost = IntVar()
        self.var_match_win = IntVar()

        self.button_max_rounds = Checkbutton(self.root, text="All rounds played", variable=self.var_max_rounds, fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_max_rounds.place(y=75, x=25)
        self.button_ko_finish = Checkbutton(self.root, variable=self.var_ko_win, text="KO win", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_ko_finish.place(y=100, x=25)
        self.button_full_hall = Checkbutton(self.root, variable=self.var_full_hall, text="Full hall", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_full_hall.place(y=125, x=25)
        self.button_venom_equipment = Checkbutton(self.root, variable=self.var_venom_equipment, text="Venom Equipment", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_venom_equipment.place(y=150, x=25)
        self.button_main_even = Checkbutton(self.root, variable=self.var_main_event, text="Main Event", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_main_even.place(y=175, x=25)
        self.button_match_win = Checkbutton(self.root, variable=self.var_match_win, text="Match win", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_match_win.place(y=200, x=25)
        self.button_match_loss = Checkbutton(self.root, variable=self.var_match_lost, text="Match lost", fg="#52595D", onvalue=1, offvalue=0, command=self.start_salary)
        self.button_match_loss.place(y=225, x=25)

        self.button_calculate = Button(self.root, text="Calculate my salary", font=('verdana', 10, 'bold'), fg="#52595D",
                                       command=self.calculating_salary)
        self.button_calculate.place(y=345, x=30)
        self.button_calculate = Button(self.root, text="Delete", font=('verdana', 10, 'bold'),
                                       fg="#52595D", command=self.deleting)
        self.button_calculate.place(y=345, x=770)
        self.buttonClicked = False
        #Salary Information
        self.total_money = Label(self.root, text="Total Money:", bg="white")
        self.total_money.place(y=75, x=730)
        self.total_money = Label(self.root, text="Training camp:", bg="white")
        self.total_money.place(y=105, x=730)
        self.total_money = Label(self.root, text="Trainers purse:", bg="white")
        self.total_money.place(y=135, x=730)
        self.total_money = Label(self.root, text="Taxes:", bg="white")
        self.total_money.place(y=165, x=730)
        self.total_money = Label(self.root, text="Total Nett Salary", bg="white", font=('verdana', 10, 'bold'), fg="#52595D")
        self.total_money.place(y=235, x=743)
        self.root.mainloop()

    def start_salary(self):
        starting_salary = 0
        if self.var_match_win.get() == 1:
            starting_salary = 60_000
        elif self.var_match_lost.get() == 1:
            starting_salary = 25_000

        if self.var_ko_win.get() == 1:
            starting_salary += 25_000

        if self.var_full_hall.get() == 1:
            starting_salary += 25_000

        if self.var_main_event.get() == 1:
            starting_salary += 35_000

        if self.var_venom_equipment.get() == 1:
            starting_salary += 35_000

        if self.var_max_rounds.get() == 1:
            starting_salary += 20_000

        return starting_salary

    def calculating_salary(self):
        try:
            self.salary_money.destroy()
            self.salary_camp.destroy()
            self.salary_money.destroy()
            self.salary_taxes.destroy()
            self.salary_trainers.destroy()
            self.nett_sal.destroy()
        except:
            print("not defined")
        training_camp_money = 10000
        trainers_purse = 20000
        taxes = 15000

        self.salary_money = Label(self.root, text=self.start_salary(), bg="white", font=('verdana', 10, 'bold'), fg="#52595D")
        self.salary_money.place(y=74, x=826)
        self.salary_camp = Label(self.root, text=-training_camp_money, bg="white", font=('verdana', 10, 'bold'), fg="#52595D")
        self.salary_camp.place(y=105, x=820)
        self.salary_trainers = Label(self.root, text=-trainers_purse, bg="white", font=('verdana', 10, 'bold'), fg="#52595D")
        self.salary_trainers.place(y=134, x=820)
        self.salary_taxes = Label(self.root, text=-taxes, bg="white", font=('verdana', 10, 'bold'), fg="#52595D")
        self.salary_taxes.place(y=163, x=820)
        self.nett_sal = Label(self.root, text=str(self.start_salary()-trainers_purse-training_camp_money-taxes)+"$", bg="white", font=('verdana', 10, 'bold'),
                                 fg="#52595D")
        self.nett_sal.place(y=257, x=775)
        self.button_venom_equipment.deselect()
        self.button_full_hall.deselect()
        self.button_max_rounds.deselect()
        self.button_match_loss.deselect()
        self.button_ko_finish.deselect()
        self.button_match_win.deselect()
        self.button_main_even.deselect()


    def deleting(self):
        self.salary_money.destroy()
        self.salary_taxes.destroy()
        self.salary_trainers.destroy()
        self.salary_camp.destroy()
        self.nett_sal.destroy()

BoxingSalary()