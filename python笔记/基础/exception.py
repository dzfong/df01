#coding=utf-8

#------ 异常处理 #exception ---------
#1、第一种方法，出现异常报错，后面的不执行
#try:
#	检测范围
#except Exception [as reason]:    #例如：except OSError as reason:
#	出现异常 (Exception)后的处理代码
#

try :
	sum = 1 + '1'
	print(sum)
except TypeError as reason:
	print("类型错误：" + str(reason))


print('\n' * 3)


#2、第二种方法，出现异常报错后，执行某段代码。比如关闭文件
#try:
#	检测范围
#finally:
#	无论如果都被执行的代码

try :
	f = open("你好.txt",'w')
	print(f.write('hello world!'))
	sum = 1 + '1'
except (TypeError , OSError):
	print("出错了T_T")
finally :
	f.close()

print('\n' * 3)
#3、没有出现异常的执行判断，用 else :
#try:
#	检测范围
#except Exception [as reason]:    #例如：except OSError as reason:
#	出现异常 (Exception)后的处理代码
#else:
#	没有出现异常会打印

try:
	sum = 1+1
	print(sum)
except :
	print("出错了")
else :
	print("没有出现异常，继续。。。")


print('\n' * 3)

#4、如果往哪个文件写入什么，但是没有这个文件，后面用finally 关闭文件是错误的
#这种情况下可以用 with ...  as ..:
try :
	with open('data.txt' , 'w') as f:
		for each_line in f:
			print(each_line)
except OSError as reason:
	print("出错啦：" + str(reason))
	
