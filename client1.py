import socket
import threading
import sys
import os
from datetime import*
import subprocess
import  platform
from tkinter import*
def write():
    while True:
        try:
            today=datetime.today()
            time=today.strftime('%X')        
            message = '{}:{}'.format(nickname,ent2.get())
            client.send(message.encode('utf-8'))
        except EOFError:
            text.insert(1.0,'Вы отсоединились от сервера!До скорой встречи!')
            sys.exit()
            break
root=Tk()
lab1=Label(root,text='Введите свой Nickname:').grid(row=1,column=1)
lab2=Label(root,text='Введите сообщение:').grid(row=2,column=1)
ent1=Entry(root)
ent1.grid(row=1,column=2)
ent2=Entry(root)
ent2.grid(row=3,column=2)
text=Text(root)
text.grid(row=2,column=2)
btn1=Button(root,text='Отправить',command=write)
btn1.grid(row=3,column=3)
# Choosing Nickname
nickname ='nick'

# Connecting To Server
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.145', 8975))
except ConnectionRefusedError:
    text.insert(1.0,'Сервер не доступен!')
    client.close()
# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(500000000).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                text.insert(1.0,message)
        except:
            # Close Connection When Error
            text.insert(1.0,"Соединение прервано!"+'\n'+'Чтобы выйти из приложения зажмите клавиши CTRL и C')
            client.close()
            break
# Sending Messages To Server

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

#write_thread = threading.Thread(target=write)
#write_thread.start()
root.mainloop()
