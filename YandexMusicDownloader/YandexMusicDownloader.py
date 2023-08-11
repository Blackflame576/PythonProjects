from yandex_music import Client
import os
import sys
from progress.bar import Bar
import time
import platform

OS = platform.system()
HomeDir = os.path.expanduser("~")
# os.chdir(HomeDir)
AppDir = os.path.dirname(os.path.realpath(__file__))
client = Client.from_credentials('p4sha.safonov@yandex.ru', 'pavel0818')
playlist = len(client.users_likes_tracks())

def DownloadAll():
    ProgressBar = Bar('Progress:', max = len(client.users_likes_tracks()),suffix='%(percent)d%%')
    for i in range(0,playlist):
        artist = client.users_likes_tracks()[i].fetch_track()["artists"][0]["name"]
        music = client.users_likes_tracks()[i].fetch_track()["title"]
        filename = "{} - {}.mp3".format(music,artist)
        if OS == "Windows":
            exist = HomeDir + '\\Music\\{}'.format(filename)
        else:
            exist = HomeDir + '/Music/{}'.format(filename)
        if not os.path.exists(exist):
            client.users_likes_tracks()[i].fetch_track().download(filename)
            #перемещение файла в каталог музыки
            os.replace(AppDir + '\{}'.format(filename),exist)
            print('\n' + '\n')
            ProgressBar.next()
            print('\n' + '\n')
        elif os.path.exists(exist):
            client.users_likes_tracks()[i].fetch_track().download(filename)
            os.replace(AppDir + '\{}'.format(filename),exist)
            print('\n' + '\n')
            ProgressBar.next()
            print('\n' + '\n')
        time.sleep(4)
    ProgressBar.finish()

def Download(NumberTrack):
    NumberTracks = NumberTrack.split(',')
    ProgressBar = Bar('Progress:', max = len(NumberTracks),suffix='%(percent)d%%')
    for musics in NumberTracks:
        musics = int(musics)
        artist = client.users_likes_tracks()[musics].fetch_track()["artists"][0]["name"]
        music = client.users_likes_tracks()[musics].fetch_track()["title"]
        filename = "{} - {}.mp3".format(music,artist)
        if OS == "Windows":
            exist = HomeDir + '\\Music\\{}'.format(filename)
        else:
            exist = HomeDir + '/Music/{}'.format(filename)
        if not os.path.exists(exist):
            client.users_likes_tracks()[musics].fetch_track().download(filename)
            #перемещение файла в каталог музыки
            os.replace(AppDir + '\{}'.format(filename),exist)
            print('\n' + '\n')
            ProgressBar.next()
            print('\n' + '\n')
        elif os.path.exists(exist):
            client.users_likes_tracks()[musics].fetch_track().download(filename)
            os.replace(AppDir + '\{}'.format(filename),exist)
            print('\n' + '\n')
            ProgressBar.next()
            print('\n' + '\n')
    ProgressBar.finish()

def PlaylistMusics():
    for i in range(0,playlist):
        artist = client.users_likes_tracks()[i].fetch_track()["artists"][0]["name"]
        music = client.users_likes_tracks()[i].fetch_track()["title"]
        filename = "{} - {}.mp3".format(music,artist)
        print('\n' + '{}.  '.format(i) + filename + '\n')

download = (input("Загрузить музыку(y or n)?")).lower()

if download == 'y' or download == '':
    all = input("Загрузить все песни(y or n)?")
elif download == 'n':
    sys.exit()
if all == 'y' or all == '':
    DownloadAll()
elif all == 'n':
    PlaylistMusics()
    NumberTrack = input("Введите номер трека(1,2,3...):")
    if NumberTrack != '':
        Download(NumberTrack)
    elif NumberTrack == '':
        print("Вы не ввели номер трека! Попробуйте повторно запустить программу.")
        sys.exit()