#coding = utf-8
#


#-------- 类 class -----------
# 面向对象oo：
# 对象 = 属性（静态特征） + 方法（动态操作）
# 类 = 变量  +  函数
# 类是抽象的模板，实例是根据类创建出来的一哥哥具体的对象，每个对象都拥有相同的方法，但各自的数据可能不同
# 类名约定以大写字母开头
class Student(object): 		#class后面是类型，括号里面是继承，如果没有合适的继承类，可以用object 
 	pass
# 面向对象的3特征：
# 	1、封装 ：方法的封装，只需要调用，不用知道到底是怎么实现的
# 	2、继承 ： 继承是子类自动共享父类之间的数据和方法的机制。class MyList(list) 括号里面就是父类
# 	3、多态： 不同对象对同一方法响应不用的行动。如：动物对跑的不同形态。老虎很快，乌龟很慢，青蛙是跳
#多态示例： 
class A:
	def fun(self):
		print("我是小A..")
	 				
class B:
	def fun(self):
	 	print("我是小B.")
a = A()
b = B()
a.fun()  #我是小A.
b.fun()	 #我是小B.
#a和b调用的是同一个方法，但是实现的结果不同

print("\n" * 2)
	 	
# self关键字：写类的时候把self作为函数的第一个要求
class Ball:
	def setName(self,name):
		self.name = name 
	def kick(self):
		print("我叫%s,该死的，谁踢我。。。" %self.name)

a=Ball()
a.setName("篮球")
b=Ball()
b.setName("土豆")
a.kick()
b.kick()

print('\n' * 2)
#魔法方法：如果你的对象实现了这些方法中的某一个。那么这个方法就会在特殊的情况下被Python所调用
#而这一切都是自动发生的，而这些魔法方法总是被双下划线包围。如： __init__(self)
#__init__(self):  构造方法	,第一次参数永远都是self	
class Ball:
	def __init__(self,name):   #重写构造方法，可以带参数属性也可以不带
		self.name = name 
	def kick(self):
		print("我叫%s,该死的，谁踢我。。。" %self.name)
a = Ball("番茄")
a.kick()

print('\n'* 2)
#公有和私有
#私有变量：只需要在变量或函数名前加上两个下划线“__”，那么这个函数或变量就会成为私有的了
#私有变量在外部是不可以调用的，如果需要调用需要添加个函数，getName(self): return;如果要设置某值setName(self)没有return
#私有的作用是可以在方法中对参数进行检查，避免传入无效的参数
#公有示例：
class Person:
	name = "苹果"
p = Person()
print(p.name)   #苹果 

#私有变量
class Person1:
	__name = '橘子'
p1 = Person1()
#print(p1.__name)  #AttributeError: 'Person1' object has no attribute '__name' 找不到
print(p1._Person1__name) #伪私有机制，可以通过 _类名__属性 调用
#更改
class Person2:
	__name = "香蕉"
	def getName(self):
		return self.__name
p2 = Person2()
print(p2.getName())

print('\n' * 2)
#继承
#class DerivedClassName(BaseClassName):
#多重继承
#class DerivedClassName(Base1,Base2,Base3):
#如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性
#重写了父类的方法，需要重写父类的构造方法，使用super().__init__(	)
import random as r   	#导入随机函数
import time as t 		#导入时间函数
class Fish:				#定义父类
	def __init__(self):		#父类的构造方法
		self.x = r.randint(0,10)	#取随机位置
		self.y = r.randint(0,10)
		print("起始位置：",self.x,self.y) #子类中调用，会初始化
	def mov(self):				#移动方法
		self.x -= 1 			#向西移动一位
		print("我的位置是：",self.x,self.y)

class Goldfish(Fish):	#继承Fish父类
	pass

class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):			#重写父类方法
		super().__init__()		#调用了父类的构造方法。不需要self
		self.hungry = True
	def eat(self):
		if self.hungry:
			print("吃货的梦想就是天天有的吃^_^")
			self.hungry = False
		else:
			print("太饱啦，吃不下啦！")

salmon = Salmon()	 #初始化对象。默认调用__init__中方法
salmon.mov()
salmon.mov()
print("@" *20)
shark = Shark()		#这里不会打印父类构造方法中的__init__中的打印。因为子类重写了父类的方法
shark.eat()
t.sleep(2)			#延迟2秒
shark.eat()
shark.mov() 		#出现错误：Shark 没有 x属性；因为子类重写了父类的构造方法
#解决上面的问题在于，在自定义的构造函数中调用父类构造方法 super().__inti__()
#


