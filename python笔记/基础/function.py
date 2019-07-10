#coding=utf-8

print("================ 函数 ==============")
# 通常一块具有独立功能的代码块重复利用的时候，用函数来把重复代码封装一个整体
# 定义了函数不会被执行，只有调用了才会被执行。函数名()
# 
# 函数文档说明，开发中用到，help()
# 在代码块中用 "" 括起来的就叫文档说明
#  
# 返回值：一个函数执行完成以后，把一个结果给调用者，这个值就是返回值。return
# 一般有返回值的函数都保存。放在其他变量中
# 只要函数中遇到return,函数就会结束，不会再执行函授后面的代码
# 多个返回值：1、通过列表list[] ; 2、通过元组tuple() ; 3、通过字典dict{}
#
# 
# 类型：1、无参、无返回值；2、无参、有返回值；3、有参、无返回值；4、有参、有返回值
# 
# 
# 一般主函数放在 main()中，这个main()函数是自定义的
# 先定义全局变量、然后自定义函数、然后找主函数main()
# 
# 函数嵌套：一个函数中套用另一个函数
# 语句执行是有循序的，函数定义在调用之后，会提示未定义
# 
# 递归函数： 如果一个函数中调用的是函数本身，那这个函数就是递归函数
#
#
#局部变量：函数里面定义的变量叫局部变量，作用范围只在函数中有效；形参也是局部变量
#
#全局变量：在函数外边定义的变量叫做全局变量；任何一个函数都可以使用
#全局变量在函数中不能直接修改，需要修改前必须要加关键字声明 global xxx （变量不需要加global，常量需要加）
#
#
def power(x,n=2):   #当n=2时，代表的是默认参数 ；
	"默认的求平方，带值求幂"
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

print(power(3,3))
print(power(5))

#print(help(power))

#默认参数： 定义默认参数一定要注意，，默认参数必须指向不变对象！（str、None）
#默认参数一般都是最后行；如果是多个，用形参名=实参 e=200
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L


#可变参数：定义可变参数只要在参数前面加个*args，  *args返回的是元组
#如果参数接收到的是个列表或元组那就不用可变参数，但是定义比较繁琐
#带入的是不带名字的
#当列表\元组在做实参传递时前面加个*，表示对其解包。test(11,22,*A,B) *A打印出来的是值而不是列表
def test(a,b,*agrs,**kw):
	print(a)
	print(b)
	print(agrs)
	print(kw)
A = [11,22,33]
B = {"aa":100,"bb":200}
test(11,22,*A,**B)
#(list、tuple)
def calc(*agrs):
	sum = 0
	for n in agrs:
		sum = sum + n * n
	return sum
print(calc(1,2))

#关键字参数： **kw ， 可以只传必选参数，也可以传入任意个数的关键字参数； *kww返回的是字典
#关键字参数作用：可以扩展函数的功能
#带入的是带名字的
#当字典在做实参传递时前面加个**，表示对其解包。
#(dict)
def person(name, age, **kw ):
	print('name:' , name, 'age:', age, 'other:', kw)
