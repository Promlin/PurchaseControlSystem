from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SecondExample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1300, 900)
        self.center()
        self.setWindowTitle('MainWindow')
        self.setWindowIcon(QIcon('icon.png'))

        # Adding tabs to ui
        tab_1 = QFrame()
        layout_tab_1 = QVBoxLayout()
        vertical_layout_base = self.init_first_tab()
        layout_tab_1.addLayout(vertical_layout_base)
        tab_1.setLayout(layout_tab_1)

        tab_2 = QFrame()
        layout_tab_2 = QVBoxLayout()
        vertical_layout_add = self.init_second_tab()
        layout_tab_2.addLayout(vertical_layout_add)
        tab_2.setLayout(layout_tab_2)

        tab_3 = QFrame()
        layout_tab_3 = QVBoxLayout()
        horizontal_layout_rest = self.init_third_tab()
        layout_tab_3.addLayout(horizontal_layout_rest)
        tab_3.setLayout(layout_tab_3)

        tab_4 = QFrame()
        layout_tab_4 = QVBoxLayout()
        tab_4.setLayout(layout_tab_4)

        tab_5 = QFrame()
        layout_tab_5 = QVBoxLayout()
        layout_current = self.init_fifth_tab()
        layout_tab_5.addLayout(layout_current)
        tab_5.setLayout(layout_tab_5)

        tab_6 = QFrame()
        layout_tab_6 = QVBoxLayout()
        tab_6.setLayout(layout_tab_6)

        self.tab = QTabWidget()
        self.tab.addTab(tab_1, "Base")
        self.tab.addTab(tab_2, "Adding")
        self.tab.addTab(tab_3, "Rest")
        self.tab.addTab(tab_4, "Hand")
        self.tab.addTab(tab_5, "Current Day")
        self.tab.addTab(tab_6, "End")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)

    def init_first_tab(self):
        # Creating ui for the first tab
        input_value_label = QLabel()
        input_value_label.setText("Value: ")
        input_value_label.setFont(QFont('Times Font', 13))
        input_textedit = QTextEdit()
        input_textedit.setText("100")
        input_textedit.setFont(QFont('Times Font', 13))
        input_textedit.setFixedSize(150, 45)
        rest_label = QLabel()
        rest_label.setText("Rest: ")
        rest_label.setFont(QFont('Times Font', 13))

        small_label_layout = QHBoxLayout()
        small_label_layout.addWidget(input_value_label)
        small_label_layout.addWidget(input_textedit)
        small_label_layout.addStretch(1)
        small_label_layout.addWidget(rest_label)
        small_label_layout.addStretch(2)

        pre_sum_label = QLabel()
        pre_sum_label.setText("Pre-Sum: ")
        pre_sum_label.setFont(QFont('Times Font', 13))

        discount_label = QLabel()
        discount_label.setText("Discount")
        discount_label.setFont(QFont('Times Font', 13))

        sum_label = QLabel()
        sum_label.setText("Sum: ")
        sum_label.setFont(QFont('Times Font', 13))

        label_layout = QVBoxLayout()
        label_layout.addStretch(1)
        label_layout.addWidget(pre_sum_label)
        label_layout.addWidget(discount_label)
        label_layout.addWidget(sum_label)
        label_layout.addLayout(small_label_layout)

        table_base = QTableWidget()
        table_base.setFont(QFont('Times Font', 13))
        table_base.setColumnCount(5)
        table_base.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3", "Header 4", "Header 5"])
        table_base.setFixedWidth(627)
        table_base.setFixedHeight(600)

        horizontal_layout_base = QHBoxLayout()
        horizontal_layout_base.addWidget(table_base)
        horizontal_layout_base.addStretch(1)
        horizontal_layout_base.addLayout(label_layout)
        horizontal_layout_base.addStretch(6)

        close_button = QPushButton('Close Check')
        close_button.setFixedHeight(50)
        close_layout = QHBoxLayout()
        close_layout.addWidget(close_button)

        vertical_layout_base = QVBoxLayout()
        vertical_layout_base.addStretch(1)
        vertical_layout_base.addLayout(horizontal_layout_base)
        vertical_layout_base.addStretch(2)
        vertical_layout_base.addLayout(close_layout)

        return vertical_layout_base

    def init_second_tab(self):
        # Creating UI for the second tab
        start_add_button = QPushButton("Start")
        self.set_text_style(start_add_button)
        start_add_layout = QHBoxLayout()
        start_add_layout.addStretch(1)
        start_add_layout.addWidget(start_add_button)
        start_add_layout.addStretch(15)

        id_add_label = QLabel("ID")
        self.set_text_style(id_add_label)

        title_add_label = QLabel("Title")
        self.set_text_style(title_add_label)

        price_add_label = QLabel("Price")
        self.set_text_style(price_add_label)

        amount_add_label = QLabel("Amount")
        self.set_text_style(amount_add_label)

        category_add_label = QLabel("Category")
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
        category_add_combo_box.addItem("All")
        category_add_combo_box.addItem("Dish")
        category_add_combo_box.addItem("Ground")

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

        add_add_button = QPushButton("Add")
        self.set_text_style(add_add_button)
        add_button_layout = QHBoxLayout()
        add_button_layout.addStretch(1)
        add_button_layout.addWidget(add_add_button)
        add_button_layout.addStretch(15)

        table_add = QTableWidget()
        table_add.setFont(QFont('Times Font', 13))
        table_add.setColumnCount(5)
        table_add.setHorizontalHeaderLabels(["Id", "Title", "Price", "Amount", "Category"])
        table_add.setFixedWidth(627)
        table_add.setFixedHeight(400)

        table_add_layout = QHBoxLayout()
        table_add_layout.addStretch(1)
        table_add_layout.addWidget(table_add)
        table_add_layout.addStretch(8)

        add_all_add_button = QPushButton("Add all")
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
        table_rest.setHorizontalHeaderLabels(["Id", "Title", "Price", "Rest"])
        table_rest.setFixedWidth(502)
        table_rest.setFixedHeight(700)

        category_box = QComboBox()
        category_box.setFont(QFont('Times Font', 13))
        category_box.addItem("All")
        category_box.addItem("first")
        category_box.addItem("second")

        min_max_button = QPushButton("min - max")
        min_max_button.setFont(QFont('Times Font', 13))
        max_min_button = QPushButton("max - min")
        max_min_button.setFont(QFont('Times Font', 13))

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

        checks_label = QLabel("Checks")
        self.set_text_style(checks_label)

        checks_table = QTableWidget()
        checks_table.setFont(QFont('Times Font', 13))
        checks_table.setColumnCount(4)
        checks_table.setHorizontalHeaderLabels(["Time", "Check", "Positions", "Sum"])
        checks_table.setFixedWidth(502)
        checks_table.setFixedHeight(400)

        checks_layout = QVBoxLayout()
        checks_layout.addWidget(checks_label)
        checks_layout.addWidget(checks_table)

        positions_label = QLabel("Positions")
        self.set_text_style(positions_label)

        positions_table = QTableWidget()
        positions_table.setFont(QFont('Times Font', 13))
        positions_table.setColumnCount(4)
        positions_table.setHorizontalHeaderLabels(["Title", "Price", "Amount", "Sum"])
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

        sort_label = QLabel("Sorted")
        self.set_text_style(sort_label)

        category_box = QComboBox()
        self.set_text_style(category_box)
        category_box.addItem("All")
        category_box.addItem("first")
        category_box.addItem("second")

        category_small_layout = QHBoxLayout()
        category_small_layout.addWidget(sort_label)
        category_small_layout.addStretch(1)
        category_small_layout.addWidget(category_box)
        category_small_layout.addStretch(1)

        sorted_table = QTableWidget()
        sorted_table.setFont(QFont('Times Font', 13))
        sorted_table.setColumnCount(4)
        sorted_table.setHorizontalHeaderLabels(["Title", "Price", "Amount", "Rest"])
        sorted_table.setFixedWidth(502)
        sorted_table.setFixedHeight(400)

        category_layout = QVBoxLayout()
        category_layout.addLayout(category_small_layout)
        category_layout.addWidget(sorted_table)

        check_sum_label = QLabel("Check sum")
        self.set_text_style(check_sum_label)

        cash_label = QLabel("Cash")
        self.set_text_style(cash_label)

        online_label = QLabel("Online")
        self.set_text_style(online_label)

        sum_label = QLabel("Sum")
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
