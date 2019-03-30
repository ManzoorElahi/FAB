# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FAB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import pandas as pd
import numpy as np
import benford_modified



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.startFAB = QtWidgets.QPushButton(self.centralwidget)
        self.startFAB.setObjectName("startFAB")
        self.gridLayout.addWidget(self.startFAB, 4, 2, 1, 1)
        self.outputImage = QtWidgets.QLabel(self.centralwidget)
        self.outputImage.setMinimumSize(QtCore.QSize(600, 600))
        self.outputImage.setFrameShape(QtWidgets.QFrame.Box)
        self.outputImage.setObjectName("outputImage")
        self.gridLayout.addWidget(self.outputImage, 6, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.pushButton.clicked.connect(self.file_open)
        self.startFAB.clicked.connect(self.showImage)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        
    def dialog_critical(self, s):
        dlg = QMessageBox(None)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()
        
    
       
    def file_open(self):
        
        fname,_ = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\',"CSV file (*.csv)")

        try:
            
            self.df = pd.read_csv(fname)

        except Exception as e:
            self.dialog_critical(str(e))

            
    
    def showImage(self):
        
        try:
            
            digit = int(self.comboBox.currentText())
            column_name = self.lineEdit.text()
            ds = self.df
            
            min_n = int(np.min(ds[column_name].astype(np.float64)))
            dec = len(str(min_n))
                        
            ben = benford_modified.first_digits(ds[column_name].astype(np.float64), digs=digit, 
                                                decimals=dec, show_plot=True)

            pixmap = QtGui.QPixmap('fab.png')
            myScaledPixmap = pixmap.scaled(self.outputImage.size())
            self.outputImage.setPixmap(myScaledPixmap)
            
        except Exception as e:
            self.dialog_critical(str(e))
            
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FAB - Benford\'s Law for Forensic Acounting"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.label_3.setText(_translate("MainWindow", "Select Digit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "Enter Column Name"))
        self.label.setText(_translate("MainWindow", "Open CSV File"))
        self.startFAB.setText(_translate("MainWindow", "Enter"))
        self.outputImage.setText(_translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    