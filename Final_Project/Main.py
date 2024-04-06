import tkinter
from tkinter import ttk
from tkinter import font


class FinalProject(tkinter.Tk):
  color = '#f0c33c'

  def __init__(self):
    super().__init__()
    print('Hello')
    self.window_settings()
    self.create_labels()
    self.create_buttons()
    self.create_entry()

  def window_settings(self):
    self.title('Final Project')
    self.geometry('400x200')  #Размер окна
    self.configure(background=self.color)  #Цвет фона
    self.resizable(height=False, width=False)  #Запрет на масштабирование

  def create_labels(self):
    self.label1 = tkinter.Label(self,
                                text='Test label',
                                font=('Arial', 15),
                                background=self.color)
    self.label1.grid(row=0, column=0, columnspan=2, padx=10,
                     pady=10)  #Размещение в виде таблицы

  def create_buttons(self):
    self.button1 = tkinter.Button(self, text='OK', font=('Arial', 12))
    self.button1.grid(row=2, column=0, padx=10, pady=10)

    self.button2 = tkinter.Button(self, text='CANCEL', font=('Arial', 12))
    self.button2.grid(row=2, column=1, padx=10, pady=10)

  def create_entry(self):
    self.entry = tkinter.Entry(self, font=('Arial', 12), width=20)
    self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


app = FinalProject()
app.mainloop()
