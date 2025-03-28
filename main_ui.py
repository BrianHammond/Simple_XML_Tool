# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 506)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.newFile_action = QAction(MainWindow)
        self.newFile_action.setObjectName(u"newFile_action")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.open_action = QAction(MainWindow)
        self.open_action.setObjectName(u"open_action")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.line_name = QLineEdit(self.groupBox)
        self.line_name.setObjectName(u"line_name")
        font = QFont()
        font.setPointSize(9)
        self.line_name.setFont(font)

        self.horizontalLayout.addWidget(self.line_name)

        self.line_age = QLineEdit(self.groupBox)
        self.line_age.setObjectName(u"line_age")
        self.line_age.setFont(font)

        self.horizontalLayout.addWidget(self.line_age)

        self.line_title = QLineEdit(self.groupBox)
        self.line_title.setObjectName(u"line_title")
        self.line_title.setFont(font)

        self.horizontalLayout.addWidget(self.line_title)

        self.line_department = QLineEdit(self.groupBox)
        self.line_department.setObjectName(u"line_department")
        self.line_department.setFont(font)

        self.horizontalLayout.addWidget(self.line_department)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.line_address1 = QLineEdit(self.groupBox)
        self.line_address1.setObjectName(u"line_address1")
        self.line_address1.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_address1)

        self.line_address2 = QLineEdit(self.groupBox)
        self.line_address2.setObjectName(u"line_address2")
        self.line_address2.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_address2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.line_additional = QLineEdit(self.groupBox)
        self.line_additional.setObjectName(u"line_additional")
        self.line_additional.setFont(font)

        self.horizontalLayout_3.addWidget(self.line_additional)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setObjectName(u"button_add")

        self.horizontalLayout_4.addWidget(self.button_add)

        self.button_update = QPushButton(self.centralwidget)
        self.button_update.setObjectName(u"button_update")

        self.horizontalLayout_4.addWidget(self.button_update)

        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout_4.addWidget(self.button_delete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setColumnCount(0)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 921, 22))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.line_name, self.line_age)
        QWidget.setTabOrder(self.line_age, self.line_title)
        QWidget.setTabOrder(self.line_title, self.line_department)
        QWidget.setTabOrder(self.line_department, self.line_address1)
        QWidget.setTabOrder(self.line_address1, self.line_address2)
        QWidget.setTabOrder(self.line_address2, self.line_additional)
        QWidget.setTabOrder(self.line_additional, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_update)
        QWidget.setTabOrder(self.button_update, self.button_delete)
        QWidget.setTabOrder(self.button_delete, self.table)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_about_qt)
        self.menuSettings.addAction(self.action_dark_mode)
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XML Tool", None))
        self.newFile_action.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.newFile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.open_action.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.open_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Employee Information", None))
        self.line_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.line_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.line_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.line_department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.line_address1.setText("")
        self.line_address1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address 1", None))
        self.line_address2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address 2", None))
        self.line_additional.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Additional Information", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update Employee", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Employee", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

