from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QDialog, QComboBox, QTextEdit, QPushButton, QHBoxLayout, QLabel)
from PySide6.QtCore import QDate, QSize
from PySide6.QtGui import QTextCharFormat, QColor

CATEGORY_COLORS = {
    "家": QColor('pink'),
    "学校": QColor('palegreen'),
    "職場": QColor('sandybrown'),
    "プライベート": QColor('mediumpurple'),
    "その他":QColor('gray'),
}


class ScheduleDialog(QDialog):
    def __init__(self, date, schedule_data, category_index=0, parent=None):
        super().__init__(parent)
        self.selected_date = date
        self.schedule_data = schedule_data
        self.setWindowTitle("予定の追加")
        self.setGeometry(100, 100, 400, 200)
        self.layout = QVBoxLayout(self)

        # 分類を選ぶためのコンボボックス
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(["家", "学校", "職場", "プライベート","その他"])
        self.category_combobox.setCurrentIndex(category_index)
        self.layout.addWidget(self.category_combobox)

        # 予定の詳細を入力するためのラベル
        self.details_label = QLabel("予定の詳細を入力:")
        self.layout.addWidget(self.details_label)

        # 予定の詳細を入力するためのテキストエリア（テキストエディタ）
        schedule = schedule_data.get(date.toString('yyyyMMdd'), {'details': '', 'category': ''})
        details = schedule['details']  # 辞書から詳細テキストを取得
        self.details_text_edit = QTextEdit(details)  # 正しい文字列を渡す
        self.details_text_edit.setFixedHeight(100)
        self.layout.addWidget(self.details_text_edit)

        # ボタンの配置
        self.buttons_layout = QHBoxLayout()
        self.save_button = QPushButton("保存")
        self.cancel_button = QPushButton("戻る")
        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addWidget(self.cancel_button)

        # ボタンのシグナルをスロットに接続
        self.save_button.clicked.connect(self.save_details)
        self.cancel_button.clicked.connect(self.close)

        self.layout.addLayout(self.buttons_layout)

    def save_details(self):
        # 予定の詳細とカテゴリーを取得
        details = self.details_text_edit.toPlainText()
        category = self.category_combobox.currentText()
        
        # 予定の詳細を辞書に保存
        self.schedule_data[self.selected_date.toString('yyyyMMdd')] = {
            'category': category,
            'details': details
        }

        # ダイアログを閉じる
        self.accept()

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("カレンダーアプリ")
        self.resize(800, 600)

        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.open_schedule_dialog)

        self.layout.addWidget(self.calendar)
        self.setCentralWidget(self.central_widget)

        # 日付をキーとして予定を保持する辞書
        self.schedule_data = {}

    def open_schedule_dialog(self, date):
        # 以前の予定があれば、カテゴリのインデックスを取得
        prev_schedule = self.schedule_data.get(date.toString('yyyyMMdd'))
        category_index = 0
        if prev_schedule:
            # 保存されたカテゴリに基づいてインデックスを取得
            categories = ["家", "学校", "職場", "プライベート","その他"]
            category_index = categories.index(prev_schedule['category'])
        
        # ScheduleDialogを開いて予定を編集
        dialog = ScheduleDialog(date, self.schedule_data, category_index, self)

        if dialog.exec():
            # ダイアログが保存で閉じられた場合、予定を更新
            self.schedule_data[date.toString('yyyyMMdd')] = dialog.schedule_data[date.toString('yyyyMMdd')]
            self.mark_dates_with_schedules()  # 予定がある日付にマーカーを設定

    def showEvent(self, event):
        super().showEvent(event)
        self.mark_dates_with_schedules()  # カレンダーが表示されたときにマーカーを設定

    def mark_dates_with_schedules(self):
        # すべての日付のフォーマットをクリア
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())
        
        # 予定がある日付にマーカーを設定
        for date_str, schedule in self.schedule_data.items():
            if schedule['details']:  # 詳細が空でない場合にマーカーを付ける
                date = QDate.fromString(date_str, 'yyyyMMdd')
                format = QTextCharFormat()
                
                # 色を設定
                category = schedule.get('category', 'その他') 
                color = CATEGORY_COLORS.get(category) 
                format.setBackground(color)
                
                self.calendar.setDateTextFormat(date, format)