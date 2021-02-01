import pyautogui as pg
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from base_if import Ui_Form

def base():
		# call base page
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    	#base
    alc = 'является нелегальным ресурсом, для создания которого необходимо наличие рецепта ( он покупается у главаря банды Атиры за 3000 репутации ), для создания необходимо (кукуруза, яблоки, стеклянная бутылка, дрожжи - по одной штуке каждого). Для упаковки одной ящика нужно 50 бутылок.'
    base = {
    "алкоголь":alc
    }

		# code
    def base_page():
        res_name = (ui.lineEdit.text())
        res_info = base[f'{res_name}']

        pg.alert(f"Информация o {res_name} : \n {res_info}", "Done", button="Продолжить")

    ui.pushButton.clicked.connect(base_page)

		# close menu page
    sys.exit(app.exec_())

base()
