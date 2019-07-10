#
# numpy  
# 
# 	一个在Python中做科学计算的基础库，重在数值计算，也是大部分PYTHON科学计算库的基础库，多用于在大型、多维数组上执行数值运算
#
# python 中没有数组类型   （数字、字符串、列表，元组，字典，集合）
# 
# 
# 
# 	list 转 numpy
#	np.array(a)
#	ndarray 转 list
#	a.tolist()
# 




import numpy as np 
import random

# 一、创建np数据的3种方式
# 1
t1 = np.array([1, 2, 3])
print(t1)				# [1 2 3] 和列表相同，中间没有,
print(type(t1))			# <class 'numpy.ndarray'> 类型，numpy的数组类型

# 2
t2 = np.array(range(10))
print(t2)

# 3
t3 = np.arange(10)
print(t3)
print(t3.dtype)			# int32 

# 4
#def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None):
# endpoint 如果为True, stop是最后一个值；stop - start / num-1
# endpoint 如果为False, 生成的数组不包含stop值， stop - start / num
# retstep 如果为True, 会返回样本之间的间隙
t = np.linspace(1,5,5)
print("t = {}".format(t))
t = np.linspace(1,5,5,endpoint=False)
print("t = {}".format(t))
print("__"*20)

tt1 = np.zeros((2, 4))
print("tt1 = {}".format(tt1))		# [[0. 0. 0. 0.] [0. 0. 0. 0.]]		构建全是0 的2行4列数组

tt2 = np.ones((2,4))
print("tt2 = {}".format(tt2))		# [[1. 1. 1. 1.] [1. 1. 1. 1.]]		构建全是1 的2行4列数组

tt3 = np.empty((2,2))
print("tt3= {}".format(tt3))		# [[2.678655121e+185 1.695551123e+190] [9.48223232323e+077 1.68451212122-306 ]]  构建随机的2行2列的数组

tt4 = np.full((2,2),3)
print("tt4 = {}".format(tt4))		# [[3 3] [3 3]]		构建了一个填充为3 的2行2列数组

tt5 = np.eye(3)						
print("tt5 = {}".format(tt5))		# [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]	创建方阵  一个对角线为1 ，其他为0的数组



# 二、np中的数据类型
t4 = np.arange(1,9,2,dtype='float32')
print("t4 = {} ".format(t4))
print(t4.dtype)

# 三、np中数据类型转换
t5 = t4.astype('int8')
print(t5.dtype)

# 修改浮点类型的小数位
np.random.seed(10)						# 随机数种子，10 是给定的种子值，因为计算机生成的是伪随机数，所以通过设定相同的随机数种子，可以生成相同的随机数		
t66 = np.random.randint(0,20,(3,4))		# 创建3行4列的数组
print("t66 = {}".format(t66))
t6 = np.array([random.random() for i in range(10)])
print(t6)
print(t6.dtype)

t7 = np.round(t6,2)		# round 取小数位
print(t7)
print(t7.dtype)			

print("==="* 20)



# 四、numpy的形状 ，几行几列
#  查看数组形状 a.shape
#  修改数组形状 a.reshape(3, 4)
#  快速的把多维数组转化为一维数组 a.flatten()
a = np.array([[3,4,5,6,7],[4,5,6,7,8]])
print(a.shape)				# 2行5列，2维的数组

b = a.reshape((10,))		# 一维数组，表示个数
c =  a.reshape(10,1)		# 二维数组，10行1列
print(b)
print(c)
print("\n" * 5)

d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("{0} = {1}".format('d', d))
print(d.shape)  		# (2, 2, 3)   表示2块2行3列
print(d.size)			# 12 ,12个数
print(d.itemsize)		# 4 占用了4个字节，一个字节8位，32位/8 =4
print(d.ndim)			# 3  数组的维度
print(d.nbytes)			# 48 数组中所有数据消耗掉的字节数

e = d.reshape(12,)
print(e)

f = np.arange(24).reshape(2,3,4)	
g = np.arange(24).reshape((2,3,4))
print(f)
print("=============")			# f == g
print(g)


