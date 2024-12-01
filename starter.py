import win32api
import os

current_lang_id = win32api.GetKeyboardLayout()
import pyautogui as gui
if current_lang_id != 67699721:
    print('Переключение раскладки на английскую')
    gui.hotkey(['alt', 'shift'])
print('Start')
os.system('''C:/Users/1/AppData/Local/Microsoft/WindowsApps/python3.12.exe d:/!PycharmProjects/!Helper/main.py''')
print('OK')