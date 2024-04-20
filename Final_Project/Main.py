import tkinter
from tkinter import ttk
from tkinter import font


class FinalProject(tkinter.Tk):
  color = '#f0c33c'

  def __init__(self):
    super().__init__()
    self.window_settings()
    self.create_labels()
    self.create_buttons()
    self.create_entry()
    self.result()


  def result(self):
    Currency = float(self.currency.get())
    self.result1 = (Currency / 3.27)
    self.result2 = (Currency / 3.48)


  def window_settings(self):
    self.title('Конвертер валют')
    self.geometry('400x200')  #Размер окна
    self.configure(background=self.color)  #Цвет фона
    self.resizable(height=True, width=True)  #Запрет на масштабирование


  def create_labels(self):
    self.label1 = tkinter.Label(self,
                                text=('Введите валюту(BYN)'),
                                font=('Arial', 15),
                                background=self.color)
    self.label1.grid(row=0, column=0, columnspan=2, padx=10,
                     pady=10)  #Размещение в виде таблицы
    self.label2 = tkinter.Label(self,
                                text=(f'Результат(USD): {self.result1}'),
                                font=('Arial', 15),
                                background=self.color)
    self.label2.grid(row=2, column=0, columnspan=2, padx=10,
                     pady=10)

    self.label3 = tkinter.Label(self,
                                text=(f'Результат(EUR): {self.result2}'),
                                font=('Arial', 15),
                                background=self.color)
    self.label3.grid(row=3, column=0, columnspan=2, padx=10,
                    pady=10)


  def create_buttons(self):
    self.conv_button = tkinter.Button(self, text='Рассчитать', font=('Arial', 12))
    self.conv_button.grid(row=0, column=2, padx=10, pady=10)


  def create_entry(self):
    self.currency = tkinter.Entry(self, font=('Arial', 12), width=20)
    self.currency.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


app = FinalProject()
app.mainloop()
