import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
for voice in voices:
    print(voice.name)
    if voice.name == 'Microsoft David Desktop - English (United States)':
        tts.setProperty('voice', voice.id)

tts.say('Hello! This test of voice synthesis on python')
tts.runAndWait()
