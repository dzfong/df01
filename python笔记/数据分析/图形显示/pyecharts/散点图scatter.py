# 散点图
# 
# 	直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件。
# 	

from pyecharts import Scatter

def createScatter():

	data = [
		[28604, 77, 17096869],
	    [31163, 77.4, 27662440],
	    [1516, 68, 1154605773],
	    [13670, 74.7, 10582082],
	    [28599, 75, 4986705],
	    [29476, 77.1, 56943299],
	    [31476, 75.4, 78958237],
	    [28666, 78.1, 254830],
	    [1777, 57.7, 870601776],
	    [29550, 79.1, 122249285],
	    [2076, 67.9, 20194354],
	    [12087, 72, 42972254],
	    [24021, 75.4, 3397534],
	    [43296, 76.8, 4240375],
	    [10088, 70.8, 38195258],
	    [19349, 69.6, 147568552],
	    [10670, 67.3, 53994605],
	    [26424, 75.7, 57110117],
	    [37062, 75.4, 252847810]
		]

	x_axis = [v[0] for v in data]
	y_axis = [v[1] for v in data]
	extra_data = [v[2] for v in data]
	
	sc = Scatter("散点图示例")

	sc.add(
		"scatter",								# name -> str 
		x_axis,									# x_axis -> list , x轴坐标数据
		y_axis,									# y_axis -> list , y轴坐标数据
		extra_data = extra_data,				# extra_data -> list[int] , 第三维度数据
		extra_name = None,						# extra_name -> list[str] , 数据项的名称
		symbol_size = 0,						# symbol_size -> int ,  标记图形大小，默认为0
		is_visualmap = True,					# is_visualmap -> bool ,  显示渐变
		visual_dimension = 2,					
		visual_orient = 'verticality',			# visual_orient -> str , 渐变条的方向 垂直：verticality   水平：horizontal
		visual_type = 'size',					# visual_type
		visual_range = [25483, 1154605773],		# visual_range -> list ,  渐变的取值范围
		visual_text_color = "#000",				# visual_text_color -> str , 渐变条的文字颜色
		)

	sc.render("./散点图.html")



def main():
	createScatter()


if __name__ == '__main__':
	main()