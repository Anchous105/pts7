import tkinter
from currency_converter import CurrencyConverter

class CurrencyConv():
    def __init__(self):
        super().__init__()
        self.CurConv()
        self.exchange()
        self.window_settings()
        self.set_header()
        self.course()
        self.sum()
        self.ConvButton()
        self.res()

    def CurConv(self):
        self.c = CurrencyConverter()

    def window_settings(self):
        self.root = tkinter.Tk()
        self.root.title('Конвертер валют')
        self.root.geometry('400x250')
        self.root.resizable(False, False)

    def set_header(self):
        self.header_frame = tkinter.Frame(self.root)
        self.header_frame.pack(fill='x')

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

    def course(self):
        self.course = tkinter.Label(self.header_frame, text='Курс валют:', font='Arial, 12')
        self.course.grid(row=0, column=0, columnspan=2)


        self.EUR_course1 = tkinter.Label(self.header_frame, text = 'EUR', font='Arial, 10')
        self.EUR_course1.grid(row=2, column=0)
        self.EUR_course2 = tkinter.Label(self.header_frame, text = '1', font='Arial, 10')
        self.EUR_course2.grid(row=2, column=1)
        self.EUR_course3 = tkinter.Label(self.header_frame, text = '%.2f' % self.c.convert(1, 'EUR', 'USD'), font='Arial, 10')
        self.EUR_course3.grid(row=2, column=2)

    def sum(self):
        self.sum_BYN = tkinter.Label(self.header_frame, text='Введите сумму(USD)', font='Arial, 10')
        self.sum_BYN.grid(row=4, column=0)

        self.sum_BYN_entry = tkinter.Entry(self.header_frame, font='Arial, 10', justify='center')
        self.sum_BYN_entry.grid(row=5, column=0)

    def exchange(self):
        self.sum=float(self.sum_BYN_entry.get())
        self.result = (self.c.convert(self.sum, 'USD', 'EUR'))

        self.result = tkinter.Label(self.header_frame, text=f'{self.result:.2f}', font='Arial, 10')
        self.result.grid(row=8, column=1)

    def ConvButton(self):
        self.conv_button = tkinter.Button(self.header_frame, text='Конвертировать', font='Arial, 10', command=self.exchange)
        self.conv_button.grid(row=5, column=1)

    def res(self):
        self.Result = tkinter.Label(self.header_frame, text='Результат:', font='Arial, 10')
        self.Result.grid(row=6, column=0)


        self.Result_EUR = tkinter.Label(self.header_frame, text='EUR', font='Arial, 10')
        self.Result_EUR.grid(row=8, column=0)


app = CurrencyConv()
#CurrencyConverter не поддерживает валюту BYN