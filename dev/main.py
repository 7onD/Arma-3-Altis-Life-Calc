import pyautogui as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc import Ui_Calc
from menu import Ui_Menu
from t_notes import note
from base_if import Ui_Form

menuapp = QtWidgets.QApplication(sys.argv)
Menu = QtWidgets.QWidget()
menu = Ui_Menu()
menu.setupUi(Menu)
Menu.show()

calcapp = QtWidgets.QApplication(sys.argv)
Calc = QtWidgets.QWidget()
calc = Ui_Calc()
calc.setupUi(Calc)

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

alc = 'является нелегальным ресурсом, для создания которого необходимо наличие рецепта ( он покупается у главаря банды Атиры за 3000 репутации ), для создания необходимо (кукуруза, яблоки, стеклянная бутылка, дрожжи - по одной штуке каждого). Для упаковки одной ящика нужно 50 бутылок.'
base = {
	'алкоголь':alc
}

def page_switch():
	Calc.show()

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

def base_page():
    res_name = (ui.lineEdit.text())
    if res_name not in base:
    	pg.alert(f"В нашей базе нету информации о {res_name}, проверьте правильность написания. Либо вы можете обратиться к нам с просьбой добавить этот ресурс, по адресу: https://github.com/7onD/Arma-3-Altis-Life-Calc в разделе issues", "Error", button="Продолжить")
    else:
    	res_info = base[f'{res_name}']
    	pg.alert(f"Информация o {res_name} : \n {res_info}", "Done", button="Продолжить")

def base_open():
	Form.show()

calc.pushButton.clicked.connect(bp)
menu.pushButton.clicked.connect(open_notes)
menu.pushButton_2.clicked.connect(page_switch)
menu.pushButton_3.clicked.connect(base_open)
ui.pushButton.clicked.connect(base_page)


sys.exit(menuapp.exec_())
sys.exit(calcapp.exec_())
sys.exit(app.exec_())