# a.flatten()
#	将多维数组转化为一维数组
h = f.flatten()
print(h)


print("数组的计算==============")

# 五、数组的计算
# 	
# 	数组与数字的计算 ： numpy的广播机制，加减乘除的值被广播到所有的元素上面
# 	0 / 0 = nan  
# 	3 / 0 = inf
# 	
# 	数组与数组的计算 : 对应数组的位置进行计算
# 	
# 	
#	数组与不同形状数组之间的计算： 
#		如果两个数组的后缘维度（即从末尾开始算起的维度）的轴长度相符或其中一方的长度为1，则认为他们是广播兼容，广播会在缺失或长度为1的维度上进行



i = f + 2
print(i)		# 每个数据都 + 2

j = np.arange(100,124).reshape(2,3,4)
print(j)

k = f + j
print("{0} = {1}".format('k',k))

# 	特殊运算
# 		dot, sum, min, max, cumsum	
# 
# 	
#  dot()返回的是两个数组的点积(dot product)	,  
#  矩阵积计算不遵循交换律,np.dot(a,b) 和 np.dot(b,a) 得到的结果是不一样的
#  1.如果处理的是一维数组，则得到的是两数组的內积
#  
a = np.array(range(1,5))			# [1 2 3 4]
b = np.arange(1,5)					# [1 2 3 4]
c = np.array(range(1,9)).reshape(4,2)	# [[1 2] [3 4] [5 6] [7 8]]
d = np.arange(1,5).reshape(2,2)
print("{} = {}".format('a',a))
print("{} = {}".format('b',b))
print("{} = {}".format('c',c))
print("{} = {}".format('d',d))

m = a.dot(b)  
l = np.dot(a, b)
print("{} = {}".format('m',m)) 	# m=30     1*1 + 2*2 + 3*3 + 4*4 = 30
print("{} = {}".format('l',l)) 	# l=30    a.dot(b) == np.dot(a,b)  

print("\n" *2)

#  2.如果是二维数组（矩阵）之间的运算，则得到的是矩阵积（mastrix product）。
n = a.dot(c)
print("{} = {}".format('n',n))	 # n =  [50 60]    1*1 + 2*3 + 3*5 + 4*7 = 50 ; 1*2 + 2*4 + 3*6 + 4*8 = 60


#   sum()
print(a.sum())		# 10   1+2+3+4=10
#	min()
print(a.min())		# 1   最小值
#	max()
print(a.max())		# 4 	最大值
#	cumsum()
print(a.cumsum())	# [1 3 6 10]  	 [1 1+2 1+2+3 1+2+3+4] 





# 六、轴（axis)
# 
# 	一维数组： 只有0轴，个数
# 	二维数组:  0.1    axis = 0 是行 横轴， 1是列 竖轴；
# 	三维数组： 0.1.2   方向0 是块，1 是行横着的， 2是列竖着的
# 	     





# 七、读取文件
# 
# 
# 	文件 csv : 逗号分隔值文件
# 	表格形式显示
# 	
# 	一般都是用pandas 读取文件的
# 	
# 	np.loadtxt(frame, dtype=np.float, delimiter=None, skiprows=0, useclos=None, unpack=False)
# 	
# 	frame ---> 文件位置， 传路径
# 	dtype ---> 数据类型，可选
# 	delimiter --> 分隔字符串，默认空格，改为 逗号
# 	skiprows ---> 跳过前多少行， 一般跳过第一行 行头
# 	useclos ---> 读取指定的列， 索引， 元组类型
# 	unpack ---> 转置 行变成列，列变成行，对角线进行旋转，默认为 False
# 	
# 	
# 	
# 	转置： 	a.transpose()   
# 			a.T()
# 			a.swapaxes()
# 			
# 	转置和交换的效果一样
# 



