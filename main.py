import sys
print(sys.path)
from source import main_window_pane
from PyQt5 import QtWidgets



app = QtWidgets.QApplication(sys.argv)
main_window = main_window_pane.MainWindowPane()
main_window.show()
sys.exit(app.exec_())
