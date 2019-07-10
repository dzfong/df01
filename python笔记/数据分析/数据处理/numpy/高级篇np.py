import numpy as np
import random



# 1、取数组相同项 (长度可以不同,如果维度不同，只取第一行)
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8,10,11])
c = np.intersect1d(a,b)				# intersect1d 是数字1 ，而不是字母l
print(c)		# [2, 4]


# 2、从数组a中删除数组b中的所有项 （数组长度可以不同, 如果维度不同，只取第一行)
a = np.array([[1, 2, 3, 4, 5, 0], [2, 5, 6, 3, 2, 7]])
b = np.array([4, 5, 6, 7, 8])
c = np.setdiff1d(a, b)				# setdiff1d	是数字1，不是字母l
print(c)				

# 3、获取两个数组元素匹配的位置  （数组的长度和维度必须相同）
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a==b)
print(c)
for element in c[0].flat:
	print(element)				# 1 3 5 7 


# 4、从数组中获取指定范围的所有数字
a = np.array([2, 6, 1, 9, 10, 26])
index = np.where((a>=5)&(a<=10))  	# 1     [6 9 10]
print(a[index])
b = a[(a>=5)&(a<=10)]				# 2 	[6 9 10]
print(b)


# 5、选出两组数组中相同位置的最大值
def maxx(x, y):
	if x>=y:
		return x
	else :
		return y

pair_max = np.vectorize(maxx, otypes=[float])			# np.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)
														# 矢量函数 pyfunc :python函数或方法；otypes : 输出数据类型；doc : 函数的docstring。如果为None，则docstring将是 pyfunc.__doc__
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
c = pair_max(a, b)
print(c)			# [6. 7. 9. 8. 9. 7. 5.]


# 6、快速交换二维数组中的两列数据
arr = np.array(range(9)).reshape(3,3)					# [[0 1 2] [3 4 5] [6 7 8]]
b = arr[:,[1,0,2]]
print(b)												# [[1 0 2] [4 3 5] [7 6 8]]				


# 7、交换二维数组中的两行数据
c = arr[[1,0,2],:]	
print(c)												# [[3 4 5] [0 1 2] [6 7 8]]


# 8、反转二维数组的行
d = arr[::-1]
print(d)												# [[6 7 8] [3 4 5] [0 1 2]]


# 9、反转二维数组的列
e = arr[:,::-1]
print(e)												# [[2 1 0] [5 4 3] [8 7 6]]


# 10、只打印小数点后面的3位
# 1)
rand_arr = np.random.random([5,3])
print(rand_arr)
t = np.round(rand_arr,3)
print(t)
# 2)
np.set_printoptions(precision=3)						# 之后小数都当3位数处理
t2 = rand_arr[:]
print(t2)


# 11、限制数组中的打印数量
np.set_printoptions(threshold=6)
a = np.array(range(15))
print(a)												# [0 1 2 ... 12 13 14]

# 12、打印完整的数组而不截断
np.set_printoptions(threshold=np.inf)					# [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]
print(a)


# 13、