import tkinter
from tkinter import ttk
from config import MONDAY_SCHEDULE,TUESDAY_SCHEDULE, WEDNESDAY_SCHEDULE, THURHDAY_SCHEDULE, FRIDAY_SCHEDULE,  LESSON_TIMES

class ScheduleApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('ClassesSchedule')
        self.resizable = False, False
        self.lesson_times = LESSON_TIMES
        self.schedules = [MONDAY_SCHEDULE, TUESDAY_SCHEDULE, WEDNESDAY_SCHEDULE, THURHDAY_SCHEDULE, FRIDAY_SCHEDULE]

        self.table = ttk.Treeview(self, columns=('day', 'number', 'subject', 'time', 'classroom'), show='headings')

        self._create_table()

    def _create_table(self):
        self.table.heading('day', text='День недели')
        self.table.heading('number', text='Номер урока')
        self.table.heading('subject', text='Учебный предмет')
        self.table.heading('time', text='Время')
        self.table.heading('classroom', text='Аудитория')


        for schedule in self.schedules:
            for lesson_number, lesson in schedule.items():
                start_time = self.lesson_times[lesson_number - 1]['start_time']
                end_time = self.lesson_times[lesson_number - 1]['end_time']

                self.table.insert('', 'end', values=(lesson.day, lesson_number, lesson.name, f'{start_time}-{end_time}', lesson.classroom))
                
        self.table.insert('', 'end')

        self.table.column('day', anchor='center')
        self.table.column('number', anchor='center')
        self.table.column('subject', anchor='center')
        self.table.column('time', anchor='center')
        self.table.column('classroom', anchor='center')

        self.table.pack(fill='both', expand=True)

app = ScheduleApp()
app.mainloop()