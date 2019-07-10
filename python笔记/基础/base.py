#coding=utf-8

print("hello world!")
print("你好")


print('I\'m "ok"')
print("‘中文’的gb2312的编码是 %s" %('中文'.encode('gb2312')))


x= "a"
y= "b"


ages = 	10 + \
		20 + \
		30

print("ages的值为：",ages)
print("ages的类型为",type(ages))
print("我今年" + str(ages) + "岁了")


#换行输出
print (x)
print (y)

print("``````````````")


#不换行输出
print (x, y)


print('''
	标示符 -----   由字母、下划线和数字组成，且数字不能开头（大小驼峰、下划线写法）
	myName
	MyName
	my_name
	''')

'''
s = input("请输入：")
print("您刚才输入的是：%s"%s)
'''

print("=========系统关键字 ============")
import keyword   #导入模块
print(keyword.kwlist) #调用模块中的某个属性keyword.kwlist
 

print("----------" * 5)


from keyword import kwlist  #也是导入模块。只导入使用的那个模块，使用的时候不需要模块的前缀
print(kwlist)


print("----------" * 5)
import time;
ticks = time.time()
print( "当前时间戳为：", ticks)
print("---------------")

localtime = time.localtime(time.time())
print("本地时间为：",localtime)
print("---------------")

loacltime = time.asctime(time.localtime(time.time()))
print("本地时间为：",loacltime)

print("==========格式化日期 strftime============")
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

print("===========获取某年某月某日 calendar==========")
import calendar

cal = calendar.month(2018, 3)
print ("以下输出2018年3月份的日历：")
print (cal)

#定义函数
'''
    多行注释

    函数代码块以 def 关键词开头，后接函数名和圆括号加冒号 ():
    如何传入的参数必须放在圆括号中间
    return[表达式]结束函数，返回一个值给调用方，不带表达式的return相当于返回None
    
	定义函数时，需要确定函数名和参数个数；如果必要可以先对参数类型做检查；
	函数体内部可以用return 随时返回函数结果；函数执行完毕也没有return语句时，自动return None
	函数可以同时返回多个值，但其实就是个tuple。

'''
print ("============== 函数 -================")
#定义函数
def printme(str):
    "打印任何传入的字符串"
    print (str);
    return ;
#调用函数
printme("我要调用用户自定义函数！")
printme("再次调用")
print("-" * 30)



print("========数据类型========")
# 数据类型和运算
b = 10 / 3
print('10 / 3 = ',b)

c = 20 // 3
print('20 // 3 = ',c)

d = 20 % 3
print('20 % 3 = ',d)

print("内置运算函数: 比较两个值cmp(item1, itme2); len(item)计算容器中元素个数; max(item)返回容器中的最大值; min(item)返回容器中的最小值; del(item)删除变量")



print("==========列表list===========")
print("list是一种有序的集合，可以随时添加和删除其中的元素，索引是以0开始的")
list1 = ['michael' , 'bob','tracy']
print(list1[1])
#插入元素
list1.append('hone')
print(list1)
print(len(list1))
print("***********")
#删除元素
list1.pop(2)
print(list1)
#元素数量
print(len(list1))

z = "hello world!"
print("------ 列表list ---------")
print("输出Z的值：%s"%z)
print(z[0])
print(z[2:5])
print(z[2:])
print(z + "  python")

print("----列表生成器----")
print("---以下是列表生成式---")
list2 = [ x * x for x in range(1,11) if x % 2 == 0] #筛选出1*1 2*2 。。。10*10 的偶数平方
print(list2)
list3 = [ m + n for m in 'ABC' for n in 'XYZ']
print(list3)

print("---以下是列表生成器 generator---")
#考虑到文件比较大的时候用列表生成器
#generator保存的是算法
list4 = (x * x for x in range(1,11)) 
print(list4)  #<generator object <genexpr> at 0x1022ef630>
#如果需要一个个打印出来，next(list4),一次打印一个；直到最后没有更多的元素抛出StopIteration的错误，基本上很少用，
#还是用迭代 for..in循环取出来


print("----------列表的增删改查-----------")
print('''
# 增 --- 1、append(object) ; 2、insert(index,object); 3、extend(object)两个列表合并
# 删 --- 1、del list[index] ; 2、pop(index) ；3、remove(object)根据值去删
# 改 ---  list[index] 根据下标去删
# 查 --- 1、in 判断是否存在; 2、 not in 判断不存在; 3、index(object)寻找下标; 4、count(object)出现次数
# 排序 --- 1、sort() 默认从小到大 ; 2、reverse()逆序。3、从大到小 sort(reverse=True);如果是字符串就会以字符串ascll码
	''')



print("~" * 30)
print("=========== 元组tuple ==============")
tuple1= ("x",'y','z',15)
print(tuple1)
print("元组是有序的，和list很像，但是tuple一旦初始化了就不能修改")
print("元祖里面的类型可以是多种的")
print("只有一个值的时候用逗号，tuple(0.3,)")
print("内置函数：index,count")

print("~ " * 20)
print("=============切片sclice[num1:num2]")
print("切片的num1是索引起始位，num2是索引结束位但不包含；-1是倒数第一个元素")
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[2:-1]) #  ['Tracy', 'Bob']

print("-" * 30)
print("================  字典dict ================")
dict1 = {'Alice': 2341 , 'Beth' : 9102 , 'Cecil': '3258'}
print(dict1)
print(dict1.keys()) 	#打印字典所有键
print(dict1.values()) 	#打印字典所有值
print(dict1["Beth"]) 	#取 Beth 的值
if 'Alice' in dict1:    # 通过in 判断key是否存在
	print("Alice的值为：",dict1["Alice"])
