import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class InitClass(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.resize(1300, 900)
        self.center()
        self.setWindowTitle('MainWindow')
        self.setWindowIcon(QIcon('icon.png'))

        # Creating ui for the first tab
        input_value_label = QLabel()
        input_value_label.setText("Полученная сумма: ")
        input_value_label.setFont(QFont('Times Font', 16))

        input_text_edit = QTextEdit()
        input_text_edit.setText("100")
        input_text_edit.setFont(QFont('Times Font', 16))
        input_text_edit.setFixedSize(150, 45)

        rest_label = QLabel()
        rest_label.setText("Сдача: ")
        rest_label.setFont(QFont('Times Font', 16))

        small_label_layout = QHBoxLayout()
        small_label_layout.addWidget(input_value_label)
        small_label_layout.addWidget(input_text_edit)
        small_label_layout.addStretch(1)
        small_label_layout.addWidget(rest_label)
        small_label_layout.addStretch(2)

        pre_sum_label = QLabel()
        pre_sum_label.setText("Подытог: ")
        pre_sum_label.setFont(QFont('Times Font', 16))

        discount_label = QLabel()
        discount_label.setText("Скидка: ")
        discount_label.setFont(QFont('Times Font', 16))

        discount_text_edit = QTextEdit()
        discount_text_edit.setText("0")
        discount_text_edit.setFont(QFont('Times Font', 16))
        discount_text_edit.setFixedSize(150, 45)

        discount_layout = QHBoxLayout()
        discount_layout.addWidget(discount_label)
        discount_layout.addWidget(discount_text_edit)
        discount_layout.addStretch(2)

        sum_label = QLabel()
        sum_label.setText("Итог: ")
        sum_label.setFont(QFont('Times Font', 16))

        label_layout = QVBoxLayout()
        label_layout.addStretch(1)
        label_layout.addWidget(pre_sum_label)
        label_layout.addLayout(discount_layout)
        label_layout.addWidget(sum_label)
        label_layout.addLayout(small_label_layout)

        table = QTableWidget()
        table.setFixedWidth(627)
        table.setFixedHeight(600)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Наименование", "Цена", "Количество", "Сумма"])

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(table)
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(label_layout)
        horizontal_layout.addStretch(6)

        close_button = QPushButton("Закрыть чек")
        close_button.setFont(QFont('Times Font', 16))
        close_button.setFixedHeight(50)
        close_layout = QHBoxLayout()
        close_layout.addWidget(close_button)

        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch(2)
        vertical_layout.addLayout(close_layout)

        # Creating UI for the third tab
        table_rest = QTableWidget()
        table_rest.setColumnCount(4)
        table_rest.setHorizontalHeaderLabels(["ID", "Наименование", "Цена", "Количество"])
        table_rest.setFixedWidth(502)
        table_rest.setFixedHeight(700)

        category_box = QComboBox()
        category_box.addItem("Все")
        category_box.addItem("Посуда")
        category_box.addItem("Удобрения")

        min_max_button = QPushButton("min - max")
        max_min_button = QPushButton("max - min")

        button_layout = QHBoxLayout()
        button_layout.addWidget(min_max_button)
        button_layout.addStretch(1)
        button_layout.addWidget(max_min_button)

        small_rest_layout = QVBoxLayout()
        small_rest_layout.addStretch(1)
        small_rest_layout.addWidget(category_box)
        small_rest_layout.addLayout(button_layout)
        small_rest_layout.addStretch(10)

        horizontal_layout_rest = QHBoxLayout()
        horizontal_layout_rest.addWidget(table_rest)
        horizontal_layout_rest.addStretch(1)
        horizontal_layout_rest.addLayout(small_rest_layout)
        horizontal_layout_rest.addStretch(8)

        # Adding tabs to ui
        tab_main = QFrame()
        layout_tab_main = QVBoxLayout()
        layout_tab_main.addLayout(vertical_layout)
        tab_main.setLayout(layout_tab_main)

        tab_adding = QFrame()
        layout_tab_adding = QVBoxLayout()
        tab_adding.setLayout(layout_tab_adding)

        tab_rest = QFrame()
        layout_tab_rest = QVBoxLayout()
        layout_tab_rest.addLayout(horizontal_layout_rest)
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
