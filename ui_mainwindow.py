# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(397, 283)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 351, 221))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.serial_port = QComboBox(self.widget)
        self.serial_port.setObjectName(u"serial_port")

        self.horizontalLayout.addWidget(self.serial_port)

        self.open_serial_button = QPushButton(self.widget)
        self.open_serial_button.setObjectName(u"open_serial_button")

        self.horizontalLayout.addWidget(self.open_serial_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.road1_selected = QCheckBox(self.widget)
        self.road1_selected.setObjectName(u"road1_selected")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.road1_selected.sizePolicy().hasHeightForWidth())
        self.road1_selected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.road1_selected, 0, 1, 1, 1)

        self.road1_set_time = QSpinBox(self.widget)
        self.road1_set_time.setObjectName(u"road1_set_time")

        self.gridLayout.addWidget(self.road1_set_time, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.road1_open = QPushButton(self.widget)
        self.road1_open.setObjectName(u"road1_open")

        self.gridLayout.addWidget(self.road1_open, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.road2_selected = QCheckBox(self.widget)
        self.road2_selected.setObjectName(u"road2_selected")
        sizePolicy1.setHeightForWidth(self.road2_selected.sizePolicy().hasHeightForWidth())
        self.road2_selected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.road2_selected, 1, 1, 1, 1)

        self.road2_set_time = QSpinBox(self.widget)
        self.road2_set_time.setObjectName(u"road2_set_time")

        self.gridLayout.addWidget(self.road2_set_time, 1, 2, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.road2_open = QPushButton(self.widget)
        self.road2_open.setObjectName(u"road2_open")

        self.gridLayout.addWidget(self.road2_open, 1, 4, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.road3_selected = QCheckBox(self.widget)
        self.road3_selected.setObjectName(u"road3_selected")
        sizePolicy1.setHeightForWidth(self.road3_selected.sizePolicy().hasHeightForWidth())
        self.road3_selected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.road3_selected, 2, 1, 1, 1)

        self.road3_set_time = QSpinBox(self.widget)
        self.road3_set_time.setObjectName(u"road3_set_time")

        self.gridLayout.addWidget(self.road3_set_time, 2, 2, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.road3_open = QPushButton(self.widget)
        self.road3_open.setObjectName(u"road3_open")

        self.gridLayout.addWidget(self.road3_open, 2, 4, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.road4_selected = QCheckBox(self.widget)
        self.road4_selected.setObjectName(u"road4_selected")
        sizePolicy1.setHeightForWidth(self.road4_selected.sizePolicy().hasHeightForWidth())
        self.road4_selected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.road4_selected, 3, 1, 1, 1)

        self.road4_set_time = QSpinBox(self.widget)
        self.road4_set_time.setObjectName(u"road4_set_time")

        self.gridLayout.addWidget(self.road4_set_time, 3, 2, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.road4_open = QPushButton(self.widget)
        self.road4_open.setObjectName(u"road4_open")

        self.gridLayout.addWidget(self.road4_open, 3, 4, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.road_all_selected = QCheckBox(self.widget)
        self.road_all_selected.setObjectName(u"road_all_selected")
        sizePolicy1.setHeightForWidth(self.road_all_selected.sizePolicy().hasHeightForWidth())
        self.road_all_selected.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.road_all_selected, 4, 1, 1, 1)

        self.road_all_set_time = QSpinBox(self.widget)
        self.road_all_set_time.setObjectName(u"road_all_set_time")

        self.gridLayout.addWidget(self.road_all_set_time, 4, 2, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)

        self.road_all_open = QPushButton(self.widget)
        self.road_all_open.setObjectName(u"road_all_open")

        self.gridLayout.addWidget(self.road_all_open, 4, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53f7", None))
        self.open_serial_button.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8def1", None))
        self.road1_selected.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.road1_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8def2", None))
        self.road2_selected.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.road2_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8def3", None))
        self.road3_selected.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.road3_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8def4", None))
        self.road4_selected.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.road4_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.road_all_selected.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.road_all_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
    # retranslateUi

