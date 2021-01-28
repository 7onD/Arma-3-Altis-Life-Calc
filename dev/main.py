import pyautogui as pg
import time
import eel
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc import Ui_Form
from menu import Ui_Menu
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from t_notes import note

menuapp = QtWidgets.QApplication(sys.argv)
Menu = QtWidgets.QWidget()
menu = Ui_Menu()
menu.setupUi(Menu)
Menu.show()

calcapp = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
calc = Ui_Form()
calc.setupUi(Form)


def page_switch():
	Form.show()

def open_notes():
	note()

def get_res(all_butles, in_one_pack, res_price, vip_cash):

	if vip_cash == 1:
		one_proc = res_price / 100 * 10
		res_price = res_price + one_proc

	if vip_cash == 2:
		one_proc = res_price / 100 * 15
		res_price = res_price + one_proc

	if vip_cash == 3:
		one_proc = res_price / 100 * 20
		res_price = res_price + one_proc

	if vip_cash == 4:
		one_proc = res_price / 100 * 30
		res_price = res_price + one_proc

	final = (((all_butles / in_one_pack) * res_price))
	return final

def bp():
	all_butles = int(calc.lineEdit.text())
	in_one_pack = int(calc.lineEdit_3.text())
	res_price = int(calc.lineEdit_2.text())
	vip_cash = int(calc.lineEdit_4.text())

	final = get_res(all_butles, in_one_pack, res_price, vip_cash)
	pg.alert(f"Вы заработаете {final}", "Done", button="Продолжить")


calc.pushButton.clicked.connect(bp)
menu.pushButton_2.clicked.connect(page_switch)
menu.pushButton.clicked.connect(open_notes)


sys.exit(menuapp.exec_())
sys.exit(calcapp.exec_())