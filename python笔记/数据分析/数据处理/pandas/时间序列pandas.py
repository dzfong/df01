# 时间序列
# 
# 	时间序列都是一种非常重要的数据形式，很多统计数据以及数据的规律也都和时间序列有着非常重要的联系

import pandas as pd 
from  matplotlib  import pyplot as plt
import numpy as np

# 生成一段时间范围
# 	pd.date.range(start=None, end=None, periods=None, freq='D')
# 	start 开始  
# 	end  结束   	periods  个时间索引，只能用一个
# 	freq   频率   'D' 天    ； 'M' 月 ； 'B' 工作日 ； 'H' 小时； 'T' 每分； 'S' 秒； 'L' 毫秒

dt = pd.date_range(start='20180130', end='20180228',freq='5D')   # 相隔5天   dtype = 'datetime64[ns]'
dt1 = pd.date_range(start='20180130', periods=6, freq='5D') 	# periods=5  freq='5D'  相隔5天建6个日期
print(type(dt1))												# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>


# 时间格式化
# 
# 		t.strftime('%Y%m%d')
 
 
# 把分开的时间字符串通过periodIndex的方法转化为 pandas的时间类型
# 		period = pd.periodIndex(year=df['year',], month=df['month'],day=df['day'],hour=df['hour'],freq='H')
# 		



# 重采样
# 	
# 		将时间序列从一个频率转化为另一个频率进行处理的过程，
# 		将高频率数据转化为低频率数据为 降采样，
# 		将低频率转化为高频率为 升采样
# 		
# 		t.resample("M").mean()   按月统计平均值
# 		t.resample("10D").count()  	





def creatCate():

	# 分割字符串转化为列表
	temp_list = df['title'].str.split(": ").tolist()
	# 提取列表中第一个元素
	cate_list = [i[0] for i in temp_list]
	# 把第一个元素添加为列，表示分类
	df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

	# 重新建立以时间戳为索引的数组  注意先后次序，
	df.set_index('timeStamp', inplace=True)				# inplace=True 原地修改

	# 分组
	for group_name, group_data in  df.groupby(by='cate'):
		
		# 统计出911数据中不同月份电话次数
		month_count = group_data.resample('M').count()['title']

		# 画图
		
		_x = month_count.index
		_y = month_count.values

		# for i in _x:
		# 	print(dir(i)) 	# 查看 i 的方法
		# 	break

		# 格式化日期, 去掉时刻
		_x = [i.strftime('%Y%m%d')  for i in _x]

		plt.plot(range(len(_x)), _y, label= group_name)
		plt.xticks(range(len(_x)), _x, rotation=45)

	



if __name__ == '__main__':
	
	df = pd.read_csv("./911.csv")

	# 把时间字符串转换为时间类型
	df['timeStamp'] = pd.to_datetime(df['timeStamp'])


	plt.figure(figsize=(15,8), dpi=80)

	plt.legend(loc='best')

	creatCate()

	plt.show()




