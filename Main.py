import random
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.configure(bg="#065569")
win.geometry("600x400")
win.title("Number Guessing Game")
win.resizable(width=False,height=False)

result = StringVar()
chances = IntVar()
chances1 = IntVar()
choice = IntVar()
no = random.randint(0, 999)
result.set("Guess a number between 0 to 999 ")
chances.set(5)
chances1.set(chances.get())


def fun():
    chances1.set(chances.get())
    if chances.get() > 0:

        if choice.get() > 999 or choice.get() < 0:
            result.set("You just lost 1 Chance")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no == choice.get():
            result.set("Congratulation YOU WON!!!")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no > choice.get():
            result.set("Your guess was too low: Guess a number higher ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
        elif no < choice.get():
            result.set(
                "Your guess was too High: Guess a number Lower ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
    else:
        result.set(
            "Game Over You Lost")


def restart():
    no = random.randint(1, 999)
    result.set("Guess a number between 0 to 999 ")
    choice.set(0)
    chances.set(5)
    chances1.set(chances.get())


ent1 = Entry(win, textvariable=choice,
             font=("Arial", 15), relief=GROOVE)
ent1.place(x=180, y=150)

ent2 = tk.Label(win, textvariable=result, width=40,
             font=("Arial", 15, "normal", "italic"), fg="White", bg="#065569", relief=GROOVE)
ent2.place(x=60, y=210)

ent3 = Entry(win, text=chances1, state='disabled', width=4,
             font=("Arial", 15), fg="black", relief=GROOVE)
ent3.place(x=350, y=250)

msg = Label(win, text='Number Guessing Game',
            font=("Arial", 24), fg="#fffcbd", bg="#065569", relief=GROOVE)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaninig Chances',
             font=("Arial", 15, "normal", "italic"), fg="White", bg="#065569", relief=GROOVE)
msg2.place(x=150, y=250)

try_no = Button(win, text='TRY', font=("Arial", 13), width=5, fg="#13d675", bg="Black", command=fun, relief=GROOVE)
try_no.place(x=360, y=147)

stop = tk.Button(win, text='stop', width=8, command=win.destroy,
                 font=("Arial", 14), fg="white", bg="red", relief=GROOVE)
stop.place(x=300,y=350)

reset = tk.Button(win, text='Restart', width=8, command=restart,
                  font=("Arial", 14), fg="white", bg="green", relief=GROOVE)
reset.place(x=170, y=350)

win.mainloop()