# 八、numpy的索引和切片
# 
# 	取行：
#		a[2]   取a数据的第三行
#		a[2:]   取a数据连续的多行
#		a[[2,8,10]]  取不连续的多行
#	取列：
#		b[:,0]  取所有行的第一列
#		b[:,2:]  取所有行的连续列
#		b[[2,3,5],[4,5,9]]  取的是某几个点的结果
#	
#	索引
#		a[0][0]   第一行第一列的值
#
# 	数值的修改：
# 		t[:,2:4] = 0   , 把所有行的第3到第5列中间的不包含5列修改为 0 
# 		t[t<10] = 3  ,	把所有小于10的值替换为3
# 	
# 	布尔索引：三元运算符
# 		np.where(t<10,0,10)  当t数组的值小于10 替换为0，其他的替换为10
# 	
# 	裁剪：
# 		t.clip(10,18)	把小于10的替换为10，大于18的替换为18
# 	
# 	迭代器:			
# 		for element in t.flat:
# 			print(element)		打印每个元素

a = np.arange(0, 100, 10)

print(a)							# [0 10 20 30 40 50 60 70 80 90]

# 花式索引
b = [1 ,5, -1]					
c = a[b]
print("{} = {}".format("c",c))		# [10 50 90]  取 2 ，6 和倒数第一位

d = np.where(a < 50) 				# where函数  三元运算符，
print(b)

e = a.clip(30, 60)
print(e)							# [30 30 30 30 40 50 60 60 60 60]	小于30的替换30，大于60的替换60





	


#	九、NaN
#	
#	NaN （not a number）表示不是一个数字； float 类型
#		NaN：1、读取本地文件为float类型的时候，如果有缺失 就会出现NaN 
#			 2、当0除以0时，也会出现NaN
#			 3、当无穷大(inf)减去无穷大，也会出现NaN
#		inf: 一个值除以0 会出现 inf
#		
#		np.nan == np.nan  这是不相等的，False
#		np.nan != np.nan
#		
#		判断nan的个数：  np.count_nonzero(t!=t)
#						 np.count_nonzero(np.isnan(t))
#						 
#		把nan替换为0 ：t[np.isnan(t)] = 0
#						 
#		nan 和任何值计算都是 nan
#		

v1 = np.arange(12).reshape((3,4))	# [[0 1 2 3] [4 5 6 7] [8 9 10 11]]
print(np.sum(v1))					# 0+1+2+3+4+5+6+7+8+9+10+11 = 66
print(np.sum(v1,axis=0))			# [12 15 18 21]   0+4+8 1+5+9 2+6+10 3+7+11
print(np.sum(v1,axis=1))			# [6 22 38]		0+1+2+3  4+5+6+7 8+9+10+11


# 	在计算的时候，一般会把nan缺省值替换为 均值(中值)；或者直接删除有缺失值的一行
# 	
v2 = np.array([[1, 3, 5, 7] ,[12, 15, 19, 23] ,[32, 12, 16,15]])

# 均值
# 是数学统计术语,是指在一组数据中所有数据之和再除以这组数据的个数。 平均数
# 它是反映数据集中趋势的一项指标。解答平均数应用题的关键在于确定“总数量”以及和总数量对应的总份数
print(v2.mean(axis=0))				# [15. 10. 13.33333 15]		v2每行的均值; 受离群点的影响较大

# 中值
# 是数学统计术语，是指组距的上下限之算术平均数。
# 当变量值的项数N为奇数时，处于中间位置的变量值即为中位数；
# 当N为偶数时，中位数则为处于中间位置的2个变量值的平均数	
print(np.median(v2,axis=1))			# [4. 17. 15.5]		v2每列的中值；

# 最大值
print(v2.max(axis=1))		# [7 23 32]

# 最小值
print(v2.min(axis=1))		# [1 12 12]

# 极值
# 在数学分析中，函数的最大值和最小值（最大值和最小值）被统称为极值（极数）
# 是给定范围内的函数的最大值和最小值（本地 或相对极值）或函数的整个定义域（全局或绝对极值）
# 如集合理论中定义的，集合的最大值和最小值分别是集合中最大和最小的元素。 无限无限集，如实数集合，没有最小值或最大值。
print(v2.ptp(axis=0))		# [31 12 14 16]   极值差，每行的最大值减去最小值



