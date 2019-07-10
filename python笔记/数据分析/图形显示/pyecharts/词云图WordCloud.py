# 词云图
# 	WordCloud
# 	
# 	

from pyecharts import WordCloud

def createWordCloud():
	
	name = [
    	'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    	'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    	'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
   	 	'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'
    	]
	
	value = [
    	10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    	965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265
    	]
	
	wordcloud = WordCloud(width = 1300, height = 620)

	wordcloud.add(
    	"",								# 标题
    	name,							# attr -> list , 属性列表
    	value,							# value -> list , 属性所对应的值
    	shape = "diamond",				# shape -> str , 词云图的轮廓，默认'circle','cardioid','diamond','triangle-forward','triangle','pentagon','star'
    	word_gap = 20,					# word_gap -> int , 单词间隔，默认为20
    	word_size_range = None,			# word_size_range -> list , 单词字体大小范围，默认为[12, 60]
    	rotate_step = 45,				# rotate_step -> int , 旋转单词角度，默认为45； 当shape = 'circle'时，rotate_step 才有效	
    	)
	
	wordcloud.render("./词云图.html")


def main():
	createWordCloud()


if __name__ == '__main__':
  	main()