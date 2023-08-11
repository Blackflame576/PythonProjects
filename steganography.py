from stegano import exifHeader
import os
from tkinter import filedialog as fd


file = fd.askopenfile()
if file: 
    f=(file.name)
    text = open(f,'r',encoding='utf-8')
    t = text.read()
secret = exifHeader.hide(r"C:\Users\Werty-28\Documents\Blackflame\обои\wallhaven-9mxz8k.jpg", r"C:\Users\Werty-28\Documents\Blackflame\обои\wallhaven-9mxz8k(1).jpg",t)

result = exifHeader.reveal(r"C:\Users\Werty-28\Documents\Blackflame\обои\wallhaven-9mxz8k(1).jpg")
result = result.decode()
print(result)

