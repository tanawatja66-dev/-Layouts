import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QLineEdit, QTextEdit, QVBoxLayout)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Review")
        self.resize(400, 300)

        form_layout = QFormLayout()

        self.input_title = QLineEdit()
        self.input_author = QLineEdit()
        self.input_review = QTextEdit()

        # 2. เพิ่มช่องลงในฟอร์ม
        form_layout.addRow("Title", self.input_title)
        form_layout.addRow("Author", self.input_author)
        form_layout.addRow("Review", self.input_review)

        self.input_title.textChanged.connect(self.update_window_title)
 
        self.input_author.textChanged.connect(self.update_review_text)

        self.setLayout(form_layout)

    def update_window_title(self, text):
        self.setWindowTitle(text)

    def update_review_text(self, text):
        self.input_review.setPlainText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())