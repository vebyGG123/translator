# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from translate import Translator as tl
from tkinter import messagebox


class Ui_Perevodchik(object):
    def setupUi(self, Perevodchik):
        Perevodchik.setObjectName("Perevodchik")
        Perevodchik.resize(537, 302)
        self.centralwidget = QtWidgets.QWidget(Perevodchik)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 183, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(-1, 70, 541, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(97, 97, 97);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 85, 85);")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(426, 184, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(188, 171, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(98, 98, 98);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Perevodchik.setCentralWidget(self.centralwidget)

        self.retranslateUi(Perevodchik)
        QtCore.QMetaObject.connectSlotsByName(Perevodchik)

    def retranslateUi(self, Perevodchik):
        _translate = QtCore.QCoreApplication.translate
        Perevodchik.setWindowTitle(_translate("Perevodchik", "MainWindow"))
        self.label.setText(_translate("Perevodchik", "Разработчик: Veby, TG: @vebytop"))
        self.comboBox.setItemText(0, _translate("Perevodchik", "Русский"))
        self.comboBox.setItemText(1, _translate("Perevodchik", "Английский"))
        self.textEdit.setHtml(_translate("Perevodchik", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Perevodchik", "                                        Напишите текст"))
        self.comboBox_2.setItemText(0, _translate("Perevodchik", "Английский"))
        self.comboBox_2.setItemText(1, _translate("Perevodchik", "Русский"))
        self.pushButton.setText(_translate("Perevodchik", "Перевести"))
        self.label_3.setText(_translate("Perevodchik", "Перевести с "))
        self.label_4.setText(_translate("Perevodchik", "на"))

        self.translit()


    def translit(self):
        self.pushButton.clicked.connect(self.main_perevod)


    def main_perevod(self):
        perevod_c = self.comboBox.currentText()
        perevod_po = self.comboBox_2.currentText()

        if perevod_c == perevod_po:
                messagebox.showinfo("Внимание!", "Выберите два разных языка!")
                

        if perevod_c == "Русский" and perevod_po == "Английский":
                perevod_slovo = self.textEdit.toPlainText()
                translate = tl(from_lang="ru", to_lang="en")
                translate_text = translate.translate(perevod_slovo)

                self.textEdit.setText(f"Перевод: {translate_text}")

        elif perevod_c == "Английский" and perevod_po == "Русский":
                perevod_slovo = self.textEdit.toPlainText()
                translate = tl(from_lang="en", to_lang="ru")
                translate_text = translate.translate(perevod_slovo)

                self.textEdit.setText(f"Перевод: {translate_text}")


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Perevodchik()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

