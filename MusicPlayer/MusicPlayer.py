#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Modules
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import os
import time
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
#Variables
StyleSheet = '''
    QLabel{
        color: #ffffff;
    }
    QListWidget::item { 
        margin: 10px;
        padding: 10px;
        color:  #ffffff;
        border-radius: 18px;
	    border: 1px solid;
        border-color:#485656;
    }
    QListWidget::item:hover {
        margin: 10px;
        padding: 10px;
        background:#485656;
        border-radius: 18px;
	    border: 0px solid;
        border-color:#242a2a;
    }
    QListWidget::item::focus {
        margin: 10px;
        padding: 10px;
        background: #161616;
        border-radius: 18px;
	    border: 0px solid;
        border-color:#242a2a;
    }
    QScrollBar:vertical {              
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
        height: 20px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QListWidget {
        border-radius: 18px;
	    border: 0px solid;
        border-color:#242a2a;
    }
    QPushButton{
        background:#242a2a;
    }
    QPushButton:hover{
        background:#242a2a;
    }
'''
# .QSlider {
#         background: #5F4141;
#     }

#     .QSlider::groove:horizontal {
#         height: 8px;
#         background: #ffffff;
#         margin: 0 12px;
#         border-radius: 18px;
# 	    border: 1px solid;
#         border-color:#ffffff;
#     }

