import tkinter
import subprocess
import webbrowser
from PIL import Image, ImageTk


class LauncherApp(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.window_settings()
        self.setup_ui()
        self.setup_icons()
        self.create_button()
        self.open_browser()
        self.run_program()

    def window_settings(self):
        self.title("LauncherApp")

    def setup_icons(self):
        '''
        Создание иконок
        :return:
        '''
        self.notepad_icon = Image.open('images/notepad_22522.png')
        self.notepad_icon = self.notepad_icon.resize((35, 35))
        self.notepad_icon.tk = ImageTk.PhotoImage(self.notepad_icon)

        self.calc_icon = Image.open('images/10310245.png') #Получение пути к картинке
        self.calc_icon = self.calc_icon.resize((35, 35)) #Масштабирование картинки
        self.calc_icon.tk = ImageTk.PhotoImage(self.calc_icon)

        self.paint_icon = Image.open('images/paint_icon.png')
        self.paint_icon = self.paint_icon.resize((35, 35))
        self.paint_icon.tk = ImageTk.PhotoImage(self.paint_icon)

        self.browser_icon = Image.open('images/browser_icon.png')
        self.browser_icon = self.browser_icon.resize((35, 35))
        self.browser_icon.tk = ImageTk.PhotoImage(self.browser_icon)

        self.youtube_icon = Image.open('images/youtube_icon.png')
        self.youtube_icon = self.youtube_icon.resize((35, 35))
        self.youtube_icon.tk = ImageTk.PhotoImage(self.youtube_icon)

        self.github_icon = Image.open('images/github_icon.png')
        self.github_icon = self.github_icon.resize((35, 35))
        self.github_icon.tk = ImageTk.PhotoImage(self.github_icon)

    def create_button(self, text, image, action, action_args, row, column):
        button = tkinter.Button(self, text=text, image=image, compound='left', font=('Arial', 12),
                                command = lambda: action(action_args))
        button.grid(row=row, column=column, padx=5, pady=5, sticky='we', ipadx=5)
        return button


    def run_program(self, program_path: str):
        subprocess.Popen(program_path)

    def open_browser(self, path:str):
        webbrowser.open(path)

    def setup_ui(self):
        apps_label = tkinter.Label(self, text='Приложения', font = ('Arial, 16'))
        apps_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        notepad_button = self.create_button(text='Блокнот', image=self.notepad_22522.tk, action=self.run_program,
                                            action_args='notepad.exe', row=1, column=0)

        calc_button = self.create_button(text='Калькулятор', image=self.calc_icon.tk, action=self.run_program,
                                          action_args='calc.exe', row=1, column=1)

        paint_button = self.create_button(text='Paint', image=self.paint_icon.tk, action=self.run_program,
                                          action_args='mspaint.exe', row=2, column=0)

        websites_label = tkinter.Label(self, text='Вебсайты', font=('Arial', 16))
        websites_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        browser_button = self.create_button(text='Browser', image=self.browser_icon.tk, action=self.run_program,
                                            action_args='Browser.exe', row=4, column=0)

        youtube_button = self.create_button(text='Youtube', image=self.youtube_icon.tk, action=self.run_program,
                                            action_args='Youtube.exe', row=4, column=1)

        github_button = self.create_button(text='Youtube', image=self.github_icon.tk, action=self.run_program,
                                            action_args='Github.exe', row=5, column=0)



if __name__ == '__main__':
    app = LauncherApp()
    app.mainloop()




