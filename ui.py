# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Devpratim\Desktop\sna_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 481, 221))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 471, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choice1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.choice1.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.choice1.setFont(font)
        self.choice1.setChecked(True)
        self.choice1.setObjectName("choice1")
        self.verticalLayout.addWidget(self.choice1)
        self.choice2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.choice2.setFont(font)
        self.choice2.setObjectName("choice2")
        self.verticalLayout.addWidget(self.choice2)
        self.choice3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.choice3.setFont(font)
        self.choice3.setObjectName("choice3")
        self.verticalLayout.addWidget(self.choice3)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(480, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.input_tag = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_tag.setGeometry(QtCore.QRect(240, 260, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.input_tag.setFont(font)
        self.input_tag.setToolTip("")
        self.input_tag.setToolTipDuration(1)
        self.input_tag.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_tag.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_tag.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.input_tag.setPlainText("")
        self.input_tag.setPlaceholderText("")
        self.input_tag.setObjectName("input_tag")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 360, 631, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 240, 631, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input_tweet = QtWidgets.QSpinBox(self.centralwidget)
        self.input_tweet.setGeometry(QtCore.QRect(240, 310, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_tweet.setFont(font)
        self.input_tweet.setWhatsThis("")
        self.input_tweet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_tweet.setMaximum(3000)
        self.input_tweet.setSingleStep(10)
        self.input_tweet.setProperty("value", 10)
        self.input_tweet.setObjectName("input_tweet")
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(20, 380, 391, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progress.setFont(font)
        self.progress.setProperty("value", 0)
        self.progress.setTextVisible(False)
        self.progress.setOrientation(QtCore.Qt.Horizontal)
        self.progress.setObjectName("progress")
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setGeometry(QtCore.QRect(50, 460, 511, 301))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.display_label.setFont(font)
        self.display_label.setText("")
        self.display_label.setObjectName("display_label")
        self.neticon = QtWidgets.QLabel(self.centralwidget)
        self.neticon.setGeometry(QtCore.QRect(580, 10, 70, 70))
        self.neticon.setText("")
        self.neticon.setObjectName("neticon")
        self.netstatus = QtWidgets.QLabel(self.centralwidget)
        self.netstatus.setGeometry(QtCore.QRect(580, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.netstatus.setFont(font)
        self.netstatus.setText("")
        self.netstatus.setObjectName("netstatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "SEARCH TYPE"))
        self.choice1.setText(_translate("MainWindow", "Keyword / Tag Based"))
        self.choice2.setText(_translate("MainWindow", "Tweets to a person"))
        self.choice3.setText(_translate("MainWindow", "Tweets from a person"))
        self.search_button.setText(_translate("MainWindow", "SEARCH"))
        self.label.setText(_translate("MainWindow", "Enter Keyword / tag :"))
        self.label_2.setText(_translate("MainWindow", "Enter No. of Tweets :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

