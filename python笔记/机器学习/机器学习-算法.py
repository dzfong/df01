
#
#   算法是核心， 数据和计算是基础
#   
#   找准定位：
#   	大部分复杂模型的算法设计都是算法工程师在做，而开发工程师
#   		· 分析很多的数据
#   		· 分析具体的业务
#   		· 应用常见的算法
#   		· 特征工程、调参数、优化
#   
#   怎么做：
#   	· 学会分析问题，使用机器学习算法的目的，想要算法完成何种任务
#   	· 掌握算法基本思想，学会对问题用相应的算法解决
#   	· 学会利用库或框架解决问题
#   
#   
#   
#   机器学习算法的判别依据
#   
#  		数据类型： 
#  			离散型数据： 区间内不可分；计数
#  				由记录不同类别个体的数目所得到的数据，又称计数数据，所有这些数据全部都是整数，
#  				而且不能再细分，也不能进一步提高他的精确度。
#  				
#  			连续型数据： 区间内可分；取值
#  				变量可以在某个范围内取任一数，即变量的取值可以是连续的，如： 长度、时间、质量值等，
#  				这类数据通常是非整数，含有小数部分
#  	
#
#
#  	机器学习的算法分类
#  		
#  		监督学习（预测）： 特征值 + 目标值
#  			
#  			分类：目标值离散型
#  				k-近邻算法 、 贝叶斯分类、 决策树与随机森林、 逻辑回归、 神经网络
#  			
#  			回归：目标值连续型
#  				线性回归、 岭回归
#  				
#  			标注： 隐马尔可夫模型
#  		
#  		无监督学习： 	特征值
#  			
#  			聚类: k-means
#  			
#  			
#  	
#  	
#  	数据：
#  		1、公司本身就有的数据
#  		2、合作过来的数据
#  		3、购买的数据
#  		
#  		
#  		
#  		
#  		
#  	
#  	开发流程
#  	
#  	
#  		建立模型  -----   根据数据类型划分应用种类  （模型：算法 + 数据）
#  	
#  		原始数据  -----   明确问题做什么
#  	
#  		数据的基本处理 	-----	pd去处理数据 （缺失值，合并表。。。）
#  	
#  		特征工程 	-----	特征处理 （特征抽取、预处理、降维等处理）
#  	
#  		找到合适的算法进行预测分析	-----	分类、回归
#  	
#  		模型的评估 	----- 	判定效果
#  	
#  		上线使用	-----	以API形式提供
#  	
#   
#   
#   
#   
#   
#   
#   sklearn数据集
#   
#   	1、数据集划分：
#   		训练集：构建模型	70%		80%		75%(最多)
#   		测试集：评估模型	30%		20%		25%
#   	
#		2、sklearn数据集接口介绍：
#   		数据集划分API:	sklearn.model_selection.train_test_split
#   		
#   		加载获取数据集
#   			· datasets.load_*(): 获取小规模数据集，数据包含在datasets里
#   			· datasets.fetch_*(data_home=None): 获取大规模数据集，需要从网络上下载，data_home表示数据集下载的目录，默认是 ~/scikit_learn_data/
#   		
#   		获取的数据集的格式
#   			load_* 和 fetch_*返回的数据类型 datasets.base.Bunch(字典格式)
#   				· data：特征数据数组，是[n_samples*n_features]的二维numpy.ndarray数组   （特征值，行列）
#   				· target: 标签数组，是n_samples的一维numpy.ndarray数组			（结果集）
#   				· DESCR：数据描述
#   				· feature_names: 特征名， 新闻数据，手写数字，回归数据集没有
#   				· target_names: 标签名，回归数据集没有
#  
#   				  					 				  					
#		3、sklearn分类数据集
#		
#			 sklearn.datasets.load_iris()
#			
#			 sklearn.datasets.load_digits()
#			 
#			 数据集进行分割：
#			 	sklearn.model_selection.train_test_split(*arrays, **options)
#			 		· x : 数据集的特征值
#			 		· y : 数据集的目标值
#			 		· test_size  测试集的大小，一般为float
#			 		· random_state 随机数种子，不同的种子会造成不同的随机采样结果，相同的种子采样结果相同
#			 		· return 训练集特征值，测试集特征值，训练标签， 测试标签   (默认随机取)
#		
#		4、sklearn回归数据集
#		
#			 sklearn.datasets.load_boston()
#			 
#			 sklearn.datasets.load_diabetes()



# 加载数据集
from sklearn.datasets import load_iris, load_boston
# 加载网络数据集，默认先下载
from sklearn.datasets import fetch_20newsgroups
# 导入划分api
from sklearn.model_selection import train_test_split

# 分类数据集
li = load_iris()
# print("特征值：")
# print(li.data)
# print("目标值：")
# print(li.target)
# print("数据描述：")
# print(li.DESCR)
# print(li.feature_names)
# print(li.target_names)

# 特征值，目标值，测试集大小 test_size 0.25 是 25%
# 注意返回值，训练集 train  x_train,y_train    测试集  test x_test, y_test
x_train, x_test, y_train, y_test = train_test_split(li.data, li.target, test_size=0.25)
# print("训练集特征值和目标值：", x_train, y_train)
# print("测试集特征值和目标值：", y_test, y_test)

# 网络大数据
news = fetch_20newsgroups(subset='all')
# print(news.target)


# 回归数据集
lb = load_boston()
print(lb.target)




#-----------------------------
#
#	转换器和估计器(estimator)
#
#-----------------------------
#
# 转换器实现了 特征工程的API       fit_transform()   fit()  transform()
# 
# 估计器实现了 算法的API		
# 		1、用于分类的估计器：
# 			sklearn.neighbors	k-近邻算法
# 			sklearn.naive_bayes		贝叶斯
# 			sklearn.linear_model.LogisticRegression		逻辑回归
# 			sklearn.tree			决策树与随机森林
# 		
# 		2、用于回归的估计器：
# 			sklearn.linear_model.LinearRegression	线性回归
# 			sklearn.linear_model.Ridge	岭回归
# 			
# 