from tkinter import*
import os, winshell
from win32com.client import Dispatch
import getpass
from tkinter import messagebox as mb
import webbrowser

dir= os.path.dirname(__file__) 
USER_NAME = getpass.getuser()
ln=os.path.dirname(os.path.abspath(__file__))

def press():
    if (var1.get() == 1) and (var2.get() == 1):
        desktop = winshell.desktop()
        # Соединяем пути, с учётом разных операционок.
        path = os.path.join(desktop, "Folder_archiver.lnk")
        # Задаём путь к файлу, к которому делаем ярлык.
        target = '{}\Folder_archiver.exe'.format(ln)
        # Назначаем путь к рабочей папке.
        wDir = '{}'.format(dir)
        # Путь к нужной нам иконке.
        icon = '{}\icon.ico'.format(ln)
        # С помощью метода Dispatch, обьявляем работу с Wscript (работа с ярлыками, реестром и прочей системной информацией в windows)
        shell = Dispatch('WScript.Shell')
        # Создаём ярлык.
        shortcut = shell.CreateShortCut(path)
        # Путь к файлу, к которому делаем ярлык.
        shortcut.Targetpath = target
        # Путь к рабочей папке.
        shortcut.WorkingDirectory = wDir
        # Тырим иконку.
        shortcut.IconLocation = icon
        # Обязательное действо, сохраняем ярлык.
        shortcut.save()
        USER_NAME = getpass.getuser()
        file_path = ln + r'\Folder_archiver.exe'
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "Folder_archiver.bat", "w+") as bat_file:
            bat_file.write(r'start  %s' % file_path)
        mb.showinfo('Применено','Настройки применены успешно.')
    elif (var1.get() == 1):
        desktop = winshell.desktop()
        # Соединяем пути, с учётом разных операционок.
        path = os.path.join(desktop, "Folder_archiver.lnk")
        # Задаём путь к файлу, к которому делаем ярлык.
        target = '{}\Folder_archiver.exe'.format(ln)
        # Назначаем путь к рабочей папке.
        wDir = '{}'.format(ln)
        # Путь к нужной нам иконке.
        icon = '{}\icon.ico'.format(ln)
        # С помощью метода Dispatch, обьявляем работу с Wscript (работа с ярлыками, реестром и прочей системной информацией в windows)
        shell = Dispatch('WScript.Shell')
        # Создаём ярлык.
        shortcut = shell.CreateShortCut(path)
        # Путь к файлу, к которому делаем ярлык.
        shortcut.Targetpath = target
        # Путь к рабочей папке.
        shortcut.WorkingDirectory = wDir
        # Тырим иконку.
        shortcut.IconLocation = icon
        # Обязательное действо, сохраняем ярлык.
        shortcut.save()
        mb.showinfo('Применено','Настройки применены успешно.')
    elif (var2.get() == 1):
        USER_NAME = getpass.getuser()
        file_path = ln + r'\Folder_archiver.exe'
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "Folder_archiver.bat", "w+") as bat_file:
            bat_file.write(r'start  %s' % file_path)
        mb.showinfo('Применено','Настройки применены успешно.')
def documentation():
    url = 'https://anysoftware64.herokuapp.com/'
    webbrowser.open_new(url)
fc="#EAEDED"
font='Arial 11'
bg='#1B2631'
root=Tk()
root.title('Настройка программы')
root.geometry("520x200")
root.iconbitmap(ln + r'\icon_2.ico')
root.resizable(0, 0)
root.configure(bg='#1B2631')
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь",command=documentation)
helpmenu.add_command(label="Отправить отзыв")
mainmenu.add_cascade(label="Справка", menu=helpmenu)
var1 = IntVar()
var2 = IntVar()
ch1=Checkbutton(root,bg=bg,variable=var1,onvalue=1,offvalue=0,)
ch1.grid(row=2,column=1,padx=15,pady=10)
ch2=Checkbutton(root,bg=bg,variable=var2,onvalue=1,offvalue=0)
ch2.grid(row=4,column=1,padx=15,pady=10)
lab1=Label(root,text='Добавить ярлык на рабочий стол:',bg=bg,fg=fc,font=font)
lab1.grid(row=2,column=3,padx=15,pady=10)
lab2=Label(root,text='Добавить программу в автозагрузку Windows:',bg=bg,fg=fc,font=font)
lab2.grid(row=4,column=3,padx=15,pady=10)
btn1=Button(root,text='Применить',font=font,command=press)
btn1.grid(row=5,column=6,padx=15,pady=10)
root.mainloop()