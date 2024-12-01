def searchProgram(text: list, programs: list) -> str:
    print("Поиск среди: ", text)
    for namesStr, path in programs:
        namesSps = namesStr.split('|')
        for name in namesSps:
            if name in text:
                return True, name, path
    return False, "F", "F"


def check(text: str, check: list) -> bool:
    for checkWord in check:  # приветприветпривет
        if checkWord in text:
            try:
                return text.split().index(checkWord.split()[-1])
            except Exception as e:
                return -14
    return -1


def main():
    LT = time.time() - 2 * s.TIMEOUT
    stop = False

    while not stop:
        if time.time() - LT > s.TIMEOUT:
            text = audio.listen_phrase()
        else:
            text = audio.listenMy()
        text = text.lower()
        textSps = text.split()
        st = False
        print(f"обработка, {time.time() - LT:.2f} секунд с прошлой обработки")
        if text == "-":
            print("ниче не сказали")
            st = True
            print("окончание обработки")

        elif check(text, ["напиши", "впиши"]) >= 0:
            index = check(text, ["напиши", "впиши"])  # hello привет
            towrite = " ".join(textSps[index+1:])
            print("пишем:", towrite)
            type_text(towrite)
            audio.sayReady("start")

        elif check(text, ["загуглить", "загугли", 'если']) >= 0:
            # hello привет
            index = check(text, ["загуглить", "загугли", 'если'])
            togoogle = " ".join(textSps[index+1:])
            if GogoleSearch(togoogle):
                audio.sayReady("start")
                st = True
            else:
                audio.sayReady("err")

        elif check(text, ["как", "где", "что такое", "сколько это"]) >= 0:
            index = check(text, ["как", "где", "что такое",
                          "сколько это"])  # hello привет
            togoogle = " ".join(textSps[index:])
            if GogoleSearch(togoogle):
                audio.sayReady("start")
                st = True
            else:
                audio.sayReady("err")

        elif check(text, ["измени раскладку", "смени раскладку", "переключи раскладку", "поменяй раскладку"]) >= 0:
            change_selected_text_layout()
            audio.sayReady("start")

        elif check(text, ["удали комментарии", "удали комментарий"]) >= 0:
            audio.sayReady("start")
            code = get_selected_text().splitlines()
            codeChange = []
            for line in code:
                if '#' in line:
                    lineChange = line[:line.index('#')]
                else:
                    lineChange = line
                codeChange.append(lineChange)
            code = '\n'.join(codeChange)
            type_text(code)

        elif check(text, ["переведи"]) >= 0:
            audio.sayReady("start")
            try:
                type_text(translate_text())
            except Exception as e:
                audio.sayReady("err")
                print(e)

        elif check(text, ["прочти", "прочитай"]) >= 0:
            audio.say(get_selected_text())

        elif check(text, ["запусти", "включи", "открой"]) >= 0:
            index = check(text, ["запусти", "включи", "открой"])
            lastIndex = len(textSps) - 1
            mabyProgram = []
            programs = db.GetData(1, "`Name`, `Path`")
            if index + 2 <= lastIndex:
                mabyProgram.append(
                    f'{textSps[index + 1]} {textSps[index + 2]}')
            if index > 2:
                mabyProgram.append(
                    f'{textSps[index - 2]} {textSps[index - 1]}')
            result = searchProgram(mabyProgram, programs)
            if not result[0]:
                mabyProgram = []
                if index + 1 <= lastIndex:
                    mabyProgram.append(textSps[index + 1])
                if index > 1:
                    mabyProgram.append(textSps[index - 1])
                result = searchProgram(mabyProgram, programs)
            if result[0]:
                try:
                    if "GOOGLE:" in result[2]:
                        link = result[2][7:]
                        print("проход по:", link)
                        if SearchHTTPS(link):
                            audio.sayReady("start")
                        else:
                            audio.sayReady("err")
                    else:
                        start = f'''"{result[2]}"'''
                        print(f'''запуск {start}''')
                        threading.Thread(target=os.system, args=[
                                         start], daemon=True, name=result[0]).start()
                        audio.sayReady("start")
                except Exception as e:
                    audio.sayReady("err")
                    print("Ошибка:", e)
            else:
                audio.say("Не смог распознать программу")

        elif check(text, ["посчитай", "посчитать"]) >= 0:
            index = check(text, ["посчитай", "посчитать"])
            try:
                tocalculate = " ".join(textSps[index+1:])
                tocalculate = tocalculate.replace("х", "*")
                print("считем:", tocalculate)
                form = tocalculate.split()
                result = 0.0
                d = -1
                for dig in form:
                    if dig in ["+", "-", "*", "/"]:
                        d = dig
                    elif dig in ["поизведение", "сумма", "разность", "частное"]:
                        sl = {"поизведение": "*",
                              "сумма": "+",
                              "разность": "-",
                              "частное": "/"}
                        d = [sl[dig], 1, 0, d]
                    else:
                        try:
                            dig = dig.replace(".", "")
                            dig = dig.replace(",", ".")
                            dig = float(dig)
                            if d == -1:
                                result += dig
                            elif isinstance(d, str):
                                if d == "+":
                                    result += dig
                                elif d == "-":
                                    result -= dig
                                elif d == "*":
                                    result *= dig
                                elif d == "/":
                                    result /= dig
                            elif isinstance(d, list):
                                if d[1] != 1:
                                    if d[0] == "+":
                                        d[2] += dig
                                    elif d[0] == "-":
                                        d[2] -= dig
                                    elif d[0] == "*":
                                        d[2] *= dig
                                    elif d[0] == "/":
                                        d[2] /= dig
                                else:
                                    d[2] = dig
                                d[1] += 1
                                if d[1] == 3:
                                    if d[3] == "+":
                                        result += d[2]
                                    elif d[3] == "-":
                                        result -= d[2]
                                    elif d[3] == "*":
                                        result *= d[2]
                                    elif d[3] == "/":
                                        result /= d[2]
                        except Exception as e:
                            # %SystemRoot%\system32\rundll32.exe USER32.DLL LockWorkStation
                            print(e)
                print(float_to_fraction(result),
                      float_to_fraction_with_reading(result))
                audio.say(float_to_fraction_with_reading(result))
                LT = time.time() + s.TIMEOUT
                continue
            except Exception as e:
                print(e)
                audio.sayReady("ошибка")

        elif check(text, ["заблокируй", "заблочь"]) >= 0:  # LL
            if 'отмена' not in text:
                print('''hotkey(['winleft', "L"])''')
                os.system(
                    '%SystemRoot%/system32/rundll32.exe USER32.DLL LockWorkStation')
                st = True
                print("окончание обработки")
            else:
                audio.sayReady("CanselFrase")

        elif check(text, ["отключайся", "выключайся"]) >= 0:
            if 'отмена' not in text:
                audio.sayReady("bye")
                stop = True
            else:
                audio.sayReady("CanselFrase")

        elif check(text, ["заверши работу"]) >= 0:
            if 'отмена' not in text:
                os.system('shutdown /s /t 0')
                LT = time.time() - 2 * s.TIMEOUT
                st = True
                print("окончание обработки")
            else:
                audio.sayReady("CanselFrase")

        elif check(text, ["спасибо", "подожди", 'жди', "молодец", "пока", "хорош"]) >= 0:
            st = True
            print("окончание обработки")
            if "молодец" in text or "хорош" in text:
                audio.play('sound/stopFrase0.mp3')
            elif "спасибо" in text:
                audio.play('sound/stopFrase1.mp3')

        elif check(text, ["иди", 'пошёл', 'тупой', 'заткнись', 'дебил', 'дурак']) >= 0:
            st = True
            print("окончание обработки")
            audio.play('sound/stopFrase2.mp3')

        else:
            audio.say('я такого не умею')

        if st:
            LT = time.time() - 1.1 * s.TIMEOUT
        else:
            LT = time.time()


if __name__ == '__main__':
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
    import audio
    import os
    import time
    import settings as s
    import db
    from Functions import (type_text,
                           change_selected_text_layout,
                           float_to_fraction,
                           float_to_fraction_with_reading,
                           translate_text,
                           get_selected_text,
                           get_text,
                           GogoleSearch,
                           SearchHTTPS,
                           InitMy)
    import threading
    # threading.Thread(target=audio.Buffer, daemon=True, name="Buffer").start()
    InitMy()
    audio.init()
    """
    audio._saveSound('start', 'start0')
    audio._saveSound('В процессе', 'start1')
    audio._saveSound('Будет сделано', 'start2')
    audio._saveSound('Так точно', 'start3')
    audio._saveSound('Хорошо', 'start4')

    audio._saveSound('Пока', 'bye0')
    audio._saveSound('До связи', 'bye1')

    audio._saveSound('произошла ошибка', 'err')

    audio._saveSound('Спасибо!', 'stopFrase1')
    audio._saveSound('Всегда к вашим услугам', 'stopFrase2')
    audio._saveSound('За что?!', 'stopFrase3')
    """
    main()
