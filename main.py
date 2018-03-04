from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
from PIL import Image,ImageTk

srt_ = '/Users/test/PycharmProjects/18test_1/test2.jpg'

def selectPath():
    path_ = askdirectory()
    path.set(path_)

def selectPath2():
    global path2
    path_ = askopenfilename()
    path2 = path_

root = Tk()
root.title('Picture Editor')
path = StringVar()


Label(root,text = "图片编辑器",bg='green').grid(row=0,column=1)

Label(root,text = "图片路径:").grid(row = 1, column = 0)

Entry(root, textvariable = path).grid(row = 1, column = 1)

Button(root, text = "图片选择", command = selectPath2()).grid(row = 1, column = 2)


img = Image.open(path2)
img_jpg = ImageTk.PhotoImage(img)
Label(root,image=img_jpg).grid(row = 2, column = 1)



root.mainloop()

