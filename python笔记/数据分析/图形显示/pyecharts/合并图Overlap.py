# 合并图
# 	
# 	用户可以自定义结合 Line/Bar/Kline, Scatter/EffectScatter 图表，
# 	将不同类型图表画在一张图上。利用第一个图表为基础，往后的数据都将会画在第一个图表上
# 	
# 	Overlap
# 	
#	关于双Y轴对齐，可以使用 yaxis_force_interval 参数，强制分割成相同分数的刻度，
#	这里有个小技巧，可以先设置 y 轴最大值。举个例子，如果双 y 轴一个最大值为 700，一个最大值为 400。
#	那你可以把两个的 yaxis_force_interval 参数分别设置为 140 和 80，那就会都分成均等的 5 份了。
#


from pyecharts import Bar, Line, Overlap

def createOverlap():

	attr = ["{}月".format(i) for i in range(1, 13)]

	v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
	v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
	v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

	bar = Bar()
	bar.add("蒸发量", attr, v1)
	bar.add(
		"降水量", 
		attr, 
		v2, 
		yaxis_formatter = 'ml',			# y轴 单位
		yaxis_interval = 50,			# y轴间距
		yaxis_max = 250					# y轴最大值
		)

	line = Line()

	line.add(
		"平均温度",
		attr,
		v3,
		yaxis_formatter = "℃",			# 新的Y轴 单位
		yaxis_interval = 5,				# 新的Y轴间距
		)

	overlap = Overlap(width = 1200, height = 600)

	overlap.add(bar)					# 把柱状图添加到合并图 , 默认不新增X、Y轴，并且x、y轴的索引都是0

	overlap.add(						# 把折线图添加到合并图
		line, 
		yaxis_index = 1, 				# 新增一个Y轴，索引为 1
		is_add_yaxis = True 			
		)

	overlap.render("./合并图.html")





def main():
	createOverlap()


if __name__ == '__main__':
	main()