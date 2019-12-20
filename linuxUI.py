# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from lib.linux import get_browsers,get_drives,get_hw_info,get_network_info,get_os_info,get_package_list,get_ports,get_startup_list,list_files

class Ui_Cinfo(object):
    def setupUi(self, Cinfo):
        Cinfo.setObjectName("Cinfo")
        Cinfo.resize(777, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Cinfo.setWindowIcon(icon)
        Cinfo.setIconSize(QtCore.QSize(32, 24))
        self.centralwidget = QtWidgets.QWidget(Cinfo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        ## For Listing files
        self.listfIles = QtWidgets.QCheckBox(self.centralwidget)
        self.listfIles.setObjectName("listfIles")
        self.verticalLayout_2.addWidget(self.listfIles)
        ##  For Startup Applications
        self.startUpapplications = QtWidgets.QCheckBox(self.centralwidget)
        self.startUpapplications.setObjectName("startUpapplications")
        self.verticalLayout_2.addWidget(self.startUpapplications)
        ##  For Installed Applications
        self.instaLledApplications = QtWidgets.QCheckBox(self.centralwidget)
        self.instaLledApplications.setObjectName("instaLledApplications")
        self.verticalLayout_2.addWidget(self.instaLledApplications)
        ##  For Network
        self.networkInfo = QtWidgets.QCheckBox(self.centralwidget)
        self.networkInfo.setObjectName("networkInfo")
        self.verticalLayout_2.addWidget(self.networkInfo)
        ##  About Your Machine
        self.aboutYourMachine = QtWidgets.QCheckBox(self.centralwidget)
        self.aboutYourMachine.setObjectName("aboutYourMachine")
        self.verticalLayout_2.addWidget(self.aboutYourMachine)
        ##  For Installed Browsers
        self.installedBrowsers = QtWidgets.QCheckBox(self.centralwidget)
        self.installedBrowsers.setObjectName("installedBrowsers")
        self.verticalLayout_2.addWidget(self.installedBrowsers)
        ##  Opened Ports
        self.openedPorts = QtWidgets.QCheckBox(self.centralwidget)
        self.openedPorts.setObjectName("openedPorts")
        self.verticalLayout_2.addWidget(self.openedPorts)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.returnData)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        Cinfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cinfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menuExport_As.setFont(font)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menuOption.setFont(font)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        Cinfo.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Cinfo)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(30, 24))
        self.toolBar.setObjectName("toolBar")
        Cinfo.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(Cinfo)
        self.statusBar.setObjectName("statusBar")
        Cinfo.setStatusBar(self.statusBar)
        self.actionExcel = QtWidgets.QAction(Cinfo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExcel.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionExcel.setFont(font)
        self.actionExcel.setObjectName("actionExcel")
        self.actionJson = QtWidgets.QAction(Cinfo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Json.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJson.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionJson.setFont(font)
        self.actionJson.setObjectName("actionJson")
        self.actionText = QtWidgets.QAction(Cinfo)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionText.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionText.setFont(font)
        self.actionText.setObjectName("actionText")
        self.actionRefresh = QtWidgets.QAction(Cinfo)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/Refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.actionRefresh.setFont(font)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionExit = QtWidgets.QAction(Cinfo)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Cinfo)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(Cinfo)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(Cinfo)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Prefrences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.actionPreferences.setFont(font)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuExport_As.addAction(self.actionExcel)
        self.menuExport_As.addAction(self.actionJson)
        self.menuExport_As.addAction(self.actionText)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOption.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExcel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionJson)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionText)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()

        self.retranslateUi(Cinfo)
        QtCore.QMetaObject.connectSlotsByName(Cinfo)

    def retranslateUi(self, Cinfo):
        _translate = QtCore.QCoreApplication.translate
        Cinfo.setWindowTitle(_translate("Cinfo", "Cinfo"))
        self.listfIles.setText(_translate("Cinfo", "List Files"))
        self.startUpapplications.setText(_translate("Cinfo", "List Startup Applications"))
        self.instaLledApplications.setText(_translate("Cinfo", "List Installed Applications"))
        self.networkInfo.setText(_translate("Cinfo", "Network Information"))
        self.aboutYourMachine.setText(_translate("Cinfo", "About Your Machine"))
        self.installedBrowsers.setText(_translate("Cinfo", "List Installed Browsers"))
        self.openedPorts.setText(_translate("Cinfo", "List Open Ports"))
        self.pushButton.setText(_translate("Cinfo", "Let\'s Go"))
        self.label.setText(_translate("Cinfo", "Choose Service :"))
        self.textBrowser.setPlainText("Deepak Chauhan")
        self.label_2.setText(_translate("Cinfo", "Result :"))
        self.menuFile.setTitle(_translate("Cinfo", "File"))
        self.menuExport_As.setTitle(_translate("Cinfo", "Export As"))
        self.menuOption.setTitle(_translate("Cinfo", "Option"))
        self.menuHelp.setTitle(_translate("Cinfo", "Help"))
        self.toolBar.setWindowTitle(_translate("Cinfo", "toolBar"))
        self.actionExcel.setText(_translate("Cinfo", "Excel"))
        self.actionExcel.setToolTip(_translate("Cinfo", "Export Record IntoExcel"))
        self.actionJson.setText(_translate("Cinfo", "Json"))
        self.actionJson.setToolTip(_translate("Cinfo", "Export into json File"))
        self.actionText.setText(_translate("Cinfo", "Text"))
        self.actionText.setToolTip(_translate("Cinfo", "Export Into Text File"))
        self.actionRefresh.setText(_translate("Cinfo", "Refresh"))
        self.actionRefresh.setToolTip(_translate("Cinfo", "refresh"))
        self.actionRefresh.setShortcut(_translate("Cinfo", "Ctrl+F5"))
        self.actionExit.setText(_translate("Cinfo", "Exit"))
        self.actionExit.setToolTip(_translate("Cinfo", "Exit Window"))
        self.actionExit.setShortcut(_translate("Cinfo", "Ctrl+Q"))
        self.actionAbout.setText(_translate("Cinfo", "About"))
        self.actionAbout.setToolTip(_translate("Cinfo", "Information "))
        self.actionAbout.setShortcut(_translate("Cinfo", "Ctrl+I"))
        self.actionHelp.setText(_translate("Cinfo", "Help"))
        self.actionHelp.setShortcut(_translate("Cinfo", "Ctrl+F1"))
        self.actionPreferences.setText(_translate("Cinfo", "Preferences"))

    def returnData(self):
        packages = get_package_list.get_package_list()
        startup = get_startup_list.get_startup_list()
        network = get_network_info.get_network_info()
        browsers = get_browsers.get_browsers()
        ports = get_ports.get_ports()
        drives = get_drives.get_drives()
        os_info = get_os_info.get_os_info()
        hardware = get_hw_info.get_hw_info()
        files = list_files.list_files()
        data = ""
        if self.aboutYourMachine.isChecked() is True:
            data += "~~~About Your Machine~~".center(30)+'\n'+os_info.work()+"\n\n"+hardware.work()+"\n\n"+drives.work()+"\n\n"

        self.textBrowser.setPlainText(data)
        print([self.listfIles.isChecked(),self.startUpapplications.isChecked(),self.instaLledApplications.isChecked(),self.networkInfo.isChecked(),self.aboutYourMachine.isChecked(),self.installedBrowsers.isChecked(),self.openedPorts.isChecked()])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cinfo = QtWidgets.QMainWindow()
    ui = Ui_Cinfo()
    ui.setupUi(Cinfo)
    Cinfo.show()
    sys.exit(app.exec_())
