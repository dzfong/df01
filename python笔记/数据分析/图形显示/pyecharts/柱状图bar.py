# 安装包:
# 
#	pip install pyecharts
#	pip install pyecharts-snapshot 
#	pip install echarts-themes-pypkg  
#
# 柱状图 ： Bar
# 
# 饼图： Pie
# 
# 箱体图： Boxplot
# 
# 折线图： Line
# 
# 雷达图： 	Rader
# 
# 散点图：	Scatter
# 
# 图标布局：	Grid
# 
# 两图结合:		Overlap
# 
# 词云图：	WordCloud
# 
# 地图(需要安装包)：	Map
# pip install echarts-countries-pypkg
# pip install echarts-china-provinces-pypkg
# pip install echarts-china-cities-pypkg
# pip install echarts-china-counties-pypkg
# pip install echarts-china-misc-pypkg
# pip install echarts-united-kingdom-pypkg
# 


# 柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。


from pyecharts import Bar
from pyecharts import Bar3D


# 基本柱状图/条形图
def creatBar():

	# 设置主标题与副标题
	# title_ 标题的属性， title_color颜色，title_pos位置
	# width宽度，height高度，background_color图表的背景色
	bar = Bar('基本柱状图','副标题',title_color='blue', width=1200, height=600)


	# 设置背景色,自带白色(默认)和暗色(dark)，
	# 如果需要其他颜色，需要安装包 echarts-themes-pypkg  
	# 全部更改为统一主题： 
	# from pyecharts import configure
	# configure(global_theme='vintage') 放首行
	bar.use_theme('vintage')


	# 添加柱状图的数据及配置项
	# 标签的属性 
	# mark_ 类： mark_point_textcolor, mark_line_symbolsize
	# legend_ 类： legend_pos=‘left’：标签的位置
	# dataZoom_类： dataZoom_type = 'inside' 滑动效果
	# is_ 类： is_label_show=True：显示每个点的值，is_datazoom_show=True：实现移动控制x轴的数量，    is_convert = True：x，y轴是否调换
	bar.add('服装',		# 图例名称：注解-label
	        ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'],	# X轴数据，列表 columns
	        [5,20,36,10,75,90],		# Y轴数据列表 纵坐标  data
	        mark_line=["average"],	# 平均线
	        mark_point=["max","min"],	# 显示最大值、最小值
	        bar_category_gap = '20%',	# 类目轴柱状距离，默认20% ; 如果设为0%，那么就是直方图
	        is_stack = True,			# 数据堆叠，同个类目轴上系统配置相同的stack值可以堆叠放置
	        is_more_utils = True    # 设置最右侧工具栏
	        )

	# 调试输出pyecharts的js配置信息, 等同于  bar.print_echarts_options()
	bar.show_config()    

	# 生成本地文件（默认为.html文件）           
	bar.render('./柱状条形图.html')

def creatBarTwo():
	# 堆叠柱状图 
	attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]
	bar = Bar('柱状信息堆叠图')
	bar.add('商家A',attr,v1,is_stack = True )  #is_stack = True才表示堆叠在一起
	bar.add('商家B',attr,v2,is_stack = True )
	bar.render('./柱状堆叠图.html')  


def creatBarThree():
	# 并列柱状图
	attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]
	bar = Bar('并列柱状图')
	bar.add('商家A',attr,v1,mark_point = ['average'] )     #标记点：商家A的平均值
	bar.add('商家B',attr,v2,mark_line = ['min','max'])    #标记线：商家B最小/最大值
	bar.render('./柱状并列图.html')


def creatBarFour():
	# X 轴与 Y 轴交换
	attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
	v1 = [5,20,36,10,75,90]
	v2 = [10,25,8,60,20,80]
	bar = Bar('X 轴与 Y 轴交换')
	bar.add('商家A',attr,v1)  
	bar.add('商家B',attr,v2,is_convert = True)    # is_convert = True:X 轴与 Y 轴交换
	bar.render('./横向柱状图.html')  

def createBar3D():
	# 创建3D柱状图
	
	x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"
    ]
	
	y_axis = [
    "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"
    ]
	
	# data -> [list] 包含列表的列表，每一行是数据项，每一列是维度 
	data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
	
	range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

	bar3d = Bar3D("3D柱状图示例", width = 1200, height = 600)

	bar3d.add("我也不知道是什么图", x_axis, y_axis,	# x_axis, y_axis -> str 是坐标数据，需为类目轴，也就是不能为数值
    	[[d[1],d[0],d[2]] for d in data],			# 3维数组的维度转换 d[1]对应的y_axis, d[0]对应的x_axis，d[2]是数据
    	is_visualmap = True,						# 颜色值变化
    	visual_range = [0,20],
    	visual_range_color = range_color,
    	grid3d_opacity = 1,							# ->int 3d笛卡尔坐标系组的透明度(柱状的透明度),默认为1，不透明
    	grid3d_width = 200,
    	grid3d_depth = 80,
    	grid3d_shading = "lambert",					# 三维柱状图中三维图形的着色效果；color:只显示颜色，不受光照其他因素影响
    												# lambert: 通过经典的 lambert 着色表现光照带来的明暗
													# realistic: 真实感渲染，配合light.ambientCubemap 和 postEffect 使用可以让展示的画面效果和质感有质的提升，ECharts GL 中使用了基于物理的渲染（PBR) 来表现真实感材质
		is_grid3d_rotate = True,				# 自动旋转
		grid3d_rotate_speed = 10,				# 自动旋转速度
		)
	bar3d.render("./柱状3D图.html")



if __name__ == '__main__':
	# creatBar()
	# creatBarTwo()
	# creatBarThree()
	# creatBarFour()

	createBar3D()