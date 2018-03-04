# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(350, 250)
widget.setWindowTitle(u'第一个窗口')
widget.show()
sys.exit(app.exec_())