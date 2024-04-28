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

    def window_settings(self):
        self.root = tkinter.Tk()
        self.root.title('Конвертер валют')
        self.root.geometry('400x170')
        self.root.resizable(False, False)

    def set_header(self):
        self.header_frame = tkinter.Frame(self.root)
        self.header_frame.pack(fill='x')

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

    def course(self):
        course = tkinter.Label(self.header_frame,
                                    text='Курсы валют:',
                                    font='Arial, 12')
        course.grid(row=0, column=0, columnspan=2)


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

    def sum_USD(self):
        self.USD = tkinter.Label(self.header_frame,
                                     text='Введите сумму(USD)',
                                     font='Arial, 10')
        self.USD.grid(row=4, column=0)

        self.USD_entry = tkinter.Entry(self.header_frame,
                                           font='Arial, 10',
                                           justify='center')
        self.USD_entry.grid(row=5, column=0)

    def exchange(self):
        self.sum=float(self.USD_entry.get())
        self.result = (self.c.convert(self.sum, 'EUR', 'USD'))

        self.result = tkinter.Label(self.header_frame,
                                    text=f'{self.result:.2f}',
                                    font='Arial, 10')
        self.result.grid(row=8, column=1)

    def ConvButton(self):
        self.conv_button = tkinter.Button(self.header_frame,
                                          text='Конвертировать',
                                          font='Arial, 10',
                                          command=self.exchange)
        self.conv_button.grid(row=5, column=1)

    def res(self):
        self.Result = tkinter.Label(self.header_frame,
                                    text='Результат:',
                                    font='Arial, 10')
        self.Result.grid(row=6, column=0)


        self.Result_EUR = tkinter.Label(self.header_frame,
                                        text='EUR',
                                        font='Arial, 10')
        self.Result_EUR.grid(row=8, column=0)


if __name__ == '__main__':
    app = CurrencyConv()
    app.mainloop()

#CurrencyConverter не поддерживает валюту BYN