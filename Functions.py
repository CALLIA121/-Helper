import settings as s
import os
from fractions import Fraction
import pyperclip
import time
from googletrans import Translator
translator = Translator()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def InitMy():
    global gui
    import pyautogui as gui


def hotkey(keys: list):
    gui.hotkey(keys)
    time.sleep(0.1)


def get_text():
    selected_text = pyperclip.paste()
    return selected_text


def get_selected_text():
    time.sleep(0.1)
    gui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    selected_text = pyperclip.paste()
    return selected_text


def type_text(text):
    pyperclip.copy(text)
    gui.hotkey('ctrl', 'v')


def translate_text():

    text = get_selected_text()

    if text != "":
        # Определяем язык по первому символу
        first_char = text[0].lower()
        if 'а' <= first_char <= 'я':
            src_lang = 'ru'
            dest_lang = 'en'
        elif 'a' <= first_char <= 'z':
            src_lang = 'en'
            dest_lang = 'ru'
        else:
            raise ValueError("Не удалось определить язык по первому символу")

        # Переводим текст
        translation = translator.translate(text, src=src_lang, dest=dest_lang)

        return translation.text


def is_periodic(number):
    # Преобразуем число в строку и удаляем десятичную точку
    decimal_str = str(number).split('.')[1]
    # Проверяем, является ли десятичная часть периодической
    for i in range(1, len(decimal_str) // 2 + 1):
        if decimal_str[:i] * (len(decimal_str) // i) == decimal_str:
            return True
    return False


def float_to_fraction(number):
    if is_periodic(number):
        # Преобразуем число в дробь
        fraction = Fraction(number).limit_denominator()
        whole_part = fraction.numerator // fraction.denominator
        numerator = fraction.numerator % fraction.denominator
        denominator = fraction.denominator
        if numerator == 0:
            return f"{whole_part}"
        else:
            return f"{whole_part} {numerator}/{denominator}"
    else:
        return number


def drob_to_words(d):
    d1, d2 = map(int, d.split("/"))
    if d1 % 10 == 1:
        if d1 % 100 == 11:
            reed1 = str(d1)
        else:
            if d // 10 * 10 == 0:
                reed1 = "одна"
            else:
                reed1 = str(d // 10 * 10) + " одна"
    elif d1 % 10 == 2:
        if d1 % 100 == 12:
            reed1 = str(d1)
        else:
            if d1 // 10 * 10 == 0:
                reed1 = "две"
            else:
                reed1 = str(d1 // 10 * 10) + " две"
    else:
        reed1 = str(d1)
    ddown = {"1": "ых", "2": "ых", "3": "их", "4": "ых", "5": "ых",
             "6": "ых", "7": "ых", "8": "ых", "9": "ых", "0": "ых"}
    reed2 = str(d2) + "-" + ddown[str(d2)]
    return reed1 + " " + reed2


def read_fraction(value):
    if isinstance(value, float):
        whole_part, decimal_part = str(value).split('.')
        if decimal_part != "0":
            return f"{whole_part} точка {decimal_part}"
        else:
            return whole_part
    elif isinstance(value, str):
        parts = value.split()
        if len(parts) == 1:
            drob = parts[0]
            return drob_to_words(drob)
        else:
            whole_part = parts[0]
            drob = parts[1]
            if whole_part == '0':
                return drob_to_words(drob)
            else:
                return f"{int(whole_part)} целая, {drob_to_words(drob)}"
    else:
        return str(value)


def float_to_fraction_with_reading(number):
    fraction = float_to_fraction(number)
    return read_fraction(fraction)


def change_layout(text):
    # Словари для соответствия символов в разных раскладках
    en_to_ru = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
        'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
        'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
        ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
        'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '`': 'ё', '~': 'Ё',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
        'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы',
        'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
        ':': 'Ж', '"': 'Э', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И',
        'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ','
    }

    ru_to_en = {v: k for k, v in en_to_ru.items()}

    # Определяем раскладку по первому символу
    if text[0].lower() in en_to_ru:
        layout_dict = en_to_ru
    else:
        layout_dict = ru_to_en

    # Преобразование текста
    converted_text = ''.join(layout_dict.get(char, char) for char in text)
    return converted_text


def change_selected_text_layout():
    text = get_selected_text()
    if text != "":
        converted_text = change_layout(text)
        type_text(converted_text)


def GogoleSearch(qvery):
    try:
        os.system(f"{s.PATH}googleSearch.bat {qvery}")
        return True
    except Exception as e:
        return False


def SearchHTTPS(qvery):
    try:
        os.system(f"{s.PATH}googleHTTPS.bat {qvery}")
        return True
    except Exception as e:
        return False
