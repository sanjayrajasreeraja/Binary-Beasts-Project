from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkcalendar import *
import tkinter as tk
import tkinter
import winsound
import time
import math
from time import strftime


mydb=sqlite3.connect("student.db")

mycursor = mydb.cursor()

mycursor.execute("create table if not exists forstudent (username char(20),pwd char(20))")
print("Table created")

root= Tk()
root.title("Scholar's Club(Login)")
root.geometry("1000x700")
root.resizable(0,0)
root.iconbitmap("icon.ico")

login_bg_img= ImageTk.PhotoImage(Image.open("bg_login.jpg"))
img1= Label(root,image=login_bg_img)
img1.place(x=0,y=0)

white= ImageTk.PhotoImage(Image.open("white_board.png"))
img2= Label(root,image=white,relief=SUNKEN)
img2.place(x=270,y=70)

login_pic= ImageTk.PhotoImage(Image.open("login_pic.png"))
img3= Label(root,image=login_pic)
img3.place(x=440,y=110)

text1=Label(root,text="Welcome To Scholar's Club",font=("Verdana",16,'bold')).place(x=360,y=280)

login_icon= ImageTk.PhotoImage(Image.open("username-icon.png"))
img4= Label(root,image=login_icon)
img4.place(x=380,y=350)

text2=Label(root,text="Username:",font=("Verdana",12,'bold')).place(x=420,y=355)

user_entry=Entry(root)
user_entry.place(x=530,y=355)

pass_icon= ImageTk.PhotoImage(Image.open("password_icon.png"))
img5= Label(root,image=pass_icon)
img5.place(x=380,y=400)

text3=Label(root,text='Password:',font=("Verdana",12,'bold')).place(x=420,y=405)

pwd_entry=Entry(root, show="*")
pwd_entry.place(x=530,y=405)

text4=Label(root,text="""If you have don't have an account already, 

you can register here->                             """,font=('Verdana',13)).place(x=340,y=560)

def register():
    global signin_bg_img
    global white10
    global login_pic10
    global login_icon10
    global pass_icon10
    top= Toplevel()
    top.title("Scholar's Club(Sign in)")
    top.geometry("1000x700")
    top.resizable(0,0)
    top.iconbitmap("icon.ico")

    signin_bg_img = ImageTk.PhotoImage(Image.open("bg_login.jpg"))
    img10 = Label(top, image=signin_bg_img)
    img10.place(x=0, y=0)

    white10 = ImageTk.PhotoImage(Image.open("white_board.png"))
    img20 = Label(top, image=white10,relief=SUNKEN)
    img20.place(x=270, y=70)

    login_pic10 = ImageTk.PhotoImage(Image.open("login_pic.png"))
    img30 = Label(top, image= login_pic10)
    img30.place(x=440, y=110)

    text1 = Label(top, text="Registration", font=("Verdana", 16, 'bold','underline')).place(x=440, y=280)

    login_icon10 = ImageTk.PhotoImage(Image.open("username-icon.png"))
    img40 = Label(top, image=login_icon10)
    img40.place(x=380, y=350)

    text2 = Label(top, text="Username:", font=("Verdana", 12, 'bold')).place(x=420, y=355)

    name_entry = Entry(top)
    name_entry.place(x=530, y=355)


    pass_icon10 = ImageTk.PhotoImage(Image.open("password_icon.png"))
    img50 = Label(top, image=pass_icon10)
    img50.place(x=380, y=400)

    text3 = Label(top, text='Password:', font=("Verdana", 12, 'bold')).place(x=420, y=405)

    pass_entry = Entry(top, show="*")
    pass_entry.place(x=530, y=405)

    text40 = Label(top, text="""
    NOTE:The username and password can be changed by  
going to the account settings in the home page.""", font=('Verdana', 11,'bold')).place(x=280, y=540)

    def insertdetails():
        user = name_entry.get()
        passd = pass_entry.get()
        if user == "" or passd == "":
            messagebox.showerror("Error!","Please enter a valid username or password")
        else:
            #sql = "INSERT INTO forstudent(username,pwd)VALUES(%s,%s)"
            args=(user,passd)
            mycursor.execute(f"INSERT INTO forstudent VALUES {args}")
            mydb.commit()
            print(mycursor.rowcount, "Records inserted.")
            name_entry.delete(0, END)
            pass_entry.delete(0,END)

    sign_in = Button(top, image=button_img,borderwidth=0,command=insertdetails).place(x=400,y=440)

    def Redraw():
        root.deiconify()
        top.withdraw()

    root.withdraw()

    button = ttk.Button(top, text='BACK', command=Redraw)
    button.place(x=30, y=70)

