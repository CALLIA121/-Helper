import speech_recognition as sr
import pyaudio
import pygame
import os
import random
import time
import wave
import settings as s
import numpy as np

from gtts import gTTS

PATHMAIN = s.PATH
HURD_UPDATE = s.HURD_UPDATE
PFRASE_READY_MADE = s.ReadyMadePfrase
PhraseKeys = []
mode = 'Buffer'


def sintes(text, path):
    tts = gTTS(text=text, lang='ru')
    tts.save(path)


def init():
    print('Иницилизация audio...')
    global recognizer
    recognizer = sr.Recognizer()
    pygame.mixer.init()
    # model = vosk.Model(PATHMAIN + "vosk-model-small-ru-0.22")
    global HURD_UPDATE
    global PFRASE_READY_MADE, PhraseKeys
    for Phrase in PFRASE_READY_MADE:
        if Phrase[0] == "P":
            text, path = Phrase[1:]
            if not os.path.exists(PATHMAIN + "sound/" + path + ".mp3") or HURD_UPDATE:
                print('Создание:', PATHMAIN + "sound/" + path + ".mp3")
                sintes(text, PATHMAIN + "sound/" + path + ".mp3")
            else:
                print('Файл уже есть, пропуск:',
                      PATHMAIN + "sound/" + path + ".mp3")
        elif Phrase[0] == "K":
            PhraseKeys.append((Phrase[1], Phrase[2]))


def regizon(filePath):
    try:
        print("Распознавание...")
        with sr.AudioFile(filePath) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        print(f"Вы сказали: {text}")
        return str(text).lower()
    except sr.UnknownValueError:
        return "-"
    except sr.RequestError as e:
        print(f"Не удалось запросить результаты из Google Web Speech API; {e}")
        return "-"


def listenMy() -> str:
    global recognizer
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = PATHMAIN + "sound/output.wav"
    frames = []
    average_volume = 0
    timeout = 1  # Таймаут в секундах
    last_volume_time = time.time()
    microphone = sr.Microphone()
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    with microphone:
        print("ГОВОРИ!!!!")
        play("sound/ready.mp3")
        while True:
            data = stream.read(CHUNK)
            frames.append(data)

            # Преобразование данных в массив numpy
            audio_data = np.frombuffer(data, dtype=np.int16)

            # Вычисление текущей громкости
            current_volume = np.linalg.norm(
                audio_data) / np.sqrt(len(audio_data))

            # Обновление средней громкости
            average_volume = 0.9 * average_volume + 0.1 * current_volume

            # Проверка условия для остановки записи
            # print(current_volume, average_volume)
            if current_volume > (average_volume * 1.5):
                last_volume_time = time.time()
            else:
                if time.time() - last_volume_time > timeout:
                    play("sound/finish.mp3")
                    print("Запись остановлена из-за низкой громкости.")
                    wf = wave.open(OUTPUT_FILENAME, 'wb')
                    wf.setnchannels(CHANNELS)
                    wf.setsampwidth(audio.get_sample_size(FORMAT))
                    wf.setframerate(RATE)
                    wf.writeframes(b''.join(frames))
                    wf.close()
                    break
    return regizon(OUTPUT_FILENAME)


def play(PATH, waitEnd=True):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()  # Освобождаем файл
    PATH = PATHMAIN + PATH
    print("play:", PATH)
    pygame.mixer.music.load(PATH)
    pygame.mixer.music.play()

    # Ожидание окончания воспроизведения
    while pygame.mixer.music.get_busy() and waitEnd:
        pass
    # После воспроизведения освобождаем файл и удаляем его
    pygame.mixer.music.unload()  # Освобождаем файл


def say(text, waitEnd=True):
    # Проверяем, не играет ли музыка, и останавливаем
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()  # Освобождаем файл

    # Синтез речи и сохранение в фа
    sintes(text, PATHMAIN + "sound/speech.mp3")

    # Загрузка и воспроизведение
    pygame.mixer.music.load(PATHMAIN + "sound/speech.mp3")
    pygame.mixer.music.play()

    # Ожидание окончания воспроизведения
    while pygame.mixer.music.get_busy() and waitEnd:
        pass

    # После воспроизведения освобождаем файл и удаляем его
    pygame.mixer.music.unload()  # Освобождаем файл
    if os.path.exists(PATHMAIN + "sound/speech.mp3"):
        os.remove(PATHMAIN + "sound/speech.mp3")


def sayReady(key, waitEnd=True):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    global PhraseKeys

    if key in [x[0] for x in PhraseKeys]:
        Index = [x[0] for x in PhraseKeys].index(key)
        path = f'{PATHMAIN}sound/' \
            f'{key}{random.randint(0, PhraseKeys[Index][1] - 1)}.mp3'
        print(PhraseKeys[Index][1])
        print("play", path)
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy() and waitEnd:
            pass

        pygame.mixer.music.unload()


def Buffer():
    global recognizer
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = PATHMAIN + "sound/buff.wav"
    frames = []
    average_volume = 0
    timeout = 0.5  # Таймаут в секундах
    last_volume_time = time.time()
    microphone = sr.Microphone()
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    with microphone:
        print("Запись")
        while True:
            data = stream.read(CHUNK)
            frames.append(data)

            # Преобразование данных в массив numpy
            audio_data = np.frombuffer(data, dtype=np.int16)

            # Вычисление текущей громкости
            current_volume = np.linalg.norm(
                audio_data) / np.sqrt(len(audio_data))

            # Обновление средней громкости
            average_volume = 0.9 * average_volume + 0.1 * current_volume

            # Проверка условия для остановки записи
            # print(current_volume, average_volume)
            if current_volume > average_volume:
                last_volume_time = time.time()
            else:
                if time.time() - last_volume_time > timeout:
                    print("Запись остановлена.")
                    wf = wave.open(OUTPUT_FILENAME, 'wb')
                    wf.setnchannels(CHANNELS)
                    wf.setsampwidth(audio.get_sample_size(FORMAT))
                    wf.setframerate(RATE)
                    wf.writeframes(b''.join(frames))
                    wf.close()
                    break


def listen_phrase(activation_phrase="ассистент"):
    global mode
    print("Слушаю активационную фразу...")
    FILENAME = PATHMAIN + "sound/buff.wav"
    while True:
        Buffer()
        text = regizon(FILENAME).split()
        if activation_phrase in text:
            print("Активационная фраза распознана.")
            index = text.index(activation_phrase)
            if len(text) - 1 > index:
                print('Фраза уже содержит команду:', " ".join(text[index+1:]))
                return " ".join(text[index+1:])
            else:
                print("Слушаю следующий текст...")
                return listenMy()
