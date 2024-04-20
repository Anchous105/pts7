import tkinter

class FinalProject(tkinter.Tk):
    def __init__(self):
        self.window_settings
        self.create_conv_button





    currency = {
        'Доллар': 'USD',
        'Рубль': 'RUB',
        'Белорусский рубль': 'BYN'
    }

    
    def window_settings(self):
        self.root.title("Конвертер валют")
        self.root.geometry('600x400')
        self.root.resizable(False, False)

    def create_conv_button(self):
        """
        Создание кнопки для конвертации валют
        :return:
        """
        button = tkinter.Button(self.root, text="Рассчитать", font=('Arial', 12))
self.button2 = tkinter.Button(self, text='CANCEL', font=('Arial', 12))
    self.button2.grid(row=2, column=1, padx=10, pady=10)

    self.button3 = tkinter.Button(self, text='CANCEL', font=('Arial', 12))
    self.button3.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

self.result_label = tkinter.Button(self,
                                   text='',
                                   font=('Arial', 15),
                                   background=self.color)
self.result_label.grid(row=2, column=0, columnspan=2, padx=10,
                       pady=10)