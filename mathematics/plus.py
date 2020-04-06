from tkinter import *
from tkinter import ttk
from random import randint as rnd
from time import *


def start(*args):
    global point, count
    point = count = 0


def new(*args):
    x1.set(rnd(0,50))
    x2.set(rnd(0,50))
    result.set(" ")
    status.set('')
    equil['state'] = 'instate'
    equil.delete(0, 'end')
    equil.focus()


def calc(*args):
    global point, count
    user = int(answer.get())
    summa = int(x1.get())+int(x2.get())
    if user == summa:
        result.set('Отлично')
        point += 1
    else:
        result.set('Плохо')
    count += 1
    equil['state'] = 'readonly'


def stop(*args):
    global point, count
    status.set('Верных ответов: '+str(point)+' Неверных ответов: '+str(count-point))
    point = 0
    count = 0
    result.set("Ваш результат)")
    equil['state'] = 'instate'
    x1.set(0)
    x2.set(0)
    answer.set(0)


root = Tk()
root.title('Сложение чисел')
# root.geometry('500x300')
point = 0
count = 0
# генерация примера
x1 = StringVar()
x2 = StringVar()
answer = StringVar()
result = StringVar()
status = StringVar()
x1.set(0)
x2.set(0)
answer.set(0)
# создание интерфейса
frm_1 = ttk.Frame(root, padding="30")
frm_1.grid(column=0, row=0, sticky=(W, E))
ttk.Label(frm_1, textvariable=x1, font='Arial 45').grid(row=3, column=1, columnspan=2)
ttk.Label(frm_1, text='+', font='Arial 45').grid(row=3, column=3, sticky=(W,E))
ttk.Label(frm_1, textvariable=x2, font='Arial 45').grid(row=3, column=4, columnspan=2)
ttk.Label(frm_1, text='=', font='Arial 45').grid(row=3, column=6)
equil = ttk.Entry(frm_1, width=3, font='Arial 45', textvariable=answer)
equil.grid(row=3, column=8, sticky=E, padx=20, pady=40)
# кнопки
btn_1 = ttk.Button(frm_1, text='Новый', command=new).grid(row=1, column=1, columnspan=2)
btn_2 = ttk.Button(frm_1, text='Ответить', command=calc).grid(row=1, column=4, columnspan=2)
btn_3 = ttk.Button(frm_1, text='Завершить', command=stop).grid(row=1, column=8, columnspan=2)
btn_start = ttk.Button(frm_1, text='Старт', command=start)
btn_start.grid(row=0, column=1, columnspan=2, pady=20)

ttk.Label(frm_1, textvariable=result, font='Arial 45').grid(row=6, column=1, columnspan=8, sticky=W)
# статус
stat_1 = ttk.Label(frm_1, textvariable=status, font='Arial 20')
stat_1.grid(row=8, column=1, columnspan=8, sticky=W, pady=20)

root.bind('<Return>', calc)
root.bind('<Shift_L>', new)
root.bind('<Tab>', stop)
root.mainloop()