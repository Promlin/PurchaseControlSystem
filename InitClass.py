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

        # Adding tabs to ui
        tab_main = QFrame()
        vertical_layout = self.init_base_tab()
        tab_main.setLayout(vertical_layout)

        tab_adding = QFrame()
        layout_tab_adding = self.init_second_tab()
        tab_adding.setLayout(layout_tab_adding)

        tab_rest = QFrame()
        horizontal_layout_rest = self.init_third_tab()
        tab_rest.setLayout(horizontal_layout_rest)

        tab_hand = QFrame()
        layout_tab_hand = QVBoxLayout()
        tab_hand.setLayout(layout_tab_hand)

        tab_stats = QFrame()
        layout_tab_stats = self.init_fifth_tab()
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

    def init_base_tab(self):
        # Creating ui for the first tab
        input_value_label = QLabel()
        input_value_label.setText("Полученная сумма: ")
        input_value_label.setFont(QFont('Times Font', 13))

        input_text_edit = QTextEdit()
        input_text_edit.setText("100")
        input_text_edit.setFont(QFont('Times Font', 13))
        input_text_edit.setFixedSize(150, 45)

        rest_label = QLabel()
        rest_label.setText("Сдача: ")
        rest_label.setFont(QFont('Times Font', 13))

        small_label_layout = QHBoxLayout()
        small_label_layout.addWidget(input_value_label)
        small_label_layout.addWidget(input_text_edit)
        small_label_layout.addStretch(1)
        small_label_layout.addWidget(rest_label)
        small_label_layout.addStretch(2)

        pre_sum_label = QLabel()
        pre_sum_label.setText("Подытог: ")
        pre_sum_label.setFont(QFont('Times Font', 13))

        discount_label = QLabel()
        discount_label.setText("Скидка: ")
        discount_label.setFont(QFont('Times Font', 13))

        discount_text_edit = QTextEdit()
        discount_text_edit.setText("0")
        discount_text_edit.setFont(QFont('Times Font', 13))
        discount_text_edit.setFixedSize(150, 45)

        discount_layout = QHBoxLayout()
        discount_layout.addWidget(discount_label)
        discount_layout.addWidget(discount_text_edit)
        discount_layout.addStretch(2)

        sum_label = QLabel()
        sum_label.setText("Итог: ")
        sum_label.setFont(QFont('Times Font', 13))

        label_layout = QVBoxLayout()
        label_layout.addStretch(1)
        label_layout.addWidget(pre_sum_label)
        label_layout.addLayout(discount_layout)
        label_layout.addWidget(sum_label)
        label_layout.addLayout(small_label_layout)

        table = QTableWidget()
        table.setFont(QFont('Times Font', 13))
        table.setFixedWidth(627)
        table.setFixedHeight(600)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Количество", "Сумма"])

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(table)
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(label_layout)
        horizontal_layout.addStretch(6)

        close_button = QPushButton("Закрыть чек")
        close_button.setFont(QFont('Times Font', 13))
        close_button.setFixedHeight(50)
        close_layout = QHBoxLayout()
        close_layout.addWidget(close_button)

        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch(2)
        vertical_layout.addLayout(close_layout)

        return vertical_layout

    def init_second_tab(self):

        # Creating UI for the second tab
        start_add_button = QPushButton("Добавить")
        self.set_text_style(start_add_button)
        start_add_layout = QHBoxLayout()
        start_add_layout.addStretch(1)
        start_add_layout.addWidget(start_add_button)
        start_add_layout.addStretch(15)

        id_add_label = QLabel("ID")
        self.set_text_style(id_add_label)

        title_add_label = QLabel("Название")
        self.set_text_style(title_add_label)

        price_add_label = QLabel("Цена")
        self.set_text_style(price_add_label)

        amount_add_label = QLabel("Количество")
        self.set_text_style(amount_add_label)

        category_add_label = QLabel("Категория")
        self.set_text_style(category_add_label)

        label_add_layout = QHBoxLayout()
        label_add_layout.addStretch(4)
        label_add_layout.addWidget(id_add_label)
        label_add_layout.addStretch(1)
        label_add_layout.addWidget(title_add_label)
        label_add_layout.addStretch(1)
        label_add_layout.addWidget(price_add_label)
        label_add_layout.addStretch(1)
        label_add_layout.addWidget(amount_add_label)
        label_add_layout.addStretch(1)
        label_add_layout.addWidget(category_add_label)
        label_add_layout.addStretch(20)

        id_add_textedit = QTextEdit()
        self.set_text_style(id_add_textedit)

        title_add_textedit = QTextEdit()
        self.set_text_style(title_add_textedit)

        price_add_textedit = QTextEdit()
        self.set_text_style(price_add_textedit)

        amount_add_textedit = QTextEdit()
        self.set_text_style(amount_add_textedit)

        category_add_combo_box = QComboBox()
        self.set_text_style(category_add_combo_box)
        category_add_combo_box.addItem("Все")
        category_add_combo_box.addItem("Посуда")
        category_add_combo_box.addItem("Удобрения")

        button_add_layout = QHBoxLayout()
        button_add_layout.addStretch(4)
        button_add_layout.addWidget(id_add_textedit)
        button_add_layout.addStretch(1)
        button_add_layout.addWidget(title_add_textedit)
        button_add_layout.addStretch(1)
        button_add_layout.addWidget(price_add_textedit)
        button_add_layout.addStretch(1)
        button_add_layout.addWidget(amount_add_textedit)
        button_add_layout.addStretch(1)
        button_add_layout.addWidget(category_add_combo_box)
        button_add_layout.addStretch(20)

        add_add_button = QPushButton("Добавить")
        self.set_text_style(add_add_button)
        add_button_layout = QHBoxLayout()
        add_button_layout.addStretch(1)
        add_button_layout.addWidget(add_add_button)
        add_button_layout.addStretch(15)

        table_add = QTableWidget()
        table_add.setFont(QFont('Times Font', 13))
        table_add.setColumnCount(5)
        table_add.setHorizontalHeaderLabels(["Id", "Название", "Цена", "Количество", "Категория"])
        table_add.setFixedWidth(627)
        table_add.setFixedHeight(400)

        table_add_layout = QHBoxLayout()
        table_add_layout.addStretch(1)
        table_add_layout.addWidget(table_add)
        table_add_layout.addStretch(8)

        add_all_add_button = QPushButton("Добавить все")
        add_all_add_button.setFont(QFont('Times Font', 13))
        add_all_add_button.setFixedHeight(50)

        vertical_layout_add = QVBoxLayout()
        vertical_layout_add.addStretch(1)
        vertical_layout_add.addLayout(start_add_layout)
        vertical_layout_add.addStretch(1)
        vertical_layout_add.addLayout(label_add_layout)
        vertical_layout_add.addLayout(button_add_layout)
        vertical_layout_add.addStretch(1)
        vertical_layout_add.addLayout(add_button_layout)
        vertical_layout_add.addStretch(3)
        vertical_layout_add.addLayout(table_add_layout)
        vertical_layout_add.addStretch(1)
        vertical_layout_add.addWidget(add_all_add_button)

        return vertical_layout_add

    def init_third_tab(self):
        # Creating UI for the third tab
        table_rest = QTableWidget()
        table_rest.setFont(QFont('Times Font', 13))
        table_rest.setColumnCount(4)
        table_rest.setHorizontalHeaderLabels(["ID", "Название", "Цена", "Количество"])
        table_rest.setFixedWidth(502)
        table_rest.setFixedHeight(700)

        category_box = QComboBox()
        self.set_text_style(category_box)
        category_box.addItem("Все")
        category_box.addItem("Посуда")
        category_box.addItem("Удобрения")

        min_max_button = QPushButton("min - max")
        self.set_text_style(min_max_button)
        max_min_button = QPushButton("max - min")
        self.set_text_style(max_min_button)

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

        return horizontal_layout_rest

    def init_fifth_tab(self):

        checks_label = QLabel("Чеки")
        self.set_text_style(checks_label)

        checks_table = QTableWidget()
        checks_table.setFont(QFont('Times Font', 13))
        checks_table.setColumnCount(4)
        checks_table.setHorizontalHeaderLabels(["Время", "Номер", "Позиций", "Сумма"])
        checks_table.setFixedWidth(502)
        checks_table.setFixedHeight(400)

        checks_layout = QVBoxLayout()
        checks_layout.addWidget(checks_label)
        checks_layout.addWidget(checks_table)

        positions_label = QLabel("Позиции")
        self.set_text_style(positions_label)

        positions_table = QTableWidget()
        positions_table.setFont(QFont('Times Font', 13))
        positions_table.setColumnCount(4)
        positions_table.setHorizontalHeaderLabels(["Название", "Цена", "Количество", "Сумма"])
        positions_table.setFixedWidth(502)
        positions_table.setFixedHeight(400)

        positions_layout = QVBoxLayout()
        positions_layout.addWidget(positions_label)
        positions_layout.addWidget(positions_table)

        first_part_layout = QHBoxLayout()
        first_part_layout.addLayout(checks_layout)
        first_part_layout.addStretch(1)
        first_part_layout.addLayout(positions_layout)
        first_part_layout.addStretch(1)

        sort_label = QLabel("Сортировка")
        self.set_text_style(sort_label)

        category_box = QComboBox()
        self.set_text_style(category_box)
        category_box.addItem("Все")
        category_box.addItem("Удобрения")
        category_box.addItem("Посуда")

        category_small_layout = QHBoxLayout()
        category_small_layout.addWidget(sort_label)
        category_small_layout.addStretch(1)
        category_small_layout.addWidget(category_box)
        category_small_layout.addStretch(1)

        sorted_table = QTableWidget()
        sorted_table.setFont(QFont('Times Font', 13))
        sorted_table.setColumnCount(4)
        sorted_table.setHorizontalHeaderLabels(["Название", "Цена", "Количество", "Остаток"])
        sorted_table.setFixedWidth(502)
        sorted_table.setFixedHeight(400)

        category_layout = QVBoxLayout()
        category_layout.addLayout(category_small_layout)
        category_layout.addWidget(sorted_table)

        check_sum_label = QLabel("Сумма чека")
        self.set_text_style(check_sum_label)

        cash_label = QLabel("Наличные")
        self.set_text_style(cash_label)

        online_label = QLabel("Безнал")
        self.set_text_style(online_label)

        sum_label = QLabel("Сумма")
        self.set_text_style(sum_label)

        labels_layout = QVBoxLayout()
        labels_layout.addWidget(check_sum_label)
        labels_layout.addStretch(1)
        labels_layout.addWidget(cash_label)
        labels_layout.addWidget(online_label)
        labels_layout.addWidget(sum_label)
        labels_layout.addStretch(1)

        second_part_layout = QHBoxLayout()
        second_part_layout.addLayout(category_layout)
        second_part_layout.addStretch(1)
        second_part_layout.addLayout(labels_layout)
        second_part_layout.addStretch(1)

        layout = QVBoxLayout()
        layout.addLayout(first_part_layout)
        layout.addStretch(1)
        layout.addLayout(second_part_layout)

        return layout

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_text_style(self, item):
        item.setFont(QFont('Times Font', 13))
        item.setFixedSize(150, 37)