else:
	print("没有找到Alice")
print(dict1.get("Alice",-1))  #通过get得到某个键的值，如果没找到返回指定的值如果没有指定返回None,建议用get 系统不会报错
print("字典是无序的，字典是可以修改的,但是作为key是不可变的，所以list不能作为key，整数和字符串可以做key")
print("删除 del dict1[""]; 全删：dict1.clear()")
print("items:返回的是元祖列表； dict1.items()")
print("判断key是否在字典中，如果在返回true.否则false; dict1.has_key('key')")
print("遍历字典 for key, value in dict1.items()")


print("~" * 30)
print("------------------- 集合set ---------------")
print("集合和字典很类似，也是一组key的集合，但不存储值，key不重复，要建立set,需要提供一个list作为输入集合")
s = set([1,3,5,4,2,2,2,0])
print(s)  #{0,1,2,3,4,5} 有序的，唯一的




print("~"  * 30)
print("============字符串操作===========")
print('''
1、find(object) 查找 等同于 index(object)
2、count(object) 出现的次数
3、replace(object,object1) 替换
4、split(" ") 分割
5、capitalize() 把字符串的第一个字符大写
6、title() 把字符串的每个单词首字母大写
7、starswith(obeject) 字符串以什么开头的，返回的是布尔值 True False
8、endswith(object) 字符串以什么结尾，可以用来判断文件的后缀名
9、lower() 转换字符串中的所有大写字母为小写
10、upper() 转换字符串中的所有小写字母为大写
11、ljust(index) 返回一个原字符串左对齐，不足用空格填充至index-1的长度
12、rjust(index) 返回一个原字符串右对齐，不足用空格填充至index-1的长度
13、center(index) 居中显示
14、strip() 删除字符串两端的空白字符
15、lstrip() 删除字符串左边的空白字符、换行等
16、rstrip() 删除字符串右边的空白字符、换行等
17、partition(object) 把字符串以 object 关键字分割成3个部分，str前 str str后
18、rpartition(object) 从右边开始分割
19、splitlines() 按照行分割，返回一个包含各行作为元素的列表
20、isalpha() 判断所有的字符是不是都是字母，返回布尔值（常用）
21、isdigit() 判断字符串只包含数字	
22、isalnum() 判断所有的字符都是字母或数字，不能包含其他字符如空格等
23、isspace() 判断是否全是空格
24、str.join(object) obeject中的每个字符串后面插入str,构造出一个新的字符串，最后面有没有str
	''')

print("~" * 30)



print("==================  条件判断 =================")
# if判断格式，条件语句中只要前面有空格的都会执行；
# 嵌套语句，第3个嵌套以后都用elif,elif使用前前面必须有if
print('''
	if 条件:
		当满足条件执行什么
		可是是多行，只要不和前面的if齐平
		if 分支条件：
			满足条件执行
		elif 分支条件：
			满足条件执行
		else:
			不满足条件执行什么
	else ：
		不满足条件执行什么
	''')



print("==================  条件循环 =================")
# while 循环 ， while 也可以嵌套
print('''
	初始化值
	while 值条件 ：
		条件满足执行。。。。
	''')

# break 和 continue 关键字，
# break 结束循环
# 
print("====提前结束循环=====")
n = 1
while n <= 100:
	if n > 10:
		break  #提前结束循环
	print(n)
	n = n + 1
print("END")
# 
# continue 跳出本次循环，继续执行下次循环
# 
print("===打印1-10奇数===")
m = 0 
while m < 10:
	m = m + 1
	if m%2 == 0:
		continue  #跳出单次循环
	print(m)






print("==========9 * 9 乘法口诀表 ============")
i = 1
while i <= 9 :
 	j = 1
 	while j <= i:
 		print("%d * %d = %d"%(j,i,i*j)),
 		j += 1
 	print("")
 	i += 1


print("~~~!" * 10)
print("=============示例 猜拳游戏 ===========")

num = "1"
while num == "1" :
	#1、电脑随机出
	import random 					#导入随机数
	rand = random.randint(0,2) 		#随机整数：0 1 2 
	#2、出拳
	player = input("请出拳：0、石头；1、剪刀；2、布 ------")
	#3、判断
	#先判断输入的是否是有效数字
	if player.isdigit() == True :
		player1 = int(player)
		if (0 <= player1 and player1 <= 2) :
			#先列出赢局的条件
			if (player1 == 0 and rand == 1) or (player1 == 1 and rand == 2) or (player1 == 2 and rand == 0):
				print("you win")
			#平局条件
			elif player1 == rand:
				print("平局")
			#剩下的就是输局
			else :
				print("you lose")
		else :
			print("输入错误：0、石头；1、剪刀；2、布")
	else :
		print("让你猜拳不是打字")
	num = input("继续请按1-----")



print("~~~" * 10)
print("============== for-in循环  （迭代） ================")
#for-in 循环  
'''
	for 临时变量 in 列表或字符串等：
		满足条件执行。。。
	else:
		循环不满足执行。。。。。

'''
print("计算0-100整数之和： 方法1")
list2 = list(range(101))  #0-100的列表
sum1 = 0 #保存结果
for x in list2:
	sum1 = sum1 + x
print("0-100整数之和 = ",sum1)
print("计算0-100整数之和： 方法2")
sum2 = 0
n = 100
while n > 0:
	sum2 = sum2 + n
	n = n - 1
print(sum2)


