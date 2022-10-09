from tkinter import *
from tkinter import messagebox as mb
import numpy
import re

class Window(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.geometry('540x500')
		self.title('Calculator')
		self.resizable(width = False, height = False)
		self['bg'] = '#778899'

		for i in range(8):
			self.grid_columnconfigure(i, minsize = 60)
			self.grid_rowconfigure(i, minsize = 60)

		self.grid_rowconfigure(0, minsize = 30)
		global stringvar1
		stringvar1 = StringVar()
		stringvar1.set("0")
		screen = Label(self, textvariable = stringvar1, font = ("Arial", 25), bg = '#808000', borderwidth = 5, relief = 'groove', width = 10)
		screen.grid(row = 1, column = 1, columnspan = 7, sticky = 'news')
		
def printsym(sym, event = None): 
	if len(str(sym)) <= 2:
		if stringvar1.get() != '0': stringvar1.set(f'{stringvar1.get()}{sym}')
		else: stringvar1.set(f'{stringvar1.get()[:-1]}{sym}')
	else: 
		sym = re.sub(r'.*keysym=(\d).*', r'\1', str(sym))
		printsym(sym)

def printop(sym, event = None):
	if len(str(sym)) > 1: 
		sym = re.sub(r".*char='(.)'.*", r'\1', str(sym))
	if stringvar1.get()[-1] not in '+*/.-': 
		stringvar1.set(f'{stringvar1.get()}{sym}')

	else: stringvar1.set(f'{stringvar1.get()[:-1]}{sym}')

def deletelast():
	stringvar1.set(f'{stringvar1.get()[:-1]}')

def clearall():
	stringvar1.set('0')

def calculate():
	express = stringvar1.get()
	if 'pi' in stringvar1.get():
		express = re.sub(r'pi', '3.14159265', stringvar1.get())
	try:
		stringvar1.set(f'{eval(express)}')
	except:
		stringvar1.set('0')
		mb.showerror('Error.', "Something went wrong...")

def recip():
	calculate()
	x = stringvar1.get()
	try:
		res = 1/float(x)
		stringvar1.set(str(res))
	except Exception as e:
		print(e)
		stringvar1.set('0')
		mb.showerror('Error.', "Something went wrong...")

def sinus():
	calculate()
	stringvar1.set(str(numpy.sin(float(stringvar1.get()))))

def cosinus():
	calculate()
	stringvar1.set(str(numpy.cos(float(stringvar1.get()))))

def tangent():
	calculate()
	stringvar1.set(str(numpy.tan(float(stringvar1.get()))))

def arcsinus():
	calculate()
	stringvar1.set(str(numpy.arcsin(float(stringvar1.get()))))

def arccosinus():
	calculate()
	stringvar1.set(str(numpy.arccos(float(stringvar1.get()))))

def arctangent():
	calculate()
	stringvar1.set(str(numpy.arctan(float(stringvar1.get()))))

def natlog():
	calculate()
	stringvar1.set(str(numpy.log(float(stringvar1.get()))))

def loga10():
	calculate()
	stringvar1.set(str(numpy.log10(float(stringvar1.get()))))

Calculator = Window()

BUTTONS09 = [Button(Calculator, text = f'{i}', command = lambda x = i: printsym(f'{x}'), font = ('Arial', 15), fg = 'white', bg = '#1C3879', 
					bd = 3).grid(row = 3 + int((i)/3), column = 2 + int(i%3), sticky = 'news', padx = 5, pady = 5) for i in [j for j in range(1, 10)] + [0]]
operations = ['+', '-', '/', '*', '.']
dict = {'del': [deletelast, 2, 6, 2, 'orange', 'white'], 'clear': [clearall, 3, 6, 2, 'orange', 'white'], 
		'=': [calculate, 4, 6, 2, '#607EAA', 'white'], '1/x': [recip, 2, 4, 1, '#607EAA', 'white'], 
		'(': [lambda x = 0: printsym('('), 5, 6, 1, '#607EAA', 'white'],
		')': [lambda x = 0: printsym(')'), 5, 7, 1, '#607EAA', 'white'],
		'sin': [sinus, 2, 3, 1, '#607EAA', 'white'], 'cos': [cosinus, 2, 2, 1, '#607EAA', 'white'],
		'arcsin': [arcsinus, 2, 1, 1, '#607EAA', 'white'], 'arccos': [arccosinus, 3, 1, 1, '#607EAA', 'white'],
		'tan': [tangent, 4, 1, 1, '#607EAA', 'white'], 'arctan': [arctangent, 5, 1, 1, '#607EAA', 'white'],
		'ln': [natlog, 6, 6, 1, '#607EAA', 'white'], 'lg': [loga10, 6, 7, 1, '#607EAA', 'white'], 
		'^': [lambda x = 0: printsym('**'), 6, 4, 1, '#607EAA', 'white'], 'pi': [lambda x = 0: printsym('pi'), 6, 3, 1, '#607EAA', 'white'],
		}
#[function, row, column, columnspace, bg, fg]
#[0,          1,      2,           3,  4,  5]

i = 0
for key in dict:
	Button(Calculator, text = key, command = dict[key][0], font = ('Arial', 15), bg = dict[key][4], fg = dict[key][5], bd = 3).grid(
		column = dict[key][2], row = dict[key][1], columnspan = dict[key][3], sticky = 'news', padx = 5, pady = 5)
	i += 1
for i in range(len(operations)):
	Button(Calculator, text = f'{operations[i]}', command = lambda x = i: printop(f'{operations[x]}'), font = ('Arial', 15), fg = 'white', 
		bg = '#607EAA', bd = 3).grid(row = 2 + i, column = 5, sticky = 'news', padx = 5, pady = 5)
for j in range(10):
	if j <= 4:
		Calculator.bind(operations[j], printop)
	Calculator.bind(str(j), printsym)




Calculator.mainloop()	