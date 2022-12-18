import time

from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

global user_data
import api
import threading
import uiAdmin
class Ui_MainWindow:
    signal_incomingText = QtCore.pyqtSignal(str)
    def setupUi(self, MainWindow):

        self.to = None
        self.MainWin = MainWindow
        self.MainWin.setObjectName("ЯОператор")
        self.MainWin.resize(534, 316)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        if user_data['role'] == 'admin':
            self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4.setMaximumSize(QtCore.QSize(250, 16777215))
            self.pushButton_4.setObjectName("pushButton_4")
            self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        # self.thread = Worker()
        # self.thread.signal.connect(self.update_chat)
        # thr = threading.Thread(target=self.thread.thread, daemon=True)
        # thr.start()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "ЯОператор: Поддержка 1.0 ({0})".format(user_data['login'])))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_2.setText(_translate("MainWindow", "закрыть вопрос"))
        self.pushButton_3.setText(_translate("MainWindow", "обновить пользователей"))
        if user_data['role'] == 'admin':
            self.pushButton_4.setText(_translate("MainWindow", "добавить пользователей"))
        self.pushButton.clicked.connect(lambda x: self.push_go(self.lineEdit.text()))
        self.pushButton_2.clicked.connect(lambda x: self.close_quest())
        self.pushButton_3.clicked.connect(lambda x: self.update_user_list())
        if user_data['role'] == 'admin':
            self.pushButton_4.clicked.connect(lambda x: self.show_admin_menu())

        self.update_user_list()

        self.listWidget.currentRowChanged.connect(self.setToRow)

    def close_quest(self):
        api.API().close_quest(self.to)
        self.update_user_list()

    def update_user_list(self):
        self.listWidget.clear()
        for i in api.API().get_now_answer():
            self.listWidget.addItem(str(i['id']))

    def show_admin_menu(self):

        ui = uiAdmin.Ui_MainWindow()
        ui.setupUi(self.MainWin)
        self.MainWin.show()


    def setToRow(self, alpha):
        if self.listWidget.item(alpha) is not None:
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

    def signal_udpate(self, *args):
        while True:
            self.signal_incomingText.emit(None)
            time.sleep(1)


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        result = self.fn(*self.args, **self.kwargs)

        self.signals.finished.emit()  # Done