from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

def win ():
    win = QMessageBox()
    win.setText("молодець правельно")
    win.exec_()

def loose ():
    loose = QMessageBox()
    loose.setText("неправельно")
    loose.exec_()

app = QApplication([])  #створюєм додаток
main_win = QWidget()
main_win.setWindowTitle("Конкурс від Crezy people")
main_win.resize(400,200)

question = QLabel("в якому році канал отримав'золоту кнопку'кнопку ютубу")

btn1 = QPushButton("2005")
btn2 = QPushButton("2010")
btn3 = QPushButton("2015")
btn4 = QPushButton("2020")

main_layout = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


main_layout = QVBoxLayout()
layoutH1.addWidget(question,alignment = Qt.AlignCenter)
layoutH2.addWidget(btn1,alignment = Qt.AlignCenter)
layoutH2.addWidget(btn2,alignment = Qt.AlignCenter)
layoutH3.addWidget(btn3,alignment = Qt.AlignCenter)
layoutH3.addWidget(btn4,alignment = Qt.AlignCenter)


main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

main_win.setLayout(main_layout)

btn1.clicked.connect(win)
btn2.clicked.connect(loose)
btn3.clicked.connect(loose)
btn4.clicked.connect(loose)

main_win.show()
app.exec_()