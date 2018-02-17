# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QUrl
from PyQt5.QtWebKitWidgets import QWebView as Web
import datetime
from PARSER import Cenzor,ZelvRU,ZelvUA

from append_date import append_date
from MAP import Show_map
import sqlite3
import math

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1014, 664)
        dekstop = QtWidgets.QApplication.desktop()
        x = (dekstop.width() - Form.width()) // 2
        y = (dekstop.height() - Form.height() - 200) // 2
        Form.move(x,y)

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 831, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.browser = Web(self.frame)
        ur = QUrl("file:/home/myroslav/PycharmProjects/bakal/mymap.html")
        self.browser.load(ur)
        self.browser.setGeometry(QtCore.QRect(1, 1, 830, 400))
        self.browser.setObjectName("WebView")

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(840, 0, 171, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 8, 151, 20))
        self.label_5.setObjectName("label_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(6, 33, 161, 145))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(12, 6, 141, 20))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox.setGeometry(QtCore.QRect(8, 34, 93, 25))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_2.setGeometry(QtCore.QRect(8, 70, 93, 25))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_3.setGeometry(QtCore.QRect(8, 106, 93, 25))
        self.checkBox_3.setObjectName("checkBox_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(5, 184, 161, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(9, 1, 131, 20))
        self.label_3.setObjectName("label_3")

        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_4)
        self.dateEdit_3.setGeometry(QtCore.QRect(33, 25, 121, 32))
        self.dateEdit_3.setObjectName("dateEdit_3")
        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        self.dateEdit_3.setDisplayFormat("dd - MM - yyyy")
        self.dateEdit_3.setDate(QtCore.QDate(b, b1, b2))
        self.dateEdit_3.setDateRange(QtCore.QDate(2017,1,1),QtCore.QDate(b, b1, b2))

        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_4)
        self.dateEdit_4.setGeometry(QtCore.QRect(34, 61, 121, 32))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.dateEdit_4.setDisplayFormat("dd - MM - yyyy")
        self.dateEdit_4.setDate(QtCore.QDate(b, b1, b2))
        self.dateEdit_4.setDateRange(QtCore.QDate(2017,1,1),QtCore.QDate(b, b1, b2))

        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(10, 32, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 61, 31, 31))
        self.label_2.setObjectName("label_2")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.dateEdit_3.raise_()
        self.dateEdit_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(5, 292, 161, 101))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setGeometry(QtCore.QRect(5, 68, 72, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setGeometry(QtCore.QRect(83, 67, 72, 28))
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(5, 6, 151, 28))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Event_Refresh_DB)
        self.pushButton.clicked.connect(self.Event_Progress_Bar)

        self.progressBar = QtWidgets.QProgressBar(self.frame_6)
        self.progressBar.setGeometry(QtCore.QRect(4, 40, 151, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")

        self.pushButton.raise_()
        self.progressBar.raise_()
        self.pushButton_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.progressBar.raise_()

        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 410, 1011, 251))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 974, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 7, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #self.gridLayout_2.setRowMinimumHeight(0,100)

        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1010, 250))
        self.scrollArea.setObjectName("scrollArea")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.pushButton_2.clicked.connect(self.create_text)
        self.pushButton_3.clicked.connect(self.clear_text)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.retranslateUi(Form)
        # self.textEdit_5.mouseDoubleClickEvent = self.web
    def create_text(self):
        self.TextEditContainer = []

        dat = self.Current_date()
        datt = []
        for i in range(dat.__len__()):
            if dat[i][-2] == '0':
                datt.append([dat[i][-1] + dat[i][4:6] + dat[i][2:4] + '0000',
                             dat[i][-1] + dat[i][4:6] + dat[i][2:4] + '2460'])
            else:
                datt.append([dat[i][6:8] + dat[i][4:6] + dat[i][2:4] + '0000',
                             dat[i][6:8] + dat[i][4:6] + dat[i][2:4] + '2460'])

        self.con = sqlite3.connect('All_Pars_BD.db3')
        self.cur = self.con.cursor()
        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE name='main'").fetchone()
        if not dd: print("Базу даних з вхідним текстом не знайдено")

        Cenzor_status = self.checkBox.checkState()
        ZelvRU_status = self.checkBox_2.checkState()
        ZelvUA_status = self.checkBox_3.checkState()

        All = [Cenzor_status,ZelvRU_status,ZelvUA_status]
        tx = []


        if All ==[0,2,2] :
            self.domain = ['ЗелвРУ','ЗелвЮА']
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' or domain = '{1}' and date BETWEEN {2} and {3} ORDER BY date".format(
                        self.domain[0],self.domain[1], datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]

        if All ==[2,0,2] :
            self.domain = ['ЗелвЮА','Цензор']
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' or domain = '{1}' and date BETWEEN {2} and {3} ORDER BY date".format(
                        self.domain[0],self.domain[1], datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]
        if All ==[2,2,0] :
            self.domain = ['ЗелвРУ','Цензор']
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' or domain = '{1}' and date BETWEEN {2} and {3} ORDER BY date".format(
                        self.domain[0],self.domain[1], datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]

        if All ==[2,2,2] :
            self.domain = ['ЗелвЮА','ЗелвРУ','Цензор']
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' or domain = '{1}' or domain = '{2}'and date BETWEEN {3} and {4} ORDER BY date".format(
                        self.domain[0],self.domain[1],self.domain[2], datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]

        if All ==[0,0,2] :
            self.domain = 'ЗелвЮА'
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' and date BETWEEN {1} and {2} ORDER BY date".format(
                        self.domain, datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]

        if All == [0, 2, 0]:
            self.domain = 'ЗелвРУ'
            for i in range(datt.__len__()):
                self.cur.execute(
                    "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' and date BETWEEN {1} and {2} ORDER BY date".format(
                        self.domain, datt[i][0], datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [list(tx[i]) for i in range(tx.__len__())]

        if All == [2, 0, 0]:
            self.domain = 'Цензор'
            for i in range(datt.__len__()):
                self.cur.execute(
                "SELECT title,date,body,domain,link FROM main WHERE domain = '{0}' and date BETWEEN {1} and {2} ORDER BY date".format(self.domain,datt[i][0],datt[i][1]))
                tx += self.cur.fetchall()
            self.con.close()
            tx = [ list(tx[i]) for i in range(tx.__len__())]

        if All == [0, 0, 0]:
            print('Виберіть ресурс')

        for i in range(tx.__len__()):
            tx[i][0] = str(tx[i][0]).replace('\xa0','')
            #tx[i] = '\n\n'.join(tx[i])
            #print(tx[i])

        row = math.ceil(len(tx)/3)
        i=0
        for x in range(row):
            for y in range(3):
                self.TextEditContainer.append(QtWidgets.QTextEdit(self.scrollAreaWidgetContents))
                self.TextEditContainer[-1].setObjectName("textEdit{0}".format(i))
                self.TextEditContainer[-1].setFixedSize(320, 300)
                self.TextEditContainer[-1].setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
                self.TextEditContainer[-1].setFont(QtGui.QFont("Calibri",9, QtGui.QFont.Bold))
                #self.TextEditContainer[-1].setText('\n\n\n')
                try:
                    t = str(tx[i][1])
                    t = "{0}.{1} о {2}:{3}".format(t[:-8], t[-8:-6], t[-4:-2], t[-2:])
                except: continue

                self.TextEditContainer[-1].setText('   {0}\t    {1}\n   {2}\n\n   {3}'.format(t,tx[i][3],tx[i][0],tx[i][2]))

                self.TextEditContainer[-1].mouseDoubleClickEvent = lambda event,url = tx[i][4]:self.web(event,url)#tx[i][4])
                self.gridLayout_2.addWidget(self.TextEditContainer[-1], x, y, 1, 1)
                i += 1

    def clear_text(self):
        [self.TextEditContainer[i].deleteLater() for i in range(self.TextEditContainer.__len__())]
    def web(self, event,url):

        import webbrowser
        webbrowser.open(url)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Панель налаштування"))
        self.label_4.setText(_translate("Form", "Новинний ресурс"))
        self.checkBox.setText(_translate("Form", "Cenzor"))
        self.checkBox_2.setText(_translate("Form", "Zelv RU"))
        self.checkBox_3.setText(_translate("Form", "Zelv UA"))
        self.label_3.setText(_translate("Form", "Дата"))
        self.label.setText(_translate("Form", "З"))
        self.label_2.setText(_translate("Form", "По"))
        self.pushButton_2.setText(_translate("Form", "Вивід"))
        self.pushButton_3.setText(_translate("Form", "Очистка"))
        self.pushButton.setText(_translate("Form", "Оновлення БД"))
        self.progressBar.setFormat(_translate("Form", "%p%"))

    def Current_date(self):
        date = [self.dateEdit_3.date(), self.dateEdit_4.date()]
        date = [str(i)[18:].replace("(", '').replace(")", '').replace(" ", '').split(',') for i in date]
        for j in range(date.__len__()):
            for i in range(date[0].__len__()):
                if len(date[j][i]) == 1:
                    date[j][i] = "0" + date[j][i]
        start = ''.join(date[0])
        end = ''.join(date[1])
        dat = append_date(start, end)
        if dat == 'Помилка вводу':
            print("помилка вводу дати")
        return dat

    #@QtCore.pyqtSlot()

    def Event_Refresh_DB(self):

        dat = self.Current_date()
        Cenzor_status = self.checkBox.checkState()
        ZevlRU_status = self.checkBox_2.checkState()
        ZelvUA_status = self.checkBox_3.checkState()


        if ZelvUA_status == 2:
            for i in range(dat.__len__()):
                dT = '{2}{1}{0}'.format(dat[i][:4],dat[i][4:6],dat[i][-2:])
                refr = ZelvUA().write_bd(dT)

        if ZevlRU_status == 2:
            for i in range(dat.__len__()):
                dT = '{2}{1}{0}'.format(dat[i][:4],dat[i][4:6],dat[i][-2:])
                refr = ZelvRU().write_bd(dT)

        if Cenzor_status == 2:
            for i in range(dat.__len__()):
                dT = '{0}-{1}-{2}'.format(dat[i][:4],dat[i][4:6],dat[i][-2:])
                refr = Cenzor().write_bd(dT)


    #@QtCore.pyqtSlot()
    def Event_Progress_Bar(self):

        active = Show_map('AIzaSyCOZ0t8PvYAnCPM5s6ZCiOngYr25C_oUy4')
        ur = QUrl("file:///home/myroslav/PycharmProjects/bakal/mymap.html")
        self.browser.load(ur)

        from PyQt5.QtCore import QBasicTimer
        self.timer = QBasicTimer()
        self.step = 0

        if self.timer.isActive():
                    self.timer.stop()
        else:
                    self.timer.start(100, self)

    def timerEvent(self, e):
            if self.step >= 100:
                self.timer.stop()
                return

            self.step = self.step + 1
            self.progressBar.setValue(self.step)










