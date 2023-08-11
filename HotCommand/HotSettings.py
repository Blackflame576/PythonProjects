#Libraries
import os
import sys
import keyboard
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5 import QtGui
import json
#Paths
BlenderFromDir = None
BlenderToDir = None
UnityFromDir = None
UnityToDir = None
EnableMusic = None
Shutdown = None
Reboot = None
Hibernation = None
BlenderBackup = None
UnityBackup = None
PauseMusic = None
NextMusic = None
commands = {}
lines = []
ErrorLines = False
HomeDir = os.path.expanduser("~")
appPath = os.path.dirname(os.path.realpath(__file__))
iconPath = os.path.dirname(os.path.realpath(__file__)) + r'\HotSettings.png'
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
class HotSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.Interface()
        
        try:
            with open(HomeDir + r'\HotCommandSettings.json') as file:
                dataFile = json.load(file)
            line1.setText(dataFile["BlenderBackup"])
            line2.setText(dataFile["UnityBackup"])
            line3.setText(dataFile["EnableMusic"])
            line4.setText(dataFile["Shutdown"])
            line5.setText(dataFile["Reboot"])
            line6.setText(dataFile["Hibernation"])
            line7.setText(dataFile["PauseMusic"])
            line8.setText(dataFile["NextMusic"])
        except KeyError:
            self.EmptyJSON()
            with open(HomeDir + r'\HotCommandSettings.json','w+',encoding='UTF-8') as file:
                json.dump(commands,file,ensure_ascii=False,sort_keys=True, indent=2)
        except json.decoder.JSONDecodeError:
            self.EmptyJSON()
            with open(HomeDir + r'\HotCommandSettings.json','w+',encoding='UTF-8') as file:
                json.dump(commands,file,ensure_ascii=False,sort_keys=True, indent=2)
        except FileNotFoundError:
            with open(HomeDir + r'\HotCommandSettings.json','w+',encoding='UTF-8') as file:
                json.dump(DefaultCommands,file,ensure_ascii=False,sort_keys=True, indent=2)
    def EmptyJSON(self):
        global commands
        global BlenderBackup
        global UnityBackup
        global EnableMusic
        global Shutdown
        global Reboot
        global Hibernation
        global PauseMusic
        global NextMusic
        global dataDict
        global lines

        with open(HomeDir + r'\HotCommandSettings.json') as file:
            dataFile = json.load(file)

        BlenderBackup = line1.text()
        UnityBackup = line2.text()
        EnableMusic = line3.text()
        Shutdown = line4.text()
        Reboot = line5.text()
        Hibernation = line6.text()
        PauseMusic = line7.text()
        NextMusic = line8.text()
        commands = {
            "BlenderBackup": BlenderBackup,
            "UnityBackup": UnityBackup,
            "EnableMusic": EnableMusic,
            "Shutdown": Shutdown,
            "Reboot": Reboot,
            "Hibernation": Hibernation,
            "BlenderFromDir": BlenderFromDir,
            "BlenderToDir": BlenderToDir,
            "UnityFromDir": UnityFromDir,
            "UnityToDir": UnityToDir,
            "PauseMusic": PauseMusic,
            "NextMusic": NextMusic,
        }

        dataBlender = dataFile["BlenderBackup"]
        dataUnity = dataFile["UnityBackup"]
        dataEnableMusic = dataFile["EnableMusic"]
        dataShutdown = dataFile["Shutdown"]
        dataReboot = dataFile["Reboot"]
        dataHibernation = dataFile["Hibernation"]
        dataPauseMusic = dataFile["PauseMusic"]
        dataNextMusic = dataFile["NextMusic"]
        dataDict = [dataBlender,dataUnity,dataEnableMusic,dataShutdown,dataReboot,dataHibernation,dataPauseMusic,dataNextMusic]

        lines = [line1.text(),line2.text(),line3.text(),line4.text(),line5.text(),line6.text(),line7.text(),line8.text()]
            
    def OpenBlenderFilesFromDir(self):
        global BlenderFromDir
        BlenderFromDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', r'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        print(BlenderFromDir)
    def OpenBlenderFilesToDir(self):
        global BlenderToDir
        BlenderToDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', r'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
    def OpenUnityFilesFromDir(self):
        global UnityFromDir
        UnityFromDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', r'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
    def OpenUnityFilesToDir(self):
        global UnityToDir
        UnityToDir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', r'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
    def Save(self):
        self.EmptyJSON()
        with open(HomeDir + r'\HotCommandSettings.json') as file:
            json.dump(commands,file,ensure_ascii=False,sort_keys=True, indent=2)
    def closeEvent(self,event):
        self.EmptyJSON()
        for data in dataDict:
            if data != lines:
                save = QMessageBox(self)
                save.setIcon(QMessageBox.Question)
                save.setText("Save this settings?")
                save.setWindowTitle("Saving")
                save.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                if save.exec_() == QMessageBox.Yes:
                    self.Save()
                    break
                elif save.exec_() == QMessageBox.No:
                    sys.exit()
            
    def SaveSettings(self):
        self.EmptyJSON()
        for dataLine in lines:
            if dataLine == "":
                error = QMessageBox(self)
                error.setIcon(QMessageBox.Question)
                error.setText('No hotkey combinations have been entered in the fields. Do you want to save the settings with the entered key combinations?')
                error.setWindowTitle('Do you want to save?')
                error.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                if error.exec_() == QMessageBox.Yes:
                    self.Save()
                    break
                elif error.exec_() == QMessageBox.No:
                    break
            else:
                self.Save()
                break
                 
                
            
                
    def BlenderListen(self):
        line1.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def UnityListen(self):
        line2.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def MusicListen(self):
        line3.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def ShutdownListen(self):
        line4.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def RebootListen(self):
        line5.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def HibernationListen(self):
        line6.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def PauseMusicListen(self):
        line7.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def NextMusicListen(self):
        line8.setText(keyboard.read_hotkey(suppress=False))
        keyboard.unhook_all_hotkeys()
    def Interface(self):
        global line1
        global line2
        global line3
        global line4
        global line5
        global line6
        global line7
        global line8
        lab1 = QLabel(self)
        lab1.setText('Blender files from directory:')
        lab1.setFont(QFont('Arial', 12))
        lab1.move(50,50)

        btn = QPushButton('Show', self)
        btn.resize(btn.sizeHint())
        btn.move(250,50)
        btn.setFont(QFont('Arial',10))
        btn.clicked.connect(self.OpenBlenderFilesFromDir)

        lab2 = QLabel(self)
        lab2.setText("Blender files to directory:")
        lab2.setFont(QFont('Arial', 12))
        lab2.move(50,100)

        btn2 = QPushButton('Show', self)
        btn2.resize(btn2.sizeHint())
        btn2.move(250,100)
        btn2.setFont(QFont('Arial',10))
        btn2.clicked.connect(self.OpenBlenderFilesToDir)

        lab3 = QLabel(self)
        lab3.setText("Unity files from directory:")
        lab3.setFont(QFont('Arial', 12))
        lab3.move(50,150)

        btn3 = QPushButton('Show', self)
        btn3.resize(btn3.sizeHint())
        btn3.move(250,150)
        btn3.setFont(QFont('Arial',10))
        btn3.clicked.connect(self.OpenUnityFilesFromDir)

        lab4 = QLabel(self)
        lab4.setText("Unity files to directory:")
        lab4.setFont(QFont('Arial', 12))
        lab4.move(50,200)

        btn4 = QPushButton('Show', self)
        btn4.resize(btn4.sizeHint())
        btn4.move(250,200)
        btn4.setFont(QFont('Arial',10))
        btn4.clicked.connect(self.OpenUnityFilesToDir)

        lab5 = QLabel(self)
        lab5.setText("Blender backup(key1 + key2...):")
        lab5.setFont(QFont('Arial', 12))
        lab5.move(50,250)

        line1 = QLineEdit(self)
        line1.move(300,250)
        line1.setFont(QFont('Arial', 10))

        button1 = QPushButton(self)
        button1.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button1.move(450,250)
        button1.clicked.connect(self.BlenderListen)

        lab6 = QLabel(self)
        lab6.setText("Unity backup(key1 + key2...):")
        lab6.setFont(QFont('Arial', 12))
        lab6.move(50,300)

        line2 = QLineEdit(self)
        line2.move(300,300)
        line2.setFont(QFont('Arial', 10))

        button2 = QPushButton(self)
        button2.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button2.move(450,300)
        button2.clicked.connect(self.UnityListen)

        lab7 = QLabel(self)
        lab7.setText("Enable music(key1 + key2...):")
        lab7.setFont(QFont('Arial', 12))
        lab7.move(50,350)

        line3 = QLineEdit(self)
        line3.move(300,350)
        line3.setFont(QFont('Arial', 10))

        button3 = QPushButton(self)
        button3.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button3.move(450,350)
        button3.clicked.connect(self.MusicListen)

        lab8 = QLabel(self)
        lab8.setText("Shutdown(key1 + key2...):")
        lab8.setFont(QFont('Arial', 12))
        lab8.move(50,400)

        line4 = QLineEdit(self)
        line4.move(300,400)
        line4.setFont(QFont('Arial', 10))

        button4 = QPushButton(self)
        button4.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button4.move(450,400)
        button4.clicked.connect(self.ShutdownListen)

        lab9 = QLabel(self)
        lab9.setText("Reboot(key1 + key2...):")
        lab9.setFont(QFont('Arial', 12))
        lab9.move(50,450)

        line5 = QLineEdit(self)
        line5.move(300,450)
        line5.setFont(QFont('Arial', 10))

        button5 = QPushButton(self)
        button5.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button5.move(450,450)
        button5.clicked.connect(self.RebootListen)

        lab10 = QLabel(self)
        lab10.setText("Hibernation(key1 + key2...):")
        lab10.setFont(QFont('Arial', 12))
        lab10.move(50,500)

        line6 = QLineEdit(self)
        line6.move(300,500)
        line6.setFont(QFont('Arial', 10))

        button6 = QPushButton(self)
        button6.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button6.move(450,500)
        button6.clicked.connect(self.HibernationListen)

        lab11 = QLabel(self)
        lab11.setText("Pause music:")
        lab11.setFont(QFont('Arial', 12))
        lab11.move(50,550)

        line7 = QLineEdit(self)
        line7.move(300,550)
        line7.setFont(QFont('Arial', 10))

        button7 = QPushButton(self)
        button7.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button7.move(450,550)
        button7.clicked.connect(self.PauseMusicListen)

        lab12 = QLabel(self)
        lab12.setText("Pause music:")
        lab12.setFont(QFont('Arial', 12))
        lab12.move(50,600)

        line8 = QLineEdit(self)
        line8.move(300,600)
        line8.setFont(QFont('Arial', 10))

        button8 = QPushButton(self)
        button8.setIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + r'\keyboard.png'))
        button8.move(450,600)
        button8.clicked.connect(self.NextMusicListen)

        btn5 = QPushButton('Save settings', self)
        btn5.resize(85,25)
        btn5.move(500,640)
        btn5.setFont(QFont('Arial',10))
        btn5.clicked.connect(self.SaveSettings)


        window_height = 780
        window_width = 640
        window_x = 440
        window_y = 50
        self.setWindowIcon(QtGui.QIcon(iconPath))
        self.setWindowTitle("HotSettings")
        self.setGeometry(window_x,window_y,window_width,window_height)
        self.setFixedSize(window_width,window_height)
        self.show()
        


#Run code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotSettings()
    sys.exit(app.exec_())