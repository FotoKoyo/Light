import os
from time import sleep
import speech_recognition as sr
from fuzzywuzzy  import fuzz
import pyttsx3
import datetime
import webbrowser as web
from colorama import Fore
import random
import pyautogui as pg
import subprocess
import getpass
from tkinter import *
import ctypes           
import keyboard
import requests
from gtts import gTTS 
# import playsound
# from pyowm import OWM
# from sound import Sound
# from PIL import Image

from Core.internet   import *


banner1 = ('''
▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀
▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀
▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄''')


banner2 = ('''
.%%...%%..%%%%%%..%%.......%%%%....%%%%...%%...%%..%%%%%%.
.%%...%%..%%......%%......%%..%%..%%..%%..%%%.%%%..%%.....
.%%.%.%%..%%%%....%%......%%......%%..%%..%%.%.%%..%%%%...
.%%%%%%%..%%......%%......%%..%%..%%..%%..%%...%%..%%.....
..%%.%%...%%%%%%..%%%%%%...%%%%....%%%%...%%...%%..%%%%%%.
..........................................................''')


banner3 = ('''
              _                          
             | |                         
__      _____| | ___ ___  _ __ ___   ___ 
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
 \ V  V /  __/ | (_| (_) | | | | | |  __/
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|''')


banner4 = ('''
+-+-+-+-+-+-+-+
|w|e|l|c|o|m|e|
+-+-+-+-+-+-+-+''')


banner5 = ('''
  _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ 
( W | e | l | c | o | m | e )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ ''')


banner6 = ('''
 __      __          ___                                        
/\ \  __/\ \        /\_ \                                       
\ \ \/\ \ \ \     __\//\ \     ___    ___     ___ ___      __   
 \ \ \ \ \ \ \  /'__`\\ \ \   /'___\ / __`\ /' __` __`\  /'__`\ 
  \ \ \_/ \_\ \/\  __/ \_\ \_/\ \__//\ \L\ \/\ \/\ \/\ \/\  __/ 
   \ `\___x___/\ \____\/\____\ \____\ \____/\ \_\ \_\ \_\ \_____
    '\/__//__/  \/____/\/____/\/____/\/___/  \/_/\/_/\/_/\/____/''')


banner7 = ('''
 _  _  ____  __     ___  __   _  _  ____ 
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)''')


banner8 = ('''
   ___   ###########################
  /\:/\  ##|:+:|####\`~'/#####(:)###
 /(o:o)\ ##(o:o)####(o o)#####|:|###
   (:)   ###(:)######\ / \####|:|###
         #############"#############''')


banner9 = ('''
 ________         __                            
|  |  |  |.-----.|  |.----.-----.--------.-----.
|  |  |  ||  -__||  ||  __|  _  |        |  -__|
|________||_____||__||____|_____|__|__|__|_____|''')


banner10 = ('''
 **       **          **                                     
/**      /**         /**                                     
/**   *  /**  *****  /**  *****   ******  **********   ***** 
/**  *** /** **///** /** **///** **////**//**//**//** **///**
/** **/**/**/******* /**/**  // /**   /** /** /** /**/*******
/**** //****/**////  /**/**   **/**   /** /** /** /**/**//// 
/**/   ///**//****** ***//***** //******  *** /** /**//******
//       //  ////// ///  /////   //////  ///  //  //  ////// ''')


banner11 = ('''
W     W     l                    
W     W     l                    
W  W  W eee l  ccc ooo mmmm  eee 
 W W W  e e l c    o o m m m e e 
  W W   ee  l  ccc ooo m m m ee  ''')


banner12 = ('''
             __                  
 _    _____ / /______  __ _  ___ 
| |/|/ / -_) / __/ _ \/  ' \/ -_)
|__,__/\__/_/\__/\___/_/_/_/\__/ 
''')


