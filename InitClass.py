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

        table = QTableWidget(self)
        table.setFixedWidth(628)
        table.setFixedHeight(800)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Наименование", "Цена", "Количество", "Сумма"])

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(button1)
        hlayout.addWidget(button2)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addWidget(table)
        vlayout.addStretch(2)
        vlayout.addLayout(hlayout)

        tab_main = QFrame()
        layout_tab_main = QVBoxLayout()
        layout_tab_main.addLayout(vlayout)
        tab_main.setLayout(layout_tab_main)

        tab_adding = QFrame()
        layout_tab_adding = QVBoxLayout()
        tab_adding.setLayout(layout_tab_adding)

        tab_rest = QFrame()
        layout_tab_rest = QVBoxLayout()
        tab_rest.setLayout(layout_tab_rest)

        tab_hand = QFrame()
        layout_tab_hand = QVBoxLayout()
        tab_hand.setLayout(layout_tab_hand)

        tab_stats = QFrame()
        layout_tab_stats = QVBoxLayout()
        tab_stats.setLayout(layout_tab_stats)

        tab_end = QFrame()
        layout_tab_end = QVBoxLayout()
        tab_end.setLayout(layout_tab_end)

        self.tab = QTabWidget()
        self.tab.addTab(tab_main, "Рабочий режим")
        self.tab.addTab(tab_adding, "Добавление товара")
        self.tab.addTab(tab_rest, "Просмотр остатков")
        self.tab.addTab(tab_hand, "Ручной ввод")
        self.tab.addTab(tab_stats, "Статистика")
        self.tab.addTab(tab_end, "Конец дня")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)




    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
