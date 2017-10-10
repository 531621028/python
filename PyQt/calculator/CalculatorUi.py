#coding:utf-8

from PyQt5 import QtGui,QtCore,QtWidgets
import sys
import Calculator
import logging

class MainUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.isCalculate = False
        self.result = 0.0

    def initUI(self):
        #self.setGeometry(100, 80, 270, 300)
        self.setWindowTitle('计算器')
        self.initInput()
        self.initBtnBox()


        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.input_Line)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
        self.show()

    def initInput(self):
        print('input')
        self.input_Line =   QtWidgets.QTextEdit()
        font = QtGui.QFont()
        font.setPointSize(25)
        self.input_Line.setFont(font)
        self.input_Line.setFixedSize(350,90)


    def initBtnBox(self):
        self.buttonBox = QtWidgets.QGroupBox()
        layout = QtWidgets.QGridLayout()
        names = ['Cls', 'Bck', '(', ')',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QtWidgets.QPushButton(name)
            button.clicked.connect(self.display)
            font = QtGui.QFont()
            font.setPointSize(20)
            button.setFont(font)
            layout.addWidget(button, *position)
        self.buttonBox.setLayout(layout)

    def display(self):
        sender = self.sender()
        if self.isCalculate:
            self.input_Line.clear()
            self.input_Line.setText(str(self.result))
        self.isCalculate = False
        if sender.text() == 'Close':
            self.close()
        elif sender.text() == 'Cls':
            self.input_Line.clear()
        elif sender.text() == 'Bck':
            text = self.input_Line.toPlainText()
            self.input_Line.setText(str(text)[0:-1])
        elif sender.text() == '=':
            text = self.input_Line.toPlainText()
            try:
                self.result = Calculator.calculate(str(text))
                self.input_Line.append(str(self.result))
                self.isCalculate = True
            except Exception as e:
                self.input_Line.clear()
                logging.warn('表达式格式不对')
        else:
            text = self.input_Line.toPlainText()
            self.input_Line.setText(text+sender.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())