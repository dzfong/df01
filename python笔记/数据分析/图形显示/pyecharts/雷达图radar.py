# 雷达图
# 	Gadar
# 	
# 	
#	雷达图主要用于表现多变量的数据


from pyecharts import Radar


def createRadar():

	schema = [
		("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    	("客服", 38000), ("研发", 52000), ("市场", 25000)
		]

	v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
	v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

	radar = Radar("雷达示意图")

	radar.set_radar_component(
		schema = schema,				# 
		rader_text_color="blue",
		)

	radar.add(
		"预算分配",						# 图例名称
		 v1, 							# value -> [list] 包含列表的列表数据
		 is_splitline_show=False,		# 是否显示分割线，默认为True
		 is_axisline_show=True,			# 是否显示坐标轴线，默认为True
		 item_color='red'				# 图例颜色
		 )

	radar.add(
		"实际开销", 
		v2, 
		item_color='#4e79a7', 
		is_area_show=True, 				# 是否显示填充区域
		area_opacity = 0.4,				# 填充区域透明度
		area_color = 'green',			# 天聪颜色
		legend_selectedmode='single'	# 单例显示，可点击	
		)

	radar.render("./雷达图.html")


def main():

	createRadar()


if __name__ == '__main__':
	main()