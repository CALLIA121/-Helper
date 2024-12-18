import sqlite3 as sq
TIMEOUT = 10

HURD_UPDATE = False
VOISE_NAME = 'Russian'

PATH = None
PATH_ME = __file__[:len(__file__) - 11]

print(f'Load config from {PATH_ME}config.txt')

with open(f'{PATH_ME}config.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip().split(';') for line in f.readlines()]
    for atribute, value in lines:
        if atribute == 'PATH':
            PATH = value

if PATH is None:
    print('Нет PATH')
    exit(0)


Say = False
DBlist = {1: "Programs", 2: "Data"}
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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Programs (
    ID   INTEGER PRIMARY KEY ASC AUTOINCREMENT
                 UNIQUE
                 NOT NULL
                 DEFAULT ( -1),
    Name TEXT    UNIQUE
                 NOT NULL
                 DEFAULT None,
    Path TEXT    UNIQUE
                 NOT NULL
                 DEFAULT None
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Data (
    ID  TEXT PRIMARY KEY
             NOT NULL
             UNIQUE
             DEFAULT (0),
    Val TEXT
);
''')
connect.commit()
