from pprint import pprint

import requests
import tkinter
from tkinter import ttk
from datetime import datetime



class WeatherApp(tkinter.Tk):
    key = '8d1190f5d14aec57ec38911c0605755e'
    url = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self):
        super().__init__()

        self.title('Погода')
        self.setup_ui()
        self.get_weather()
        self.mainloop()
        self.update_time()

    def setup_ui(self):
        self.resizable(False, False)

        self.datetime_label = tkinter.Label(self, text='')
        self.datetime_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.city_label = ttk.Label(self, text='Город:')
        self.city_label.grid(row=1, column=0, padx=5, pady=5)


        self.city_entry = ttk.Entry()
        self.city_entry.grid(row=1, column=1, padx=5, pady=5)


        self.weather_button = ttk.Button(self, text='Узнать погоду', command=self.get_weather())
        self.weather_button.grid(row=1, column=2, padx=5, pady=5)


        self.weather_icon = ttk.Label(self)
        self.weather_icon.grid(row=2, column=0, padx=5, pady=5)


        self.weather_info = ttk.Label(self, text ='')
        self.weather_info.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


    def update_time(self):
        current_time = datetime.now().strftime('%d.%m.%Y.%H:%M.%S')
        self.datetime_label.config(text=f'Дата и время: {current_time}')
        self.after(1000, self.update_time)




    def get_weather(self):
        city=self.city_entry.get()
        response = requests.get(self.url, params={
            'q': 'Гомель',
            'lang': 'ru',
            'appid': self.key,
            'units': 'metric'
        })

        data=response.json()

        try:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            feels_like = data['main']['feels_like']
            humidity = data['main']['feels_like']

            weather_icon=f'https://api.openweathermap.org/img/w/{data["weather"][0]["icon"]}.png'
            icon = tkinter.PhotoImage(data=requests.get(weather_icon).content)
            self.weather_icon.configure(image=icon)
            self.weather_icon.image = icon

            self.weather_info.config(text=f'Погода в городе {city}: {description}, температура: {temperature}\n'
                                          f'Ощущается как {feels_like}, влажность: {humidity}%')
        except KeyError:
            self.weather_info.config(text='Ошибка получения погоды.')


app = WeatherApp()






