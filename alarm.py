from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from threading import Thread
import threading
from pygame import mixer
from time import sleep

from PIL import ImageTk, Image

#color
bg_color = "#ffffff"
col1 = "#ff80ff"
col2 = "#00ffff"


window = Tk()
window.geometry("500x350")
window.title("Alarm Clock")
window.configure(bg=bg_color)

frame_line = Frame(window, width=500, height=10, bg=col1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=500, height=300, bg=bg_color)
frame_body.grid(row=1, column=0)

img = Image.open("alarm.png")
img.resize((200, 200))
img = ImageTk.PhotoImage(img)

alarm_img = Label(frame_body, height=200, image=img, bg=bg_color)
alarm_img.place(x=20, y=20)

name = Label(frame_body, text="Alarm clock", font="Courier 20 bold", bg=bg_color)
name.place(x=200, y=80)

hour = Label(frame_body, text="hour", font="Courier 12 bold", bg=bg_color, fg=col2)
hour.place(x=200, y=110)

minute = Label(frame_body, text="Minute", font="Courier 12 bold", bg=bg_color, fg=col2)
minute.place(x=280, y=110)

second = Label(frame_body, text="Second", font="Courier 12 bold", bg=bg_color, fg=col2)
second.place(x=360, y=110)

period = Label(frame_body, text="Period", font="Courier 12 bold", bg=bg_color, fg=col2)
period.place(x=430, y=110)


c_hour = Combobox(frame_body, font="Courier", width=2)
c_hour["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=202, y=130)

c_minute = Combobox(frame_body, font="Courier", width=2)
c_minute["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minute.current(0)
c_minute.place(x=282, y=130)

c_second = Combobox(frame_body, font="Courier", width=2)
c_second["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_second.current(0)
c_second.place(x=362, y=130)

c_perid = Combobox(frame_body, font="Courier", width=2)
c_perid["values"] = ("AM", "PM")
c_perid.current(0)
c_perid.place(x=432, y=130)

exitFlag = False
def activate_alarm():
    global t
    t = Thread(target=fire_alarm)
    t.start()
def turn_off():
    global exitFlag
    exitFlag = True

def deactivate_alarm():
    print("deactivate_alarm", selected.get())
    mixer.music.stop()

selected= IntVar()

rad1 = Radiobutton(frame_body, font="Courier 18 bold",value=1, bg=bg_color, text="Set", fg=col2, command=activate_alarm, variable=selected)
rad1.place(x = 222, y=180)


button1 = Button(frame_body, font="Courier 12 bold", bg=bg_color, text="Cancel", fg=col2, command=turn_off)
button1.place(x = 222, y=220)

def close():
     window.destroy()

button2 = Button(frame_body, font="Courier 12 bold", bg=bg_color, text="Close", fg=col2, command=close)
button2.place(x = 320, y=220)



def sound_alarm():
    mixer.music.load("alarm2.mp3")
    mixer.music.play()
    print(selected.get())

    selected.set(0)

    rad2 = Radiobutton(frame_body, font="Courier 18 bold",value=1, bg=bg_color, text="Turn Off", fg=col2, command=deactivate_alarm, variable=selected)
    rad2.place(x = 320, y=180)


def fire_alarm():
    while True:
        control = 1
        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_second = c_second.get()
        alarm_period = c_perid.get()
        alarm_period = str(alarm_period).upper()

        if exitFlag:
             break

        now = datetime.now()
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1 and alarm_hour == hour and alarm_minute == minute and alarm_second == second and alarm_period == period:
            print("time to break")
            sound_alarm()
        sleep(1)
mixer.init()

window.mainloop()
