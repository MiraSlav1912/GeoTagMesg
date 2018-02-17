from PyQt5 import QtCore, QtWidgets, QtGui
from GUI import Ui_Form


class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self,parent = None)
        self.setupUi(self)
        pass

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    u = MyWindow()
    u.show()
    sys.exit(app.exec_())