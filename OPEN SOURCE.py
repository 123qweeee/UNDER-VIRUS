import time
import os
from tkinter import Tk, Label, Button, Frame

def countdown_and_shutdown():
    # Удаляем все кнопки перед началом таймера
    for widget in frame.winfo_children():
        widget.destroy()

    label.config(text="Самоуничтожение через 3...", font=("Arial", 40))
    root.update()
    time.sleep(1)
    
    label.config(text="Самоуничтожение через 2...")
    root.update()
    time.sleep(1)
    
    label.config(text="Самоуничтожение через 1...")
    root.update()
    time.sleep(1)
    
    os.system("shutdown /s /t 1")  # Выключение ПК

def next_question(question_text, answers, command):
    global label
    label.config(text=question_text)
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    for answer in answers:
        Button(frame, text=answer, font=("Arial", 20), command=command).pack()

def question_3():
    next_question("Любишь школу?", ["Нет", "Нет"], countdown_and_shutdown)

def question_2():
    next_question("Скачивал когда-либо вирусы?", ["Да", "Да"], question_3)

def start_quiz():
    start_button.destroy()  # Удаляем кнопку "НАЧАТЬ"
    next_question("СОСАЛ?", ["Да", "Да"], question_2)

root = Tk()
root.attributes("-fullscreen", True)  # Полный экран
root.attributes("-topmost", True)  # Поверх всех окон
root.protocol("WM_DELETE_WINDOW", lambda: None)  # Блокируем закрытие

label = Label(root, text="Нажми, чтобы начать", font=("Arial", 30))
label.pack(pady=50)

frame = Frame(root)
frame.pack()

start_button = Button(root, text="НАЧАТЬ", font=("Arial", 25), command=start_quiz)
start_button.pack(pady=20)

root.mainloop()
