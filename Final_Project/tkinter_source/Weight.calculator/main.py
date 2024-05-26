import tkinter

def button_click():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        result = weight / (height**2)
        text = f'Индекс массы тела равен: {result:.2f}'
    except ValueError:
        text = f'Данные должны иметь числовой тип'
    result_label.config(text = text)

root = tkinter.Tk()
root.title('Калькулятор веса')
root.geometry('400x250')

height_label = tkinter.Label(root, text = 'Введите рост(м)', font=('Arial', 15))
height_label.place(relx=0.5, rely=0.1, anchor='center')

height_entry = tkinter.Entry(root, font=('Arial', 15), justify='center')
height_entry.place(relx=0.5, rely=0.2, anchor='center')

weight_label = tkinter.Label(root, text='Введите вес(кг)', font=('Arial', 15))
weight_label.place(relx=0.5, rely= 0.35, anchor = 'center')

weight_entry = tkinter.Entry(root, font=('Arial', 15), justify='center')
weight_entry.place(relx=0.5, rely= 0.45, anchor = 'center')

button = tkinter.Button(root, text='Рассчитать', font = ('Arial', 15))
button.place(relx=0.5, rely= 0.65, anchor = 'center')

result_label = tkinter.Button(root, font = ('Arial', 15), command=button_click)
result_label.place(relx=0.5, rely= 0.85, anchor = 'center')
if __name__ == '__main__':
    root.mainloop()



