import tkinter
from tkinter import ttk
from googletrans import Translator

class App:
    languages = {
        'Русский': 'ru',
        'Английский':'en',
        'Французкий':'fr'
    }


    def __init__(self):
        self.root = tkinter.Tk()
        self.window_settings()
        self.set_header()
        self.input_text()
        self.output_text()
        self.create_translate_button()
        self.root.mainloop()
    def window_settings(self):
        self.root.title("Переводчик")
        self.root.geometry('600x400')
        self.root.resizable(False, False)


    def set_header(self):
        header_frame = tkinter.Frame(self.root)
        header_frame.pack(fill='x')

        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)

        self.lang_menu_from = ttk.Combobox(header_frame, values=[lang for lang in self.languages], state='readonly')
        self.lang_menu_from.current(0)
        self.lang_menu_from.grid(row=0, column=0)

        self.lang_menu_to = ttk.Combobox(header_frame, values=[lang for lang in self.languages], state='readonly')
        self.lang_menu_to.current(1)
        self.lang_menu_to.grid(row=0, column=2)

    def input_text(self):
        """
        Создание поля для ввода текста, который будем переводить
        :return:
        """

        self.text_input = tkinter.Text(self.root, width = 50, height = 8, font=('Arial', 12))
        self.text_input.pack(pady=10)

    def create_translate_button(self):
        """
        Создание кнопки для перевода
        :return:
        """
        button =tkinter.Button(self.root, text="Перевести", font =('Arial', 12), command=self.translate_text)
        button.pack()

    def output_text(self):
        """
        Поле с результатом перевода
        :return:
        """
        self.text_output = tkinter.Text(self.root, width=50, height=8, font=('Arial', 12))
        self.text_output.pack(pady=10)


    def translate_text(self):
        """
        Функция для перевода текста
        :return:
        """
        translator = Translator()
        language_suffix = self.languages.get(self.lang_menu_to.get())
        text = self.text_input.get('1.0', tkinter.END)

        translation=translator.translate(text, dest=language_suffix)

        self.text_output.delete('1.0', tkinter.END)
        self.text_output.insert('1.0', translation.text)



app=App()







