# -*- coding: utf-8 -*-
#! usr/bin/env python3
from defs import *
import faulthandler
faulthandler.enable()

"""
To dos:-

Folder choice.
broad search, or narrow in tags

per_page images, fading of image and video checkbox when user_name radio button is clicked.
In image preview, maintain image raio. For that first search method for getting information about the image width and height.(dimensions)

lineEdit for general text in tags mode.

make a reset function and pause function
Many things like progress bar etc's handlings would be done by that.

imgc not working when app quited from cross icon.

Frequent same error:-
QObject: Cannot create children for a parent that is in a different thread.
(Parent is QWidget(0x556a9222fef0), parent's thread is QThread(0x556a9235ffd0), current thread is multithread(0x556a92b10f10)
QObject::killTimer: Timers cannot be stopped from another thread
"""

class Ui_FlickrDownloader(object):
    def setupUi(self, FlickrDownloader):
        FlickrDownloader.setObjectName("FlickrDownloader")
        FlickrDownloader.resize(817, 556)
        FlickrDownloader.setMinimumSize(QtCore.QSize(817, 556))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        FlickrDownloader.setFont(font)
        FlickrDownloader.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.centralwidget = QtWidgets.QWidget(FlickrDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(500)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 6, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStatusTip("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(48, 255, 113);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 7, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 6, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 4, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("background-color: rgb(41, 180, 255);\n"
"background-color: rgb(39, 89, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout.addWidget(self.line_7)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 200))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 9, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 2, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 2, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        FlickrDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FlickrDownloader)
        self.statusbar.setObjectName("statusbar")
        FlickrDownloader.setStatusBar(self.statusbar)
        preview('nologo.png', self.label_5)
        message(' :) ', self.label_4)

        self.retranslateUi(FlickrDownloader)
        QtCore.QMetaObject.connectSlotsByName(FlickrDownloader)
        self.pushButton.clicked.connect(self.go)
        self.checkBox_3.clicked.connect(self.cb3)
        self.main_dir = os.getcwd()
        if not os.path.exists('logs'): self.checkBox_3.setDisabled(True)
        else:
            self.api_set = False
            try:
                with open('logs', 'r') as  var:
                    self.lines = [i.rstrip() for i in var.readlines() if len(i) ]
            except FileNotFoundError:
                with open('logs', 'w+') as  var:
                    self.lines = []
            self.dict_ids = {}
            #ids_handeling
            id1_set, id2_set = 0, 0
            for line in self.lines:
                if 'id1' in line:
                    self.dict_ids['id1'] = ''.join(line.split(' ')[1:])
                    id1_set = 1
                if 'id2' in line:
                    self.dict_ids['id2'] = ''.join(line.split(' ')[1:])
                    id2_set = 1
            if not id1_set or not id2_set: self.checkBox_3.setDisabled(True)
    def retranslateUi(self, FlickrDownloader):
        _translate = QtCore.QCoreApplication.translate
        FlickrDownloader.setWindowTitle(_translate("FlickrDownloader", "Flickr Media Downloader"))
        self.label_6.setText(_translate("FlickrDownloader", "Image Counts ->"))
        self.checkBox_3.setText(_translate("FlickrDownloader", "Use previously used keys"))
        self.label.setText(_translate("FlickrDownloader", "API Key"))
        self.label_2.setText(_translate("FlickrDownloader", "API Secret Key"))
        self.lineEdit_3.setPlaceholderText(_translate("FlickrDownloader", "Search Here ( comma seperated if tags search )"))
        self.radioButton.setText(_translate("FlickrDownloader", "Search by user name"))
        self.radioButton_2.setText(_translate("FlickrDownloader", " Search by tags"))
        self.pushButton.setText(_translate("FlickrDownloader", "Go"))
        self.checkBox_2.setText(_translate("FlickrDownloader", "Other media like videos etc"))
        self.checkBox.setText(_translate("FlickrDownloader", "Images"))
        self.label_3.setText(_translate("FlickrDownloader", "Image Preview"))
    def cb3(self):
        if self.checkBox_3.checkState() == 2 and self.api_set == False:
            self.lineEdit.setText(self.dict_ids['id1'])
            self.lineEdit_2.setText(self.dict_ids['id2'])
            self.api_set = True
    def go(self):
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            #message here
            message('select search criteria ', self.label_4)
            return
        if self.checkBox_3.checkState() == 0 and not self.lineEdit.text().strip() + self.lineEdit_2.text().strip():
            #message Here
            message('give valid ids', self.label_4)
            return
        if not self.lineEdit_3.text().strip():
            #message Here
            message('give search terms', self.label_4)
            return
        if self.checkBox.checkState() == 0 and self.checkBox_2.checkState() == 0:
            #message here
            message(' please select type of \nmedia to download ', self.label_4)
            return
        if self.checkBox_3.checkState() == 2:
            self.id1 = self.dict_ids['id1']
            self.id2 = self.dict_ids['id2']
            self.lineEdit.setText(self.id1)
            self.lineEdit_2.setText(self.id2)
        else:
            self.id1 = self.lineEdit.text()
            self.id2 = self.lineEdit_2.text()
        try:
            if not checkIds(self.id1, self.id2):
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.checkBox_3.setChecked(False)
                self.api_set = False
                self.label_4.setText('Wrong Keys!! Try Again')
                return
            else:
                with open('logs', 'w+') as var:
                    var.writelines(['id1 {}\n'.format(self.id1), 'id2 {}'.format(self.id2)])
                self.tag = self.radioButton_2.isChecked()
                self.name = self.radioButton.isChecked()
                self.pushButton.setDisabled(True)
                self.label_7.setStyleSheet("background-color: rgb(255, 0, 255);")
                self.label_8.setStyleSheet("background-color: rgb(41, 180, 255);\n"
    "background-color: rgb(39, 89, 255);")
                self.label_4.setText('Processing...')
                caller(self.main_runner)
                os.chdir(self.main_dir)
        except NetworkError: message('Network Error !!\n Try Again', self.label_4)

        """
        (540, 40, 251, 321) -> (x, y, width, height)
        """
    def main_runner(self):
        global flickr
        flickr=flickrapi.FlickrAPI(self.id1, self.id2)
        flickr_api.set_keys(api_key = self.id1, api_secret = self.id2)
        if self.checkBox.checkState() == 2 and self.checkBox_2.checkState() == 2:
            search_this = 'both'
        elif self.checkBox.checkState() == 2 and self.checkBox_2.checkState() == 0:
            search_this = 'images'
        elif self.checkBox.checkState() == 0 and self.checkBox_2.checkState() == 2:
            search_this = 'others'
        if self.tag:
            k = searchnDownload(self.lineEdit_3.text(), flickr, 'tags', self.progressBar,
            [self.label_5, self.label_7, self.label_8], self.centralwidget, self.spinBox, search_this, self.id1)
            if k == 1: self.label_4.setText('Images Downloaded')
            elif k == 0: self.label_4.setText('No images found')
        else:
            try:
                k = searchnDownload(self.lineEdit_3.text(), flickr, 'name', self.progressBar,
                [self.label_5, self.label_7, self.label_8], self.centralwidget, self.spinBox, None, self.id1)
                if k == 1: self.label_4.setText('Images Downloaded')
                elif k == 0: self.label_4.setText('No images found')
            except NoUserFound:
                message('User Name Invalid !!', self.label_4)
        self.pushButton.setDisabled(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FlickrDownloader = QtWidgets.QMainWindow()
    ui = Ui_FlickrDownloader()
    ui.setupUi(FlickrDownloader)
    FlickrDownloader.show()
    sys.exit(app.exec_())
