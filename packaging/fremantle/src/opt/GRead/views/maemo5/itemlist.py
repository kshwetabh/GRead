# -*- coding: utf-8 -*-

"""
Item list view
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ..basic.itemlist import ItemListDelegate as BasicItemListDelegate
from ..mobile.itemlist import ItemListView as BasicItemListView

class ItemListDelegate(BasicItemListDelegate):
    
    def sizeHint(self, *args, **kwargs):
        """
        Maemo5 optimization : all rows are 70 pixel height
        """
        size = QStyledItemDelegate.sizeHint(self, *args, **kwargs)
        if size.height() != 70:
            size.setHeight(70)
        return size
        
class ItemListView(BasicItemListView):

    def get_itemlist_delegate_class(self):
        return ItemListDelegate
