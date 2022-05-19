import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["America","India","Australia"]

questions = []

for i in answers:
	words = list(i)
	shuffle(words)
	questions.append(words)

num = random.randint(0,len(questions)-1)

def initial():
	global questions, num
	lb1.configure(text=questions[num]) #configure is a method

def answercheck():
	global questions, num, answers
	userinput = e1.get()
	if userinput == answers[num]:
		messagebox.showinfo('Success','Your answer was correct')
	else:
		messagebox.showinfo('Error','Your answer was incorrect')

def resetswitch():
	global questions,num,answers
	#everytime it generates a new question.
	num = random.randint(0,len(questions)-1)
	lb1.configure(text=questions[num])
	e1.delete(0,END)

window = Tk()

window.geometry("300x300")
window.configure(background='#35BDD0')
window.title("jumblebot")
window.iconbitmap("icon.ico")

lb1 = Label(window, font='times 20', bg='#E03B8B', fg='#8D3DAF')
#ipady= internal pad in y axis, pad= padding in y axis
lb1.pack(pady=30, ipady=10, ipadx=10)

answer = StringVar()
e1 = Entry(window, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

button1 = Button(window,text="Check",width=20,bg='#B4161B', command=answercheck)
button1.pack(pady=40)

button2 = Button(window, text="Reset",width=20, bg='#E21717',command=resetswitch)
button2.pack()

initial()
window.mainloop()