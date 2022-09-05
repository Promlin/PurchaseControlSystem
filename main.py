import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class InitClass(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.resize(1300, 900)
        self.center()
        self.setWindowTitle('MainWindow')
        self.setWindowIcon(QIcon('icon.png'))

        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(button1)
        hlayout.addWidget(button2)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)

        tab_1 = QFrame()
        layout_tab_1 = QVBoxLayout()
        layout_tab_1.addLayout(vlayout)
        tab_1.setLayout(layout_tab_1)

        tab_2 = QFrame()
        layout_tab_2 = QVBoxLayout()
        tab_2.setLayout(layout_tab_2)

        self.tab = QTabWidget()
        self.tab.addTab(tab_1, "Base")
        self.tab.addTab(tab_2, "Addition")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    root = InitClass()
    root.show()

    sys.exit(app.exec_())