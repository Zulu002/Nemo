


from PyQt6 import QtCore, QtGui, QtWidgets

global user_data
import api
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.to = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ЯОператор")
        MainWindow.resize(530, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(4)
        self.splitter.setObjectName("splitter")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.splitter)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(
                _translate("MainWindow", "ЯОператор: Поддержка 1.0 ({0})".format(user_data['login'])))
            self.pushButton.setText(_translate("MainWindow", "Отправить"))
            self.pushButton_2.setText(_translate("MainWindow", "Добавить пользователя "))
            self.pushButton.clicked.connect(lambda x: ButtonCommand().push_go(self.lineEdit.text(), self.textBrowser))

            for i in api.API().get_now_answer():
                self.listWidget.addItem(str(i['id']))
            self.listWidget.currentRowChanged.connect(self.setToRow)

    def setToRow(self, alpha):
            self.to = self.listWidget.item(alpha).text()
            self.update_chat()

    def update_chat(self):
            if self.to is not None:
                print(self.to)
                self.textBrowser.clear()
                data = api.API().get_user_message(self.to)
                # print(data, '213213213')
                string_msg = ''
                for i in data:
                    string_msg = "({}) {}: {}".format(i["datetime"], i['id'], i['question'])
                    ButtonCommand().push_go(string_msg, self.textBrowser)

class ButtonCommand:
    def __init__(self):
        pass

    def push_go(self, text, wordarea):
        wordarea.append(text)

    def set_user(self, *args):
        print(args)