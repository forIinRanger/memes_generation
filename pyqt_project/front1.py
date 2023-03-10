# -*- coding: utf-8 -*-
import io
# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from PIL import Image, ImageFont, ImageDraw
import sqlite3
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 1)
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setEnabled(True)
        self.result.setMinimumSize(QtCore.QSize(500, 350))
        self.result.setMaximumSize(QtCore.QSize(400, 500))
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 2, 0, 1, 1)
        self.instruction = QtWidgets.QLabel(self.centralwidget)
        self.instruction.setMinimumSize(QtCore.QSize(0, 0))
        self.instruction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.instruction.setObjectName("instruction")
        self.gridLayout.addWidget(self.instruction, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout.addWidget(self.label_text)
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setObjectName("input_text")
        self.horizontalLayout.addWidget(self.input_text)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_photo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_photo.setFont(font)
        self.label_photo.setObjectName("label_photo")
        self.horizontalLayout_2.addWidget(self.label_photo)
        self.choose_photoq = QtWidgets.QPushButton(self.centralwidget)
        self.choose_photoq.setObjectName("choose_photoq")
        self.horizontalLayout_2.addWidget(self.choose_photoq)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout_3.addWidget(self.label_type)
        self.choose_type = QtWidgets.QComboBox(self.centralwidget)
        self.choose_type.setObjectName("choose_type")
        self.choose_type.addItem("")
        self.choose_type.addItem("")
        self.choose_type.addItem("")
        self.choose_type.addItem("")
        self.horizontalLayout_3.addWidget(self.choose_type)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.showq = QtWidgets.QPushButton(self.centralwidget)
        self.showq.setObjectName("showq")
        self.horizontalLayout_4.addWidget(self.showq)
        self.saveq = QtWidgets.QPushButton(self.centralwidget)
        self.saveq.setStyleSheet("")
        self.saveq.setAutoRepeat(False)
        self.saveq.setAutoExclusive(False)
        self.saveq.setAutoDefault(False)
        self.saveq.setDefault(False)
        self.saveq.setFlat(False)
        self.saveq.setObjectName("saveq")
        self.horizontalLayout_4.addWidget(self.saveq)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MemesGenerator"))
        self.result.setText(_translate("MainWindow", "Здесь будет Ваш резултат))"))
        self.instruction.setText(_translate("MainWindow", "а здесь будет инструкция"))
        self.label_text.setText(_translate("MainWindow", "Тext:"))
        self.label_photo.setText(_translate("MainWindow", "Photo:"))
        self.choose_photoq.setText(_translate("MainWindow", "..."))
        self.label_type.setText(_translate("MainWindow", "Filter:"))
        self.choose_type.setItemText(0, _translate("MainWindow", "демотиватор"))
        self.choose_type.setItemText(1, _translate("MainWindow", "2 мужика удивляются"))
        self.choose_type.setItemText(2, _translate("MainWindow", "лев из Мадагаскара"))
        self.choose_type.setItemText(3, _translate("MainWindow", "кот плачет и показывает лайк"))
        self.showq.setText(_translate("MainWindow", "Apply"))
        self.saveq.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.saveq.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "History:"))


class ShowError:
    def __init__(self, text, class_):
        mes = QMessageBox.warning(class_, 'Что-то пошло не так',
                                  text, QMessageBox.Ok)


