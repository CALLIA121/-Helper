import pyautogui
import shutil
import sys
import os
from time import sleep as sl
from PyQt6.QtWidgets import QApplication, QMessageBox


def show_message_box(text, mainText='Информация', title='Ассистент'):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setText(mainText)
    msg_box.setInformativeText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(
        QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)

    retval = msg_box.exec()
    if retval == QMessageBox.StandardButton.Ok:
        return True
    else:
        return False


def show_text(text, mainText='Информация', title='Ассистент'):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setText(mainText)
    msg_box.setInformativeText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(
        QMessageBox.StandardButton.Ok)
    msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)

    msg_box.exec()


def show_text_command(command):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setText('Информация')
    msg_box.setInformativeText(
        f'Хорошо, напишите сами: \n"{command}".\n Могу скопировать команду в буффер обмена для удобства.')
    msg_box.setWindowTitle('Ассистент')

    copy_button = msg_box.addButton(
        "Скопировать", QMessageBox.ButtonRole.ActionRole)
    no_copy_button = msg_box.addButton(
        "Не копировать", QMessageBox.ButtonRole.ActionRole)

    msg_box.setDefaultButton(no_copy_button)

    msg_box.exec()

    if msg_box.clickedButton() == copy_button:
        clipboard = QApplication.clipboard()
        clipboard.setText(command)


def run():
    PATH_ME = __file__[:len(__file__) - len('instalGit.py')]
    with open(f'{PATH_ME}config.txt', 'r', encoding='utf-8') as f:
        CONFIG = [line.strip().split(';') for line in f.readlines()]

    PATH = None

    for atribute, value in CONFIG:
        if atribute == 'PATH':
            PATH = value

    if PATH is None:
        PATH = input('Для работы напишите путь, к дерриктории с файлами: ')
        while True:
            if os.path.exists(PATH):
                break
            else:
                print('Дерриктории по написанному пути не существует\n. Напишите Y если нужно создать деррикторию по написанному пути, или другой путь.')
                inp = input()
                if inp == 'Y':
                    os.mkdir(PATH)
                else:
                    PATH = inp

    if PATH[-1] != '/':
        PATH += '/'
    app = QApplication(sys.argv)
    ok = show_message_box(
        'Разрешите открыть PowerShell для выполнения уставки данных с Git. Если вы нажмете отказать, придется выполнить установку вручную', 'Требуется разрешение')
    if ok:
        sl(0.1)
        pyautogui.hotkey(['win', 'r'])
        sl(0.1)
        pyautogui.typewrite('PowerShell')
        sl(0.5)
        pyautogui.press('enter')
        sl(0.5)
        pyautogui.typewrite(f'cd "{PATH}"')
        sl(0.2)
        pyautogui.press('enter')
        sl(0.5)
        pyautogui.typewrite(
            f'git clone --branch HelperData https://github.com/CALLIA121/-Helper.git')
        sl(0.2)
        pyautogui.press('enter')
        show_text('Нажмите ОК после окончания установки')
    else:
        show_text('Хорошо, откройте PowerShell. \nOK для следующего действия')
        show_text(f'Напишите "cd {PATH}" \nOK для следующего действия')


if __name__ == '__main__':
    run()
