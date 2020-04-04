from tkinter import *
from tkinter import ttk
from random import randint as rnd


def example():
    x1.set(rnd(0,20))
    x2.set(rnd(0,20))
    result.set(" ")
    answer.set('')


def calc(*args):
    user = int(answer.get())
    summa = int(x1.get())+int(x2.get())
    if user == summa:
        result.set('Отлично')
    else:
        result.set('Плохо')


root = Tk()
root.title('Сложение чисел')
# root.geometry('500x300')

# генерация примера
x1 = StringVar()
x2 = StringVar()
answer = StringVar()
result = StringVar()
# создание интерфейса
frm_1 = ttk.Frame(root, padding="30")
frm_1.grid(column=0, row=0, sticky=(W, E))
ttk.Label(frm_1, textvariable=x1, font='Arial 45').grid(row=3, column=1, columnspan=2)
ttk.Label(frm_1, text='+', font='Arial 45').grid(row=3, column=3, sticky=(W,E))
ttk.Label(frm_1, textvariable=x2, font='Arial 45').grid(row=3, column=4, columnspan=2)
ttk.Label(frm_1, text='=', font='Arial 45').grid(row=3, column=6)
equil = ttk.Entry(frm_1, width=3, font='Arial 45', textvariable=answer)
equil.grid(row=3, column=8, sticky=E, padx=20)
btn_1 = ttk.Button(frm_1, text='Начать', command=example).grid(row=1, column=1, columnspan=2)
btn_2 = ttk.Button(frm_1, text='Ответить', command=calc).grid(row=1, column=4, columnspan=2)
ttk.Label(frm_1, textvariable=result, font='Arial 45').grid(row=6, column=1, columnspan=4)
root.bind('<Return>', calc)
root.mainloop()