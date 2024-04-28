import tkinter


def exchange():
    sum=float(sum_BYN_entry.get())
    result1=float(sum/3.28)
    result2 = float(sum / 3.51)
    result3 = float(sum * 28.1)
    result1 = tkinter.Label(header_frame, text=f'{result1:.2f}', font='Arial, 10')
    result1.grid(row=7, column=1)
    result2 = tkinter.Label(header_frame, text=f'{result2:.2f}', font='Arial, 10')
    result2.grid(row=8, column=1)
    result3 = tkinter.Label(header_frame, text=f'{result3:.2f}', font='Arial, 10')
    result3.grid(row=9, column=1)

root = tkinter.Tk()
root.title('Конвертер валют')
root.geometry('400x250')
root.resizable(False, False)

header_frame = tkinter.Frame(root)
header_frame.pack(fill='x')

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

course = tkinter.Label(header_frame, text='Курс валют:', font='Arial, 12')
course.grid(row=0, column=0, columnspan=2)

USD_course = tkinter.Label(header_frame, text = 'USD         1     3,28', font='Arial, 10')
USD_course.grid(row=1, column=0, columnspan=2)

EUR_course = tkinter.Label(header_frame, text = 'EUR         1     3,51', font='Arial, 10')
EUR_course.grid(row=2, column=0, columnspan=2)

RUB_course = tkinter.Label(header_frame, text = 'RUB         1     28,1', font='Arial, 10')
RUB_course.grid(row=3, column=0, columnspan=2)


sum_BYN = tkinter.Label(header_frame, text='Введите сумму', font='Arial, 10')
sum_BYN.grid(row=4, column=0)

sum_BYN_entry = tkinter.Entry(header_frame, font='Arial, 10', justify='center')
sum_BYN_entry.grid(row=5, column=0)

conv_button = tkinter.Button(header_frame, text='Конвертировать', font='Arial, 10', command=exchange)
conv_button.grid(row=5, column=1)

Result = tkinter.Label(header_frame, text='Результат:', font='Arial, 10')
Result.grid(row=6, column=0)

Result_USD = tkinter.Label(header_frame, text='USD', font='Arial, 10')
Result_USD.grid(row=7, column=0)

Result_EUR = tkinter.Label(header_frame, text='EUR', font='Arial, 10')
Result_EUR.grid(row=8, column=0)

Result_RUB = tkinter.Label(header_frame, text='RUB', font='Arial, 10')
Result_RUB.grid(row=9, column=0)



root.mainloop()
