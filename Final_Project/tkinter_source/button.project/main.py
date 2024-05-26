import sys
import tkinter
import random
from tkinter import messagebox





class App:
    def __init__(self):
        self.root = tkinter.Tk()

        self.window_settings()
        self.set_label()
        self.set_button_no()
        self.set_button_yes()

        self.root.mainloop()

    def window_settings(self):
        """

        :param self:
        :return:
        """
        self.root.title('опрос')
        self.root.geometry('600x400')
        self.root.resizable(False, True)

    def set_label(self):
        """

        :return:
        """

        question = tkinter.Label(self.root, text = 'Вы хотите увеличить зарплату?', font =('Arial', 20))
        question.place(relx=0.5, rely=0.1, anchor='center')

    def set_button_yes(self):
        self.btn_yes = tkinter.Button(self.root, text='да', font=('Arial', 20))
        self.btn_yes.place(relx=0.3,rely=0.5,anchor='center')
        self.btn_yes.bind('<Enter>', self.motion_button_yes)

    def set_button_no(self):
        btn_no=tkinter.Button(self.root, text='нет', font=('Arial', 20), command=self.button_no_click)
        btn_no.place(relx=0.7,rely=0.5,anchor='center')
    @staticmethod
    def button_no_click():
        tkinter.messagebox.showinfo('Ответ', 'Спасибо, ваш ответ учтен ')
        sys.exit()

    def motion_button_yes(self, *args):
        self.btn_yes.place(x=random.randint(0,400), y=random.randint(0,200))

app=App()