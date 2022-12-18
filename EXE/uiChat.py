


from PyQt6 import QtCore, QtGui, QtWidgets

global user_data
import api
import threading


class Ui_MainWindow:

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
            self.pushButton.clicked.connect(lambda x: self.push_go(self.lineEdit.text()))
            self.pushButton_2.clicked.connect(lambda x: self.set_user("trtrt"))

            self.update_user_list()

            self.listWidget.currentRowChanged.connect(self.setToRow)

    def update_user_list(self):
        for i in api.API().get_now_answer():
            self.listWidget.addItem(str(i['id']))
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
                how_send = i['operator_id'] if i.get('operator_id') is not None else i['id']
                string_msg = "({}) {}: {}".format(i["datetime"], how_send, i['question'])
                self.textBrowser.append(string_msg)

    def push_go(self, text):
        self.textBrowser.append(text)
        api.API().send_message_user(user_data['id'], int(self.to), text)
        self.update_chat()
        self.lineEdit.clear()

    def set_user(self, *args):
        print(args)