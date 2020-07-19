# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.terminal = QtWidgets.QTextEdit(self.groupBox)
        self.terminal.setObjectName("terminal")
        self.verticalLayout_3.addWidget(self.terminal)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.file_viewer = QtWidgets.QTreeView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_viewer.sizePolicy().hasHeightForWidth())
        self.file_viewer.setSizePolicy(sizePolicy)
        self.file_viewer.setMaximumSize(QtCore.QSize(500, 1677721))
        self.file_viewer.setObjectName("file_viewer")
        self.gridLayout.addWidget(self.file_viewer, 0, 0, 1, 1)
        self.button_get_files = QtWidgets.QPushButton(self.tab)
        self.button_get_files.setObjectName("button_get_files")
        self.gridLayout.addWidget(self.button_get_files, 1, 0, 1, 1)
        self.button_reset_connection = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_reset_connection.sizePolicy().hasHeightForWidth())
        self.button_reset_connection.setSizePolicy(sizePolicy)
        self.button_reset_connection.setObjectName("button_reset_connection")
        self.gridLayout.addWidget(self.button_reset_connection, 1, 1, 1, 2)
        self.VideoPlayer = QtWidgets.QGroupBox(self.tab)
        self.VideoPlayer.setObjectName("VideoPlayer")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.VideoPlayer)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_play_pause = QtWidgets.QPushButton(self.VideoPlayer)
        self.button_play_pause.setObjectName("button_play_pause")
        self.gridLayout_3.addWidget(self.button_play_pause, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.VideoPlayer)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_3.addWidget(self.horizontalSlider, 1, 3, 1, 1)
        self.main_video_frame = QtWidgets.QTextEdit(self.VideoPlayer)
        self.main_video_frame.setObjectName("main_video_frame")
        self.gridLayout_3.addWidget(self.main_video_frame, 0, 0, 1, 4)
        self.button_screenshot = QtWidgets.QPushButton(self.VideoPlayer)
        self.button_screenshot.setObjectName("button_screenshot")
        self.gridLayout_3.addWidget(self.button_screenshot, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.VideoPlayer, 0, 1, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_live_stream = QtWidgets.QWidget()
        self.tab_live_stream.setObjectName("tab_live_stream")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_live_stream)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_live_stream)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.birghtness_slider = QtWidgets.QFrame(self.groupBox_2)
        self.birghtness_slider.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.birghtness_slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.birghtness_slider.setObjectName("birghtness_slider")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.birghtness_slider)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.birghtness_slider)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.slider_exposure = QtWidgets.QSlider(self.birghtness_slider)
        self.slider_exposure.setOrientation(QtCore.Qt.Horizontal)
        self.slider_exposure.setObjectName("slider_exposure")
        self.horizontalLayout.addWidget(self.slider_exposure)
        self.label_5 = QtWidgets.QLabel(self.birghtness_slider)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.birghtness_slider)
        self.Zoom = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Zoom.sizePolicy().hasHeightForWidth())
        self.Zoom.setSizePolicy(sizePolicy)
        self.Zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Zoom.setObjectName("Zoom")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Zoom)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zoom_label = QtWidgets.QLabel(self.Zoom)
        self.zoom_label.setObjectName("zoom_label")
        self.horizontalLayout_2.addWidget(self.zoom_label)
        self.verticalLayout.addWidget(self.Zoom)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.slider_zoom = QtWidgets.QSlider(self.frame_2)
        self.slider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom.setObjectName("slider_zoom")
        self.horizontalLayout_4.addWidget(self.slider_zoom)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame = QtWidgets.QFrame(self.groupBox_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.slider_leftright = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_leftright.sizePolicy().hasHeightForWidth())
        self.slider_leftright.setSizePolicy(sizePolicy)
        self.slider_leftright.setOrientation(QtCore.Qt.Horizontal)
        self.slider_leftright.setObjectName("slider_leftright")
        self.horizontalLayout_3.addWidget(self.slider_leftright)
        self.label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout.addWidget(self.frame)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.frame_3 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.slider_updown = QtWidgets.QSlider(self.frame_3)
        self.slider_updown.setOrientation(QtCore.Qt.Horizontal)
        self.slider_updown.setObjectName("slider_updown")
        self.horizontalLayout_5.addWidget(self.slider_updown)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.verticalLayout.addWidget(self.frame_3)
        self.button_apply_settings = QtWidgets.QPushButton(self.groupBox_2)
        self.button_apply_settings.setObjectName("button_apply_settings")
        self.verticalLayout.addWidget(self.button_apply_settings)
        self.button_auto_settings = QtWidgets.QPushButton(self.groupBox_2)
        self.button_auto_settings.setObjectName("button_auto_settings")
        self.verticalLayout.addWidget(self.button_auto_settings)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.live_image = QtWidgets.QLabel(self.tab_live_stream)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_image.sizePolicy().hasHeightForWidth())
        self.live_image.setSizePolicy(sizePolicy)
        self.live_image.setText("")
        self.live_image.setObjectName("live_image")
        self.gridLayout_5.addWidget(self.live_image, 0, 0, 3, 1)
        self.button_live_stream = QtWidgets.QPushButton(self.tab_live_stream)
        self.button_live_stream.setObjectName("button_live_stream")
        self.gridLayout_5.addWidget(self.button_live_stream, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_live_stream, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Recent Activity"))
        self.button_get_files.setText(_translate("MainWindow", "Download Camera Files"))
        self.button_reset_connection.setText(_translate("MainWindow", "Reset Connection"))
        self.VideoPlayer.setTitle(_translate("MainWindow", "Video Player"))
        self.button_play_pause.setText(_translate("MainWindow", "Play"))
        self.button_screenshot.setText(_translate("MainWindow", "Screenshot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "Exposure Time:"))
        self.label_4.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Max"))
        self.zoom_label.setText(_translate("MainWindow", "Zoom:"))
        self.label_9.setText(_translate("MainWindow", "0%"))
        self.label_10.setText(_translate("MainWindow", "100%"))
        self.label_3.setText(_translate("MainWindow", "Slide Image (Left/Right):"))
        self.label_6.setText(_translate("MainWindow", "Left"))
        self.label_7.setText(_translate("MainWindow", "Right"))
        self.label_8.setText(_translate("MainWindow", "Slide Image (Bottom/Top):"))
        self.label_11.setText(_translate("MainWindow", "Bottom"))
        self.label_12.setText(_translate("MainWindow", "Top"))
        self.button_apply_settings.setText(_translate("MainWindow", "Apply"))
        self.button_auto_settings.setText(_translate("MainWindow", "Auto"))
        self.button_live_stream.setText(_translate("MainWindow", "Start Live Stream"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_live_stream), _translate("MainWindow", "Live Stream"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
