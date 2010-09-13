# -*- coding: utf-8 -*-

"""
Feed list view
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *
    
from views.maemo5.ui.Ui_itemlist import Ui_winItemList
from views.maemo5 import MAEMO5_PRESENT, ListModel, View

from engine import settings
from engine.models import *

class ItemListDelegate(QStyledItemDelegate):
    
    def current_special_feed(self, view):
        if isinstance(view.current_feed, (SpecialFeed, CategoryFeed, )):
            return view.current_feed
        return None
    
    def sizeHint(self, option, index):
        size = super(ItemListDelegate, self).sizeHint(option, index)
        try:
            model = index.model()
            item = model.listdata[index.row()]
            if self.current_special_feed(model.view):
                metrics = QFontMetrics(option.font)
                min_height = int(metrics.height() * 1.8) * 1.1
                if size.height() < min_height:
                    size.setHeight(min_height)
        except:
            pass
        return size

    def paint(self, painter, option, index):
        """
        Paint the list item with the default options, and bold unread items
        """
        painter.save()

        try:            
            model = index.model()
            item = model.listdata[index.row()]

            styleOption = QStyleOptionViewItemV4(option)
            styleOption.text = item.title
            if item.unread:
                styleOption.font.setWeight(QFont.Bold)

            special_feed = self.current_special_feed(model.view)

            if special_feed:
                styleOption.displayAlignment = Qt.AlignTop | Qt.AlignLeft

            self.parent().style().drawControl(QStyle.CE_ItemViewItem, styleOption, painter)

            if special_feed:
                text = ''
                if special_feed == item.account.special_category.special_feeds['broadcast-friends']:
                    friend = item.g_item.data['via'][0]['title'].rstrip("'s shared items")
                    try:
                        text = "by %s (%s)" % (friend, item.normal_feeds[0].title)
                    except:
                        text = "by %s" % friend
                elif special_feed == item.account.special_category.special_feeds['created']:
                    # TODO: use something better than g_item here !!!
                    text = item.g_item.data['origin']['title']
                else:
                    try:
                        text = item.normal_feeds[0].title
                    except:
                        # TODO: use something better than g_item here !!!
                        text = item.g_item.data['origin']['title']

                if text:
                    styleOption2 = QStyleOptionViewItemV4(option)
                    font = styleOption2.font
                    font.setPointSizeF(font.pointSizeF() * 0.8)
                    font.setStyle(QFont.StyleItalic)
                    font.setWeight(QFont.Normal)
                    painter.setFont(font)

                    rect = styleOption2.rect
                    painter.drawText(rect, Qt.AlignBottom | Qt.AlignLeft, text)
                    rect.adjust(3, 0, 0, -int(rect.size().height()*0.1))

        finally:
            painter.restore()
            
class ItemListModel(ListModel):
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()].title)
        else:
            return QVariant()


class ItemListEventFilter(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type()  == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_A and event.modifiers() & Qt.ShiftModifier:
                self.emit(SIGNAL("mark_all_read"))
                return True
            elif key == Qt.Key_R:
                self.emit(SIGNAL("refresh"))
                return True
            elif key == Qt.Key_F:
                self.emit(SIGNAL("fetch_more"))
                return True
        return QObject.eventFilter(self, obj, event)

class ItemListView(View):
    def __init__(self, controller):
        super(ItemListView, self).__init__(controller, Ui_winItemList, controller.feedlist_view.win)

        self.current_feed  = None
        self.selected_item = None

        self.unread_only_default = True
        self.show_mode_save      = True
        self.settings_updated()

        # menu bar

        self.add_orientation_menu()

        # menu boutons : group for show all/updated
        self.group_show = QActionGroup(self.win)
        self.action_show_all = QAction("Show all", self.group_show)
        self.action_show_all.setCheckable(True)
        self.action_show_unread_only = QAction("Unread only", self.group_show)
        self.action_show_unread_only.setCheckable(True)
        if self.unread_only_default:
            self.action_show_unread_only.setChecked(True)
        else:
            self.action_show_all.setChecked(True)
        self.ui.menuBar.addActions(self.group_show.actions())
        self.action_show_unread_only.toggled.connect(self.toggle_unread_only)

        # other menu boutons
        self.action_refresh = QAction("Refresh", self.win)
        self.action_refresh.setObjectName('actionRefresh')
        self.ui.menuBar.addAction(self.action_refresh)
        self.action_refresh.triggered.connect(self.trigger_refresh)

        self.action_fetch_more = QAction("Fetch more", self.win)
        self.action_fetch_more.setObjectName('actionFetchMore')
        self.ui.menuBar.addAction(self.action_fetch_more)
        self.action_fetch_more.triggered.connect(self.trigger_fetch_more)

        self.action_mark_all_read = QAction("Mark all as read", self.win)
        self.action_mark_all_read.setObjectName('actionMarkAllRead')
        self.ui.menuBar.addAction(self.action_mark_all_read)
        self.action_mark_all_read.triggered.connect(self.trigger_mark_all_read)

        # item list
        ilm = ItemListModel(data=[], view=self)
        ild = ItemListDelegate(self.win)
        self.ui.listItemList.setModel(ilm)
        self.ui.listItemList.setItemDelegate(ild)
        self.ui.listItemList.activated.connect(self.activate_item)

        # events
        self.eventFilter = ItemListEventFilter(self.win)
        #self.win.installEventFilter(self.eventFilter)
        self.ui.listItemList.installEventFilter(self.eventFilter)
        QObject.connect(self.eventFilter, SIGNAL("mark_all_read"), self.trigger_mark_all_read)
        QObject.connect(self.eventFilter, SIGNAL("refresh"), self.trigger_refresh)
        QObject.connect(self.eventFilter, SIGNAL("fetch_more"), self.trigger_fetch_more)


    @property
    def show_unread_only(self):
        """
        Return true if this feed must show only unread items
        """
        return getattr(self.current_feed, 'unread_only', self.unread_only_default)

    @property
    def can_fetch_more(self):
        return self.current_feed.can_fetch_more(self.show_unread_only)

    def toggle_unread_only(self, checked):
        """
        Action when the "unread only" button is checked or unchecked
        """
        self.get_selected()
        self.current_feed.unread_only = checked
        self.update_item_list()
        
    def get_selected(self, item=None):
        """
        Save the current selected item for select it back when the list will
        be refreshed
        """
        if item is None:
            try:
                index = self.ui.listItemList.selectedIndexes()[0]
            except:
                pass
            else:
                item = index.model().listdata[index.row()]
        if item is not None:
            self.selected_item = item
        
    def set_selected(self, item=None):
        """
        Try to restore the selected item in the list
        """
        if item is None:
            item = self.selected_item
        else:
            self.selected_item = item
        if item:
            index = self.ui.listItemList.model().index_of(item)
            if index:
                self.ui.listItemList.setCurrentIndex(index)
        
    def trigger_refresh(self):
        """
        Called when the refresh button is called
        """
        self.get_selected()
        self.manage_menu_bar(hide_menu=True)
        self.current_feed.fetch_content(unread_only=self.show_unread_only)
            
    def trigger_fetch_more(self):
        """
        Called when the "fetch more" button is called
        """
        self.get_selected()
        self.manage_menu_bar(hide_menu=True)
        self.current_feed.fetch_more_content(unread_only=self.show_unread_only)
        
    def set_current_feed(self, feed):
        """
        Set the current item as the on selected in the list
        """
        self.update_listview(content=[])
        self.current_feed = feed
        self.manage_menu_bar()
        self.update_title()
        self.update_item_list()
        return True
        
    def manage_menu_bar(self, hide_menu=None):
        """
        Hide the menu bar if a operation is currently running or waiting 
        for this feed (or a category_feed in which it is present)
        """
        if hide_menu is None:
            hide_menu = False
        if not hide_menu:
            if not self.current_feed:
                hide_menu = True
            else:
                if self.current_feed.is_loading:
                    hide_menu = True
                else:
                    for category in self.current_feed.categories:
                        if category.category_feed and category.category_feed.is_loading:
                            hide_menu = True
                            break
        # display show mode
        if self.show_unread_only:
            self.action_show_unread_only.setChecked(True)
        else:
            self.action_show_all.setChecked(True)
        # hide mark as read if needed
        self.action_mark_all_read.setDisabled(not self.current_feed.unread)
        # hide fetch more if needed
        self.action_fetch_more.setDisabled(not self.can_fetch_more)
        # hide menu bar if needed
        self.ui.menuBar.setDisabled(hide_menu)
        # and then manage loading animation
        if hide_menu:
            self.start_loading()
        else:
            self.stop_loading()
        
    def get_title(self):
        """
        Get the title for this view : the feed title and the unread count
        """
        title = ""
        if self.current_feed:
            if self.current_feed.unread:
                title = "%s (%d)" % (self.current_feed.title, self.current_feed.unread)
            else:
                title = self.current_feed.title
        return title
        
    def update_item_list(self):
        """
        Empty and then refill the items' feed with current options
        """
        self.update_listview(content=self.current_feed.get_items(unread_only=self.show_unread_only))
        self.set_selected()
        self.action_fetch_more.setDisabled(not self.can_fetch_more)
        
    def feed_content_fetching_started(self, feed):
        """
        Called when a feed content fetching operation begins
        """
        if not self.current_feed:
            return
        if isinstance(feed, CategoryFeed):
            if self.current_feed not in feed.categories[0].feeds:
                return
        elif feed != self.current_feed:
            return
        self.manage_menu_bar(hide_menu=True)
        
    def feed_content_fetched(self, feed):
        """
        Called when a feed content was just fetched, to redraw the ui
        """
        if not self.current_feed:
            return
        if isinstance(feed, CategoryFeed):
            if self.current_feed not in feed.categories[0].feeds:
                return
        elif feed != self.current_feed:
            return
        self.get_selected()
        self.update_item_list()
        self.manage_menu_bar()

    def update_listview(self, content=[]):
        """
        Update the list with feed's items
        """
        old_model = self.ui.listItemList.model()
        model = ItemListModel(data=content, view=self)
        self.ui.listItemList.setModel(model)
        del old_model
        
    def activate_item(self, index):
        """
        Called when the list in clicked, to display the item selected
        """
        item = index.model().listdata[index.row()]
        self.get_selected(item)
        self.controller.display_item(item)
        
    def activate_next_item(self):
        """
        Activate the item just after the current one in the list.
        Used with keyboard shortcuts
        """
        item = self.ui.listItemList.model().get_next(self.selected_item)
        if item:
            self.set_selected(item)
            self.controller.display_item(item)
        else:
            if self.can_fetch_more:
                self.controller.display_message("No more message, please fetch more !")
            else:
                self.controller.display_message("No more message !")

    def activate_previous_item(self):
        """
        Activate the item just before the current one in the list.
        Used with keyboard shortcuts
        """
        item = self.ui.listItemList.model().get_previous(self.selected_item)
        if item:
            self.set_selected(item)
            self.controller.display_item(item)
        else:
            self.controller.display_message("No more message, you're at the top of the list")
        
    def settings_updated(self):
        """
        Called when settings are updated
        """
        super(ItemListView,  self).settings_updated()
        show_mode = str(settings.get('items', 'show_mode'))
        self.unread_only_default = show_mode.find('unread') != -1
        self.show_mode_save      = show_mode.find('nosave') == -1

    def update_item(self, item):
        """
        Called when a category is updated, to refresh it's entry in the list, 
        and it's category_feed if it has one
        """
        try:
            index = self.ui.listItemList.model().index_of(item)
            # TODO: missing a way to insert row, don't know how to add data with insertRows
            # see https://svn.enthought.com/svn/enthought/TraitsBackendQt/trunk/enthought/traits/ui/qt4/list_str_model.py
            #if item.isRead() and self.show_updated_only():
            #    self.ui.listItemList.model().removeRow(index.row())
            #else:
            self.ui.listItemList.update(index)
        except:
            pass
        self.update_title()

    def trigger_mark_all_read(self):
        """
        Called when the button "mark all as read" is activated
        """
        self.current_feed.mark_as_read()
        self.controller.feed_read(self.current_feed)
        
    def feed_read(self, feed):
        """
        Visually update all the items in the list
        """
        if feed != self.current_feed:
            return
        self.action_mark_all_read.setDisabled(True)
        for item in self.current_feed.get_items():
            self.update_item(item)
        
    def item_read(self, item):
        """
        Called when an item the unread/read status of an item is changed, to 
        visually update it in the list
        """
        self.update_item(item)
        
    def item_shared(self, item):
        """
        Called when an item the shared status of an item is changed, to 
        visually update it in the list
        """
        self.update_item(item)
        
    def item_starred(self, item):
        """
        Called when an item the starred status of an item is changed, to 
        visually update it in the list
        """
        self.update_item(item)
