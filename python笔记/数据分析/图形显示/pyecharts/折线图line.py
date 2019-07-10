# 折现图
#	Line
#	Line3D
#	

#	折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。


from pyecharts import Line

def createLineOne():
	# 普通的折现图
	# 
	attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]

	line = Line("折现图实例")

	# Line.add(
	# 		name,x_axis,y_axis,
	# 		is_symbol_show = True,		#是否显示标记图形
	# 		is_smooth = False,			#是否显示平滑曲线
	# 		is_stack = False,			#是否数据堆叠
	# 		is_step = False,			#是否是阶梯线
	# 		is_fill = False, **kwargs   #是否填充曲线区域面积
	# )
	line.add("商家A", attr, v1, mark_point = ['average','max','min'],
	 		mark_point_symbol = 'diamond', 		# 标注点：钻石形状
			mark_point_textcolor = '#40ff27'	# 标注点：标注文本颜色
			)
	line.add("商家B", attr, v2, 
			is_smooth = True, 
			mark_point = ['average','max','min'],
			mark_line = ['max','average'],
			mark_point_symbol = 'arrow',	# 标注点：三角形状
			mark_point_symbolsize = 40
			)

	line.show_config() 

	line.render("./折线图.html")



def createLineTwo():
	# 折现面积图
	#
	attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]
	line = Line('折线面积示例图')

	line.add("商家A", attr, v1, is_fill = True,		# 是否填充
			line_opacity = 0.2, 		# 线条不透明度
			area_opacity = 0.4,			# 填充不透明度

			)

	line.add("商家B", attr, v2, is_fill = True,
			line_color = '#000', 		# 黑色填充
			area_opacity = 0.3,
			is_smooth = True

			)

	line.render('./折现面积图.html')

if __name__ == '__main__':
	createLineOne()
	createLineTwo()