import pyautogui as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc import Ui_Calc
from menu import Ui_Menu
from t_notes import note
from base_if import Ui_Form
from newers import Ui_newers
from faq import Ui_Faq

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

newersapp = QtWidgets.QApplication(sys.argv)
newersForm = QtWidgets.QWidget()
newersui = Ui_newers()
newersui.setupUi(newersForm)

faqapp = QtWidgets.QApplication(sys.argv)
faqForm = QtWidgets.QWidget()
faqui = Ui_Faq()
faqui.setupUi(faqForm)

alc = 'является нелегальным ресурсом, для создания которого необходимо наличие рецепта ( он покупается у главаря банды Атиры за 3000 репутации ), для создания необходимо (кукуруза, яблоки, стеклянная бутылка, дрожжи - по одной штуке каждого). Для упаковки одной ящика нужно 50 бутылок.'
bottle = 'может встречаться в двух видах стеклянная и пластиковая. Для создания стеклянной нужен рецепт который покупается у мэра Кавалы (за ), Для создания нужен (песок * 3).'
rep = 'вид валюты который используется в основном для покупки крафтов у мэров городов и главарей банд. Для получения необходимо выполнять задания и этих НПС.'
boep = 'Добывать на складе боеприпасов. Потом упаковывать на нелегальной упаковке. Затем продавать в аэропорту контрабандистов.'
legres = 'в основном отмечены (голубыми квадратиком), ресурсы того типа упаковываются на легальной упаковке (сведения о необходимости упаковки можно найти наведя курсор на ресурс в инвентаре), продаж осуществляется в порту с помощью погрузчика.'
unlegres = '\xd0Отмечены на карте (красным квадратиком), за добычу таких ресурсов вас может арестовать полиция, сведения о необходимости упаковки можно найти наведя курсор на ресурс в инвентаре, продаж осуществляется в аэропорту контрабандистов, Важно после продажи вы получите грязные наличные'
gr = 'ресурс который вы получаете после продажи нелегала, их можно отмыть у любого главаря банды или в через банкомат в афшорный счёте (если такой имеется), за грязный нал вы можете так же закупаться в нелегальных магазинах.'
ass = 'покупается за 50000А.Д с его помощью можно отмывать грязные наличные в любом банкомате.'
craft = 'вид деятельности который позволяет создавать предметы, для крафта нужен чертеж (покупается у мэра или главаря банды) и ресурсы (какие именно можно посмотреть в планшете, раздел крафты,) в сложных предметах для крафта необходим верстак или иные приспособления.'
tg = 'события которое происходит случайно на карте и заключается в доставке машины(ОЧЕНЬ МЕДЛЕННОЙ), на другой конец карты, при этом вас могут убить все, так же если вы не состоите в группировке даже не едьте туда (ОНО ВАС УБЬЁТ), если вы не состоите в организации то вы сможете получить целое ничего.'
shops = 'есть два вида, нелегальный (отмечены в виде человека с балаклавой) покупка осуществляется за грязный нал и легальный (в виде витрины) покупка осуществляется за наличные'
ypr = 'базовую информацию об управлении игрок сможет найти открыв карту и в левом верхнем углу найти меню, если понадобится изменить то ESC - настройки - управление - настройки дополнения - Tactical Life.'
lifehack = '\xd0Если ты ненормальный и хочешь всего и сразу то беги(машины то у тебя нет хах) в магазин грузовиков покупай фуру на которую хватит денег, и едь в порт который находится в кавале (точнее рядом с ним есть РЦ), там берём доставку и едем куда нибудь (туда где рядом),таким образом ты получаешь деньги и тратиться только на бензин, возможно вы сможете найти таким образом знакомых но основная задача получить дэнег, теперь когда у тебя есть деньги ты можешь купить себе вертолет и заняться продажей (воровоные боеприпасы). Главное помни не лети туда если цена за упакованный ресурс ниже 18000.'
base = {
	'алкоголь':alc,
	'бутылка':bottle,
	'репутация':rep,
	'ворованные боеприпасы':boep,
	'легальный ресурс':legres,
	'нелегальный ресурс':unlegres,
	'грязные наличные':gr,
	'афшорный счёт':ass,
	'крафт':craft,
	'тайный груз':tg,
	'магазины':shops,
	'управление':ypr,
	'лайфхак':lifehack,
	'Алкоголь':alc,
	'Бутылка':bottle,
	'Репутация':rep,
	'Ворованные боеприпасы':boep,
	'Легальный ресурс':legres,
	'Нелегальный ресурс':unlegres,
	'Грязные наличные':gr,
	'Афшорный счёт':ass,
	'Крафт':craft,
	'Тайный груз':tg,
	'Магазины':shops,
	'Управление':ypr,
	'Лайфхак':lifehack
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

def newers_open():
	newersForm.show()

def newers_close():
	newersForm.close()

def faq_open():
	faqForm.show()

def faq_close():
	faqForm.close()

calc.pushButton.clicked.connect(bp)
menu.pushButton.clicked.connect(open_notes)
menu.pushButton_2.clicked.connect(page_switch)
menu.pushButton_3.clicked.connect(base_open)
ui.pushButton.clicked.connect(base_page)
ui.pushButton_3.clicked.connect(newers_open)
newersui.pushButton.clicked.connect(newers_close)
ui.pushButton_2.clicked.connect(faq_open)
faqui.pushButton.clicked.connect(faq_close)


sys.exit(menuapp.exec_())
sys.exit(calcapp.exec_())
sys.exit(app.exec_())
sys.exit(newersapp.exec_())
sys.exit(app.exec_())