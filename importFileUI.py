# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importFileUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_importFileDialog(object):
    def setupUi(self, importFileDialog):
        importFileDialog.setObjectName("importFileDialog")
        importFileDialog.resize(637, 487)
        self.verticalLayout = QtWidgets.QVBoxLayout(importFileDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(importFileDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.A_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_path.sizePolicy().hasHeightForWidth())
        self.A_path.setSizePolicy(sizePolicy)
        self.A_path.setObjectName("A_path")
        self.gridLayout.addWidget(self.A_path, 0, 1, 1, 1)
        self.A_pushButton = QtWidgets.QPushButton(self.widget)
        self.A_pushButton.setObjectName("A_pushButton")
        self.gridLayout.addWidget(self.A_pushButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.B_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_path.sizePolicy().hasHeightForWidth())
        self.B_path.setSizePolicy(sizePolicy)
        self.B_path.setObjectName("B_path")
        self.gridLayout.addWidget(self.B_path, 1, 1, 1, 1)
        self.B_pushButton = QtWidgets.QPushButton(self.widget)
        self.B_pushButton.setObjectName("B_pushButton")
        self.gridLayout.addWidget(self.B_pushButton, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.zhuhu_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zhuhu_path.sizePolicy().hasHeightForWidth())
        self.zhuhu_path.setSizePolicy(sizePolicy)
        self.zhuhu_path.setObjectName("zhuhu_path")
        self.gridLayout.addWidget(self.zhuhu_path, 2, 1, 1, 1)
        self.zhuhu_pushButton = QtWidgets.QPushButton(self.widget)
        self.zhuhu_pushButton.setObjectName("zhuhu_pushButton")
        self.gridLayout.addWidget(self.zhuhu_pushButton, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.zhuzhai_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zhuzhai_path.sizePolicy().hasHeightForWidth())
        self.zhuzhai_path.setSizePolicy(sizePolicy)
        self.zhuzhai_path.setObjectName("zhuzhai_path")
        self.gridLayout.addWidget(self.zhuzhai_path, 3, 1, 1, 1)
        self.zhuzhai_pushButton = QtWidgets.QPushButton(self.widget)
        self.zhuzhai_pushButton.setObjectName("zhuzhai_pushButton")
        self.gridLayout.addWidget(self.zhuzhai_pushButton, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.xiaoqu_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xiaoqu_path.sizePolicy().hasHeightForWidth())
        self.xiaoqu_path.setSizePolicy(sizePolicy)
        self.xiaoqu_path.setObjectName("xiaoqu_path")
        self.gridLayout.addWidget(self.xiaoqu_path, 4, 1, 1, 1)
        self.xiaoqu_pushButton = QtWidgets.QPushButton(self.widget)
        self.xiaoqu_pushButton.setObjectName("xiaoqu_pushButton")
        self.gridLayout.addWidget(self.xiaoqu_pushButton, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.zy_path = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zy_path.sizePolicy().hasHeightForWidth())
        self.zy_path.setSizePolicy(sizePolicy)
        self.zy_path.setObjectName("zy_path")
        self.gridLayout.addWidget(self.zy_path, 5, 1, 1, 1)
        self.zy_pushButton = QtWidgets.QPushButton(self.widget)
        self.zy_pushButton.setObjectName("zy_pushButton")
        self.gridLayout.addWidget(self.zy_pushButton, 5, 2, 1, 1)
        # self.label_7 = QtWidgets.QLabel(self.widget)
        # self.label_7.setObjectName("label_7")
        # self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        # self.codes_path = QtWidgets.QLineEdit(self.widget)
        # self.codes_path.setObjectName("codes_path")
        # self.gridLayout.addWidget(self.codes_path, 6, 1, 1, 1)
        # self.codes_pushButton = QtWidgets.QPushButton(self.widget)
        # self.codes_pushButton.setObjectName("codes_pushButton")
        # self.gridLayout.addWidget(self.codes_pushButton, 6, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(importFileDialog)
        self.buttonBox.accepted.connect(importFileDialog.accept)
        self.buttonBox.rejected.connect(importFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(importFileDialog)

    def retranslateUi(self, importFileDialog):
        _translate = QtCore.QCoreApplication.translate
        importFileDialog.setWindowTitle(_translate("importFileDialog", "导入相关文件"))
        self.groupBox.setTitle(_translate("importFileDialog", "请选择对应文件路径："))
        self.label.setText(_translate("importFileDialog", "A表："))
        self.A_pushButton.setText(_translate("importFileDialog", "浏览"))
        self.label_2.setText(_translate("importFileDialog", "B表："))
        self.B_pushButton.setText(_translate("importFileDialog", "浏览"))
        self.label_4.setText(_translate("importFileDialog", "住户表："))
        self.zhuhu_pushButton.setText(_translate("importFileDialog", "浏览"))
        self.label_5.setText(_translate("importFileDialog", "住宅表："))
        self.zhuzhai_pushButton.setText(_translate("importFileDialog", "浏览"))
        self.label_3.setText(_translate("importFileDialog", "小区名录："))
        self.xiaoqu_pushButton.setText(_translate("importFileDialog", "浏览"))
        self.label_6.setText(_translate("importFileDialog", "账页表："))
        self.zy_pushButton.setText(_translate("importFileDialog", "浏览"))
        # self.label_7.setText(_translate("importFileDialog", "编码手册："))
        # self.codes_pushButton.setText(_translate("importFileDialog", "浏览"))