class MemesGeneration(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # зададим стандартные размеры шаблона и фото соответственно, к которым будем приводить все полученные картинки
        self.SIZE_BOARD = 500, 500
        self.SIZE_PHOTO = 400, 300
        super(MemesGeneration, self).__init__()
        self.setupUi(self)
        # начальная картинка приложения - инструкция по применению.
        self.instruction.setPixmap(QPixmap('start_img_2.jpg').scaled(476, 500))
        # начальная картинка приложения - занимает место будущих результатов генерации
        self.result.setPixmap(QPixmap('start_img_1.jpg').scaled(500, 500))

        # в переменной curr будут храниться картинки (то, что сейчас показывается на экране) -
        # под сохранение (либо под генерацию).
        self.curr = None
        # ниже идёт связка функций и кнопочек.
        self.showq.clicked.connect(self.showw)
        self.choose_photoq.clicked.connect(self.photo_choose)
        self.saveq.clicked.connect(self.save_img)
        self.error_string = ''
        self.con = sqlite3.connect("images.sqlite")
        self.cur = self.con.cursor()
        # result = self.cur.execute("""SELECT * FROM user_history""").fetchall()
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.cellClicked.connect(self.get_from_history)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.verticalScrollBar().setSingleStep(7)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

    def get_from_history(self, row, column):
        result_ = self.cur.execute(f"""SELECT user_history.image FROM user_history
WHERE user_history.id = {abs(row - self.tableWidget.rowCount()) - 1}""").fetchall()[0][0]
        board = Image.open(io.BytesIO(result_))
        # тут происходит конвертация PIL.Image -> QPixmap
        im2 = board.convert("RGBA")
        data = im2.tobytes("raw", "BGRA")
        qim = QtGui.QImage(data, board.width, board.height, QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        # выводим результат
        self.result.setPixmap(pixmap)
        self.curr = board

    def convert_to_binary_data(self, file):
        img_byte_arr = io.BytesIO()
        file.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

    def showw(self):
        # если в curr уже лежит картинка:
        if self.curr:
            # создаем пустой чёрный шаблон
            board = Image.new('RGB', self.SIZE_BOARD)
            im = self.curr
            # создаём свой шрифт, чтобы кириллица расшифровывалась корректно
            font = ImageFont.truetype('20989.ttf', size=29)
            # получаем длину введенного текста для центрирования подписи
            txt = self.input_text.text()
            size = font.getlength(txt)
            # тут мы вставляем текст на фото
            draw_text = ImageDraw.Draw(board)

            if self.choose_type.currentText() == 'демотиватор':
                draw_text.text(((self.SIZE_BOARD[0] - size) // 2, self.SIZE_BOARD[1] - 100),
                               self.input_text.text(),
                               font=font)
                # подгоняем фотку под стандартный размер и вставляем
                new_im = im.resize(self.SIZE_PHOTO)
                board.paste(new_im, (50, 60))
                # делаем рамку, как в настоящем демотиваторе
                draw_text.rectangle((46, 56, 454, 364), outline="white")

            elif self.choose_type.currentText() == 'кот плачет и показывает лайк':
                board = im.resize(self.SIZE_BOARD)

                new_im = Image.open('images/4th.png').resize((200, 200)).convert('RGBA')
                board.paste(new_im, (300, 300), new_im)

                draw_text = ImageDraw.Draw(board)
                draw_text.text((50, 50),
                               txt, fill=(150, 150, 150, 50),
                               font=font)

            elif self.choose_type.currentText() == 'лев из Мадагаскара':

                board = Image.new('RGB', self.SIZE_BOARD, 'white')
                lion = Image.open('images/fifths.png').resize((300, 300)).convert('RGBA')
                board.paste(lion, (-10, -10), lion)
                board.paste(im.resize((300, 300)), (150, 150))

                # new_im = Image.open('images/fifths.png').resize(self.SIZE_BOARD).convert('RGBA')
                # # board.paste(new_im, (300, 300), new_im)
                # board = Image.blend(new_im, board, 0.5)
                #
                draw_text = ImageDraw.Draw(board)
                draw_text.text((250, 50),
                               txt, fill=(0, 0, 0, 100),
                               font=font)
                draw_text.rectangle((146, 146, 454, 454), outline="orange", width=3)

            else:
                board = im.resize(self.SIZE_BOARD)
                new_im = Image.open('images/1st.png').resize((self.SIZE_BOARD[0], 300)).convert('RGBA')
                board.paste(new_im, (0, self.SIZE_BOARD[1] - 300), new_im)

                # new_im = Image.open('images/fifths.png').resize(self.SIZE_BOARD).convert('RGBA')
                # # board.paste(new_im, (300, 300), new_im)
                # board = Image.blend(new_im, board, 0.5)
                #
                draw_text = ImageDraw.Draw(board)
                draw_text.text((160, self.SIZE_BOARD[1] - 100),
                               txt, fill=(100, 100, 0, 50),
                               font=font)

            # тут происходит конвертация PIL.Image -> QPixmap
            im2 = board.convert("RGBA")
            data = im2.tobytes("raw", "BGRA")
            qim = QtGui.QImage(data, board.width, board.height, QtGui.QImage.Format_ARGB32)
            pixmap = QtGui.QPixmap.fromImage(qim)
            # выводим результат
            self.result.setPixmap(pixmap)
            self.curr = board

            # общение с базой
            sqlite_insert_blob_query = """ INSERT INTO user_history
                                                                  (image, date, id) VALUES (?, ?, ?)"""
            blobPhoto = self.convert_to_binary_data(self.curr)
            data_tuple = (
                blobPhoto, datetime.datetime.now().strftime('%H:%M:%S %d %b'), self.tableWidget.rowCount())
            self.cur.execute(sqlite_insert_blob_query, data_tuple)

            # общение с таблицей из GUI
            label_123 = QtWidgets.QLabel()
            pixmap = pixmap.scaledToWidth(150)
            pixmap = pixmap.scaledToHeight(150)
            label_123.setPixmap(pixmap)
            self.tableWidget.insertRow(0)
            self.tableWidget.setCellWidget(0, 0, label_123)
            self.tableWidget.setItem(0, 1, QTableWidgetItem(datetime.datetime.now().strftime('%H:%M:%S %d %b')))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.item(0, 1).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.tableWidget.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

        # если в curr нет картинки выводим текст ниже
        else:
            ShowError('Вы не выбрали картинку', self)

    def photo_choose(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                            'Все файлы (*);;Картинка (*.jpg);;Картинка (*.jpeg);;Картинка (*.png')[0]
        # если картинка выбрана:
        if fname[-3:] in ('jpg', 'png') or fname[-4:] == 'jpeg':
            # полученную картинку растягиваем до SIZE_BOARD (для красоты, впоследствии размер будет SIZE_PHOTO)
            board = Image.open(fname).resize(self.SIZE_BOARD)
            # сохраняем в curr для последующей работы
            self.curr = board
            # тут происходит конвертация PIL.Image -> QPixmap
            im2 = board.convert("RGBA")
            data = im2.tobytes("raw", "BGRA")
            qim = QtGui.QImage(data, board.width, board.height, QtGui.QImage.Format_ARGB32)
            pixmap = QtGui.QPixmap.fromImage(qim)
            # выводим результат
            self.result.setPixmap(pixmap)
            self.instruction.setPixmap(QPixmap('inst.jpg').scaled(476, 500))

            # общение с базой
            sqlite_insert_blob_query = """ INSERT INTO user_history
                                              (image, date, id) VALUES (?, ?, ?)"""
            blobPhoto = self.convert_to_binary_data(self.curr)
            data_tuple = (blobPhoto, datetime.datetime.now().strftime('%H:%M:%S %d %b'), self.tableWidget.rowCount())
            self.cur.execute(sqlite_insert_blob_query, data_tuple)

            # общение с таблицей из GUI
            label_123 = QtWidgets.QLabel()
            pixmap = pixmap.scaledToWidth(150)
            pixmap = pixmap.scaledToHeight(150)
            label_123.setPixmap(pixmap)
            self.tableWidget.insertRow(0)
            self.tableWidget.setCellWidget(0, 0, label_123)
            self.tableWidget.setItem(0, 1, QTableWidgetItem(str(datetime.datetime.now().strftime('%H:%M:%S %d %b'))))

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.item(0, 1).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.tableWidget.item(0, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)

            # self.cur.execute("""DELETE FROM user_history""")
            # self.con.commit()

        # если картинка не выбрана и до этого картинка не выбиралась:
        elif not fname and not self.curr:
            ShowError('Вы не выбрали картинку, попробуйте еще раз', self)
        elif not self.curr:
            ShowError('Вы открываете не картинку, попробуйте еще раз', self)

    def save_img(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранение шедевра', '',
                                            'Картинка (*.jpg)')[0]
        self.curr.save(fname)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MemesGeneration()
    ex.show()
    sys.exit(app.exec())
