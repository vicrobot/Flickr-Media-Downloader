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

To handel:- ConnectionError
"""

class Ui_FlickrDownloader(object):
    def setupUi(self, FlickrDownloader):
        FlickrDownloader.setObjectName("FlickrDownloader")
        FlickrDownloader.resize(815, 400)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        FlickrDownloader.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FlickrDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 70, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 100, 111, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 161, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 161, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 170, 481, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(32, 242, 471, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 280, 85, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(340, 310, 211, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 280, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(330, 80, 211, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 310, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 10, 141, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 20, 191, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(540, 40, 251, 321))
        self.graphicsView.setObjectName("graphicsView")
        FlickrDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FlickrDownloader)
        self.statusbar.setObjectName("statusbar")
        FlickrDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(FlickrDownloader)
        QtCore.QMetaObject.connectSlotsByName(FlickrDownloader)
        self.pushButton.clicked.connect(self.go)
        self.checkBox_3.clicked.connect(self.cb3)
        self.lineEdit_3.setText('search here (comma separated)')
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
        self.work_being_done = False
    def retranslateUi(self, FlickrDownloader):
        _translate = QtCore.QCoreApplication.translate
        FlickrDownloader.setWindowTitle(_translate("FlickrDownloader", "MainWindow"))
        self.label.setText(_translate("FlickrDownloader", "API Key"))
        self.label_2.setText(_translate("FlickrDownloader", "API Secret Key"))
        self.radioButton.setText(_translate("FlickrDownloader", "Search by user name"))
        self.radioButton_2.setText(_translate("FlickrDownloader", " Search by tags"))
        self.checkBox.setText(_translate("FlickrDownloader", "Images"))
        self.checkBox_2.setText(_translate("FlickrDownloader", "Other medias like videos"))
        self.pushButton.setText(_translate("FlickrDownloader", "Go"))
        self.checkBox_3.setText(_translate("FlickrDownloader", "Use previously used keys"))
        self.label_3.setText(_translate("FlickrDownloader", "Preview of image"))
    def cb3(self):
        if self.checkBox_3.checkState() == 2 and self.api_set == False:
            self.lineEdit.setText(self.dict_ids['id1'])
            self.lineEdit_2.setText(self.dict_ids['id2'])
            self.api_set = True
    def go(self):
        if self.work_being_done: return
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            #message here
            print('press radio buttons')
            return
        if self.checkBox_3.checkState() == 0 and not self.lineEdit.text().strip() + self.lineEdit_2.text().strip():
            #message Here
            print('give valid ids')
            return
        if not self.lineEdit_3.text().strip():
            #message Here
            print('give search terms')
            return
        if self.checkBox.checkState() == 0 and self.checkBox_2.checkState() == 0:
            #message here
            print(' please select type of media to download ')
            return
        if self.checkBox_3.checkState() == 2:
            self.id1 = self.dict_ids['id1']
            self.id2 = self.dict_ids['id2']
            self.lineEdit.setText(self.id1)
            self.lineEdit_2.setText(self.id2)
        else:
            self.id1 = self.lineEdit.text()
            self.id2 = self.lineEdit_2.text()
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
            self.work_being_done = True
            self.label_4.setText('Processing...')
            print('label setted') # debugging
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
                self.graphicsView, self.centralwidget, search_this, self.id1)
            else:
                k = searchnDownload(self.lineEdit_3.text(), flickr, 'name', self.progressBar, 
                self.graphicsView, self.centralwidget, None, self.id1)
            if k == 1: self.label_4.setText('Images Downloaded')
            elif k == 0: self.label_4.setText('No images found')
            os.chdir(self.main_dir)
            self.work_being_done = False
        """
        Scenes are visualized by graphicsView sort of objs.
        Size of graphics view:- (540, 40, 251, 321) (x, y, width, height)
        """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FlickrDownloader = QtWidgets.QMainWindow()
    ui = Ui_FlickrDownloader()
    ui.setupUi(FlickrDownloader)
    FlickrDownloader.show()
    sys.exit(app.exec_())
