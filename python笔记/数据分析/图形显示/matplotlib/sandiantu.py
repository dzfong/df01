# 散点图 （分布规律）
# 	判断变量之间是否存在数量关联趋势，展示离群点
# 	观察数据的离散聚合程度
# 	
# 	区别在于 plt.plot()  和 plt.scatter()


from matplotlib import pyplot as plt
from matplotlib import font_manager


# 设置中文字体，默认英文
my_font = font_manager.FontProperties(fname="c:\Windows\Fonts\msyh.ttf")

# 读取数据
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(51,82)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 调整X轴刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3 ]
_xtick_labels += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_labels[::3],fontproperties=my_font,rotation=45)


# 添加描述信息
plt.xlabel("月份",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("标题 ",fontproperties=my_font)


# 绘制图形
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")

# 添加图例
plt.legend(loc="upper left",prop=my_font)

# 展示图形
plt.show()