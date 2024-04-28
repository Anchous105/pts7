import tkinter
from currency_converter import CurrencyConverter


def exchange(): #Конвертация валют
    sum=float(sum_BYN_entry.get())
    result = (c.convert(sum, 'USD', 'EUR'))

    result = tkinter.Label(header_frame, text=f'{result:.2f}', font='Arial, 10')
    result.grid(row=8, column=1)



root = tkinter.Tk()
root.title('Конвертер валют')
root.geometry('400x170')
root.resizable(False, False)
c = CurrencyConverter()

header_frame = tkinter.Frame(root)
header_frame.pack(fill='x')

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

course = tkinter.Label(header_frame, text='Курс валют:', font='Arial, 12')
course.grid(row=0, column=0, columnspan=2)


EUR_course1 = tkinter.Label(header_frame, text = 'EUR', font='Arial, 10')
EUR_course1.grid(row=2, column=0)
EUR_course2 = tkinter.Label(header_frame, text = '1', font='Arial, 10')
EUR_course2.grid(row=2, column=1)
EUR_course3 = tkinter.Label(header_frame, text = '%.2f' % c.convert(1, 'EUR', 'USD'), font='Arial, 10')
EUR_course3.grid(row=2, column=2)


sum_BYN = tkinter.Label(header_frame, text='Введите сумму(USD)', font='Arial, 10')
sum_BYN.grid(row=4, column=0)

sum_BYN_entry = tkinter.Entry(header_frame, font='Arial, 10', justify='center')
sum_BYN_entry.grid(row=5, column=0)

conv_button = tkinter.Button(header_frame, text='Конвертировать', font='Arial, 10', command=exchange)
conv_button.grid(row=5, column=1)

Result = tkinter.Label(header_frame, text='Результат:', font='Arial, 10')
Result.grid(row=6, column=0)


Result_EUR = tkinter.Label(header_frame, text='EUR', font='Arial, 10')
Result_EUR.grid(row=8, column=0)


root.mainloop()
#CurrencyConverter не поддерживает валюту BYN