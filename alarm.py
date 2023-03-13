from tkinter.ttk import *
from tkinter import *

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
minutes = []
for i in range(60):
    i = str(i)
    minutes.append(i)
minutes = tuple(minutes)
c_minute = Combobox(frame_body, font="Courier", width=2)
c_minute["values"] = minutes
c_minute.current(0)
c_minute.place(x=282, y=130)

c_second = Combobox(frame_body, font="Courier", width=2)
c_second["values"] = minutes
c_second.current(0)
c_second.place(x=362, y=130)

c_perid = Combobox(frame_body, font="Courier", width=2)
c_perid["values"] = ("AM", "PM")
c_perid.current(0)
c_perid.place(x=432, y=130)

selected= IntVar()

rad1 = Radiobutton(frame_body, font="Courier 18 bold",value=1, bg=bg_color, text="Set", fg=col2)
rad1.place(x = 222, y=180)

window.mainloop()
