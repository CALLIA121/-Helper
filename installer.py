import subprocess
import sys
required_modules = [
    'pyautogui',
    'googletrans',
    'sqlite3',
    'pygame',
    'gtts'
]
for module in required_modules:
    try:
        __import__(module)
        print(f"{module} уже установлен.")
    except ImportError:
        print(f"Установка {module}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", module])
        print(f"Установлен модуль {module}")