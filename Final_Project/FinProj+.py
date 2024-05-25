import tkinter
from currency_converter import CurrencyConverter

class CurrencyConv(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.CurConv()
        self.window_settings()
        self.set_header()
        self.course()
        self.sum_USD()
        self.ConvButton()
        self.res()


    def CurConv(self):
        self.c = CurrencyConverter()

    def window_settings(self): #Создание окна
        self.root = tkinter.Tk()
        self.root.title('Конвертер валют')
        self.root.geometry('400x300')
        self.root.resizable(True, True)

    def set_header(self):
        self.header_frame = tkinter.Frame(self.root)
        self.header_frame.pack(fill='x')

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

    def course(self): #Курсы валют
        course = tkinter.Label(self.header_frame,
                                    text='Курсы валют:',
                                    font='Arial, 12')
        course.grid(row=0, column=0, columnspan=3)


        EUR_course1 = tkinter.Label(self.header_frame,
                                         text = 'EUR',
                                         font='Arial, 10')
        EUR_course1.grid(row=2, column=0)

        EUR_course2 = tkinter.Label(self.header_frame,
                                         text = '1',
                                         font='Arial, 10')
        EUR_course2.grid(row=2, column=1)

        EUR_course3 = tkinter.Label(self.header_frame,
                                         text = '%.2f' % self.c.convert(1, 'USD', 'EUR'),
                                         font='Arial, 10')
        EUR_course3.grid(row=2, column=2)


        INR_course1 = tkinter.Label(self.header_frame,
                                    text='INR',
                                    font='Arial, 10')
        INR_course1.grid(row=3, column=0)

        INR_course2 = tkinter.Label(self.header_frame,
                                    text='1',
                                    font='Arial, 10')
        INR_course2.grid(row=3, column=1)

        INR_course3 = tkinter.Label(self.header_frame,
                                    text='%.2f' % self.c.convert(1, 'USD', 'INR'),
                                    font='Arial, 10')
        INR_course3.grid(row=3, column=2)

        GBP_course1 = tkinter.Label(self.header_frame,
                                    text='GBP',
                                    font='Arial, 10')
        GBP_course1.grid(row=4, column=0)

        GBP_course2 = tkinter.Label(self.header_frame,
                                    text='1',
                                    font='Arial, 10')
        GBP_course2.grid(row=4, column=1)

        GBP_course3 = tkinter.Label(self.header_frame,
                                    text='%.2f' % self.c.convert(1, 'USD', 'GBP'),
                                    font='Arial, 10')
        GBP_course3.grid(row=4, column=2)


        PLN_course1 = tkinter.Label(self.header_frame,
                                    text='PLN',
                                    font='Arial, 10')
        PLN_course1.grid(row=5, column=0)

        PLN_course2 = tkinter.Label(self.header_frame,
                                    text='1',
                                    font='Arial, 10')
        PLN_course2.grid(row=5, column=1)

        PLN_course3 = tkinter.Label(self.header_frame,
                                    text='%.2f' % self.c.convert(1, 'USD', 'PLN'),
                                    font='Arial, 10')
        PLN_course3.grid(row=5, column=2)

    def sum_USD(self): #Создания поля для ввода суммы для конвертации
        self.USD = tkinter.Label(self.header_frame,
                                     text='Введите сумму(USD)',
                                     font='Arial, 10')
        self.USD.grid(row=6, column=0)

        self.USD_entry = tkinter.Entry(self.header_frame,
                                           font='Arial, 10',
                                           justify='center')
        self.USD_entry.grid(row=7, column=0)

    def exchange(self): #Конвертация валюты
        try:

            self.sum=float(self.USD_entry.get())
            self.result1 = (self.c.convert(self.sum, 'USD', 'EUR'))

            self.result11 = tkinter.Label(self.header_frame,
                                        text=f'        {self.result1:.2f}        ',
                                        font='Arial, 10')
            self.result11.grid(row=9, column=1, columnspan=2)


            self.result2 = (self.c.convert(self.sum, 'USD', 'INR'))

            self.result22 = tkinter.Label(self.header_frame,
                                        text=f'        {self.result2:.2f}        ',
                                        font='Arial, 10')
            self.result22.grid(row=10, column=1, columnspan=2)


            self.result3 = (self.c.convert(self.sum, 'USD', 'GBP'))

            self.result33 = tkinter.Label(self.header_frame,
                                        text=f'        {self.result3:.2f}        ',
                                        font='Arial, 10')
            self.result33.grid(row=11, column=1, columnspan=2)


            self.result4 = (self.c.convert(self.sum, 'USD', 'PLN'))

            self.result44 = tkinter.Label(self.header_frame,
                                        text=f'        {self.result4:.2f}        ',
                                        font='Arial, 10')
            self.result44.grid(row=12, column=1, columnspan=2)
        except ValueError:
            text = f'Данные должны иметь числовой тип'
            self.Result_error.config(text=text)
    def ConvButton(self): #Кнопка конвертации валюты
        self.conv_button = tkinter.Button(self.header_frame,
                                          text='Конвертировать',
                                          font='Arial, 10',
                                          command=self.exchange)
        self.conv_button.grid(row=7, column=1, columnspan=2)

    def res(self): #Результат
        self.Result = tkinter.Label(self.header_frame,
                                    text='Результат:',
                                    font='Arial, 10')
        self.Result.grid(row=8, column=0)


        self.Result_EUR = tkinter.Label(self.header_frame,
                                        text='EUR',
                                        font='Arial, 10')
        self.Result_EUR.grid(row=9, column=0)

        self.Result_INR = tkinter.Label(self.header_frame,
                                        text='INR',
                                        font='Arial, 10')
        self.Result_INR.grid(row=10, column=0)

        self.Result_GBP = tkinter.Label(self.header_frame,
                                        text='GBP',
                                        font='Arial, 10')
        self.Result_GBP.grid(row=11, column=0)

        self.Result_PLN = tkinter.Label(self.header_frame,
                                        text='PLN',
                                        font='Arial, 10')
        self.Result_PLN.grid(row=12, column=0)

        self.Result_error = tkinter.Label(self.header_frame,
                                          font='Arial, 10')
        self.Result_error.grid(row=13, column=0, columnspan=3)

if __name__ == '__main__':
    app = CurrencyConv()
    app.mainloop()
#CurrencyConverter не поддерживает валюту BYN
