import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,QHBoxLayout, QGridLayout, QPushButton, QLineEdit)
from PySide6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(350, 400) 

        main_layout = QVBoxLayout()

        self.display = QLineEdit("0")
        self.display.setAlignment(Qt.AlignRight) 
        self.display.setReadOnly(True)           
        self.display.setFixedHeight(50)         
        self.display.setStyleSheet("font-size: 20px;") 
        main_layout.addWidget(self.display)

        row1_layout = QHBoxLayout()
        btn_back = QPushButton("Backspace")
        btn_clear = QPushButton("Clear")
        btn_clear_all = QPushButton("Clear All")
        
        row1_layout.addWidget(btn_back)
        row1_layout.addWidget(btn_clear)
        row1_layout.addWidget(btn_clear_all)
        main_layout.addLayout(row1_layout)

        grid_layout = QGridLayout()
        
        buttons = [
            ('MC', 0, 0), ('7', 0, 1), ('8', 0, 2), ('9', 0, 3), ('/', 0, 4), ('Sqrt', 0, 5),
            ('MR', 1, 0), ('4', 1, 1), ('5', 1, 2), ('6', 1, 3), ('*', 1, 4), ('x²', 1, 5),
            ('MS', 2, 0), ('1', 2, 1), ('2', 2, 2), ('3', 2, 3), ('-', 2, 4), ('1/x', 2, 5),
            ('M+', 3, 0), ('0', 3, 1), ('.', 3, 2), ('±', 3, 3), ('+', 3, 4), ('=', 3, 5),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(45, 45) 
            grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())