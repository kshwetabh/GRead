# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from engine import settings

class ListModel(QAbstractListModel):
    def __init__(self, data, view):
        QAbstractListModel.__init__(self, view.win)
        self.view = view
        self.listdata   = data
        
    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)
        
    def row_of(self, item, start=0):
        row = None
        try:
            row = self.listdata.index(item)
        except:
            i = start
            for data in self.listdata[i:]:
                if data.id == item.id:
                    row = i
                    break
                i += 1
        return row
        
    def index_of(self, item, start=0):
        row = self.row_of(item, start)
        if row is not None:
            return self.index(row)
        return None
        
    def get_previous(self, item=None):
        if item is None:
            return None
        row = self.row_of(item)
        if row is None or row <= 0:
            return None
        try:
            return self.listdata[row-1]
        except:
            return None
        
    def get_next(self, item=None):
        if item is None:
            row = 0
        else:
            row = self.row_of(item)
            if row is None or row >= len(self.listdata)-1:
                return None
        try:
            return self.listdata[row + 1]
        except:
            return None

    #def removeRows(self, row, count, parent=QModelIndex()):
    #    self.beginRemoveRows(parent, row, row + count - 1)
    #    self.listdata = self.listdata[:row] + self.listdata[row+count:]
    #    self.endRemoveRows()

