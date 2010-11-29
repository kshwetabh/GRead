#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication

from engine import settings
from views import Controller
from storage.backends.sqlite import Storage

import sys
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    settings.load()
    controller = Controller()
    controller.init_storage(Storage)
    controller.run()
    result = app.exec_()
    sys.exit(result)