def condition():
    global us
    global bg_home
    global todo_button
    global cal_button
    global time_button
    global expense_button
    global schedule_button
    global acc_button
    global logout_but

    if user_entry.get()=="" or pwd_entry.get()=="":
        resp10 = messagebox.showerror("Error", "Incorrect Username or Password")

    else:
        def fetch():
            u = user_entry.get()
            p = pwd_entry.get()
            mycursor.execute(f"SELECT * FROM forstudent WHERE username=?",[u])
            try:
                myresult = mycursor.fetchall()
                return myresult

            except IndexError:
                messagebox.showerror("ERROR!","Account does not exists!")

        p=[]
        result = fetch()
        print(result)
        us = user_entry.get()
        p.append(us)
        pw = pwd_entry.get()
        p.append(pw)

        user_entry.delete(0, END)
        pwd_entry.delete(0, END)

        try:
            if us != result[0][0] or pw != result[0][1]:
                resp1 = messagebox.showerror("Error", "Incorrect Username or Password")
                Label(root, text=resp1)

            else:

                top1 = Toplevel()
                top1.title("Scholar's Club")
                top1.geometry("1000x700")
                top1.resizable(0, 0)
                top1.iconbitmap("icon.ico")

                bg_home = ImageTk.PhotoImage(Image.open("bg_home.png"))
                img20 = Label(top1, image=bg_home)
                img20.place(x=0, y=0)

                l = Label(top1, text="Welcome" + " " + us, font=("Verdana,15"))
                l.place(x=800, y=10)

                def Redraw1():
                    root.deiconify()
                    top1.withdraw()

                button = ttk.Button(top1, text='Log out', command=Redraw1)
                button.place(x=700, y=280)

                def Calculator():
                    global bg_home33
                    global bg_home09

                    class Calc():
                        def __init__(self):
                            self.total = 0
                            self.current = ""
                            self.new_num = True
                            self.op_pending = False
                            self.op = ""
                            self.eq = False

                        def num_press(self, num):
                            self.eq = False
                            temp = text_box.get()
                            temp2 = str(num)
                            if self.new_num:
                                self.current = temp2
                                self.new_num = False
                            else:
                                if temp2 == '.':
                                    if temp2 in temp:
                                        return
                                self.current = temp + temp2
                            self.display(self.current)

                        def calc_total(self):
                            self.eq = True
                            self.current = float(self.current)
                            if self.op_pending == True:
                                self.do_sum()
                            else:
                                self.total = float(text_box.get())

                        def display(self, value):
                            text_box.delete(0, END)
                            text_box.insert(0, value)

                        def do_sum(self):
                            if self.op == "add":
                                self.total += self.current
                            if self.op == "minus":
                                self.total -= self.current
                            if self.op == "times":
                                self.total *= self.current
                            if self.op == "divide":
                                self.total /= self.current
                            if self.op == "raise":
                                self.total = self.total ** self.current
                            if self.op == "rootof":
                                self.total = self.total ** (1 / self.current)
                            if self.op == "fact":
                                self.total = int(text_box.get())
                                self.total = math.factorial(self.total)
                            if self.op == "ln":
                                self.total = log(self.total)
                            if self.op == "log":
                                self.total = log(self.total, 10)
                            if self.op == "sine":
                                self.total = math.sin(self.total)
                            if self.op == "cosine":
                                self.total = math.cos(self.total)
                            if self.op == "tangent":
                                self.total = math.tan(self.total)
                            if self.op == "exp":
                                self.total = math.exp(self.total)
                            if self.op == "inv":
                                self.total = 1 / self.total
                            self.new_num = True
                            self.op_pending = False
                            self.display(self.total)

                        def operation(self, op):
                            self.current = float(self.current)
                            if self.op_pending:
                                self.do_sum()
                            elif not self.eq:
                                self.total = self.current
                            self.new_num = True
                            self.op_pending = True
                            self.op = op
                            self.eq = False

                        def clear(self):
                            self.eq = False
                            self.current = "0"
                            self.display(0)
                            self.new_num = True

                        def all_clear(self):
                            self.clear()
                            self.total = 0

                        def sign(self):
                            self.eq = False
                            self.current = -(float(text_box.get()))
                            self.display(self.current)

                    sum1 = Calc()
                    root1 = Toplevel()
                    root1.title("Scholar's Club(Calculator)")
                    root1.geometry("1000x700")
                    root1.iconbitmap("icon.ico")

                    bg_home33 = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img320 = Label(root1, image=bg_home33)
                    img320.place(x=0, y=0)

                    bg_home09 = ImageTk.PhotoImage(Image.open("calc.png"))
                    img208 = Label(root1, image=bg_home09)
                    img208.place(x=270, y=70)

                    def Redraw11():
                        top1.deiconify()
                        root1.withdraw()

                    top1.withdraw()

                    button = ttk.Button(root1, text='BACK', command=Redraw11)
                    button.place(x=50, y=80)

                    calc = Frame(root1)
                    calc.place(x=300,y=200)

                    root1.title("Calculator")
                    text_box = Entry(calc, justify=RIGHT, width=30, font="Times 16 bold")
                    text_box.grid(row=0, column=0, columnspan=8, padx=30, pady=30)
                    text_box.insert(0, "0")
                    # text_box.focus()

                    numbers = "789456123"
                    i = 0
                    bttn = []
                    for j in range(1, 4):
                        for k in range(3):
                            bttn.append(Button(calc, height=2, width=4, padx=10, pady=10, text=numbers[i]))
                            bttn[i]["bg"] = "orange"
                            bttn[i].grid(row=j, column=k, padx=1, pady=1)
                            bttn[i]["command"] = lambda x=numbers[i]: sum1.num_press(x)
                            i += 1

                    bttn_0 = Button(calc, height=2, width=4, padx=10, pady=10, text="0", bg="orange")
                    bttn_0["command"] = lambda: sum1.num_press(0)
                    bttn_0.grid(row=4, column=0, padx=1, pady=1)

                    div = Button(calc, height=2, width=4, padx=10, pady=10, text="/", bg="steel blue")
                    div["command"] = lambda: sum1.operation("divide")
                    div.grid(row=1, column=3, padx=1, pady=1)

                    mult = Button(calc, height=2, width=4, padx=10, pady=10, text="*", bg="steel blue")
                    mult["command"] = lambda: sum1.operation("times")
                    mult.grid(row=2, column=3, padx=1, pady=1)

                    minus = Button(calc, height=2, width=4, padx=10, pady=10, text="-", bg="steel blue")
                    minus["command"] = lambda: sum1.operation("minus")
                    minus.grid(row=3, column=3, padx=1, pady=1)

                    add = Button(calc, height=2, width=4, padx=10, pady=10, text="+", bg="steel blue")
                    add["command"] = lambda: sum1.operation("add")
                    add.grid(row=4, column=3, padx=1, pady=1)

                    power = Button(calc, height=2, width=4, padx=10, pady=10, text="x^y", bg="green")
                    power["command"] = lambda: sum1.operation("raise")
                    power.grid(row=2, column=4, padx=1, pady=1)

                    rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg="green")
                    rootof["command"] = lambda: sum1.operation("rootof")
                    rootof.grid(row=2, column=5, padx=1, pady=1)

                    fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!", bg="green")
                    fact["command"] = lambda: sum1.operation("fact")
                    fact.grid(row=3, column=4, padx=1, pady=1)

                    loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln", bg="green")
                    loge["command"] = lambda: sum1.operation("ln")
                    loge.grid(row=3, column=5, padx=1, pady=1)

                    log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log", bg="green")
                    log10["command"] = lambda: sum1.operation("log")
                    log10.grid(row=4, column=4, padx=1, pady=1)

                    sine = Button(calc, height=2, width=4, padx=10, pady=10, text="sin", bg="green")
                    sine["command"] = lambda: sum1.operation("sine")
                    sine.grid(row=5, column=0, padx=1, pady=1)

                    cosine = Button(calc, height=2, width=4, padx=10, pady=10, text="cos", bg="green")
                    cosine["command"] = lambda: sum1.operation("cosine")
                    cosine.grid(row=5, column=1, padx=1, pady=1)

                    tangent = Button(calc, height=2, width=4, padx=10, pady=10, text="tan", bg="green")
                    tangent["command"] = lambda: sum1.operation("tangent")
                    tangent.grid(row=5, column=2, padx=1, pady=1)

                    exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
                    exponent["command"] = lambda: sum1.operation("exp")
                    exponent.grid(row=5, column=3, padx=1, pady=1)

                    inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
                    inv["command"] = lambda: sum1.operation("inv")
                    inv.grid(row=5, column=4, padx=1, pady=1)

                    point = Button(calc, height=2, width=4, padx=10, pady=10, text=".", bg="white")
                    point["command"] = lambda: sum1.num_press(".")
                    point.grid(row=4, column=1, padx=1, pady=1)

                    neg = Button(calc, height=2, width=4, padx=10, pady=10, text="+/-", bg="white")
                    neg["command"] = sum1.sign
                    neg.grid(row=4, column=2, padx=1, pady=1)

                    clear = Button(calc, height=2, width=4, padx=10, pady=10, text="C", bg="white")
                    clear["command"] = sum1.clear
                    clear.grid(row=1, column=4, padx=1, pady=1)

                    all_clear = Button(calc, height=2, width=4, padx=10, pady=10, text="AC", bg="white")
                    all_clear["command"] = sum1.all_clear
                    all_clear.grid(row=1, column=5, padx=1, pady=1)

                    equals = Button(calc, height=6, width=4, padx=10, pady=10, text="=", bg="green")
                    equals["command"] = sum1.calc_total
                    equals.grid(row=4, column=5, columnspan=1, rowspan=2, padx=1, pady=1)


                def timer():
                    global bgpic
                    global bgpic7

                    def time():
                        string = strftime('%H:%M:%S %p')
                        lbl.config(text=string)
                        lbl.after(1000, time)

                    def countdown(count):

                        seconds = math.floor(count % 60)
                        minutes = math.floor((count / 60) % 60)
                        hours = math.floor((count / 3600))
                        label['text'] = "Hours: " + str(hours) + " Minutes:  " + str(minutes) + " Seconds: " + str(seconds)

                        if count >= 0:
                            top6.after(1000, countdown, count - 1)
                        else:
                            for x in range(3):
                                winsound.Beep(1000, 1000)
                            label['text'] = "Time is up!"

                    def updateButton():
                        hour, minute, sec = hoursE.get(), minuteE.get(), secondE.get()
                        if hour.isdigit() and minute.isdigit() and sec.isdigit():
                            time = int(hour) * 3600 + int(minute) * 60 + int(sec)
                            countdown(time)

                    top6 = Toplevel()
                    top6.title("Scholar's Club(Timer)")
                    top6.iconbitmap("icon.ico")
                    top1.withdraw()
                    top6.geometry("1000x700")
                    top6.resizable(0,0)
                    bgpic = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img200 = Label(top6, image=bgpic)
                    img200.place(x=0, y=0)
                    lbl = Label(top6, font=('calibri', 40, 'bold'), background='purple', foreground='white')
                    lbl.place(x=540,y=300)
                    time()
                    hoursT = tkinter.Label(top6, text="Hours:")
                    hoursE = tkinter.Entry(top6)
                    hoursE.insert(0,0)
                    minuteT = tkinter.Label(top6, text="Minutes:")
                    minuteE = tkinter.Entry(top6)
                    minuteE.insert(0,0)
                    secondT = tkinter.Label(top6, text="Seconds:")
                    secondE = tkinter.Entry(top6)
                    secondE.insert(0,0)
                    hoursT.place(x=270,y=300)
                    hoursE.place(x=340,y=300)
                    minuteT.place(x=270,y=350)
                    minuteE.place(x=340,y=350)
                    secondT.place(x=270,y=400)
                    secondE.place(x=340,y=400)
                    label = tkinter.Label(top6)
                    label.place(x=340,y=430)

                    bgpic7 = ImageTk.PhotoImage(Image.open("timer.png"))
                    img217 = Label(top6, image=bgpic7)
                    img217.place(x=300, y=130)

                    def Redraw151():
                        top1.deiconify()
                        top6.withdraw()

                    button = ttk.Button(top6, text='BACK', command=Redraw151)
                    button.place(x=50, y=80)

                    button = tkinter.Button(top6, text="Start Timer", command=updateButton)
                    button.place(x=340,y=460)

                def accset():
                    global bgpic
                    global bgpic00

                    top5 = Toplevel()
                    top5.title("Scholar's Club(Account Settings)")
                    top5.geometry("1000x700")
                    top5.resizable(0, 0)
                    top5.iconbitmap("icon.ico")

                    bgpic = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img21 = Label(top5, image=bgpic)
                    img21.place(x=0, y=0)

                    def Redraw3():
                        top1.deiconify()
                        top5.withdraw()

                    button22 = ttk.Button(top5, text='BACK', command=Redraw3)
                    button22.place(x=30, y=100)

                    us2 = p[0]
                    pw2 = p[1]
                    table_name11 = us2 + "savings"
                    table_name22 = us2 + "schedule"
                    table_name33 = us2 + "todo"

                    up_usl = Label(top5, text="Update Username:")
                    up_usl.place(x=400, y=280)

                    up_us = Entry(top5)
                    up_us.place(x=520, y=280)

                    pas_upl = Label(top5, text="Update Password:")
                    pas_upl.place(x=400, y=340)

                    pas_up = Entry(top5)
                    pas_up.place(x=520, y=340)

                    def up_user():
                        nus = up_us.get()
                        table_name111 = nus + "savings"
                        table_name222 = nus + "schedule"
                        table_name333 = nus + "todo"
                        if nus == "":
                            messagebox.showerror("Error!", "Please enter valid details.")
                        else:
                            #sql = "UPDATE forstudent SET username = %s WHERE username = %s"
                            #args = (nus, us2)
                            mycursor.execute("UPDATE forstudent SET username = ? WHERE username = ?",[nus,us2])
                            mydb.commit()

                            mycursor.execute(f"ALTER TABLE {table_name11} RENAME TO {table_name111}")
                            mycursor.execute(f"ALTER TABLE {table_name22} RENAME TO {table_name222}")
                            mycursor.execute(f"ALTER TABLE {table_name33} RENAME TO {table_name333}")

                    b211 = ttk.Button(top5, text="Update Username", command=up_user)
                    b211.place(x=530, y=380)

                    bgpic00 = ImageTk.PhotoImage(Image.open("acc.png"))
                    img219 = Label(top5, image=bgpic00)
                    img219.place(x=220, y=130)

                    def up_pass():
                        np = pas_up.get()

                        if np == "":
                            messagebox.showerror("Error!", "Please enter valid details.")
                        else:
                            #sql = "UPDATE forstudent SET pwd = %s WHERE pwd = %s"
                            #args = (np, pw2)
                            mycursor.execute("UPDATE forstudent SET pwd = ? WHERE pwd = ?",[np,pw2])
                            mydb.commit()
                            print(mycursor.rowcount, "records updated")

                    b221 = ttk.Button(top5, text="Update Password", command=up_pass)
                    b221.place(x=400, y=380)

                    def del_all():
                        MsgBox = tk.messagebox.askquestion('Delete Account',
                                                           'Are you sure you want to delete this account?', icon='warning')
                        if MsgBox == 'yes':
                            mycursor.execute("DELETE FROM forstudent WHERE username = ? and pwd= ?",[us2,pw2])

                            mydb.commit()

                            sql1 = f"DROP TABLE if exists {table_name11}"
                            sql2 = f"DROP TABLE if exists {table_name22}"
                            sql3 = f"DROP TABLE if exists {table_name33}"
                            mycursor.execute(sql1)
                            mycursor.execute(sql2)
                            mycursor.execute(sql3)

                            top5.withdraw()
                            root.deiconify()

                    b222 = ttk.Button(top5, text="Delete Account", command=del_all)
                    b222.place(x=480, y=415)

                    top1.withdraw()

                def Savings():
                    global bgpict
                    global pic2327

                    top3 = Toplevel()
                    top3.title("Scholar's Club(Savings And Expenses)")
                    top3.geometry("1000x700")
                    top3.resizable(0, 0)
                    top3.iconbitmap("icon.ico")

                    bgpict = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img22 = Label(top3, image=bgpict)
                    img22.place(x=0, y=0)

                    pic2327 = ImageTk.PhotoImage(Image.open("savings.png"))
                    img37 = Label(top3, image=pic2327)
                    img37.place(x=110, y=30)

                    month_label = Label(top3, text="Select Month:")
                    month_label.place(x=150, y=150)
                    options = [
                        "Select Month",
                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"
                    ]

                    clicked1 = StringVar()
                    clicked1.set(options[0])

                    drop = OptionMenu(top3, clicked1, *options)
                    drop.place(x=150, y=180)

                    month_label = Label(top3, text="Select Year:")
                    month_label.place(x=285, y=150)
                    options = [
                        "Select Year",
                        "2020",
                        "2021",
                        "2022",
                        "2023",
                        "2024",
                        "2025"
                    ]

                    clicked2 = StringVar()
                    clicked2.set(options[0])

                    drop = OptionMenu(top3, clicked2, *options)
                    drop.place(x=285, y=180)

                    amt_label = Label(top3, text="Enter Amount:")
                    amt_label.place(x=420, y=150)

                    am = Entry(top3)
                    am.place(x=420, y=185)

                    spe_label = Label(top3, text="Amount Spent:")
                    spe_label.place(x=575, y=150)

                    spe = Entry(top3)
                    spe.place(x=575, y=185)

                    def Redraw3():
                        top1.deiconify()
                        top3.withdraw()

                    button22 = ttk.Button(top3, text='BACK', command=Redraw3)
                    button22.place(x=20, y=70)

                    us1 = p[0]
                    print(us1)

                    table_name1 = us1 + "savings"
                    print(table_name1)

                    mycursor.execute(
                        f"create table if not exists {table_name1} (month char(100),year char(100),amt char(100),spent char(100),saved int)")
                    print(table_name1, "Savings Table created")

                    def fetchSavingDetails():
                        mycursor.execute(f"SELECT * FROM {table_name1}")
                        exp = mycursor.fetchall()
                        return exp

                    def table():
                        expn = fetchSavingDetails()

                        container = ttk.Frame(top3)
                        canvas = tk.Canvas(container)
                        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
                        # hor_scrollbar = ttk.Scrollbar(container,orient="horizontal",command=canvas.xview)
                        scrollable_frame = ttk.Frame(canvas)

                        scrollable_frame.bind(
                            "<Configure>",
                            lambda e: canvas.configure(
                                scrollregion=canvas.bbox("all")
                            )
                        )

                        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

                        canvas.configure(yscrollcommand=scrollbar.set)

                        for i in range(0, 50):
                            label = ttk.Label(scrollable_frame, text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t").pack()

                        r = 35
                        for col in expn:
                            c = 0

                            for row in col:
                                button = ttk.Button(scrollable_frame, text=row, state=DISABLED)
                                button.place(x=c, y=r, width=150)
                                c += 125
                            r += 30

                        head = ttk.Button(scrollable_frame, text="Month", state=DISABLED)
                        head.place(x=0, y=0, width=150)

                        head1 = ttk.Button(scrollable_frame, text="Year", state=DISABLED)
                        head1.place(x=125, y=0, width=150)

                        head2 = ttk.Button(scrollable_frame, text="Amount", state=DISABLED)
                        head2.place(x=250, y=0, width=150)

                        head3 = ttk.Button(scrollable_frame, text="Spent", state=DISABLED)
                        head3.place(x=375, y=0, width=150)

                        head4 = ttk.Button(scrollable_frame, text="Saved", state=DISABLED)
                        head4.place(x=500, y=0, width=150)

                        container.place(x=150, y=225)
                        canvas.pack(side="left", fill="both", expand=True, ipadx=130)
                        scrollbar.pack(side="right", fill=Y)

                    table()

                    def insertdetailsintosavings():
                        mon = clicked1.get()
                        yea = clicked2.get()
                        amto = am.get()
                        spen = spe.get()
                        got = int(amto)
                        gave = int(spen)
                        sav = got - gave
                        if mon == "Select Month" or yea == "Select Year" or amto == "" or spen == "":
                            messagebox.showerror("Error!", "Please enter valid details.")

                        else:
                            mycursor.execute(f"INSERT INTO {table_name1} VALUES(?,?,?,?,?)",
                                             [mon, yea, amto, spen, sav])
                            mydb.commit()
                            print(mycursor.rowcount, "Records inserted.")
                            am.delete(0, END)
                            spe.delete(0, END)

                            table()

                    b11 = ttk.Button(top3, text="Enter Details", command=insertdetailsintosavings)
                    b11.place(x=720, y=180)

                    new_det = Label(top3, text="Enter month and year to update details:")
                    new_det.place(x=150, y=510)

                    options = [
                        "Select Month to Update",
                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"
                    ]

                    clicked3 = StringVar()
                    clicked3.set(options[0])

                    drop = OptionMenu(top3, clicked3, *options)
                    drop.place(x=150, y=545)

                    options = [
                        "Select Year to Update",
                        "2020",
                        "2021",
                        "2022",
                        "2023",
                        "2024",
                        "2025"
                    ]

                    clicked4 = StringVar()
                    clicked4.set(options[0])

                    drop = OptionMenu(top3, clicked4, *options)
                    drop.place(x=320, y=545)

                    newamt = Label(top3, text="Enter new amount")
                    newamt.place(x=150, y=590)

                    newspent = Label(top3, text="Enter new spent amount")
                    newspent.place(x=300, y=590)

                    new_amt = Entry(top3)
                    new_amt.place(x=150, y=620)

                    new_spent = Entry(top3)
                    new_spent.place(x=300, y=620)

                    def updatesavings():
                        a1 = clicked3.get()
                        a2 = clicked4.get()
                        a3 = new_amt.get()
                        a4 = new_spent.get()
                        b3 = int(a3)
                        b4 = int(a4)
                        nsav = b3 - b4

                        if a1 == "Select Month to Update" or a2 == "Select Year to Update" or a3 == "" or a4 == "":
                            messagebox.showerror("Error!", "Please enter valid details.")

                        else:
                            mycursor.execute(f"UPDATE {table_name1} SET amt =?,spent =?, saved =? WHERE month =? and year =?",[a3, a4, nsav, a1, a2])
                            mydb.commit()
                            print(mycursor.rowcount, "records updated")
                            table()

                    b21 = ttk.Button(top3, text="Update Details", command=updatesavings)
                    b21.place(x=450, y=620)

                    del_det = Label(top3, text="Enter month and year to delete details:")
                    del_det.place(x=550, y=550)

                    options = [
                        "Select Month to Delete",
                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"
                    ]

                    clicked5 = StringVar()
                    clicked5.set(options[0])

                    drop = OptionMenu(top3, clicked5, *options)
                    drop.place(x=550, y=580)

                    options = [
                        "Select Year to Delete",
                        "2020",
                        "2021",
                        "2022",
                        "2023",
                        "2024",
                        "2025"
                    ]

                    clicked6 = StringVar()
                    clicked6.set(options[0])

                    drop = OptionMenu(top3, clicked6, *options)
                    drop.place(x=720, y=580)

                    def delsavings():
                        a11 = clicked5.get()
                        a22 = clicked6.get()

                        if a11 == "Select Month to Delete" or a22 == "Select Year to Delete":
                            messagebox.showerror("Error!", "Please enter valid details.")

                        else:
                            mycursor.execute(f"DELETE FROM {table_name1} WHERE month=? and year=?",[a11, a22])
                            mydb.commit()
                            print(mycursor.rowcount, "records deleted")

                            table()

                    b21 = ttk.Button(top3, text="Delete Records", command=delsavings)
                    b21.place(x=700, y=620)

                    top1.withdraw()

                def schedule():
                    global bgpic
                    global pic23273
                    top4 = Toplevel()
                    top4.title("Scholar's Club(Schedule)")
                    top4.geometry("1000x700")
                    top4.resizable(0, 0)
                    top4.iconbitmap("icon.ico")

                    bgpic = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img22 = Label(top4, image=bgpic)
                    img22.place(x=0, y=0)

                    cal=Calendar(top4,selectmode="day")
                    cal.place(x=200,y=200)

                    event_label=Label(top4,text="Enter your event:").place(x=200,y=400)

                    pic23273 = ImageTk.PhotoImage(Image.open("schedule.png"))
                    img307 = Label(top4, image=pic23273)
                    img307.place(x=300, y=80)

                    event=Entry(top4)
                    event.place(x=300,y=400)

                    us = p[0]
                    print(us)

                    table_name1 = us + "schedule"
                    print(table_name1)

                    mycursor.execute(f"create table if not exists {table_name1} (date varchar(40), event char(40),id int auto_increment primary key)")
                    print(table_name1, "Schedule Table created")

                    my_frame = Frame(top4)
                    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

                    schedule_box = Listbox(my_frame, width=30, yscrollcommand=my_scrollbar.set, relief=RIDGE,font=("Verdana",11), bg="dark blue",fg="white")

                    my_scrollbar.config(command=schedule_box.yview)
                    my_scrollbar.pack(side=RIGHT, fill=Y)
                    my_frame.place(x=600, y=240)

                    schedule_box.pack()

                    def box():
                        mycursor.execute(f"SELECT * FROM {table_name1}")
                        for i in mycursor:
                            if len(i[0])==8 and i[2]>=10:
                                schedule_box.insert("end", str(i[2]) +"  -"+ i[0] + "        -" + i[1])

                            elif len(i[0])==8 and i[2]<10:
                                schedule_box.insert("end", str(i[2]) + "    -" + i[0] + "        -" + i[1])

                            elif len(i[0])==7 and i[2]>=10:
                                schedule_box.insert("end", str(i[2]) +"  -"+ i[0] + "          -" + i[1])

                            elif len(i[0])==7 and i[2]<10:
                                schedule_box.insert("end", str(i[2]) + "    -" + i[0] + "          -" + i[1])

                            elif len(i[0])==6 and i[2]>=10:
                                schedule_box.insert("end", str(i[2]) +"  -"+ i[0] + "            -" + i[1])

                            elif len(i[0])==6 and i[2]<10:
                                schedule_box.insert("end", str(i[2]) + "    -" + i[0] + "            -" + i[1])

                            elif len(i[0])==5 and i[2]>=10:
                                schedule_box.insert("end", str(i[2]) +"  -"+ i[0] + "              -" + i[1])

                            elif len(i[0])==5 and i[2]<10:
                                schedule_box.insert("end", str(i[2]) + "    -" + i[0] + "              -" + i[1])

                    box()


                    def Insert():
                        event_in_table = event.get()
                        date=cal.get_date()
                        if event_in_table == "":
                            messagebox.showerror("Error!", "Please enter a valid task.")

                        else:
                            mycursor.execute(f"INSERT INTO {table_name1}(date,event)VALUES(?,?)",[date,event_in_table])
                            mydb.commit()
                            print(mycursor.rowcount, "Records inserted.")
                            schedule_box.delete(0, END)

                            mycursor.execute(f"SELECT * FROM {table_name1}")
                            box()
                            event.delete(0, END)

                    def Update():
                        selected = schedule_box.get(ANCHOR)
                        print(selected)
                        a = selected.split()
                        print(a)
                        if selected == "":
                            messagebox.showerror("Error!", "Please select something!")

                        else:
                            editing = event_update.get()

                            if editing == "":
                                messagebox.showerror("Error!", "Please type in something")

                            else:
                                con = messagebox.askyesno("Confirmation", "Do you want to update it?")
                                event_checker = a[2] + "%"
                                if con == 1:
                                    mycursor.execute(f"UPDATE {table_name1} SET event=? WHERE id={a[0]}", [editing])
                                    mydb.commit()

                                    schedule_box.delete(0, END)
                                    box()

                                    print(f"{selected} is updated")

                    def Delete():
                        selected = schedule_box.get(ANCHOR)
                        print(selected)
                        a = selected.split()
                        id = a[0]
                        print(a)
                        if selected == "":
                            messagebox.showerror("Error!", "Please select something!")
                        else:
                            ask = messagebox.askyesno("Warning!", "DO YOU WANT DELETE IT?")
                            if ask == 1:
                                mycursor.execute(f"DELETE FROM {table_name1}  WHERE id={id}")
                                mydb.commit()
                                schedule_box.delete(0, END)

                                box()

                                print(f"{selected} is deleted")

                    bu1=ttk.Button(top4,text="Enter Schedule",command=Insert)
                    bu1.place(x=265,y=430)

                    event_update_label = Label(top4, text="Select and Update:").place(x=200, y=460)

                    event_update = Entry(top4)
                    event_update.place(x=310, y=460)

                    bu2 = ttk.Button(top4,text="Update",command=Update)
                    bu2.place(x=270, y=490)

                    bu3 = ttk.Button(top4,text="Delete",command=Delete)
                    bu3.place(x=270, y=520)

                    def Redraw3():
                        top1.deiconify()
                        top4.withdraw()

                    button22 = ttk.Button(top4, text='BACK', command=Redraw3)
                    button22.place(x=30, y=70)

                    top1.withdraw()


                def To_Do():
                    global bgpic
                    global picture
                    top2 = Toplevel()
                    top2.title("Scholar's Club(To-Do List)")
                    top2.geometry("1000x700")
                    top2.resizable(0, 0)
                    top2.iconbitmap("icon.ico")

                    bgpic = ImageTk.PhotoImage(Image.open("bg_feature.jpg"))
                    img21 = Label(top2, image=bgpic)
                    img21.place(x=0, y=0)

                    picture = ImageTk.PhotoImage(Image.open("todo.png"))
                    img300 = Label(top2, image=picture)
                    img300.place(x=240, y=90)

                    title_label = Label(top2, text="Enter Task:")
                    title_label.place(x=240, y=240)

                    task = Entry(top2)
                    task.place(x=340, y=240)

                    edit_label=Label(top2, text="Select and edit:")
                    edit_label.place(x=240,y=330)

                    task_edit = Entry(top2)
                    task_edit.place(x=340, y=330)


                    def Redraw2():
                        top1.deiconify()
                        top2.withdraw()

                    button22 = ttk.Button(top2, text='BACK',command=Redraw2)
                    button22.place(x=30, y=70)

                    us = p[0]
                    print(us)

                    table_name = us + "todo"
                    print(table_name)

                    mycursor.execute(f"create table if not exists {table_name} (title char(100))")
                    print(table_name, "To-Do Table created")

                    def insertdetailsintotodo():
                        title_in_table = task.get()
                        if title_in_table == "":
                            messagebox.showerror("Error!", "Please enter a valid task.")

                        else:
                            # sql = f"INSERT INTO {table_name}(title)VALUES(%s)"
                            #args=(title_in_table,)
                            mycursor.execute(f"INSERT INTO {table_name} VALUES(?)",[title_in_table])
                            mydb.commit()
                            print(mycursor.rowcount, "Records inserted.")
                            to_do_box.insert(END,title_in_table)
                            task.delete(0, END)

                    my_frame= Frame(top2)
                    my_scrollbar= Scrollbar(my_frame,orient=VERTICAL)

                    to_do_box=Listbox(my_frame,width=40,yscrollcommand=my_scrollbar.set,relief=RIDGE,bg="Sky Blue")

                    my_scrollbar.config(command=to_do_box.yview)
                    my_scrollbar.pack(side=RIGHT,fill=Y)
                    my_frame.place(x=600,y=240)

                    to_do_box.pack()

                    mycursor.execute(f"SELECT * FROM {table_name}")
                    for i in mycursor:
                        print(i)
                        to_do_box.insert("end", i[0])

                    def deletefromlist():
                        selected = to_do_box.get(ANCHOR)
                        print(selected)
                        if selected=="":
                            messagebox.showerror("Error!","Please select something!")
                        else:
                            mycursor.execute(f"DELETE FROM {table_name} WHERE title=?",[selected])
                            mydb.commit()
                            to_do_box.delete(ANCHOR)
                            print(f"{selected} is deleted")



                    def update():
                        selected = to_do_box.get(ANCHOR)
                        if selected=="":
                            messagebox.showerror("Error!","Please select something!")

                        else:
                            editing=task_edit.get()
                            if editing=="":
                                messagebox.showerror("Error!","Please type in something")

                            else:
                                sql1 = f"UPDATE {table_name} SET title='" + editing + "' WHERE title='"+selected+"'"
                                mycursor.execute(sql1)
                                mydb.commit()
                                con=messagebox.askyesno("Confirmation","Do you want to update it?")
                                if con==1:
                                    to_do_box.delete(0,END)

                                    mycursor.execute(f"SELECT * FROM {table_name}")

                                    for x in mycursor:
                                        to_do_box.insert("end", x[0])

                                print(f"{selected} is updated")

                    b3=ttk.Button(top2,text="Update",command=update).place(x=330,y=370)

                    b2=ttk.Button(top2,text="Delete",command=deletefromlist).place(x=330,y=300)

                    b1=ttk.Button(top2,text="Enter task",command=insertdetailsintotodo)
                    b1.place(x=330,y=270)


                    top1.withdraw()

                def LOGOUT():
                    top1.withdraw()
                    root.deiconify()

                todo_button = ImageTk.PhotoImage(Image.open("todobutton.png"))
                todo_label = Label(image=todo_button)

                but1 = Button(top1,text="To-Do List",image=todo_button,command=To_Do)
                but1.place(x=100,y=230)

                l1=Label(top1,text="To-Do",bg="yellow",fg="blue").place(x=130,y=340)

                cal_button = ImageTk.PhotoImage(Image.open("calcul.png"))
                cal_label = Label(image=cal_button)

                but2 = Button(top1, text="Calculator",image=cal_button, command=Calculator)
                but2.place(x=300, y=230)

                l1 = Label(top1, text="Calculator", bg="yellow", fg="blue").place(x=320, y=340)

                time_button = ImageTk.PhotoImage(Image.open("clock.png"))
                time_label = Label(image=time_button)

                but3 = Button(top1, text="Timer",image=time_button,command=timer)
                but3.place(x=500, y=230)

                l1 = Label(top1, text="Timer", bg="yellow", fg="blue").place(x=535, y=340)

                expense_button = ImageTk.PhotoImage(Image.open("expenses.png"))
                expense_label = Label(image=expense_button)

                but4 = Button(top1, text="Savings/Expenses",image=expense_button,command=Savings)
                but4.place(x=700, y=230)

                l1 = Label(top1, text="Savings & Expenses", bg="yellow", fg="blue").place(x=700, y=340)

                schedule_button = ImageTk.PhotoImage(Image.open("schedule 2.png"))
                schedule_label = Label(image=schedule_button)

                but5 = Button(top1, text="Schedule",image=schedule_button,command=schedule)
                but5.place(x=200, y=400)

                l1 = Label(top1, text="Schedule", bg="yellow", fg="blue").place(x=220, y=510)

                acc_button = ImageTk.PhotoImage(Image.open("accset.png"))
                acc_label = Label(image=acc_button)

                but6 = Button(top1, text="Account Settings",image=acc_button,command=accset)
                but6.place(x=400, y=400)

                l1 = Label(top1, text="Account Settings", bg="yellow", fg="blue").place(x=405, y=510)

                logout_but=ImageTk.PhotoImage(Image.open("logout_but.jpg"))
                logout_label = Label(image=logout_but)

                but7 = Button(top1, text="Logout", image=logout_but, command=LOGOUT)
                but7.place(x=600, y=400)

                l1 = Label(top1, text="Logout", bg="yellow", fg="blue").place(x=630, y=510)

                root.withdraw()

        except IndexError:
            messagebox.showerror("Error!","Account does not exist!")

button_img = ImageTk.PhotoImage(Image.open("sign_in_but1.png"))

button_img2=ImageTk.PhotoImage(Image.open("login1.png"))

login=Button(root,image=button_img2,borderwidth=0,command=condition).place(x=410,y=450)

button_img1= ImageTk.PhotoImage(Image.open("sign_in_but_logo.png"))

register=Button(root,image=button_img1,borderwidth=0,command=register).place(x=555,y=585)


root.mainloop()