class WindowEventFilter(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                self.parent().view.set_focused()
        elif event.type() in (QEvent.KeyPress, QEvent.ShortcutOverride) \
            and event.key() in (Qt.Key_Backspace, Qt.Key_Escape):
            if self.parent().parent():
                self.parent().hide()
                return True

        return QObject.eventFilter(self, obj, event)
        
class BannerEventFilter(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.emit(SIGNAL("hide_banner"))
            return False            

        return QObject.eventFilter(self, obj, event)
        
        
class ViewEventFilter(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        
    def isShift(self, event):
        return event.modifiers() & Qt.ShiftModifier

    def eventFilter(self, obj, event):
        if self.preEventFilter(obj, event):
            return True
        return False
        
    def preEventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Space and self.isShift(event):
                self.emit(SIGNAL("trigger_filter_feeds"))
                return False
            elif key == Qt.Key_H:
                self.emit(SIGNAL("trigger_help"))
                return False
            elif key == Qt.Key_I:
                self.emit(SIGNAL("toggle_banner"))
                return False
        
    def postEventFilter(self, obj, event):
        return False

class View(object):
    def __init__(self, controller, ui, parent=None):
        """
        Initialize window
        """
        self.controller = controller
        self.controller.add_view(self)
        
        self.launched = False
        
        self.win = QMainWindow(parent, Qt.Window)

        self.win.view = self
        self.ui = ui()
        self.ui.setupUi(self.win)
        self.win.setWindowTitle(QApplication.applicationName())
        
        self.win.installEventFilter(WindowEventFilter(self.win))

        # banner 
        if settings.get('info', 'banner_position') == 'top':
            self.banner = self.ui.bannerTop
            self.ui.bannerBottom.hide()
        else:
            self.banner = self.ui.bannerBottom
            self.ui.bannerTop.hide()

        self.banner_animation = QPropertyAnimation(self.banner, 'maximumHeight')
        self.banner_animation.finished.connect(self.hide_banner)
        banner_event_filter = BannerEventFilter(self.win)
        self.ui.bannerTop.installEventFilter(banner_event_filter)
        self.ui.bannerBottom.installEventFilter(banner_event_filter)
        QObject.connect(banner_event_filter, SIGNAL("hide_banner"), self.hide_banner)
        
        # menu & events
        self.init_menu()
        self.post_init_menu()
        self.init_events()
        
    def get_menu_container(self):
        return self.ui.toolBar
        
    def init_menu(self):
        self.context_menu        = None
        self.context_menu_widget = None
        
    def post_init_menu(self):
        pass
        
    def init_events(self):
        QObject.connect(self.event_filter, SIGNAL("trigger_filter_feeds"), self.controller.trigger_filter_feeds)
        QObject.connect(self.event_filter, SIGNAL("trigger_help"), self.controller.trigger_help)
        QObject.connect(self.event_filter, SIGNAL("toggle_banner"), self.toggle_banner)
        
    def add_event_filter(self, widget, event_filter_class):
        self.event_filter = event_filter_class(self.win)
        widget.installEventFilter(self.event_filter)
        
    def toggle_banner(self):
        if self.banner.isVisible():
            if self.banner_animation.state() == QAbstractAnimation.Running:
                self.stop_banner_sliding()
                self.show_banner()
            else:
                self.hide_banner()
        else:
            self.show_banner()

    def display_banner(self, text):
        if not text or settings.get('info', 'banner_position') == 'hide':
            return
        self.stop_banner_sliding()
        self.banner.setText(text)
        self.show_banner()
        if settings.get('info', 'banner_hide'):
            self.start_banner_sliding()
            
    def banner_delay(self):
        delay = int(settings.get('info', 'banner_hide_delay'))
        len_text = len(self.banner.text())
        if len_text > 50:
            delay += 300 * int(len(self.banner.text())/50)
        return delay
            
    def start_banner_sliding(self):
        self.banner_animation.setEasingCurve(QEasingCurve.InExpo)
        self.banner_animation.setDuration(self.banner_delay())
        self.banner_animation.setStartValue(self.banner.maximumHeight())
        self.banner_animation.setEndValue(0)
        self.banner_animation.start()
        
    def stop_banner_sliding(self):
        self.banner_animation.stop()
            
    def show_banner(self):
        self.banner.show()
        height = self.banner.sizeHint().height()
        self.banner.setMaximumHeight(height)
            
    def hide_banner(self):
        if self.banner_animation.state() == QAbstractAnimation.Running:
            self.stop_banner_sliding()
        self.banner.hide()
        
    def show(self, app_just_launched=False):
        self.win.show()
        self.launched = True
        self.update_title()
        
    def make_context_menu(self, widget):
        """
        Create a context menu for the widget (the main widget for this view)
        """
        self.context_menu_widget = widget
        self.context_menu_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.context_menu_widget.customContextMenuRequested.connect(self.request_context_menu)
        self.context_menu = QMenu()
        
    def request_context_menu(self, pos):
        """
        Called when the user ask for the context menu to be displayed
        """
        pass
        
    def display_context_menu(self, pos):
        self.context_menu.exec_(self.context_menu_widget.mapToGlobal(pos))

    def settings_updated(self):
        old_banner = self.banner
        if settings.get('info', 'banner_position') == 'top':
            self.banner = self.ui.bannerTop
        else:
            self.banner = self.ui.bannerBottom
        if old_banner != self.banner:
            self.stop_banner_sliding()
            self.banner_animation.setTargetObject(self.banner)
            self.display_banner(old_banner.text())
            old_banner.setMaximumHeight(0)
            old_banner.hide()

    def get_title(self):
        return QApplication.applicationName()
        
    def update_title(self):
        self.title = self.get_title()
        if not self.title:
            self.title = QApplication.applicationName()
        operations_part = self.controller.get_title_operations_part()
        if operations_part:
            self.title = "%s - %s" % (self.title, operations_part)
        self.win.setWindowTitle(self.title)
        
    def set_focused(self):
        self.controller.set_current_view(self)

    def start_loading(self):
        pass
            
    def stop_loading(self):
        pass

    def display_message(self, message, level="information"):
        """
        Display a message for a level ([information|warning|critical])
        """
        box = QMessageBox(self.win)
        box.setText(message)
        box.setWindowTitle(QApplication.applicationName())
        if level == "critical":
            box.setIcon(QMessageBox.Critical)
        elif level == "warning":
            box.setIcon(QMessageBox.Warning)
        else:
            box.setIcon(QMessageBox.Information)
        box.exec_()

class Dialog(object):
    def __init__(self, controller):
        self.controller = controller
        self.created = False

    def get_ui_class(self):
        pass
        
    def create(self):
        self.win = QDialog()
        self.ui = self.get_ui_class()()
        self.ui.setupUi(self.win)
        self.win.setWindowTitle(self.get_title())
        self.created = True
        
    def get_title(self):
        return QApplication.applicationName()

    def before_open(self):
        pass
        
    def after_close(self):
        pass
        
    def open(self):
        # create dialog
        if not self.created:
            self.create()
        self.before_open()
        self.win.exec_()
        self.after_close()

base_view_class = View
base_eventfilter_class = ViewEventFilter
