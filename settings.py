import sqlite3 as sq
import os
TIMEOUT = 10

HURD_UPDATE = False
VOISE_NAME = 'Russian'

PATH = None
PATH_ME = __file__[:len(__file__) - 11]

print(f'Load config from {PATH_ME}config.txt')

with open(f'{PATH_ME}config.txt', 'r', encoding='utf-8') as f:
    CONFIG = [line.strip().split(';') for line in f.readlines()]

for atribute, value in CONFIG:
    if atribute == 'PATH':
        PATH = value

if PATH is None:
    print('Нет PATH')
    PATH = input('Для работы напишите путь, к дерриктории с файлами: ')
    while True:
        if os.path.exists(PATH):
            break
        else:
            print('Дерриктории по написанному пути не существует\n. Напишите Y если нужно создать деррикторию по написанному пути, или другой путь.')
            inp = input()
            if inp == 'Y':
                os.mkdir(PATH)
                input('Скачайте архив с данными для ассистента (отсюда https://github.com/CALLIA121/-Helper/tree/HelperData). \nРаспакуйте содержимое в выбранную папку (В папке сразу должны лежать файлы)')
            else:
                PATH = inp
    with open(f'{PATH_ME}config.txt', 'w', encoding='utf-8') as f:
        print(f'PATH;{PATH}', file=f)

if PATH[-1] != '/':
    PATH += '/'


Say = False
DBlist = {1: "Programs", 2: "Data"}
DB_PATH = PATH + 'db_helper.db'
pytesseract_PATH = PATH + r'Tesseract-OCR\tesseract.exe'


ReadyMadePfrase = [
    ('K', 'start', 4),
    ('K', 'bye', 2),
    ('K', 'err', 1),
    ('K', 'stopFrase', 3),
    ('K', 'CanselFrase', 1),

    ('P', 'Отменяю', 'CanselFrase0'),

    ('P', 'Запускаю', 'start0'),
    ('P', 'В процессе', 'start1'),
    ('P', 'Будет сделано', 'start2'),
    ('P', 'Хорошо', 'start3'),

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
