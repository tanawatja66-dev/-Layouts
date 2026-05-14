import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.resize(400, 200)

        v_layout = QVBoxLayout()

        v_layout.addStretch(1)

        h_layout = QHBoxLayout()
        
        h_layout.addStretch(1) 

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.show_message) 
        h_layout.addWidget(btn_ok)

        # 4. สร้างปุ่ม Cancel
        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.close)   
        h_layout.addWidget(btn_cancel)

    
        v_layout.addLayout(h_layout)

       
        self.setLayout(v_layout)

    def show_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("คุณกดปุ่ม OK เรียบร้อยแล้วเด้อ!")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())