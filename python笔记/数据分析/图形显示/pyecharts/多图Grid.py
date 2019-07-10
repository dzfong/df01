# 并行显示多张图
# 
# 	Grid
# 	
# 	用户可以自定义结合 Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap/Boxplot 图表，将不同类型图表画在多张图上。
# 	第一个图需为 有 x/y 轴的图，即不能为 Pie，其他位置顺序任意。
# 	
# 	注意下比例 和 位置  宽高不用设置
# 	legend_top    legend_bottom    legend_left    legend_right
# 	legend_pos

from pyecharts import Bar, Scatter, Line, EffectScatter, Grid



def cBar():

	attr = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]
	bar = Bar("柱状图示例",title_pos = "65%")
	bar.add("商家A", attr, v1, is_stack = True)
	bar.add("商家B", attr, v2, is_stack = True, legend_pos = "80%")
	grid.add(bar, grid_bottom="60%", grid_left="60%")

def cLine():

	attr = ["周一","周二","周三","周四","周五","周六","周日"]
	v1 = [11, 11, 15, 13, 12, 13, 10]
	v2 = [1, -2, 2, 5, 3, 2, 0]
	line = Line("折线图示例")
	line.add("最高气温", attr, v1, mark_point=["max","min"], mark_line=["average"])
	line.add("最低气温", attr, v2, mark_point=["max","min"], mark_line=["average"], legend_pos="20%")
	grid.add(line, grid_bottom="60%", grid_right="60%")

def cScatter():

	v1 = [5, 20, 36, 10, 75, 90]
	v2 = [10, 25, 8, 60, 20, 80]
	scatter = Scatter("散点图示例", title_top='50%', title_pos='65%')
	scatter.add("Scatter", v1, v2, legend_top='50%', legend_pos='80%')
	grid.add(scatter, grid_top="60%", grid_left="60%")

def efScatter():

	v1 = [11, 11, 15, 13, 12, 13, 10]
	v2 = [1, -2, 2, 5, 3, 2, 0]
	es = EffectScatter("动态散点图示例", title_top='50%')
	es.add('EffectScatter', v1, v2, 
		effect_scale=6, 			# effect_scale -> float 动画中波纹的最大缩放比例, 默认为2.5
		legend_top='50%', 
		legend_pos='20%'
		)
	grid.add(es, grid_top="60%", grid_right="60%")




if __name__ == '__main__':

	grid = Grid(page_title="XXXX", height=720, width=1200)
	cBar()
	cLine()
	cScatter()
	efScatter()
	grid.render("./多张图合并.html")