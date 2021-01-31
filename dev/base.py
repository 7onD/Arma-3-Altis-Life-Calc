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

	# call base page
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

	# base
base = {
	"Ресурс":"Описание"
}

	# code
def base_page():
	res_name = int(Form.lineEdit.text()).lower()
	res_info = base[f'{res_name}']

	pg.alert(f"Информация o {res_name} : \n {res_info}", "Done", button="Продолжить")

	# close menu page
sys.exit(app.exec_())