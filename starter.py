import installer
import pyautogui as gui
import win32.win32api
import os
import time

import win32
import pyperclip


current_lang_id = win32.win32api.GetKeyboardLayout()
if current_lang_id != 67699721:
    pyperclip.copy("!change")
    print('Переключение раскладки на английскую')
    gui.hotkey(['alt', 'shift'])
        

print('Start')
os.system('''C:/Users/1/AppData/Local/Microsoft/WindowsApps/python3.12.exe d:/!PycharmProjects/!Helper/main.py''')
