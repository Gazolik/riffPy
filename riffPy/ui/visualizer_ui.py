# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 433)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.visualizerBox_1 = QtWidgets.QGroupBox(Form)
        self.visualizerBox_1.setTitle("")
        self.visualizerBox_1.setObjectName("visualizerBox_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.visualizerBox_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtWidgets.QPushButton(self.visualizerBox_1)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileName = QtWidgets.QLabel(self.visualizerBox_1)
        self.fileName.setObjectName("fileName")
        self.verticalLayout.addWidget(self.fileName)
        self.fileView = QtWidgets.QTreeView(self.visualizerBox_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileView.sizePolicy().hasHeightForWidth())
        self.fileView.setSizePolicy(sizePolicy)
        self.fileView.setObjectName("fileView")
        self.verticalLayout.addWidget(self.fileView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chunkName = QtWidgets.QLabel(self.visualizerBox_1)
        self.chunkName.setObjectName("chunkName")
        self.verticalLayout_3.addWidget(self.chunkName)
        self.chunkView = QtWidgets.QTextBrowser(self.visualizerBox_1)
        self.chunkView.setObjectName("chunkView")
        self.verticalLayout_3.addWidget(self.chunkView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.fileView.raise_()
        self.chunkName.raise_()
        self.fileName.raise_()
        self.verticalLayout_4.addWidget(self.visualizerBox_1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadButton.setText(_translate("Form", "Load"))
        self.fileName.setText(_translate("Form", "TextLabel"))
        self.chunkName.setText(_translate("Form", "TextLabel"))

