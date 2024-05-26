import tkinter
from tkinter import ttk
from currency_converter import CurrencyConverter


class CurrencyConv(tkinter.Tk):
    Currency = {
        'Евро (EUR)': 'EUR',
        'Доллар (USD)': 'USD',
        'Фунт (GBP)': 'GBP',
        'Злотый (PLN)': 'PLN',
        'Индийская рупия (INR)': 'INR',
        'Рубль (RUB)': 'RUB'
    }

    def __init__(self):
        super().__init__()
        self.CurConv()
        self.window_settings()
        self.set_header()
        self.sum_cur()
        self.ConvButton()
        self.res()
        self.exchange()

    def CurConv(self):
        self.c = CurrencyConverter()

    def window_settings(self):
        self.root = tkinter.Tk()
        self.root.title('Конвертер валют')
        self.root.geometry('400x160')
        self.root.resizable(True, False)

    def set_header(self):
        self.header_frame = tkinter.Frame(self.root)
        self.header_frame.pack(fill='x')

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

        self.choose_curr = tkinter.Label(self.header_frame, text='Выберите валюту', font='Arial, 10')
        self.choose_curr.grid(row=0, column=0, columnspan=2)


        self.Currency_menu_from = ttk.Combobox(self.header_frame, values=[Currency for Currency in self.Currency], state='readonly')
        self.Currency_menu_from.current(0)
        self.Currency_menu_from.grid(row=1, column=0)

        self.Currency_menu_to = ttk.Combobox(self.header_frame, values=[Currency for Currency in self.Currency], state='readonly')
        self.Currency_menu_to.current(1)
        self.Currency_menu_to.grid(row=1, column=1)

    def sum_cur(self):
        self.sum_get = tkinter.Label(self.header_frame,
                                 text='Введите сумму',
                                 font='Arial, 10')
        self.sum_get.grid(row=2, column=0, columnspan=2)

        self.sum_get_entry = tkinter.Entry(self.header_frame,
                                       font='Arial, 10',
                                       justify='center')
        self.sum_get_entry.grid(row=3, column=0)

    def exchange(self):
        self.Currency_suffix1 = self.Currency.get(self.Currency_menu_from.get())
        self.Currency_suffix2 = self.Currency.get(self.Currency_menu_to.get())
        try:
            sum = float(self.sum_get_entry.get())
            self.result1 = (self.c.convert(sum, f'{self.Currency_suffix1}', f'{self.Currency_suffix2}'))

            self.result11 = tkinter.Label(self.header_frame,
                                          text=f'        {self.result1:.2f}        ',
                                          font='Arial, 10')
            self.result11.grid(row=4, column=1, columnspan=2)
        except ValueError:
            self.text = 'Данные должны иметь числовой тип'
        self.Result_error.config(text=self.text)


    def ConvButton(self):
        self.conv_button = tkinter.Button(self.header_frame,
                                          text='Конвертировать',
                                          font='Arial, 10',
                                          command=self.exchange)
        self.conv_button.grid(row=3, column=1, columnspan=2)

    def res(self):
        self.Result = tkinter.Label(self.header_frame,
                                    text='Результат:',
                                    font='Arial, 10')
        self.Result.grid(row=4, column=0)

        self.Result_error = tkinter.Label(self.header_frame,
                                          font='Arial, 10')
        self.Result_error.grid(row=5, column=0, columnspan=2)


if __name__ == '__main__':
    app = CurrencyConv()
    app.mainloop()
# CurrencyConverter не поддерживает валюту BYN
#'Индийская рупия (INR)': 'INR',