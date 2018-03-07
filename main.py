from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename,asksaveasfilename
from PIL import Image,ImageTk
import os,sys
#from MenuPart import
srt_ = '/Users/test/PycharmProjects/18test_1/test2.jpg'

def selectPath():
    path_ = askdirectory()
    path.set(path_)

def selectPath2():
    global path2
    path2 = StringVar()
    path_ = askopenfilename()
    if path_ != '':
        path2.set(path_)
    else:
        return
'''

#功能1：保存图片(覆盖原图片)

'''
def save():
    img.save(path2.get())
'''

#功能2：另存图片为

'''
def save_as():
    #path_1 = askdirectory()
    path_1 = asksaveasfilename()
    try:
        if path_1 != '':
            filepath1,fileext1=os.path.splitext(path2.get())
            filepath2,fileext2=os.path.splitext(path_1)
            outimagefile = "{0}{1}".format(filepath2,fileext1)
            Image.open(path2.get()).save(outimagefile)
        else:
            print("Error choose!")
    except:
        print('Something wrong here!',path_1)
'''

#功能3：转化为png格式

'''
def trans_to_png():
    path_2 = asksaveasfilename()
    try:
        if path_2 != '':
            #分割文件路径和后缀名
            filepath,fileext=os.path.splitext(path_2)
            #设置保存后的文件格式
            outimagefile = "{0}.png".format(filepath)
            Image.open(path2.get()).save(outimagefile)
        else:
            print("Error Choose!")
    except:
        print('Something wrong here!',path_2)
'''

#功能4：转化为jpg格式

'''
def trans_to_jpg():
    path_3 = asksaveasfilename()
    try:
        if path_3 != '':
            filepath,fileext=os.path.splitext(path_3)
            outimagefile = "{0}.jpg".format(filepath)
            Image.open(path2.get()).save(outimagefile)
        else:
            print("Error choose!")
    except:
        print('Something wrong here!',path_3)

'''

功能5：缩放图片

'''
def resize():
    def ResizeEnter():
        path_resize = '/Users/test/PycharmProjects/test_justforfun/resize_picture.png'
        SizeNum = float(entry1.get())
        w,h = img.size
        print('The sizenum is :',SizeNum)
        n_w,n_h = w//SizeNum,h//SizeNum
        print('The new w and h is:',n_w,n_h)
        resize_img_cpoy = img.copy()
        resize_img_cpoy.thumbnail((n_w,n_h),Image.ANTIALIAS)

        #resize_img = resize_img_cpoy.resize((n_w,n_h), Image.ANTIALIAS)
        r_img = ImageTk.PhotoImage(resize_img_cpoy)
        Label(top1,image = r_img).grid(row = 1, column = 0)
        resize_img_cpoy.show()

        '''
        #保存缩放的图片
        resize_img.save(path_resize,'png')
        rimg = Image.open(path_resize)
        img_r = ImageTk.PhotoImage(rimg)
        Label(top1,image=img_r).grid(row = 1 , column = 0)
        '''
        #print('The resize pic format is :', rimg)

    size = StringVar()
    top1 = Toplevel()
    top1.title('resize')
    entry1 = Entry(top1)
    #默认光标出现
    entry1.focus()
    entry1.grid(row=0, column=0)
    Button(top1, text = 'enter', command = ResizeEnter ).grid(row = 0, column = 1)




def CutPicture():
    pass

root = Tk()
root.title('Picture Editor')

path = StringVar()
path2 = StringVar()


#GetMainMenu(root)
Label(root,text = "图片编辑器",bg='green').grid(row=0,column=1)

Label(root,text = "图片路径:").grid(row = 1, column = 0)

Button(root, text = "图片选择", command = selectPath2()).grid(row = 1, column = 2)

Entry(root, textvariable = path2, state = 'disable').grid(row = 1, column = 1)

img = Image.open(path2.get())
print('The previous pic format is:',img.format)
img_jpg = ImageTk.PhotoImage(img)
label=Label(root,image=img_jpg)
label.grid(row = 2, column = 1)
#保存图片（覆盖）按钮
Button(root,text = 'save',command = save).grid(row = 3,column = 0)
#图片另存为按钮
Button(root,text = 'save as',command = save_as).grid(row = 3 , column = 1)
#转换为png格式按钮
Button(root,text = 'trans_to_png',command = trans_to_png).grid(row = 3 ,column = 2)
#转换为jpg格式按钮
Button(root,text = 'trans_to_jpg',command = trans_to_jpg).grid(row = 3, column= 3)
#缩放图片按钮
Button(root,text = 'resize',command = resize).grid(row = 3 , column = 4 )


root.mainloop()

