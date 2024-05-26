from datetime import datetime
from typing import NamedTuple


class Lesson(NamedTuple):
    name: str
    classroom: str
    day: str

MONDAY_SCHEDULE = {
    1: Lesson(name='Трудовое обучение', classroom='1-1', day='Понедельник'),
    2: Lesson(name='Математика', classroom='1-2', day='Понедельник'),
    3: Lesson(name='Русский язык', classroom='1-3', day='Понедельник'),
    4: Lesson(name='Русская литература', classroom='1-3', day='Понедельник'),
    5: Lesson(name='Английский язык', classroom='1-4', day='Понедельник'),
    6: Lesson(name='Искусство', classroom='1-5', day='Понедельник'),
}
TUESDAY_SCHEDULE = {
    0: Lesson(name='Белорусский язык', classroom='1-6', day='Вторник'),
    1: Lesson(name='Математика', classroom='1-2', day='Вторник'),
    2: Lesson(name='Биология', classroom='1-7', day='Вторник'),
    3: Lesson(name='Химия', classroom='1-8', day='Вторник'),
    4: Lesson(name='Физика', classroom='1-9', day='Вторник'),
    5: Lesson(name='Физра', classroom='1-10', day='Вторник'),
    6: Lesson(name='Белорусская литература', classroom='1-6', day='Вторник'),
}
WEDNESDAY_SCHEDULE = {
    1: Lesson(name='Математика', classroom='1-2', day='Среда'),
    2: Lesson(name='География', classroom='1-11', day='Среда'),
    3: Lesson(name='Русский язык', classroom='1-3', day='Среда'),
    4: Lesson(name='Белорусский язык', classroom='1-6', day='Среда'),
    5: Lesson(name='Русская литература', classroom='1-3', day='Среда'),
    6: Lesson(name='Всемирная история', classroom='1-12', day='Среда'),
}
THURHDAY_SCHEDULE = {
    1: Lesson(name='Ч.З.С', classroom='1-10', day='Четверг'),
    2: Lesson(name='Математика', classroom='1-2', day='Четверг'),
    3: Lesson(name='Химия', classroom='1-8', day='Четверг'),
    4: Lesson(name='Информатика', classroom='1-13', day='Четверг'),
    5: Lesson(name='Английский язык', classroom='1-4', day='Четверг'),
    6: Lesson(name='География', classroom='1-11', day='Четверг'),
}
FRIDAY_SCHEDULE = {
    0: Lesson(name='Математика', classroom='1-2', day='Пятница'),
    1: Lesson(name='Физика', classroom='1-9', day='Пятница'),
    2: Lesson(name='Физра', classroom='1-10', day='Пятница'),
    3: Lesson(name='Английский язык', classroom='1-4', day='Пятница'),
    4: Lesson(name='Биология', classroom='1-7', day='Пятница'),
    5: Lesson(name='История Беларуси', classroom='1-12', day='Пятница'),
}
LESSON_TIMES=[
{
        'lesson_number':0,
        'start_time': '12.50',
        'end_time':'13.35'
    },
{
        'lesson_number':1,
        'start_time': '13.55',
        'end_time':'14.40'
    },
{
        'lesson_number':2,
        'start_time': '14.55',
        'end_time':'15.40'
    },
{
        'lesson_number':3,
        'start_time': '15.55',
        'end_time':'16.40'
    },
{
        'lesson_number':4,
        'start_time': '16.55',
        'end_time':'17.40'
    },
{
        'lesson_number':5,
        'start_time': '17.50',
        'end_time':'18.35'
    },
{
        'lesson_number':6,
        'start_time': '18.45',
        'end_time':'19.30'
    },
]