#     .QSlider::handle:horizontal {
#         background: red;
#         border: 5px solid #B5E61D;
#         margin: -24px -12px;
#     }
HomeDir = os.path.expanduser("~")
DefaultPathMusics = HomeDir + '\\Music'
MusicFormats = ['.mp3','.wma','.aiff','.wav','.wma','.mp2','.ac3','.amb','.snd']
Musics = []
playing = False
pausing = True
muting = False
class MusicPlayer(QWidget):
    def __init__(self):
        global player
        super().__init__()
        self.player  = QtMultimedia.QMediaPlayer()
        self.player.setVolume(45)
        self.Interface()
        self.InitMusic()
        time.sleep(0.001)
        
        

    def InitMusic(self):
        global playing
        global pausing
        files = os.listdir(DefaultPathMusics)
        for file in files:
            filename = DefaultPathMusics + '\\{}'.format(file)
            FileExtension = os.path.splitext(filename)[1]
            for format in MusicFormats:
                if FileExtension == format:
                    Musics.append(filename.replace('\\',"/"))
                    item = QListWidgetItem(file.replace(FileExtension,""))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(font)
                    ListMusic.addItem(item)
        ListMusic.setCurrentRow(0)
        Slider.setSliderPosition(0)
        playing = False
        pausing = True
    
    def ReInitMusic(self):
        ListMusic.clear()
        files = os.listdir(DefaultPathMusics)
        for file in files:
            filename = DefaultPathMusics + '\\{}'.format(file)
            FileExtension = os.path.splitext(filename)[1]
            for format in MusicFormats:
                if FileExtension == format:
                    Musics.append(filename.replace('\\',"/"))
                    item = QListWidgetItem(file.replace(FileExtension,""))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setFont(font)
                    ListMusic.addItem(item)

    def NextMusic(self):
        global ListMusic
        global Slider
        global playing
        global pausing
        global CurrentNumberTrack
        if (ListMusic.currentRow() + 1) <= len(Musics):
            Slider.setValue(0)
            ListMusic.setCurrentRow(ListMusic.currentRow() + 1)
            CurrentNumberTrack = ListMusic.currentRow()
            print(CurrentNumberTrack)
            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(Musics[CurrentNumberTrack])))
            self.player.play()
            playing = True
            pausing = False

    def PreviousMusic(self):
        global ListMusic
        global Slider
        global playing
        global pausing
        global CurrentNumberTrack
        if (ListMusic.currentRow() - 1) >= 0:
            Slider.setValue(0)
            print(ListMusic.currentRow() - 1)
            ListMusic.setCurrentRow(ListMusic.currentRow() - 1)
            print(ListMusic.currentItem().text())
            CurrentNumberTrack = ListMusic.currentRow()
            print(CurrentNumberTrack)
            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(Musics[CurrentNumberTrack])))
            self.player.play()
            playing = True
            pausing = False

    def Verification(self):
        global lab2
        global lab3
        global ListMusic
        global Slider
        global playing
        global pausing
        global CurrentNumberTrack
        if pausing == False:
            Slider.setMinimum(0)
            Slider.setMaximum(self.player.duration())
            Slider.setValue(Slider.value() + 1000)
        CurrentTime = time.strftime('%M:%S',time.localtime(self.player.position()/1000))
        FullTime = time.strftime('%M:%S', time.localtime(self.player.duration() / 1000))
        if CurrentTime == FullTime and (ListMusic.currentRow() + 1) <= len(Musics):
            Slider.setValue(0)
            ListMusic.setCurrentRow(ListMusic.currentRow() + 1)
            CurrentNumberTrack = ListMusic.currentRow()
            print(CurrentNumberTrack)
            self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(Musics[CurrentNumberTrack])))
            self.player.play()
            playing = True
            pausing = False
        lab2.setText(CurrentTime)
        lab3.setText(FullTime)

    def ChooseTrack(self):
        global CurrentNumberTrack
        global playing
        global pausing
        global Slider
        global lab2
        global lab3
        print("Pressed")
        CurrentNumberTrack = ListMusic.currentRow()
        Slider.setValue(0)
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(Musics[CurrentNumberTrack])))
        self.player.play()
        playing = True
        pausing = False
        print(CurrentNumberTrack)

    def SetPlayPosition(self):
        self.player.setPosition(Slider.value())
        print(Slider.size())
        
    def Process(self):
        global Slider
        global lab2
        global lab3
        global playing
        global pausing
        global btn1
        if pausing == False:
            self.player.pause()
            pausing = True
            playing = False
            btn1.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\play.png'))
        elif playing == False and pausing == True:
            self.player.play()
            pausing = False
            playing = True
            btn1.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\pause.png'))

    def Mute(self):
        global muting
        if muting == False:
            self.player.setMuted(True)
            muting = True
        elif muting == True:
            self.player.setMuted(False)
            muting = False
    def SetVolume(self):
        self.player.setVolume(Slider2.value())
    def Interface(self):
        global Slider2
        global ListMusic
        global font
        global Slider
        global lab2
        global lab3
        global btn1
        font = QFont()
        font.setFamily('Open Sans Condensed') # сам шрифт
        font.setPointSize(12) #  размер шрифта
        MainFont = QFont()
        MainFont.setFamily('Open Sans Condensed') # сам шрифт
        MainFont.setPointSize(24)
        lab1 = QLabel(self)
        lab1.setText("Моя музыка")
        lab1.setFont(MainFont)
        lab1.move(280,50)

        lab2 = QLabel(self)
        lab2.setText('00:00')
        lab2.move(50,502)

        lab3 = QLabel(self)
        lab3.setText('00:00')
        lab3.move(620,502)

        Timer = QTimer(self)
        Timer.timeout.connect(self.Verification)
        Timer.start(1000)

        btn1 = QPushButton(self)
        btn1.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\pause.png'))

        btn1.resize(70,50)
        btn1.setIconSize(QSize(48,48))
        btn1.move(335,560)
        btn1.clicked.connect(self.Process)

        btn2 = QPushButton(self)
        btn2.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\mute.png'))
        btn2.setIconSize(QSize(28,28))
        btn2.move(50,565)
        btn2.clicked.connect(self.Mute)

        btn3 = QPushButton(self)
        btn3.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\repeat.png'))
        btn3.setIconSize(QSize(28,28))
        btn3.move(660,470)
        btn3.clicked.connect(self.ReInitMusic)

        btn4 = QPushButton(self)
        btn4.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\previous.png'))
        btn4.setIconSize(QSize(48,48))
        btn4.resize(70,50)
        btn4.move(245,560)
        btn4.clicked.connect(self.PreviousMusic)

        btn5 = QPushButton(self)
        btn5.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + '\\forward.png'))
        btn5.setIconSize(QSize(48,48))
        btn5.resize(70,50)
        btn5.move(425,560)
        btn5.clicked.connect(self.NextMusic)
        
        Slider2 = QSlider(Qt.Horizontal,self)
        Slider2.sliderMoved[int].connect(self.SetVolume)
        Slider2.move(550,580)
        Slider2.setValue(self.player.volume())

        ListMusic = QListWidget(self,itemDoubleClicked=self.ChooseTrack)
        ListMusic.move(200,150)
        ListMusic.setGeometry(0,100,720,370)
        ListMusic.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        Slider = QSlider(Qt.Horizontal, self)
        Slider.sliderMoved[int].connect(self.SetPlayPosition)
        Slider.setGeometry(100, 460, 500, 100)
        # CurrentNumberTrack = ListMusic.currentRow()
        # print(CurrentNumberTrack)
        window_height = 680
        window_width = 720
        window_x = 300
        window_y = 50
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setWindowTitle('MusicPlayer')
        icon_path = (os.path.dirname(os.path.realpath(__file__)) + '\icon.png')
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.setFixedSize(window_width,window_height)
        self.setStyleSheet('background-color:#242a2a')
        self.show()

#Run code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    app.setStyle('fusion')
    window = MusicPlayer()
    sys.exit(app.exec_())