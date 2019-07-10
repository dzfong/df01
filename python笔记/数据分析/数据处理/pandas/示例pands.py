
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
from pyecharts import Bar




def createRuntimeList():
	# ---------------------------------------
	# 绘制 Runtime (Minutes)  分布状况图
	# ---------------------------------------
	# 提取Runtime (Minutes)数据
	runtime_data = df["Runtime (Minutes)"].values  			# numpy.ndarray的类型
	max_runtime = runtime_data.max()
	min_runtime = runtime_data.min()
	# 组距
	num_bin = (max_runtime - min_runtime) // 5

	# 设置图形大小
	plt.figure(figsize=(15,8), dpi=80)
	plt.hist(runtime_data, num_bin)
	plt.xticks(range(min_runtime, max_runtime+5, 5))
	plt.show()


def creatRatingList():
	# --------------
	# 影评分布图
	# --------------
	rating_data = df['Rating'].values
	max_rating = rating_data.max()
	min_rating = rating_data.min()
	bins = ((max_rating - min_rating) // 0.5).astype('int32')

	# 步长 和 刻度都取
	lis = [1.6]+[0.5]*15
	b = np.array(lis)
	c = b.cumsum()
	c = c.tolist()

	print(bins)
	plt.hist(rating_data, c)
	plt.xticks(c)
	plt.show()


def creatGenreList():
	# ---------------------------------
	# 字符串离散化
	# ---------------------------------
	# 
	# 统计 Genre 分类情况
	# 

	# 1、统计分类的列表 把字符串转列表
	temp_list = df['Genre'].str.split(',').tolist()			#[[] [] []]
	#print(temp_list)
	# 2、提取字符串，去掉重复项
	genre_list = list(set([i for j in temp_list for i in j]))
	#print(genre_list)
	# 3、建立个新的全为0的数组，数组的形状为所有行，列取刚提取的字符串
	zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)	# np.zeros((行, 列))
	#print(zeros_df)
	
	# 这种操作速度太慢
	# # 4、给每个电影出现分类的位置赋值给全为0的数组
	# for i in range(df.shape[0]):
	# 	# 通过标签来定义位置并赋值  temp_list[i]  是个列表，  loc[i,[ , ]] 就是取i行的[ , ]列
	# 	zeros_df.loc[i,temp_list[i]] = 1
	# 	#print(temp_list[i])
	# #print(zeros_df)
		
	# 4、 给每个电影出现分类的位置赋值给全为0的数组
	for i in genre_list:
		zeros_df[i][df['Genre'].str.contains(i)] = 1 			# zeros_df[i][包含字符串i的列]
	#print(zeros_df)

	# 5、统计每个分类电影的数量和， 统计列方向的和
	genre_count = zeros_df.sum(axis=0)
	#print(genre_count)
	# 6、排序
	genre_count =genre_count.sort_values()
	# 7、绘图
	_x = genre_count.index
	_y = genre_count.values
	plt.bar(_x, _y, width=0.4, color='orange')
	plt.xticks(rotation=45)
	plt.show()




if __name__ == '__main__':

	# 打开文件
	file_path = "IMDB-Movie-Data.csv"
	df = pd.read_csv(file_path)
	#print(df.info())
	#print(df.head(10))

	# 获取影片的平均分
	rating_mean = df["Rating"].mean().round(2)
	print(rating_mean)						# 6.72

	# 获取导演数
	#director_nums = len(set(df['Director'].tolist()))			# df['Director']是个series,tolist()转换为一个列表，然后放到set集合中，删除重复项
	director_nums = len(df['Director'].unique())				# unique()唯一的；  等同于 len(set(df['Director'].tolist()))
	print(director_nums)						#  644

	# 获取演员的人数
	temp_actors_list = df['Actors'].str.split(", ").tolist()
	#print(temp_actors_list)										# 列表中每行是个列表
	actors_list = [i.strip() for j in temp_actors_list for i in j]	# 把所有的演员取出来放一个列表   i.strip() 是去两边的空白; 格式清洗
	#print(actors_list)		
	actors_nums = len(set(actors_list))								# 去重复项
	print(actors_nums)

	# 执行函数
	# createRuntimeList()
	# creatRatingList()
	# creatGenreList()
