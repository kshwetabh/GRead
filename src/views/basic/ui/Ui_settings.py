# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/twidi/Projets/gread/src/views/basic/ui/settings.ui'
#
# Created: Thu Sep 30 00:33:51 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(442, 508)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Settings)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(Settings)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 438, 504))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Trick = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.Trick.setTextFormat(QtCore.Qt.PlainText)
        self.Trick.setAlignment(QtCore.Qt.AlignCenter)
        self.Trick.setObjectName("Trick")
        self.verticalLayout_4.addWidget(self.Trick)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.groupGoogle = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupGoogle.setObjectName("groupGoogle")
        self.formLayout = QtGui.QFormLayout(self.groupGoogle)
        self.formLayout.setObjectName("formLayout")
        self.labelSettingsAccount = QtGui.QLabel(self.groupGoogle)
        self.labelSettingsAccount.setObjectName("labelSettingsAccount")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelSettingsAccount)
        self.inputSettingsAccount = QtGui.QLineEdit(self.groupGoogle)
        self.inputSettingsAccount.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhNoAutoUppercase)
        self.inputSettingsAccount.setObjectName("inputSettingsAccount")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.inputSettingsAccount)
        self.labelSettingsPassword = QtGui.QLabel(self.groupGoogle)
        self.labelSettingsPassword.setObjectName("labelSettingsPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelSettingsPassword)
        self.inputSettingsPassword = QtGui.QLineEdit(self.groupGoogle)
        self.inputSettingsPassword.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.inputSettingsPassword.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.inputSettingsPassword.setObjectName("inputSettingsPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.inputSettingsPassword)
        self.verticalLayout_4.addWidget(self.groupGoogle)
        self.groupFeeds = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupFeeds.setObjectName("groupFeeds")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupFeeds)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSettingsHomeDefault = QtGui.QLabel(self.groupFeeds)
        self.labelSettingsHomeDefault.setObjectName("labelSettingsHomeDefault")
        self.horizontalLayout.addWidget(self.labelSettingsHomeDefault)
        self.selectSettingsHomeDefault = QtGui.QComboBox(self.groupFeeds)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectSettingsHomeDefault.sizePolicy().hasHeightForWidth())
        self.selectSettingsHomeDefault.setSizePolicy(sizePolicy)
        self.selectSettingsHomeDefault.setObjectName("selectSettingsHomeDefault")
        self.selectSettingsHomeDefault.addItem("")
        self.selectSettingsHomeDefault.addItem("")
        self.horizontalLayout.addWidget(self.selectSettingsHomeDefault)
        self.checkSettingsHomeShowUnread = QtGui.QCheckBox(self.groupFeeds)
        self.checkSettingsHomeShowUnread.setObjectName("checkSettingsHomeShowUnread")
        self.horizontalLayout.addWidget(self.checkSettingsHomeShowUnread)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupSpecials = QtGui.QGroupBox(self.groupFeeds)
        self.groupSpecials.setObjectName("groupSpecials")
        self.gridLayout = QtGui.QGridLayout(self.groupSpecials)
        self.gridLayout.setObjectName("gridLayout")
        self.checkSettingsShowStarred = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowStarred.setObjectName("checkSettingsShowStarred")
        self.gridLayout.addWidget(self.checkSettingsShowStarred, 0, 0, 1, 1)
        self.checkSettingsShowShared = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowShared.setObjectName("checkSettingsShowShared")
        self.gridLayout.addWidget(self.checkSettingsShowShared, 0, 1, 1, 1)
        self.checkSettingsShowNotes = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowNotes.setObjectName("checkSettingsShowNotes")
        self.gridLayout.addWidget(self.checkSettingsShowNotes, 0, 2, 1, 1)
        self.checkSettingsShowAll = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowAll.setObjectName("checkSettingsShowAll")
        self.gridLayout.addWidget(self.checkSettingsShowAll, 1, 0, 1, 1)
        self.checkSettingsShowRead = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowRead.setObjectName("checkSettingsShowRead")
        self.gridLayout.addWidget(self.checkSettingsShowRead, 1, 1, 1, 1)
        self.checkSettingsShowFriends = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowFriends.setObjectName("checkSettingsShowFriends")
        self.gridLayout.addWidget(self.checkSettingsShowFriends, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupSpecials)
        self.verticalLayout_4.addWidget(self.groupFeeds)
        self.groupItems = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupItems.setObjectName("groupItems")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupItems)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelSettingsItemsShowMode = QtGui.QLabel(self.groupItems)
        self.labelSettingsItemsShowMode.setObjectName("labelSettingsItemsShowMode")
        self.horizontalLayout_3.addWidget(self.labelSettingsItemsShowMode)
        self.selectSettingsItemsShowMode = QtGui.QComboBox(self.groupItems)
        self.selectSettingsItemsShowMode.setObjectName("selectSettingsItemsShowMode")
        self.selectSettingsItemsShowMode.addItem("")
        self.selectSettingsItemsShowMode.addItem("")
        self.selectSettingsItemsShowMode.addItem("")
        self.selectSettingsItemsShowMode.addItem("")
        self.horizontalLayout_3.addWidget(self.selectSettingsItemsShowMode)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupItems)
        self.groupBanner = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBanner.setObjectName("groupBanner")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBanner)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelSettingsBannerPosition = QtGui.QLabel(self.groupBanner)
        self.labelSettingsBannerPosition.setObjectName("labelSettingsBannerPosition")
        self.gridLayout_2.addWidget(self.labelSettingsBannerPosition, 0, 0, 1, 1)
        self.selectSettingsBannerPosition = QtGui.QComboBox(self.groupBanner)
        self.selectSettingsBannerPosition.setObjectName("selectSettingsBannerPosition")
        self.selectSettingsBannerPosition.addItem("")
        self.selectSettingsBannerPosition.addItem("")
        self.selectSettingsBannerPosition.addItem("")
        self.gridLayout_2.addWidget(self.selectSettingsBannerPosition, 0, 1, 1, 2)
        self.checkSettingsBannerHide = QtGui.QCheckBox(self.groupBanner)
        self.checkSettingsBannerHide.setObjectName("checkSettingsBannerHide")
        self.gridLayout_2.addWidget(self.checkSettingsBannerHide, 1, 0, 1, 1)
        self.spinSettingsBannerHideDelay = QtGui.QSpinBox(self.groupBanner)
        self.spinSettingsBannerHideDelay.setMinimum(500)
        self.spinSettingsBannerHideDelay.setMaximum(60000)
        self.spinSettingsBannerHideDelay.setSingleStep(100)
        self.spinSettingsBannerHideDelay.setProperty("value", 2000)
        self.spinSettingsBannerHideDelay.setObjectName("spinSettingsBannerHideDelay")
        self.gridLayout_2.addWidget(self.spinSettingsBannerHideDelay, 1, 1, 1, 1)
        self.labelSettingsBannerHideDelayMs = QtGui.QLabel(self.groupBanner)
        self.labelSettingsBannerHideDelayMs.setObjectName("labelSettingsBannerHideDelayMs")
        self.gridLayout_2.addWidget(self.labelSettingsBannerHideDelayMs, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addWidget(self.groupBanner)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.labelSettingsAccount.setBuddy(self.inputSettingsAccount)
        self.labelSettingsPassword.setBuddy(self.inputSettingsPassword)
        self.labelSettingsHomeDefault.setBuddy(self.selectSettingsHomeDefault)
        self.labelSettingsItemsShowMode.setBuddy(self.selectSettingsItemsShowMode)
        self.labelSettingsBannerPosition.setBuddy(self.selectSettingsBannerPosition)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        Settings.setTabOrder(self.inputSettingsAccount, self.inputSettingsPassword)
        Settings.setTabOrder(self.inputSettingsPassword, self.selectSettingsHomeDefault)
        Settings.setTabOrder(self.selectSettingsHomeDefault, self.checkSettingsHomeShowUnread)
        Settings.setTabOrder(self.checkSettingsHomeShowUnread, self.checkSettingsShowStarred)
        Settings.setTabOrder(self.checkSettingsShowStarred, self.checkSettingsShowShared)
        Settings.setTabOrder(self.checkSettingsShowShared, self.checkSettingsShowNotes)
        Settings.setTabOrder(self.checkSettingsShowNotes, self.checkSettingsShowAll)
        Settings.setTabOrder(self.checkSettingsShowAll, self.checkSettingsShowRead)
        Settings.setTabOrder(self.checkSettingsShowRead, self.checkSettingsShowFriends)
        Settings.setTabOrder(self.checkSettingsShowFriends, self.selectSettingsItemsShowMode)
        Settings.setTabOrder(self.selectSettingsItemsShowMode, self.scrollArea)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.Trick.setText(QtGui.QApplication.translate("Settings", "Trick : press \"h\" in GRead to display help about keyboard shortcuts", None, QtGui.QApplication.UnicodeUTF8))
        self.groupGoogle.setTitle(QtGui.QApplication.translate("Settings", "Google credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsAccount.setText(QtGui.QApplication.translate("Settings", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsPassword.setText(QtGui.QApplication.translate("Settings", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.groupFeeds.setTitle(QtGui.QApplication.translate("Settings", "Feeds list", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsHomeDefault.setText(QtGui.QApplication.translate("Settings", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsHomeDefault.setItemText(0, QtGui.QApplication.translate("Settings", "Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsHomeDefault.setItemText(1, QtGui.QApplication.translate("Settings", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsHomeShowUnread.setText(QtGui.QApplication.translate("Settings", "Show unread only", None, QtGui.QApplication.UnicodeUTF8))
        self.groupSpecials.setTitle(QtGui.QApplication.translate("Settings", "Show specials", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowStarred.setText(QtGui.QApplication.translate("Settings", "Starred", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowShared.setText(QtGui.QApplication.translate("Settings", "Shared", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowNotes.setText(QtGui.QApplication.translate("Settings", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowAll.setText(QtGui.QApplication.translate("Settings", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowRead.setText(QtGui.QApplication.translate("Settings", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsShowFriends.setText(QtGui.QApplication.translate("Settings", "Friends", None, QtGui.QApplication.UnicodeUTF8))
        self.groupItems.setTitle(QtGui.QApplication.translate("Settings", "Items list", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsItemsShowMode.setText(QtGui.QApplication.translate("Settings", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsItemsShowMode.setItemText(0, QtGui.QApplication.translate("Settings", "Default all, save each", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsItemsShowMode.setItemText(1, QtGui.QApplication.translate("Settings", "Default unread, save each", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsItemsShowMode.setItemText(2, QtGui.QApplication.translate("Settings", "Default all, no save", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsItemsShowMode.setItemText(3, QtGui.QApplication.translate("Settings", "Default unread, no save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBanner.setTitle(QtGui.QApplication.translate("Settings", "Informations banner", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsBannerPosition.setText(QtGui.QApplication.translate("Settings", "Position", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(0, QtGui.QApplication.translate("Settings", "Top", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(1, QtGui.QApplication.translate("Settings", "Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(2, QtGui.QApplication.translate("Settings", "Never display", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsBannerHide.setText(QtGui.QApplication.translate("Settings", "Hide after", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsBannerHideDelayMs.setText(QtGui.QApplication.translate("Settings", "ms", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Settings = QtGui.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

