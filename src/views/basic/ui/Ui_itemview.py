# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/twidi/Projets/gread/src/views/basic/ui/itemview.ui'
#
# Created: Mon Sep 27 00:07:24 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_winItemView(object):
    def setupUi(self, winItemView):
        winItemView.setObjectName("winItemView")
        winItemView.resize(800, 480)
        self.centralWidget = QtGui.QWidget(winItemView)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageBox = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageBox.sizePolicy().hasHeightForWidth())
        self.messageBox.setSizePolicy(sizePolicy)
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 0))
        self.messageBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.messageBox.setWordWrap(True)
        self.messageBox.setObjectName("messageBox")
        self.verticalLayout.addWidget(self.messageBox)
        self.webView = QtWebKit.QWebView(self.centralWidget)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        winItemView.setCentralWidget(self.centralWidget)
        self.toolBar = QtGui.QToolBar(winItemView)
        self.toolBar.setObjectName("toolBar")
        winItemView.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)

        self.retranslateUi(winItemView)
        QtCore.QMetaObject.connectSlotsByName(winItemView)

    def retranslateUi(self, winItemView):
        winItemView.setWindowTitle(QtGui.QApplication.translate("winItemView", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.messageBox.setText(QtGui.QApplication.translate("winItemView", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("winItemView", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    winItemView = QtGui.QMainWindow()
    ui = Ui_winItemView()
    ui.setupUi(winItemView)
    winItemView.show()
    sys.exit(app.exec_())