print("\n" * 2)

#类 、 类对象 和 实例对象
#实例属性属于各个实例所有，互不干扰；
#类属性属于类所有，所有实例共享一个属性
#类方法和函数的区别：类方法必须包含参数self，且为第一个参数
#方法是带括号的(),属性不用；把方法变成属性，用@property 和 @xxxx.setter
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误
#不要试图在一个类里边定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
#用不同的词性命名，如属性用名称，方法名用动词
#需要传进参数和属性，需要 def __init__(self,x,y): 构造，返回值一定是个None, 不要有任何的返回值
#__new__(cls,[,..]) : 最先调用，很少需要重写的
#示例
class CapStr(str):  #继承自字符串不可改变的类型，
	def __new__(cls,string): 	#重写 转换
		string = string.upper()
		return str.__new__(cls,string)
i = CapStr('I Love Python! hmmm]')
print(i)
print('\n' * 2)
#析构方法： __del__(self): 垃圾回收机制
#不是del XXX 就会调用的，而是当所有的都del了才会调用
#示例
class C :
	def __init__(self):
		print("我是__init__方法，我被调用了。。。")
	def __del__(self):
		print("我是__del__方法，我被调用啦。。。")


a1 = C() 	#调用__init__方法
print(0)
b1 = a1
c1 = b1
del a1
print(1)
t.sleep(2)
del b1
print(2)
t.sleep(2)
del c1		#到此才调用 __del__方法

print('\n' * 2)

#重写__str__ 和 __repr__ 这两个方法在打印的的时候会调用
#示例
class A():
	def __str__(self):
		return 'hello world!'
class B():
	"""docstring for B"""
	def __str__(self):
		return 'hello python!'

a = A()
print(a)	#直接打印 hello world!
b = B()		#直接打印 hello python!
print(b)

print('\n' * 2)
#做一个定时器
import time as t

class MyTime():
	def __init__(self):
		self.unit = ['年','月','天','小时','分钟','秒']
		self.prompt = "未开始计时！"
		self.lasted = []
		self.begin = 0
		self.end = 0

	def __str__(self):
		return self.prompt

	__repr__ = __str__

	#开始计时
	def start(self):
		self.begin = t.localtime()
		self.prompt = "提示：请先调用 stop() 停止计时！"
		print("计时开始。。。")

	#停止计时
	def stop(self):
		if not self.begin:
			print("提示：请先调用 start() 进行计时！")
		else:
			self.end = t.localtime()
			self._calc() 
			print("计时结束！")

	#内部方法，计算运行时间
	def _calc(self):
		self.lasted = []
		self.prompt = "总共运行了"
		for index in range(6):
			self.lasted.append(self.end[index] - self.begin[index])
			if self.lasted[index]:
				self.prompt += (str(self.lasted[index]) + self.unit[index])
		#为下一轮计时初始化变量
		self.begin = 0
		self.end = 0

t1 = MyTime()
print(t1)
t1.start()
t.sleep(5)
t1.stop()
print(t1)

t1.stop()


#获取对象的信息
#type(xxx) : 获取对象的类型
#isinstance(x,class类型) ：判断class的继承类型：总是优先使用isinstance()判断类型
#dir('xxx') :要获取一个对象的所有属性和方法，他返回的是一个包含字符串的list
#hasattr(obj,'x') :判断是否有属性'x'
#getattr(obj,'y') :获取属性'y'
#setattr(obj,'y') :设置一个属性'y'
#
#假设我们希望从文件流fp中读取图像，我们首先要判断fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取
def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None


c = dir('readImage')
print(c)


#@property 装饰器：把方法变成属性
#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器
#@score.setter ，负责把一个setter方法变成属性赋值
#还可以定义只读属性，只定义getter方法，不定义setter方法就时一个只读属性：
#
#@property 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
#
#

class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height = value

	@property
	def resoultion(self):
		return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resoultion = ', s.resoultion)
if s.resoultion == 786432:
	print('测试通过！')
else:
	print('测试失败！')


#python 允许使用多重继承
#