os.system("cls")
file = (r'C:\Light\Core\internet.py')
# os.system("start "+file)
f = [Fore.BLUE, Fore.YELLOW, Fore.RED, Fore.GREEN, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
d = random.choice(f)
print(d)
# print(Fore.YELLOW)
a = [banner1, banner2, banner3, banner4, banner5, banner6, banner7, banner8, banner9, banner10, banner11, banner12]
c = random.choice(a)
print(c)
print(Fore.GREEN)


discord = r"C:\Users\slow\AppData\Local\Discord\Update.exe --processStart Discord.exe"
telegram = r"D:\Проги\Telegram Desktop\Telegram.exe"
sublime = r"D:\Проги\Sublime_Text 3\sublime_text.exe"
steam = r"C:\Program_Files_(x86)\Steam\steam.exe"
epicgames = r"C:\Program_Files_(x86)\Epic_Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"

opts = {
    "alias": ('light', 'лайт', 'пожалуйста', 'прислужник', 'открой', 'покажи', 'включи', 'доброе', 'добрый'
              'сегодняшний', 'дубина','скажи', 'сколько', 'добавь', 'выключи', 'ты', 'кот', 'поменяй', 'очисти'
              'терра', 'записывай', 'за', 'на', 'сверни', 'верни', 'сделай', 'сделать', 'кликни', 'наклейки', 'компьютер'
              'голосовой', 'закрой', 'выруби', 'жукова', 'заверши', 'увеличь', 'уменьши', 'без', 'лайт', 'привет'
              'отправь', 'пока', 'какая', 'код', 'слушай', 'лайк', 'да'),

    "tbr": ('скажи','расскажи','покажи','сколько','произнеси', 'лайт', 'light', 'пожалуйста'),
    "cmds": {


        # Light
        "clear": ('очисти историю команд', 'очисти мою историю', 'очисти команды', 'историю команд', 'мою историю', 'команды', 'очисти запросы', 'запросы', 'очисти все комнды', 'все команды'),
        "ok": ('лайт', 'компьютер', 'light'),
        "banner": ('покажи все баннеры', 'все баннеры'),


        # Music
        "music": ('включи мой плейлист', 'мой плейлист'),
        "musicran": ('включи рандомную музыку', 'включи случайную музыку', 'включи рандомную песню', 'включи случайную песню', 'рандомную музыку', 'случайную музыку', 'рандомную песню', 'случайную песню'),
        "playlist1": ('включи 1 плейлист', '1 плейлист', 'включи первый плейлист', 'первый плейлист'),
        "playlist2": ('включи 2 плейлист', '2 плейлист', 'включи второй плейлист', 'второй плейлист'),
        "playlist3": ('включи 3 плейлист', '3 плейлист', 'включи третий плейлист', 'третий плейлист'),


        # Browser
        "search": ('открой свой поисковик', 'открой мой поисковик', 'мой поисковик', 'свой поисковик'),
        "youtube": ('открой youtube', 'открой ютуб', 'youtube'),
        "browser": ('открой браузер', 'браузер', 'открой основной браузер', 'основной браузер'),
        "animego": ('открой сайт по просмотру аниме', 'открой animego', 'открой сайт аниме', 'сайт по просмотру аниме', 'animego', 'сайт аниме'),
        "wikipedia": ('открой сайт wikipedia', 'открой wikipedia', 'сайт wikipedia', 'wikipedia', 'википедию', 'открой википедию'),
        "twitch": ('открой твич', 'твич', 'открой twitch', 'twitch'),
        "virustotal": ('открой virustotal', 'virustotal', 'вирус тотал', 'открой вирус тотал', 'верстат'),
        "gmail": ('открой gmail', 'gmail', 'гмаил', 'открой гмаил', 'открой мою почту', 'мою почту'),
        "vk": ('открой вк', 'вк', 'открой vk', 'vk'),
        "googletranslate": ('открой переводчик', 'переводчик', 'открой гугл переводчик', 'гугл переводчик', 'google переводчик', 'октрой google переводчик'),
        "github": ('открой i2hard', 'i2hard', 'открой github', 'github', 'открой гитхаб', 'гитхаб'),
        "whatsapp": ('открой whatsapp', 'whatsapp', 'ватсап'),
 

        # Speak
        "hello": ('привет', 'здарова', 'ку', 'лайт'),
        "bye": ('пока', 'до встречи', 'иди в жопу', 'лайт'),
        "whoareyou": ('кто ты', 'кто вы', 'что ты такое', 'что ты сдесь делаешь'),
        "why": ('почему ты здесь', 'для чего ты здесь', 'как ты здесь появилась'),
        "ctime": ('текущее время', 'сейчас времени', 'который час', 'скажи время', 'сколько сейчас времени'),
        "sun": ('утро', 'доброе утро'),
        "today": ('день', 'добрый день'),
        "omw": ('сегодняшний прогноз погоды', 'прогноз погоды'),
        "you": ('ты лох', 'ты чмо', 'ты говноед', 'ты дебил', 'ты бот', 'ты нуб', 'лох', 'чмо', 'говноед', 'дебил', 'бот', 'нуб'),
        "shut": ('выключи компьютер', 'выключи комп', 'компьютер', 'комп'),
        "work": ('за работу', 'на чём мы остановились', 'работу', 'чём мы остановились'),
        "newfrend": ('знакомься', 'знакомься это'),
        "iback": ('я вернулся', 'вернулся', 'я пришёл', 'я тут'),


        # System
        "startandstop": ('стоп', 'остановись', 'останови видео', 'старт', 'запусти', 'запусти видео'),
        "fullscreen": ('сделай видео полноэкранным', 'полноэкранным', 'сделай полный экран', 'полный экран', 'сделать видео полный экран', 'видео полный экран'),
        "scan": ('просканируй компьютер', 'просканируй комп', 'поищи модификации windows'),
        "cmd": ('открой cmd', 'открой цмд', 'открой командную строку', 'cmd', 'командную строку', 'цмд', 'центр'),
        "scandisk": ('просканируй диск', 'найди угрозы на диск', 'просканируй жёсткий диск'),
        "startup": ('открой папку автозагрузки', 'папку автозагрузки'),
        "window": ('сверни все окна', 'верни окна назад', 'сверни окна', 'верни окна', 'сверни окно', 'верни окно', 'все окна', 'окна назад', 'окна'),
        "click": ('кликни', 'клик', 'сделай клик', 'клик мышкой', 'сделай клик мышкой', 'кликни мышкой', 'мышкой'),
        "rec": ('записывай всё', 'записывай то что слышишь'),
        "stop": ('стоп', 'старт', 'включи видео', 'останови видео', 'возобнови видео', '100', 'топ'),
        "sleep": ('засни', 'спи', 'усни', 'спящий режим'),
        "input": ('голосовой ввод', 'ввод', 'голосовая клавиатура', 'клавиатура'),
        "process": ('закрой все процессы', 'выключи все процессы', 'все процессы', 'выруби все процессы', 'заверши все задачи', 'все задачи'),
        "taskmanager": ("открой диспетчер задач", 'диспетчер задач'),


        # Screen
        "1366x768": ('сделай экран 16 на 9', 'экран 16 на 9', 'сделай экран нормальным', 'экран нормальным'),
        "1280x768": ('сделай экран немного расширенным', 'экран немного расширенным'),
        "1024x768": ('сделай экран 4 на 3', 'экран 4 на 3', 'сделай расширенный экран', 'расширенный экран'),
        "light": ("включи свет", 'свет', 'включи белый экран', 'белый экран', 'включи смешной фанарик', 'смешной фанарик', 'открой белый фон', 'белый фон'),


        # Volume
        "volumeup": ('сделай звук погромче', 'звук погромче', 'увеличь звук', 'звук'),
        "volumedown": ('сделай звук пониже', 'звук пониже', 'уменьши звук', 'звук'),
        "volumeno": ('без звука', 'звука', 'сделай без звука'),


        # Explorer
        "source": ('открой свой исходный код', 'покажи свой исходный код', 'открой свой код', 'покажи свой код'),
        "autorun": ('открой папку автозагрузки', 'покажи папку автозагрузки'),
        "explorer": ('открой проводник', 'покажи проводник', 'проводник'),
        "downloads": ('открой папку загрузки', 'покажи папку загрузки', 'открой загрузки', 'открой папку загрузка', 'папку загрузки', ''),
        "temp": ('открой временные файлы', 'открой папку temp', 'покажи временные файлы', 'покажи папку temp', 'погода', 'темп', 'открой темп'),
        "programm": ('открой папку проги', 'папку проги', 'папку с программами'),
        "programmer": ('открой мои проекты', 'открой programmer', 'мои проекты', 'programmer'),
        

        # Programm
        "telegram": ('открой телеграм', 'telegram', 'телегу'),
        "discord": ('открой дискорд', 'открой дс', 'discord', 'дс'),
        "memreduct": ('открой мем редакт', 'открой mem reduct', 'дебридат', 'мем редакт'),
        "sublimetext": ('открой редактор кода', 'редактор кода', 'открой согласен текст', 'согласен текст', 'открой саблайм текс', 'саблайм текс'),
        "steam": ('открой steam', 'steam', 'открой стим', 'стим'),
        "whatsapp": ('открой whatsapp', 'открой ватсапп', 'whatsapp', 'ватсапп'),
        "wallpaper_engine": ('открой wallpaper engine', 'wallpaper engine', 'открой живые обои', 'живые обои'),
        "obs": ("открой обс", "obs", 'открой obs', 'обс'),
        "trash": ("открой корзину", 'открой мусор'),
        "epic": ('epic gamesm', 'открой epic games'),


        # Коды запуска
        "hot": ('код 113'),
        "zero": ('код 718'),
        "sp": ('код 567'),
    }
}

def color():
    f = [Fore.BLUE, Fore.YELLOW, Fore.RED, Fore.GREEN, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    d = random.choice(f)
    print(d)


# функции
def speak(what):
    print( what )
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()

def callback(recognizer, audio):
    try:
        voice = (r.recognize_google(audio, language="ru-RU")).lower()
        f = [Fore.BLUE, Fore.YELLOW, Fore.RED, Fore.GREEN, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        d = random.choice(f)
        print(d)
        print(f"[log] Распознано: {voice}")
    
        if voice.startswith(opts["alias"]):
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        # print("Я вас не слышу")
        pass
    except sr.RequestError as e:
        print(Fore.RED)
        print("[log] Пожалуйста провертьте подлючение к интернету")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))


    # Light
    elif cmd == 'clear':
        os.system("cls")

    elif cmd == 'ok':
        speak("Слушаю")

    elif cmd == 'banner':
        print(banner1)
        print(banner2)
        print(banner3)
        print(banner4)
        print(banner5)
        print(banner6)
        print(banner7)
        print(banner8)
        print(banner9)
        print(banner10)
        print(banner11)
        print(banner12)

    # Music
    elif cmd == 'music':
        web.open('https://www.youtube.com/playlist?list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT')

    elif cmd == 'musicran':
        z = ["https://www.youtube.com/watch?v=XzfWbi9xkgs&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=1",
            "https://www.youtube.com/watch?v=lrgQwvYAIC4&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=2",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=3",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=4",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=5",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=6",
            "https://www.youtube.com/watch?v=PIZ_2uZ64AI&list=PLdWvcLU6s-CQ6C5mryMJLuL6LcEdTm2LT&index=7",]
        x = random.choice(z)
        web.open(x)

    elif cmd == 'playlist1':
        web.open("https://www.youtube.com/watch?v=aEFREZRQ6FM&list=PLJN6x0_6gGDQg9QrmZ-s_2rPgxVQM7XI3&index=2")

    elif cmd == 'playlist2':
        web.open("https://www.youtube.com/watch?v=h4zJrehSzXY&list=PLJN6x0_6gGDTroaA4HSpt0Ff9Tmp6CB0x&index=7")

    elif cmd == 'playlist3':
        web.open("https://www.youtube.com/watch?v=lKAa0Qa88M4&list=PLJN6x0_6gGDQY5NWv_nBFmuU3mEDcYVMA&index=3")


    # Browser
    elif cmd == 'search':
        internet()

    elif cmd == 'youtube':
        web.open("www.youtube.com")

    elif cmd == 'browser':
        web.open("www.google.com")

    elif cmd == 'animego':
        web.open("https://animego.org/")

    elif cmd == 'wikipedia':
        web.open("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    elif cmd == 'twitch':
        web.open("https://www.twitch.tv/")

    elif cmd == 'virustotal':
        web.open("https://www.virustotal.com/gui/home/upload")

    elif cmd == 'gmail':
        web.open("https://mail.google.com/mail/u/0/#inbox")

    elif cmd == 'vk':
        web.open("https://vk.com/feed")

    elif cmd == 'googletranslate':
        web.open("https://translate.google.com/")

    elif cmd == 'gtihub':
        web.open("https://github.com/")

    elif cmd == 'whatsapp':
        web.open("https://web.whatsapp.com/")


    # Speak
    elif cmd == 'hello':
        z = ["Рада снова вас слышать!", 'Что вам угодно?', 'Привет. Чем-нибудь помочь?']
        x = random.choice(z)
        speak(x)

    elif cmd == 'bye':
        z = ["До свидание", 'Удачного дня!']
        x = random.choice(z)
        speak(x)
        quit()

    elif cmd == 'whoareyou':
        speak("Я умная машина который слушет ваши команды. Меня создали чтобы служить вам")

    elif cmd == 'why':
        z = ["Вы скачали меня", "Вы установили меня"]
        x = random.choice(z)
        speak(x)

    elif cmd == 'sun':
        z = ["Доброе утро", 'Доброе. Что вам угодно?', 'Привет. Чем-нибудь помочь?']
        x = random.choice(z)
        speak(x)

    elif cmd == 'owm':
        s_city = "Nyrba,RU"
        city_id = 0
        appid = "4178417d595eb066c767225c216a790c"
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            for i in data['list']:
                print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
        except Exception as e:
            print("Exception (forecast):", e)
            pass

    elif cmd == 'you':
        x = ['Обзываться плохо!', 'Иди в жопу', 'Сам такой']
        z = random.choice(x)
        speak(z)

    elif cmd == 'shut':
        x = ['Иди в жопу', 'Сам выключись', 'Пошёл на фиг']
        z = random.choice(x)
        speak(z)

    elif cmd == 'work':
        file = (r'C:\Проги\Sublime_Text 3\sublime_text.exe')
        os.system("start "+ file)

    elif cmd == 'newfrend':
        speak("Рада познакомиться")


    # System
    elif cmd == 'startandstop':
        pg.typewrite(["space"])

    elif cmd == 'fullscreen':
        pg.typewrite(["F"])

    elif cmd == 'cmd':
        os.system("start")

    elif cmd == 'scan':
        os.system("sfc /scannow")

    elif cmd == 'startup':
        os.system("start shell:startup")

    elif cmd == 'click':
        pg.click()

    elif cmd == 'rec':
        file = (r'C:\Light\Rec\rec.py')
        os.system("start "+ file)

    elif cmd == 'stop':
        pg.typewrite(["space"])

    elif cmd == 'sleep':
        os.system("rundll32 powrprof.dll,SetSuspendState 0,1,0")

    elif cmd == 'window':
        pg.hotkey('win','d')

    elif cmd == 'input':
        file = (r'F:\Light\Core\input\input.py')
        os.system("start "+ file)

    elif cmd == 'process':
        os.system("taskkill /FI “USERNAME eq SAMURAI” /F")

    elif cmd == 'taskmanger':
        pg.hotkey('crtl', 'shift', 'esc')


    # Screen
    elif cmd == '1366x768':
        file = (r'F:\Light\Core\1366x768.py')
        os.system("start "+ file)

    elif cmd == '1280x768':
        file = (r'F:\Light\Core\1280x768.py')
        os.system("start "+ file)

    elif cmd == '1024x768':
        file = (r'F:\Light\Core\1024x768.py')
        os.system("start "+ file)

    elif cmd == 'light':
        file = (r'F:\Light\Core\light.jpg')
        os.system("start " + file)


    # Volume
    elif cmd == 'volumeup':
        Sound.volume_up()

    elif cmd == 'volumedown':
        Sound.volume_down()

    elif cmd == 'volumeno':
        Sound.mute()


    # Explorer
    elif cmd == 'temp':
        os.system("start temp")

    elif cmd == 'source':
        file = (r"C:/Light")
        os.system("start "+file)

    elif cmd == 'explorer':
        os.system("start explorer")

    elif cmd == 'downloads':
        os.system("start downloads")

    elif cmd == 'autorun':
        pg.hotkey('win', 'r')
        pg.typewrite("shell:Startup")

    elif cmd == 'programmer':
        file = (r'F:\Programmer')
        os.system("start "+ file)

    elif cmd == 'whatsapp':
        file = (r'C:\Users\SAMURAI\AppData\Local\WhatsApp\WhatsApp.exe')
        os.system("start "+ file)


    # Programm
    elif cmd == 'telegram':
        os.system("start "+ telegram)
        
    elif cmd == 'discord':
        os.system("start "+ discord)

    elif cmd == 'memreduct':
        file = (r'C:\Проги\64\memreduct.exe')
        os.system("start "+ file)

    elif cmd == 'sublimetext':
        file = (r'C:\Проги\Sublime_Text 3\sublime_text.exe')
        os.system("start "+ sublime)

    elif cmd == 'steam':
        file = (r'C:\Program Files_(x86)\Steam\steam.exe')
        os.system("start "+ steam)

    elif cmd == 'wallpaper_engine':
        file = (r"C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper64.exe")
        os.system("start "+ file)

    elif cmd == 'trash':
        file = (r"E:\Light\lnk\Корзина.lnk")
        os.system("start "+ file)

    elif cmd == 'epic':
        os.system("start "+ epicgames)


    # Коды запуска
    elif cmd == 'hot':
        os.system("shutdown -s")

    elif cmd == 'zero':
        os.system("shutdown -r -t 0")

    elif cmd == 'sp':
        speak("Что")


    else:
        x = ["Что вы сказали?", "Я не поняла", "Повторите пожалуйса", "Команда не распознана, повторите", "Я прослушала", "Повтори"]
        c = random.choice(x)
        print(c)

# запуск
r = sr.Recognizer()
m = sr.Microphone()
 
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)
while True: sleep(0)