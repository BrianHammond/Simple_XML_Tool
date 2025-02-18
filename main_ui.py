# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.line_title = QLineEdit(self.centralwidget)
        self.line_title.setObjectName(u"line_title")
        font = QFont()
        font.setPointSize(12)
        self.line_title.setFont(font)

        self.horizontalLayout.addWidget(self.line_title)

        self.line_author = QLineEdit(self.centralwidget)
        self.line_author.setObjectName(u"line_author")
        self.line_author.setFont(font)

        self.horizontalLayout.addWidget(self.line_author)

        self.line_pages = QLineEdit(self.centralwidget)
        self.line_pages.setObjectName(u"line_pages")
        self.line_pages.setFont(font)

        self.horizontalLayout.addWidget(self.line_pages)

        self.line_year = QLineEdit(self.centralwidget)
        self.line_year.setObjectName(u"line_year")
        self.line_year.setFont(font)

        self.horizontalLayout.addWidget(self.line_year)


        self.verticalLayout.addLayout(self.horizontalLayout)

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


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setColumnCount(0)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)

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
        QWidget.setTabOrder(self.line_title, self.line_author)
        QWidget.setTabOrder(self.line_author, self.line_pages)
        QWidget.setTabOrder(self.line_pages, self.line_year)
        QWidget.setTabOrder(self.line_year, self.button_add)
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
        self.line_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"title", None))
        self.line_author.setPlaceholderText(QCoreApplication.translate("MainWindow", u"author", None))
        self.line_pages.setPlaceholderText(QCoreApplication.translate("MainWindow", u"pages", None))
        self.line_year.setPlaceholderText(QCoreApplication.translate("MainWindow", u"year published", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update File", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Row", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

