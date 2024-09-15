from tkinter import *
import math
import pygame 

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
FONT_NAME = "Garamond"
BACKGROUND = '#bc7f6f'
TIMERCOLOR = '#f8dbdd'
CHECKMARK = '#a12939'
reps = 0
timer = NONE

#timer function

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_text.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long Break", fg=TIMERCOLOR)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Short Break", fg=TIMERCOLOR)
    else: 
        count_down(work_sec)
        timer_text.config(text="Work...", fg=TIMERCOLOR)

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

#ui

window = Tk()
window.title('Pomodoro Timer')
window.config(padx= 100, pady= 50, bg= BACKGROUND)

#Image

canvas = Canvas(width= 560, height= 560, bg= BACKGROUND, highlightthickness= 0)
image = PhotoImage(file= "Hornet2.png")
canvas.create_image(280, 280, image= image)
timer_text = canvas.create_text(280, 50, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row= 1, column= 1)

title_label = Label(text= "Pomodoro Timer", fg= 'White', font=(FONT_NAME, 40), bg= BACKGROUND)
title_label.grid(row= 0, column= 1)

start_butt = Button(text= "Start Timer", font= FONT_NAME, borderwidth= 0, command= start_timer)
start_butt.grid(row= 2, column= 0)

reset_butt = Button(text= "Reset Timer", font= FONT_NAME, borderwidth= 0, command= reset_timer)
reset_butt.grid(row= 2, column= 2)

check_marks = Label(fg= CHECKMARK, bg= BACKGROUND)
check_marks.grid(column=1, row=3)

window.mainloop()