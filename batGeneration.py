PATH_ME = __file__[:len(__file__) - len('batGeneration.py')]

with open('Helper.bat', mode="w+") as f:
    f.write(f"{PATH_ME}venv/Scripts/python.exe {PATH_ME}starter.py")

print('Создан файл Helper.bat активируйте, для запуска ассистента)')