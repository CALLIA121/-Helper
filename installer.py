import subprocess
import sys
required_modules = [
    ['pyautogui', 'pyautogui'],
    ['googletrans', 'googletrans'],
    ['sqlite3', 'sqlite3'],
    ['pygame', 'pygame'],
    ['gtts', 'gtts'],
    ['pyperclip', 'pyperclip'],
    ['numpy', 'numpy'],
    ['speech_recognition', 'SpeechRecognition'],
    ['pyaudio', 'pyaudio']
]
for module, toInstall in required_modules:
    try:
        __import__(module)
        print(f"{module} уже установлен.")
    except ImportError:
        print(f"Установка {module}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", toInstall])
        print(f"Установлен модуль {module}")
