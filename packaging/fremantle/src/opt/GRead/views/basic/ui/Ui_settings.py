# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class Ui_Settings(object):
    def setupUi(self, Settings):
        self.addWidgets(Settings)
        self.setTabOrder(Settings)
        self.retranslateUi(Settings)
        
    def addWidgets(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(455, 534)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -104, 436, 692))
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
        self.formLayout_groupGoogle = QtGui.QFormLayout(self.groupGoogle)
        self.formLayout_groupGoogle.setObjectName("formLayout_groupGoogle")
        self.labelSettingsAccount = QtGui.QLabel(self.groupGoogle)
        self.labelSettingsAccount.setObjectName("labelSettingsAccount")
        self.formLayout_groupGoogle.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelSettingsAccount)
        self.inputSettingsAccount = QtGui.QLineEdit(self.groupGoogle)
        try:
            self.inputSettingsAccount.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhNoAutoUppercase)
        except:
            pass
        self.inputSettingsAccount.setObjectName("inputSettingsAccount")
        self.formLayout_groupGoogle.setWidget(0, QtGui.QFormLayout.FieldRole, self.inputSettingsAccount)
        self.labelSettingsPassword = QtGui.QLabel(self.groupGoogle)
        self.labelSettingsPassword.setObjectName("labelSettingsPassword")
        self.formLayout_groupGoogle.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelSettingsPassword)
        self.inputSettingsPassword = QtGui.QLineEdit(self.groupGoogle)
        try:
            self.inputSettingsPassword.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        except:
            pass
        self.inputSettingsPassword.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.inputSettingsPassword.setObjectName("inputSettingsPassword")
        self.formLayout_groupGoogle.setWidget(1, QtGui.QFormLayout.FieldRole, self.inputSettingsPassword)
        self.verticalLayout_4.addWidget(self.groupGoogle)
        self.groupFeeds = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupFeeds.setObjectName("groupFeeds")
        self.verticalLayout_groupFeeds = QtGui.QVBoxLayout(self.groupFeeds)
        self.verticalLayout_groupFeeds.setObjectName("verticalLayout_groupFeeds")
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
        self.verticalLayout_groupFeeds.addLayout(self.horizontalLayout)
        self.groupSpecials = QtGui.QGroupBox(self.groupFeeds)
        self.groupSpecials.setObjectName("groupSpecials")
        self.gridLayout_groupSpecials = QtGui.QGridLayout(self.groupSpecials)
        self.gridLayout_groupSpecials.setObjectName("gridLayout")
        self.checkSettingsShowStarred = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowStarred.setObjectName("checkSettingsShowStarred")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowStarred, 0, 0, 1, 1)
        self.checkSettingsShowShared = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowShared.setObjectName("checkSettingsShowShared")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowShared, 0, 1, 1, 1)
        self.checkSettingsShowNotes = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowNotes.setObjectName("checkSettingsShowNotes")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowNotes, 0, 2, 1, 1)
        self.checkSettingsShowAll = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowAll.setObjectName("checkSettingsShowAll")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowAll, 1, 0, 1, 1)
        self.checkSettingsShowRead = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowRead.setObjectName("checkSettingsShowRead")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowRead, 1, 1, 1, 1)
        self.checkSettingsShowFriends = QtGui.QCheckBox(self.groupSpecials)
        self.checkSettingsShowFriends.setObjectName("checkSettingsShowFriends")
        self.gridLayout_groupSpecials.addWidget(self.checkSettingsShowFriends, 1, 2, 1, 1)
        self.verticalLayout_groupFeeds.addWidget(self.groupSpecials)
        self.verticalLayout_4.addWidget(self.groupFeeds)
        self.groupItems = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupItems.setObjectName("groupItems")
        self.verticalLayout_groupItems = QtGui.QVBoxLayout(self.groupItems)
        self.verticalLayout_groupItems.setObjectName("verticalLayout_groupItems")
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
        self.verticalLayout_groupItems.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupItems)
        self.groupContent = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupContent.setObjectName("groupContent")
        self.verticalLayout_groupContent = QtGui.QVBoxLayout(self.groupContent)
        self.verticalLayout_groupContent.setObjectName("verticalLayout_groupContent")
        self.gridLayout_groupContent = QtGui.QGridLayout()
        self.gridLayout_groupContent.setObjectName("gridLayout_groupContent")
        self.checkSettingsDisplayFeedsTitleItemView = QtGui.QCheckBox(self.groupContent)
        self.checkSettingsDisplayFeedsTitleItemView.setObjectName("checkSettingsDisplayFeedsTitleItemView")
        self.gridLayout_groupContent.addWidget(self.checkSettingsDisplayFeedsTitleItemView, 0, 0, 1, 2)
        self.labelSettingsUserAgent = QtGui.QLabel(self.groupContent)
        self.labelSettingsUserAgent.setObjectName("labelSettingsUserAgent")
        self.gridLayout_groupContent.addWidget(self.labelSettingsUserAgent, 1, 0, 1, 1)
        self.inputSettingsUserAgent = QtGui.QLineEdit(self.groupContent)
        self.inputSettingsUserAgent.setText("")
        self.inputSettingsUserAgent.setObjectName("inputSettingsUserAgent")
        self.gridLayout_groupContent.addWidget(self.inputSettingsUserAgent, 1, 1, 1, 1)
        self.labelSettingsZoomFactor = QtGui.QLabel(self.groupContent)
        self.labelSettingsZoomFactor.setObjectName("labelSettingsZoomFactor")
        self.gridLayout_groupContent.addWidget(self.labelSettingsZoomFactor, 2, 0, 1, 1)
        self.spinSettingsZoomFactor = QtGui.QSpinBox(self.groupContent)
        self.spinSettingsZoomFactor.setMinimum(0)
        self.spinSettingsZoomFactor.setMaximum(10000)
        self.spinSettingsZoomFactor.setSingleStep(5)
        self.spinSettingsZoomFactor.setProperty("value", 100)
        self.spinSettingsZoomFactor.setObjectName("spinSettingsZoomFactor")
        self.gridLayout_groupContent.addWidget(self.spinSettingsZoomFactor, 2, 1, 1, 1)
        self.verticalLayout_groupContent.addLayout(self.gridLayout_groupContent)
        self.verticalLayout_4.addWidget(self.groupContent)
        self.groupOther = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupOther.setObjectName("groupOther")
        self.verticalLayout_groupFeeds = QtGui.QVBoxLayout(self.groupOther)
        self.verticalLayout_groupFeeds.setObjectName("verticalLayout_groupFeeds")
        self.gridLayout_groupOther = QtGui.QGridLayout()
        self.gridLayout_groupOther.setObjectName("gridLayout_groupOther")
        self.labelSettingsItemsToFetch = QtGui.QLabel(self.groupOther)
        self.labelSettingsItemsToFetch.setObjectName("labelSettingsItemsToFetch")
        self.gridLayout_groupOther.addWidget(self.labelSettingsItemsToFetch, 0, 0, 1, 1)
        self.spinSettingsItemsToFetch = QtGui.QSpinBox(self.groupOther)
        self.spinSettingsItemsToFetch.setMinimum(20)
        self.spinSettingsItemsToFetch.setMaximum(2000)
        self.spinSettingsItemsToFetch.setSingleStep(20)
        self.spinSettingsItemsToFetch.setProperty("value", 100)
        self.spinSettingsItemsToFetch.setObjectName("spinSettingsItemsToFetch")
        self.gridLayout_groupOther.addWidget(self.spinSettingsItemsToFetch, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupOther)
        self.label.setObjectName("label")
        self.gridLayout_groupOther.addWidget(self.label, 1, 0, 1, 2)
        self.verticalLayout_groupFeeds.addLayout(self.gridLayout_groupOther)
        self.verticalLayout_4.addWidget(self.groupOther)
        self.groupBanner = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBanner.setObjectName("groupBanner")
        self.verticalLayout_groupBanner = QtGui.QVBoxLayout(self.groupBanner)
        self.verticalLayout_groupBanner.setObjectName("verticalLayout_groupBanner")
        self.gridLayout_groupBanner = QtGui.QGridLayout()
        self.gridLayout_groupBanner.setObjectName("gridLayout_groupBanner")
        self.labelSettingsBannerPosition = QtGui.QLabel(self.groupBanner)
        self.labelSettingsBannerPosition.setObjectName("labelSettingsBannerPosition")
        self.gridLayout_groupBanner.addWidget(self.labelSettingsBannerPosition, 0, 0, 1, 1)
        self.selectSettingsBannerPosition = QtGui.QComboBox(self.groupBanner)
        self.selectSettingsBannerPosition.setObjectName("selectSettingsBannerPosition")
        self.selectSettingsBannerPosition.addItem("")
        self.selectSettingsBannerPosition.addItem("")
        self.selectSettingsBannerPosition.addItem("")
        self.gridLayout_groupBanner.addWidget(self.selectSettingsBannerPosition, 0, 1, 1, 1)
        self.checkSettingsBannerHide = QtGui.QCheckBox(self.groupBanner)
        self.checkSettingsBannerHide.setObjectName("checkSettingsBannerHide")
        self.gridLayout_groupBanner.addWidget(self.checkSettingsBannerHide, 1, 0, 1, 1)
        self.spinSettingsBannerHideDelay = QtGui.QSpinBox(self.groupBanner)
        self.spinSettingsBannerHideDelay.setMinimum(500)
        self.spinSettingsBannerHideDelay.setMaximum(60000)
        self.spinSettingsBannerHideDelay.setSingleStep(100)
        self.spinSettingsBannerHideDelay.setProperty("value", 2000)
        self.spinSettingsBannerHideDelay.setObjectName("spinSettingsBannerHideDelay")
        self.gridLayout_groupBanner.addWidget(self.spinSettingsBannerHideDelay, 1, 1, 1, 1)
        self.verticalLayout_groupBanner.addLayout(self.gridLayout_groupBanner)
        self.verticalLayout_4.addWidget(self.groupBanner)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.labelSettingsAccount.setBuddy(self.inputSettingsAccount)
        self.labelSettingsPassword.setBuddy(self.inputSettingsPassword)
        self.labelSettingsHomeDefault.setBuddy(self.selectSettingsHomeDefault)
        self.labelSettingsItemsShowMode.setBuddy(self.selectSettingsItemsShowMode)
        self.labelSettingsUserAgent.setBuddy(self.inputSettingsUserAgent)
        self.labelSettingsZoomFactor.setBuddy(self.spinSettingsZoomFactor)
        self.labelSettingsItemsToFetch.setBuddy(self.spinSettingsItemsToFetch)
        self.labelSettingsBannerPosition.setBuddy(self.selectSettingsBannerPosition)

    def setTabOrder(self, Settings):
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
        Settings.setTabOrder(self.selectSettingsItemsShowMode, self.checkSettingsDisplayFeedsTitleItemView)
        Settings.setTabOrder(self.checkSettingsDisplayFeedsTitleItemView, self.inputSettingsUserAgent)
        Settings.setTabOrder(self.inputSettingsUserAgent, self.spinSettingsZoomFactor)
        Settings.setTabOrder(self.spinSettingsZoomFactor, self.spinSettingsItemsToFetch)
        Settings.setTabOrder(self.spinSettingsItemsToFetch, self.selectSettingsBannerPosition)
        Settings.setTabOrder(self.selectSettingsBannerPosition, self.checkSettingsBannerHide)
        Settings.setTabOrder(self.checkSettingsBannerHide, self.spinSettingsBannerHideDelay)
        Settings.setTabOrder(self.spinSettingsBannerHideDelay, self.scrollArea)

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
        self.groupContent.setTitle(QtGui.QApplication.translate("Settings", "Item\'s view", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsDisplayFeedsTitleItemView.setText(QtGui.QApplication.translate("Settings", "display feed\'s title instead of item\'s one", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsUserAgent.setText(QtGui.QApplication.translate("Settings", "User agent", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsZoomFactor.setText(QtGui.QApplication.translate("Settings", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.spinSettingsZoomFactor.setSuffix(QtGui.QApplication.translate("Settings", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.groupOther.setTitle(QtGui.QApplication.translate("Settings", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsItemsToFetch.setText(QtGui.QApplication.translate("Settings", "Unread items to fetch by label", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "(and for each feed without label, and for special feeds)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBanner.setTitle(QtGui.QApplication.translate("Settings", "Informations banner", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSettingsBannerPosition.setText(QtGui.QApplication.translate("Settings", "Position", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(0, QtGui.QApplication.translate("Settings", "Top", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(1, QtGui.QApplication.translate("Settings", "Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.selectSettingsBannerPosition.setItemText(2, QtGui.QApplication.translate("Settings", "Never display", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSettingsBannerHide.setText(QtGui.QApplication.translate("Settings", "Hide after", None, QtGui.QApplication.UnicodeUTF8))
        self.spinSettingsBannerHideDelay.setSuffix(QtGui.QApplication.translate("Settings", "ms", None, QtGui.QApplication.UnicodeUTF8))
