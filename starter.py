import installerMain
import pyautogui as gui
import os

import win32.win32api
import pyperclip

import sys

python_interpreter_path = sys.executable

print("Путь к интерпретатору Python:", python_interpreter_path)

current_lang_id = win32.win32api.GetKeyboardLayout()
if current_lang_id != 67699721:
    pyperclip.copy("!change")
    print('Переключение раскладки на английскую')
    gui.hotkey(['alt', 'shift'])


print('Start')
PATH_ME = __file__[:len(__file__) - len('starter.py')]
os.system(f'{python_interpreter_path} "{PATH_ME}main.py"')