# 标准差
# 均方差---离均差平方的算术平均数的平方根，用σ表示。标准差是方差的算术平方根
# 标准差能反映一个数据集的离散程度
# 在概率统计中最常使用作为统计分布程度（statisticaldispersion）上的测量。
# 标准差定义是总体各单位标准值与其平均数离差平方的算术平均数的平方根。它反映组内个体间的离散程度
# 各个(标准值平方 - 均值平方）相加 / 个数 的平方根
# 所有数减去其平均值的平方和，所得结果除以该组数之个数（或个数减一，即变异数），再把所得值开根号，所得之数就是这组数据的标准
# 	
# 	一个较大的标准差，代表大部分数值和其平均值之间差异较大；一个较小的标准差，代表这些数值较接近平均值
#	反映出数据的波动稳定情况，越大表示波动越大，越不稳定
print(v2.std(axis=0))		# [12.83225104 5.09901951 6.01849003 6.53197265]

'''
这是错误的创建，因为列表没有nan值，ndarray数组才有nan值
v3 = np.array([[  0.,   1.,   2.,   3.,   4.,   5.],
       [  6.,   7.,  NaN,   9.,  10.,  11.],
       [ 12.,  13.,  14.,  NaN,  16.,  17.],
       [ 18.,  19.,  20.,  21.,  22.,  23.]], dtype=np.float)
'''


# ------------------------------------
# ndarray 数组缺失值填充每一列的均值  |
# ------------------------------------
# 
# 
v3 = np.arange(24).reshape((4,6)).astype('float')	# 创建一个float类型的数组,只有float类型的数组才能赋nan
'''	
[[0.  1.  2.  3.  4.  5.] 
 [6.  7.  8.  9.  10. 11] 
 [12. 13. 14. 15. 16. 17]
 [18. 19. 20. 21. 22. 23]]
'''
v3[1,2:] = np.nan 		# 赋值，把第2行的第3列一直到最后列的值赋为 nan
'''
[[ 0.  1.  2.  3.  4.  5.]
 [ 6.  7. nan nan nan nan]
 [12. 13. 14. 15. 16. 17.]
 [18. 19. 20. 21. 22. 23.]]
'''
print(v3.shape[1])				# 取得是数组的6列
for i in range(v3.shape[1]):	# 遍历每一列
	print(v3[[0,1],i])			# 打印出来的效果是 6行2列 ，行列转换，因为要计算的是列，所以要把列的值放在同一行
	temp_col = v3[:,i]			# 当前的一列
	nan_num = np.count_nonzero(temp_col != temp_col)	# 统计nan的数量
	if nan_num :				# 当 nan_num 为True时，说明有nan
		temp_not_nan_col = temp_col[temp_col == temp_col]	# 当前一列不为nan的数组
		temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()		# 把当前列的均值赋给nan
print(v3)
'''
[[ 0.  1.  2.  3.  4.  5.]
 [ 6.  7. 12. 13. 14. 15.]
 [12. 13. 14. 15. 16. 17.]
 [18. 19. 20. 21. 22. 23.]]
'''



# --------------------------
#  数组的拼接
# ------------------------
# 
# 竖直拼接   np.vstack(t1, t2)		vertically
# 水平拼接	 np.hstack(t1, t2)		horizontally    
# 
#
# 行交换	t[[1,2],: ] = t[[2,1],: ]
# 列交换	t[:,[0,2]] = t[:,[2,0]]




# 十、视图和复制
# 
# 	1、简单赋值不会创建数组对象或对其数据的拷贝
# 	# a 和 b是相同的，这里是引用，指针
# 	a = np.arange(12)
# 	b = a
# 	b is a   # True
# 	b.shape = 3,4
# 	a.shape  # (3, 4)
# 	
# 	2、不同的数组对象可以共享相同的数据，不同的形状
# 	c = a.view()
# 	c is a 	# False
# 	c.base is a  # True
#	c.shape = 2, 6
#	a.shape 		# (3, 4) 形状没改变
#	c[0,4] = 1234
#	a  				# [[0 1 2 3] [1234 5 6 7] [8 9 10 11]]	
# 	
# 	3、深拷贝 copy, 数据和形状不会相互影响
# 	d = a.copy()
# 	d is a 			# False
# 	d.base is a 	# False
# 	
# 	
