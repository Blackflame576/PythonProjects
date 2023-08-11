#Libraries
import json
import threading
import time
import keyboard
import shutil 
import os
import pygame
#Variables
HomeDir = os.path.expanduser("~")
MusicNumber = 0
MusicFormats = ['.mp3','.flac','.ogg','.aac','.wav','.aiff','.dsd','.mqa','.wma','.alac','.pcm']
appPath = os.path.dirname(os.path.realpath(__file__))
MusicPath = HomeDir + r'\Music'
DefaultCommands = {
    "BlenderBackup": "ctrl+shift+b",
    "UnityBackup": "ctrl+shift+u",
    "EnableMusic": "ctrl+shift+m",
    "Shutdown": "ctrl+shift+s",
    "Reboot": "ctrl+shift+r",
    "Hibernation": "ctrl+shift+h",
    "BlenderFromDir": None,
    "BlenderToDir": None,
    "UnityFromDir": None,
    "UnityToDir": None,
    "PauseMusic": "ctrl+shift+p",
    "NextMusic": "ctrl+shift+plus",
}
#Code
def Timer():
    while True:
        time.sleep(20*60)
        # win32ui.MessageBox("Время пошло. Начните зарядку для глаз!", "Начало зарядки")
        time.sleep(5*60) 
        # win32ui.MessageBox("Время зарядки(5 минут) закончилоь. Можете продолжать сидеть за компьютером!", "Время истекло") 
def StopMusic():
    def stop():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause
        elif not pygame.mixer.get_busy():
            pygame.mixer.music.unpause()
    while True:
        keyboard.add_hotkey(dataFile['PauseMusic'],stop)
        # keyboard.record(dataFile['PauseMusic'])
        stop()
        time.sleep(0.5)
        keyboard.unhook_all_hotkeys()
def NextMusic():
    while True:
        keyboard.add_hotkey(dataFile['NextMusic'],lambda:print("NextMusic"))
        time.sleep(0.5)
        keyboard.unhook_all_hotkeys()
def PlayMusic(Music):
    global MusicNumber
    pygame.mixer.music.load(Music)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pos = pygame.mixer.music.get_pos()/ 1000
    MusicNumber += 1
def HotCommand():
    global dataFile
    while True:
        try:
            with open(HomeDir + r'\HotCommandSettings.json') as file:
                dataFile = json.load(file)
        except FileNotFoundError:
            with open(HomeDir + r'\HotCommandSettings.json','w+',encoding='UTF-8') as file:
                json.dump(DefaultCommands,file,ensure_ascii=False,sort_keys=True, indent=2)
        with open(HomeDir + r'\HotCommandSettings.json') as file:
            dataFile = json.load(file)
        if keyboard.read_hotkey() == dataFile["BlenderBackup"]:
            # win32ui.MessageBox("Копирование прошло успешно.", "Копирование")
            print("BlenderBackup")
            for src_dir, dirs, files in os.walk(dataFile["BlenderFromDir"]):
                dst_dir = src_dir.replace(dataFile["BlenderFromDir"], dataFile["BlenderToDir"], 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
                    shutil.copy(src_file, dst_dir)

        elif keyboard.read_hotkey() == dataFile["UnityBackup"]:
            # win32ui.MessageBox("Копирование прошло успешно.", "Копирование")
            print("UnityBackup")
            for src_dir, dirs, files in os.walk(dataFile["UnityFromDir"]):
                dst_dir = src_dir.replace(dataFile["UnityFromDir"], dataFile["UnityToDir"], 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(dst_dir, file_)
                    if os.path.exists(dst_file):
                        os.remove(dst_file)
                    shutil.copy(src_file, dst_dir)
        elif keyboard.read_hotkey() == dataFile["Shutdown"]:
            print("Shutdown")
            os.system('shutdown /p /f')
        elif keyboard.read_hotkey() == dataFile["Reboot"]:
            print("Reboot")
            os.system("shutdown -t 0 -r -f")
        elif keyboard.read_hotkey() == dataFile["Hibernation"]:
            print("Hibernation")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  
        elif keyboard.read_hotkey() == dataFile["EnableMusic"]:
            with open(HomeDir + r'\HotCommandSettings.json') as file:
                dataFile = json.load(file)
            MusicFiles = []
            for dir, subdir, files in os.walk(MusicPath):
                for file in files:
                    print(os.path.join(dir, file))
                    file = os.path.normpath( os.path.join(dir, file))
                    format = os.path.splitext(os.path.join(dir, file))[1]
                    for MusicFormat in MusicFormats:
                        if format == MusicFormat:
                            MusicFiles.append(file)
            stop = threading.Thread(target=StopMusic)
            stop.start()
            time.sleep(1)
            next = threading.Thread(target=NextMusic)
            next.start()
            pygame.mixer.init(96000, -16, 2, 8192)
            pygame.mixer.music.set_volume(2.0)
            for Music in MusicFiles:
                PlayMusic(Music)
            
#Run code
if __name__ == '__main__':           
    timer = threading.Thread(target=Timer)
    hotcommand = threading.Thread(target=HotCommand)
    timer.start()
    hotcommand.start()

