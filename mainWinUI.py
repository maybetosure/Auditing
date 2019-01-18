# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWinUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1493, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(251, 251, 251)")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.functionPanel = QtWidgets.QWidget(self.widget_2)
        self.functionPanel.setStyleSheet("background-color:rgb(238, 238, 238)")
        self.functionPanel.setObjectName("functionPanel")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.functionPanel)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.functionPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_check = QtWidgets.QWidget()
        self.tab_check.setObjectName("tab_check")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_check)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.tab_check)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.importTable = QtWidgets.QPushButton(self.widget_4)
        self.importTable.setStyleSheet("")
        self.importTable.setObjectName("importTable")
        self.horizontalLayout_6.addWidget(self.importTable)
        self.questionCheck = QtWidgets.QPushButton(self.widget_4)
        self.questionCheck.setObjectName("questionCheck")
        self.horizontalLayout_6.addWidget(self.questionCheck)
        self.zyCheck = QtWidgets.QPushButton(self.widget_4)
        self.zyCheck.setObjectName("zyCheck")
        self.horizontalLayout_6.addWidget(self.zyCheck)
        # self.IndepentCheck = QtWidgets.QPushButton(self.widget_4)
        # self.IndepentCheck.setObjectName("IndepentCheck")
        # self.horizontalLayout_6.addWidget(self.IndepentCheck)
        # self.pushButton = QtWidgets.QPushButton(self.widget_4)
        # self.pushButton.setObjectName("pushButton")
        # self.horizontalLayout_6.addWidget(self.pushButton)
        # self.ducplictCheck = QtWidgets.QPushButton(self.widget_4)
        # self.ducplictCheck.setObjectName("ducplictCheck")
        # self.horizontalLayout_6.addWidget(self.ducplictCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.tabWidget.addTab(self.tab_check, "")
        self.tab_zy = QtWidgets.QWidget()
        self.tab_zy.setObjectName("tab_zy")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_zy)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.function_pannel = QtWidgets.QWidget(self.tab_zy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.function_pannel.sizePolicy().hasHeightForWidth())
        self.function_pannel.setSizePolicy(sizePolicy)
        self.function_pannel.setObjectName("function_pannel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_pannel)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_townList = QtWidgets.QPushButton(self.function_pannel)
        self.import_townList.setObjectName("import_townList")
        self.horizontalLayout.addWidget(self.import_townList)
        self.open_tableA = QtWidgets.QPushButton(self.function_pannel)
        self.open_tableA.setObjectName("open_tableA")
        self.horizontalLayout.addWidget(self.open_tableA)
        self.open_zy = QtWidgets.QPushButton(self.function_pannel)
        self.open_zy.setObjectName("open_zy")
        self.horizontalLayout.addWidget(self.open_zy)
        self.label = QtWidgets.QLabel(self.function_pannel)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xz_comboBox = QtWidgets.QComboBox(self.function_pannel)
        self.xz_comboBox.setEditable(False)
        self.xz_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.xz_comboBox.setObjectName("xz_comboBox")
        self.horizontalLayout.addWidget(self.xz_comboBox)
        self.label_2 = QtWidgets.QLabel(self.function_pannel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.xq_comboBox = QtWidgets.QComboBox(self.function_pannel)
        self.xq_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.xq_comboBox.setObjectName("xq_comboBox")
        self.horizontalLayout.addWidget(self.xq_comboBox)
        self.generateTz = QtWidgets.QPushButton(self.function_pannel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateTz.sizePolicy().hasHeightForWidth())
        self.generateTz.setSizePolicy(sizePolicy)
        self.generateTz.setObjectName("generateTz")
        self.horizontalLayout.addWidget(self.generateTz)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.export_taizhang = QtWidgets.QPushButton(self.function_pannel)
        self.export_taizhang.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.export_taizhang.setObjectName("export_taizhang")
        self.horizontalLayout.addWidget(self.export_taizhang)
        self.verticalLayout_5.addWidget(self.function_pannel)
        self.tabWidget.addTab(self.tab_zy, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.widget_5 = QtWidgets.QWidget(self.functionPanel)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setContentsMargins(5, 20, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.searchlineEdit = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchlineEdit.sizePolicy().hasHeightForWidth())
        self.searchlineEdit.setSizePolicy(sizePolicy)
        self.searchlineEdit.setInputMask("")
        self.searchlineEdit.setObjectName("searchlineEdit")
        self.horizontalLayout_8.addWidget(self.searchlineEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget_5)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_8.addWidget(self.searchButton)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.functionPanel)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4.addWidget(self.widget_3)
        self.splitter_2 = QtWidgets.QSplitter(self.widget_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(0)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.file_list = QtWidgets.QListWidget(self.splitter)
        self.file_list.setObjectName("file_list")
        self.table_pannel = QtWidgets.QWidget(self.splitter)
        self.table_pannel.setObjectName("table_pannel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.table_pannel)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableData = QtWidgets.QTableWidget(self.table_pannel)
        self.tableData.setObjectName("tableData")
        self.tableData.setColumnCount(0)
        self.tableData.setRowCount(0)
        self.tableData.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableData)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.textEdit = QtWidgets.QTextEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.horizontalLayout_4.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1493, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimportFile = QtWidgets.QAction(MainWindow)
        self.actionimportFile.setCheckable(True)
        self.actionimportFile.setIconText("打开文件")
        self.actionimportFile.setIconVisibleInMenu(False)
        self.actionimportFile.setObjectName("actionimportFile")
        self.actionexportFiles = QtWidgets.QAction(MainWindow)
        self.actionexportFiles.setObjectName("actionexportFiles")
        self.actionindependentChech = QtWidgets.QAction(MainWindow)
        self.actionindependentChech.setObjectName("actionindependentChech")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionA_2 = QtWidgets.QAction(MainWindow)
        self.actionA_2.setObjectName("actionA_2")
        self.actionB = QtWidgets.QAction(MainWindow)
        self.actionB.setObjectName("actionB")
        self.actionB_2 = QtWidgets.QAction(MainWindow)
        self.actionB_2.setObjectName("actionB_2")
        self.actionZY = QtWidgets.QAction(MainWindow)
        self.actionZY.setObjectName("actionZY")
        self.checkQuest = QtWidgets.QAction(MainWindow)
        self.checkQuest.setObjectName("checkQuest")
        self.checkZy = QtWidgets.QAction(MainWindow)
        self.checkZy.setObjectName("checkZy")
        self.checkIndepent = QtWidgets.QAction(MainWindow)
        self.checkIndepent.setObjectName("checkIndepent")
        self.actionworkspace = QtWidgets.QAction(MainWindow)
        self.actionworkspace.setObjectName("actionworkspace")
        self.actioncustomcheck = QtWidgets.QAction(MainWindow)
        self.actioncustomcheck.setObjectName("actioncustomcheck")
        self.actionIntroduce = QtWidgets.QAction(MainWindow)
        self.actionIntroduce.setObjectName("actionIntroduce")
        self.menu.addAction(self.actionworkspace)
        self.menu_4.addAction(self.actionIntroduce)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.label.setBuddy(self.xz_comboBox)
        self.label_2.setBuddy(self.xq_comboBox)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "调查数据处理系统"))
        self.importTable.setText(_translate("MainWindow", "导入相关表"))
        self.questionCheck.setText(_translate("MainWindow", "审核问卷"))
        self.zyCheck.setText(_translate("MainWindow", "审核账页"))
        # self.IndepentCheck.setText(_translate("MainWindow", "独立审核"))
        # self.pushButton.setText(_translate("MainWindow", "自定义审核条件"))
        # self.ducplictCheck.setText(_translate("MainWindow", "检验复核"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_check), _translate("MainWindow", "审核"))
        self.import_townList.setText(_translate("MainWindow", "导入小区名录"))
        self.open_tableA.setText(_translate("MainWindow", "打开A表"))
        self.open_zy.setText(_translate("MainWindow", "打开账页表"))
        self.label.setText(_translate("MainWindow", "乡镇街道："))
        self.label_2.setText(_translate("MainWindow", "调查小区："))
        self.generateTz.setText(_translate("MainWindow", "生成台账"))
        self.export_taizhang.setText(_translate("MainWindow", "导出当前台账"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zy), _translate("MainWindow", "台账"))
        self.label_3.setText(_translate("MainWindow", "户SID："))
        self.searchButton.setText(_translate("MainWindow", "查找"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.actionimportFile.setText(_translate("MainWindow", "打开文件"))
        self.actionimportFile.setToolTip(_translate("MainWindow", "打开文件"))
        self.actionexportFiles.setText(_translate("MainWindow", "导出文件"))
        self.actionindependentChech.setText(_translate("MainWindow", "独立审核"))
        self.actionA.setText(_translate("MainWindow", "A"))
        self.actionA_2.setText(_translate("MainWindow", "A"))
        self.actionB.setText(_translate("MainWindow", "B"))
        self.actionB_2.setText(_translate("MainWindow", "B"))
        self.actionZY.setText(_translate("MainWindow", "ZY"))
        self.checkQuest.setText(_translate("MainWindow", "审核问卷数据"))
        self.checkZy.setText(_translate("MainWindow", "审核账页"))
        self.checkIndepent.setText(_translate("MainWindow", "独立审核"))
        self.actionworkspace.setText(_translate("MainWindow", "选择工作目录"))
        self.actioncustomcheck.setText(_translate("MainWindow", "自定义审核条件"))
        self.actionIntroduce.setText(_translate("MainWindow", "使用说明"))

