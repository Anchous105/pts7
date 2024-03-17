import tkinter
from tkinter import messagebox
def button_click():
    messagebox.showinfo(title='информация', message='ты жмакнул на кнопку')
#создание основного окна
root = tkinter.Tk()
root.geometry('400x250')

#Создание заголовка
root.title('Мое приложение')

label = tkinter.Label(root, text='Меня зовут Анчоус', font=('Arial', 10))
label.pack()
button = tkinter.Button(root, text='Жмакать здесь', command = button_click)
button.pack()
#Запуск основного цикла(отрисовка)
root.mainloop()