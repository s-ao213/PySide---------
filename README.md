# Pythonを用いたカレンダーアプリ開発

## 概要
このアプリは、QtライブラリのPythonバインディングであるPySide6を使用して構築されたシンプルなカレンダーアプリケーションです。ユーザーは特定の日付にイベントを追加、表示、保存することができます。アプリにはカレンダーウィジェット、イベントの詳細を入力するためのダイアログ、イベントを異なる色でカテゴリ分けする機能が備わっています。

## 特徴
月間カレンダーの表示が可能です。
カレンダーの日付をクリックすると、その日のイベントを追加または編集できます。
イベントに「家」「学校」「職場」「プライベート」「その他」のカテゴリを割り当てることができます。
テキストエディタでイベントの詳細な説明を入力できます。
イベントを保存すると、同じ日付でダイアログを再度開いたときに情報が保持されます。
割り当てられたカテゴリに基づいて色分けされたイベントの日付をハイライトします。

## 必要条件
Python 3.x
PySide6

## 使い方
CalendarAppを起動するには、コードが含まれているPythonスクリプトを実行します。カレンダーが表示されるメインウィンドウが開きます。イベントを追加または編集するには、日付をクリックするとダイアログが表示されます。ダイアログで次の操作ができます。

- ドロップダウンメニューからカテゴリを選択します。
- テキストエリアにイベントの詳細を入力します。
- 「保存」ボタンをクリックしてイベントを保存します。
- 「戻る」ボタンをクリックして変更を破棄し、ダイアログを閉じます。
- イベントを保存すると、カレンダー上の対応する日付が選択したカテゴリに関連する色でハイライト表示されます。

## ライセンス

このアプリケーションは GNU Lesser General Public License v3.0 のもとで公開されています。詳細は `riquire.txt` ファイルを参照してください。

このアプリケーションは PySide6 を利用しています。PySide6 は LGPL v3 ライセンスの下で公開されています。詳細は [こちら](https://www.qt.io/licensing/) を参照してください。
