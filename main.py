import sys
from PyQt5.QtWidgets import *
from InitClass import InitClass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    root = InitClass()
    root.show()

    sys.exit(app.exec_())