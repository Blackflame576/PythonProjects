from tkinter import*
from tkinter import filedialog
from tkinter import messagebox as mb
import os


path=os.path.dirname(__file__) 
fg="#EAEDED"
font='Arial 11'
bg='#1B2631'
ln=os.path.dirname(os.path.abspath(__file__))

def choose():
    global directory
    global eg
    eg=(ent1.get())
    directory = filedialog.askdirectory()
def write():
    try:
        f = open('data.py','w+',encoding='utf-8')
        f.write("class Data:" + '\n' + '\t' + "name='{}'".format(eg)+ '\n' + '\t' + "path='{}'".format(directory))
        f.close()
        mb.showinfo('Применено','Настройки применены успешно.')
        
    except NameError:
       mb.showerror('Ошибка','Не введено название архива или не выбрана папка для архивации.')


root=Tk()
root.geometry("520x200")
root.title('Настройки архивации')
root.resizable(0, 0)
root.configure(bg='#1B2631')
root.iconbitmap(ln + '\icon_2.ico')
lab1=Label(root,fg=fg,bg=bg,font=font,text='Введите название архива:')
lab1.grid(row=2,column=2,padx=15,pady=10)
ent1=Entry(root,bg=fg,font=font)
ent1.grid(row=2,column=4,padx=15,pady=10)
lab2=Label(root,fg=fg,bg=bg,font=font,text='Выберите папку:')
lab2.grid(row=4,column=2,padx=15,pady=10)
but1=Button(root,bg=fg,font=font,text='Выбрать',command=choose)
but1.grid(row=4,column=4,padx=15,pady=10)
but2=Button(root,bg=fg,font=font,text='Применить',command=write)
but2.grid(row=6,column=6,padx=15,pady=3)
root.mainloop()

