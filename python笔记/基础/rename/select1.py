#coding=utf-8


from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox as messagebox
import os
import shutil

root=Tk()
root.title('批量文件重命名by-dzfong')
path1 = StringVar()
path2 = StringVar()

int1 = IntVar()
int2 = IntVar()

str1 = StringVar()
str2 = StringVar()

#设置原始路径
def sourcePath():
	path_ = askdirectory()
	path1.set(path_)

#存储路径
def destPath():
	path_ = askdirectory()
	path2.set(path_)

#判断
def uchar(uchar):
	'''判断一个unicode是否是汉字'''
	if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
		return True
	'''判断一个unicode是否为数字'''
	if uchar >= u'\u0030' and uchar <= u'\u0039':
		return False
	'''判断一个unicode是否为英文字母'''
	if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
		return False
	if uchar in ('_','-',',' , ' . ','。','?'):
		return False
	return False


#去中文
def getdir():
	cp1 = path1.get()
	cp2 = path2.get()	
	i1 = int1.get()
	if cp1 != cp2 :
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fp = file[:filePoint]
						nname = ''
						for i in range(len(fp)):
							if uchar(fp[i]) == False:
								nname = nname + fp[i]
							else:
								nname = nname + ''
						if nname :
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,nname + file[filePoint:]))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')		
	else :
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	

#去空格
def getstrip():
	cp1 = path1.get()
	cp2 = path2.get()	
	if cp1 != cp2:
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fp = file[:filePoint]
						newName = fp.replace(' ','') + file[filePoint:]
						shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,newName))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')		
	else :
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	


#取中文
def getchina():
	cp1 = path1.get()
	cp2 = path2.get()	
	if cp1 != cp2:
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fp = file[:filePoint]
						nname = ''
						for i in range(len(fp)):
							if uchar(fp[i]):
								nname = nname + fp[i]
							else:
								nname = nname + ''
						if nname :
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,nname + file[filePoint:]))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')		
	else:
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	


#保留前位数
def getNum():
	cp1 = path1.get()
	cp2 = path2.get()	
	i1 = int1.get()
	if cp1 != cp2:
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fq = file[:filePoint]
						if len(fq) >= i1:
							newName = fq[0:i1] + file[filePoint:]
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,newName))
						else:
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,file))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')		
	else :
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	


#保留后位数
def getbehind():
	cp1 = path1.get()
	cp2 = path2.get()	
	i2 = int2.get()
	if cp1 != cp2:
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fq = file[:filePoint]
						if len(fq) >= i2:
							newName = fq[-i2:] + file[filePoint:]
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,newName))
						else:
							shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,file))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')	
	else :
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	


# 替换
def getswitch():
	cp1 = path1.get()
	cp2 = path2.get()	
	s1 = str1.get()
	s2 = str2.get()
	if cp1 != cp2:
		try:
			cf = os.listdir(cp1)
			try :
				if os.path.exists(cp2) :	
					for file in cf:
						filePoint = file.rfind('.')
						fp = file[:filePoint]
						newName = fp.replace(s1,s2) + file[filePoint:]
						shutil.copyfile(os.path.join(cp1,file),os.path.join(cp2,newName))
					if file == cf[-1]:
						messagebox.showinfo('提示','转换完成')			
				else :
					messagebox.showinfo('警告','存储文件夹未选定或路径错误')
			except PermissionError :
				messagebox.showinfo('警告','命名文件中包含文件夹')
		except FileNotFoundError:
			messagebox.showinfo('警告','没有选择目标文件')		
	else :
		messagebox.showinfo('警告','目标文件夹不能和存储文件夹相同')	




Label(root,text='目标路径：').grid(row=0,column=0)
Label(root,text='存储路径：').grid(row=1,column=0)
Entry(root,textvariable=path1).grid(row=0,column=1)
Entry(root,textvariable=path2).grid(row=1,column=1)
Button(root,text="路径选择",command=sourcePath).grid(row=0,column=2)
Button(root,text="路径选择",command=destPath).grid(row=1,column=2)


Button(root,text="去中文",command=getdir).grid(row=3,column=0)
Button(root,text="去空格",command=getstrip).grid(row=3,column=1)
Button(root,text="保留中文",command=getchina).grid(row=3,column=2)
Entry(root,textvariable=int1).grid(row=5,column=1)
Button(root,text="保留前几位",command=getNum).grid(row=5,column=2)
Entry(root,textvariable=int2).grid(row=6,column=1)
Button(root,text="保留后几位",command=getbehind).grid(row=6,column=2)


Label(root,text='字符：').grid(row=7,column=0)
Entry(root,textvariable=str1).grid(row=7,column=1)
Label(root,text='替换为：').grid(row=7,column=2)
Entry(root,textvariable=str2).grid(row=8,column=1)
Button(root,text="替换",command=getswitch).grid(row=8,column=2)

root.mainloop()