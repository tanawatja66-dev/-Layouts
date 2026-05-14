import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    buttons = [
        ('Cls', 0, 0), ('Bck', 0, 1), # แถว 0
        ('7', 1, 0),   ('8', 1, 1),   ('9', 1, 2), ('/', 1, 3), # แถว 1
        ('4', 2, 0),   ('5', 2, 1),   ('6', 2, 2), ('*', 2, 3), # แถว 2
        ('1', 3, 0),   ('2', 3, 1),   ('3', 3, 2), ('-', 3, 3), # แถว 3
        ('0', 4, 0),   ('.', 4, 1),   ('=', 4, 2), ('+', 4, 3), # แถว 4
    ]

    for text, row, col in buttons:
        grid.addWidget(QPushButton(text), row, col)

    btn_close = QPushButton("Close")
    grid.addWidget(btn_close, 0, 2, 1, 2) 
    btn_close.clicked.connect(win.close)

    win.setLayout(grid)
    win.setWindowTitle("Calculator")
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    window()