extra = {'city' : 'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])

#命名关键字参数：如果要限制关键字参数的名字，就可以用命名关键字参数
#如果在位置参数和命名关键字参数中间没有可变参数必须加个*
#命名关键字参数必须传入参数名，和位置参数不同
def person1(name, age, * , city, job):
	print(name, age, city, job)
person1('Both',25,city='Beijing',job='Teacher')


#生成器 generator 
#通过列表生成式我们可以直接创建一个列表，但是受到内存的限制，列表内容量肯定是有限的；
#如果列表元素可以按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素；
#这样就不必建立完整的list，从而节约大量的空间，在Python中这种一边循环一边计算的机制叫生成器，generator
#建立generator方法1：
#	只要把列表生成式中的[]改成()
g = (x*x for x in range(10))
print(g)  # <generator object <genexpr> at 0x1022ef630>
#如果需要一个个的打印出来，用next()函数获取generator的下一个返回值
#直到最后没有更多的元素抛出StopIteration的错误，基本上很少用,还是迭代 for in 用的多
next(g) # 0
next(g) # 1
next(g) # 4

#斐波拉契数列
#这个数列用列表生成式写不出来，但是可以用函数把它打印出来却很容易
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		#print(b)
		yield b
		a, b = b , a + b   #赋值语句: t = (b, a + b) #t是个tuple , a = t[0] b = t[1]
		n = n + 1
	return 'done'
#fib(6)
for n in fib(6):  #把函数改成generator后，我们基本上不会用next()来获取下一个返回值，而是直接使用for循环来迭代
	print(n)

#使用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获到StopIteration错误，
#返回值包含在StopIteration的value中：
g = fib(6)
while True:
	try:
		x = next(g)
		print('g', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
#这个函数和generator仅一步之遥，要把fib函数变成generator,只要把print(b)改成 yield b就可以了；
#这里最难理解的是generator和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后行函数语句juice返回
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#举个例子，定义一个generator，依次返回数字1,3,5
def odd():
	print("step 1")
	yield 1
	print("step 2")
	yield 3
	print("step 3")
	yield 5

o = odd()
next(o)
next(o)
next(o)



#迭代器 Iterator
#凡是可作用于for循环的对象都是Iterable类型：
#凡是可作用于next()函数的对象都是 Iterator类型，它们表示一个惰性计算的序列
#可以使用 isinstance()判断一个对象是否是 Iterator对象
from collections import Iterator
t = isinstance((x for x in range(10)), Iterator)
print(t)
#集合数据类型如list 、 dict 、 str等是Iterable 但不是Iterator,不过可以通过iter()函数获得一个Iterator对象
t1 = isinstance(iter([]), Iterator)
print(t1)
t2 = isinstance([], Iterator)
print(t2)
#Iterator对象可以把这个数据流看做事一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而使用list	是永远不可能存储全体自然数的

for x in [1,2,3,4,5]:
	pass
#完全等价于:
it = iter([1,2,3,4,5])
while True :
	try :
		x = next(it)
	except StopIteration:
		break





#高阶函数：把函数作为参数传入，这样的函数称为高阶函数。就是让函数的参数能够接收别的函数
def add(x,y,f):
	return f(x) + f(y)

addNum = add(-5,16,abs)   #abs()是绝对值函数 
print(addNum)



#map()
#map()函数接收两个参数，一个是函数，一个是Iterable;
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
R = list(r)
print(R) #返回的是list结果
print(r) #返回的是Iterator

#转化成字符串
Str = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(Str)


#reduce()把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数
#把序列[1,3,5,7,9]变换成13579
from functools import reduce
def fn(x,y):
	return x * 10 + y
red = reduce(fn,[1,3,5,7,9])
print(red)

#把str变成int的函数
from functools import reduce 
DIGITS = {'0':0 ,'1':1, '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
	return DIGITS[s]
def str2int(s):
	return reduce(lambda x,y: x*10+y,map(char2num,s))

str = str2int('123456')
print(str)	


#filter()
#过滤序列：和map()类似，filter()也接收一个函数和一个序列
#和map()不同的是filter()把传入的幻术依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()

st = list(filter(not_empty,['a','','B',None,'c',''])) #filter()函数返回的是一个Iterator,需要用list()函数获取所得结果并返回list
print(st)

#用filter()求素数
def _odd_iter():	#这是一个生成器，并且是一个无线序列
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):		#定义一个筛选函数
	return lambda x: x % n > 0

def primes():		#定义一个生成器，不断返回下一个素数
	yield 2
	it = _odd_iter()	#初始序列
	while True:
		n = next(it) 	#返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it) #构造新序列


for n in primes():		#由于prime()也是一个无限序列，所以调用时需要设置一个退出循环的条件
	if n < 1000:
		print(n)
	else:
		break



#sorted()
#排序算法
#排序的核心是比较两个元素的大小
s = sorted([36,5,-12,9,-21], key=abs)
print(s)

'''
b = ['bob','about','Zoo','Credit']
st = sorted(b, key=str.lower, reverse=True)
print(st)
'''


#返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
#例如：求和函数，返回的是函数而不是结果
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)
print(f)		#<function lazy_sum.<locals>.sum at 0x101c6ed90>
print(f())   	#调用函数 f()  结果为25


#闭包
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量



#匿名函数: lambda args1,args2:args1+args2
#冒号前面的args1 args2表示参数
#匿名函数能接受任何数量的参数，但是只能返回一个表达式的值，不用写return
#匿名函数不能直接调用print，因为lambda需要一个表达式
#匿名函数没有名字不必担心函数名冲突
#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数
#应用场景： 可以当做参数传递引用、可以作为返回值
aaaa = lambda a,b:a+b
print(aaaa(8,10))



#装饰器 Decorator
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以 通过变量也能调用该函数
def now():
	print('2018-4-5')
f = now
f()
print(now.__name__)
print(f.__name__)
#现在我们要增强now()函数的功能，比如在函数调用前后自动打印日志，但又不希望修改now()函数的定义
#这种在代码运行期间动态增加功能的方式，称之为 装饰器 Decorator
#一个完整的decorator的写法
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2018-4-5')
f = now
f()
#在面向对象（OOP）的设计模式中，decorator被称为装饰模式，OOP的装饰模式需要通过继承和组合来实现，
#而Python除了能支持OOP的decorator外 直接从语法层次支持decorator。
#Python的decorator可以用函数实现，也可以用类实现。




#偏函数
#functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
#可以使用下面的代码创建一个新的函数int2
import functools
int2 = functools.partial(int , base = 2) #把base参数设定为默认值2，也可以在函数调用时传入其他值
a = int2('1000000')
print(a)
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
#
#
#
#





#
# 函数和方法是有区别的
# 
#  区别1：所处的位置
#  			函数是直接写在文件中 而不是class 中；
#  		   	方法是只能写在class中。
#  		   
#  区别2：定义的方式
#  			函数定义的方式： def关键字 函数名 (形参或无参)	 def functionName():
#  		    方法定义的方式： 其他方法是定义在类中的，方法必须带一个默认参数(self)，静态方法除外
#  		   def method(self): 
#  		   		   
#  区别3：调用的方式
#  			函数的调用是 直接调用 函数名(参数1，参数2)   fuctionName()
#  			方法的调用是 对象.方法 	 c = ClassName ; c.method()
#  			
#  			
#  验证类型的最好办法就是isinstance()
#  	print(isinstance(Foo.func,FunctionType))
#  	
#  	
#  	实例化出来的去调用，叫做方法.
#  	直接使用类名去调用，叫做函数.