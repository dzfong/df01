# 仪表盘
# 
#	Gauge.add()
#	
#	

from pyecharts import Gauge


def main():

	gauge = Gauge("仪表盘显示示例")

	gauge.add(
			"业务指标",					# name -> str	图表名字
			"完成率",					# attr -> list  属性名称	
			66.66,						# value -> list 属性对应的值，百分比
			angle_range = [180,0],		# angle_range -> list 角度范围 默认[225,-45]
			scale_range = [0,100],		# scale_range -> list 数据范围 默认[0,100]
			is_legend_show = True,		# 显示name
			)

	gauge.render("./仪表盘.html")

if __name__ == '__main__':
	main()