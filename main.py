import pyautogui as pg
import time
import eel
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from interface import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# @eel.expose

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
	all_butles = int(ui.lineEdit.text())
	in_one_pack = int(ui.lineEdit_3.text())
	res_price = int(ui.lineEdit_2.text())
	vip_cash = int(ui.lineEdit_4.text())

	final = get_res(all_butles, in_one_pack, res_price, vip_cash)
	pg.alert(f"Вы заработаете {final}", "Done", button="Продолжить")
ui.pushButton.clicked.connect(bp)

# eel.init('web')
# eel.start('main.html', size=(700,700))

sys.exit(app.exec_())