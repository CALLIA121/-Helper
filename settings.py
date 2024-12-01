import sqlite3 as sq
TIMEOUT = 10

HURD_UPDATE = False
VOISE_NAME = 'Russian'

PATH = "D:/!PycharmProjects/!Helper/"

Say = False
DBlist = {1: "Programs"}
DB_PATH = PATH + 'db_helper.db'


ReadyMadePfrase = [
    ('K', 'start', 5),
    ('K', 'bye', 2),
    ('K', 'err', 1),
    ('K', 'stopFrase', 3),
    ('K', 'CanselFrase', 1),

    ('P', 'Отменяю', 'CanselFrase0'),

    ('P', 'Запускаю', 'start0'),
    ('P', 'В процессе', 'start1'),
    ('P', 'Будет сделано', 'start2'),
    ('P', 'Так точно', 'start3'),
    ('P', 'Хорошо', 'start4'),

    ('P', 'Пока', 'bye0'),
    ('P', 'До связи', 'bye1'),

    ('P', 'произошла ошибка', 'err0'),

    ('P', 'Спасибо!', 'stopFrase0'),
    ('P', 'Всегда к вашим услугам!', 'stopFrase1'),
    ('P', 'За что?', 'stopFrase2')
]


connect = sq.connect(DB_PATH, check_same_thread=False)
cursor = connect.cursor()
