


# ------------------------------=----
# 
# 
# 		模型类 M  models.py
# 		
# 			
# -----------------------------------
# 
# 
# #	M : 模型，和数据库进行交互
# 
# 
# 
# 		在模型类中不用定义表的主键，在生成时 会自动添加，并且值为自动增长
# 		
# 		生成表名的默认格式：（可以通过元选项来更改数据表名称）
# 			应用名_模型类名小写    booktest_bookinfo
# 			
# 		django默认的数据库是 sqlite3
# 		
# 		
# 		(只有继承自 models.Model 才是一个模型类)
# 		class BookInfo(models.Model):
# 		
# 		
# 		
# 		迁移：
# 		
# 			1）、生成迁移文件： 	python manage.py makemigrations
# 			2）、执行迁移生成表: 	python manage.py migrate
# 		
# 		
# 		
# 		自定义后台界面：
# 		
# 			在admin.py中注册，并定义模型类
# 			
# 		
# 		
# 		
# 	1、	模型类属性命名限制：
# 			1、不能使用python 保留关键字
# 			2、不允许使用连续的下划线，这是由django的查询凡是决定的
# 			3、定义属性时需要指定字段类型，通过字段类型的参数指定选项 如： 属性名=models.字段类型(选项)
# 		
# 				
# 	2、	字段类型：btitle = models.CharField(max_length=20)
# 	
# 			使用时需要导入 django.db.models 包
# 			
# 			AutoField 							自动增长的整型 IntegerField，通常不用指定，django会自动创建属性名为 id 的自动增长属性
# 			
# 			BooleanField						布尔字段，值为True 或 False
# 			
# 			NullBooleanField					支持Null 、 True、 False
# 			
# 			CharField(max_length=number)		字符串，参数max_length表示最大字符串个数
# 			
# 			TextField							大文本字段，一般超过4000个字符时使用
# 			
# 			IntegerField 						整数
# 			
# 			DecimalField(mx_digits=None,
# 			decimal_places=None)				十进制浮点数，mx_digits表示总位。decimal_places表示小数位。 比如价格，精确到2位小数
# 			
# 			FloatField							浮点数，参数同上。  精度不同，
# 			
# 			DateField([auto_now=False, 			日期；可选参数，auto_now 设置为True ，更新时间为修改时的时间
# 			auto_now_add=False])				 	auto_now_add 设置为True 创建的时间戳为你创建时的日期。 不能同时用，只能用一个
# 						
# 			TimeField							时间，参数同 DateField
# 			
# 			DateTimeField						日期时间 ，年月日时分秒，参数同DateField
# 			
# 			FileField							上传文件字段
# 			
# 			ImageField							继承自 FileField ，对上传的内容进行校验，确保是有效的图片	
# 			
# 												
# 	3、	选项字段：		atilte = models.CharField(max_length=20,db_column='title')
# 	
# 			default								默认值
# 			
# 			primary_key							若为True ， 则该字段会成为模型的主键字段，默认为 False, 一般作为 AutoField的选项使用
# 			
# 			unique								若为True, 	则这个字段在表中必须是唯一值， 默认为False
# 			
# 			db_index							若为True,	则在表中会为此字段创建索引，默认为False
# 			
# 			db_column							字段的名称，如果未指定，则使用属性的名称， 比如 db_column = 'title'	
# 			
# 			null 								如果为True， 表示允许为空， 默认是 False; 数据表的结构
# 			
# 			blank								如果为True, 则该字段允许为空白，默认为 False; 后台管理有关
# 			
# 			choices								选择器，可以设定默认值，选择器是个列表，列表中是个元组
# 			
# 			verbose_name						别名 ， 在后台显示
# 			
# 			注意：当修改字段的选项不影响表结构是，可以不用迁移，default 和  blank
# 			
# 			
# 	
#	4、 查询
# 	
# 		修改mysql的日志文件：
# 			让其产生mysql.log ，即是mysql的日志文件，里面记录的对 mysql 数据库的操作记录
# 			
# 		1）、打开mysql的配置文件 /etc/mysql/mysql.conf.d/mysqld.cnf ，去掉 68、69行的注释
# 		2）、重启 mysql服务， 
# 		3）、打开mysql的日志文件 /var/log/mysql/mysql.log 
# 		4）、查看mysql的日志文件  tail -f /var/log/mysql/mysql.log
# 		
# 		
# 		查询函数：
# 			通过  模型类.objects  属性可以调用get \ all 函数，实现对模型类对应的数据表的查询
# 			
# 			get   		返回表中满足条件的一条且只能有一条数据，	返回值是一个模型对象
# 			
# 			all 		返回模型类对应表格中的所有数据，	返回值是一个 QuerySet,查询集
# 			
# 			filter		返回满足条件的数据， 	返回值是一个 QuerySet,查询集 	参数写查询条件
# 			
# 			exclude		返回不满足条件的数据， 	返回值是一个 QuerySet,查询集 	参数写查询条件
# 			
# 			order_by 	对查询结果进行排序。 	返回值是一个 QuerySet,查询集  	参数中写根据哪些字段进行排序   
# 						默认是升序， '-id' 降序：前面加个减号
# 			
# 				查询条件格式： 模型类属性名__条件名 = 值
# 			
# 					条件名： filter 和 exclude
# 						a) 、判等 条件名： exact   可以省略 id__exact = 1  ;   id = 1   
# 						b) 、模糊查询：	contains 		包含
# 										endswith 		以xx结尾
# 										startswith 		以xx开头
# 						c) 、空查询： isnull		btitle__isnull = False  不为空	
#						d) 、范围查询： in 	 		id__in = [1, 3, 5]
#						e) 、比较查询： gt 大于； lt 小于； gte 大于等于； lte 小于等于
#						f) 、日期查询：	year 	month   day	 也可以加条件 bpub_date__gt = date(1980,1,1)			
#
#
#
#			Q 对象：
#				
#				作用： 用于查询时条件之间的逻辑关系， not and or ，可以对 Q 对象进行 & | ~ 操作			| 或， & 且， ~ 非
#				
#				 	使用之前需要导入 包：
#				 							from django.db.models import Q
#				 	 
#				 	 使用例子： 	BookInfo.objects.filter(Q(id__gt=3)|Q(bread__gt=30))
#				 	 				BookInfo.objects.filter(Q(id__gt=3)&Q(bread__gt=30))
#				 					BookInfo.objects.filter(~Q(id=3))
#				 					
#				 					
#				 					
#				 					
#			F 对象：
#			
#				作用： 用于类属性（表字段）之间的比较
#				
#				使用之前需要导入包：	from django.db.models import F
#				
#				使用例子：
#						查询图书阅读量大于2倍的评论量：	BookInfo.objects.filter(bread__gt=F('bcomment')*2)			创建F对象
#						
#				
#								
#						
#			聚合函数：
#			
#				作用： 对查询结构进行聚合操作
#				
#				sum  count  avq  max  min
#				
#				aggregate: 调用这个函数来使用聚合， 返回值是一个字典
#				
#				使用之前需要导入包：	
#						from django.db.models import Sum, Count, Max, Min, Avq
#				
#				使用例子：
#						BookInfo.objects.all().aggregate(Count('id'))  		# 查询所有图书的数目	{'id__count' : 5} ;  .all()可以省略
#						
#						BookInfo.objects.aggregate(Sum('bread'))			# 查询所有图书的阅读量总和  {'bread__sum': 126}
#						
#				count : 返回的是一个数字，和上面的aggregate中的 count有区别
#					
#						BookInfo.objects.count()			# 统计所有图书的数目   返回的是 5
#						
#						BookInfo.objects.filter(id__gt=3).count()		# 统计id大于3的所有图书的数目 	返回的是 3
#						
#				
#		
#														
#						
#			查询集：
#			
#				all,	filter, 	exclude, 	order_by 调用这些函数会产生一个查询集，QuerySet类对象可以继续调用上面的所有函数。
#				
#				查询集特性：
#					1）、 惰性查询： 只有在实际使用查询集中的数据的时候才会产生对数据库的真正查询。没有使用数据是不会显示查询的
#					2）、 缓存： 当使用的是同一个查询集时，第一次的时候会发生实际数据库的查询，然后把结果缓存起来，
#								 之后再使用这个查询集时，使用的是缓存中的结果。 
#								 
#				限制查询集：
#					可以对一个查询集进行 取下标或切片 操作来限制查询集的结果
#					对一个查询集进行切片操作会产生一个新的查询集，下表不允许为负数。
#					
#					两种方式：   books[0]					如果不存在，会抛出 IndexError异常
#								 books[0:1].get()			如果不存在，会抛出 DoesNotExist异常
#					
#				exists: 
#					判断一个查询集中是否有数据，返回值 True, False
#					books[0].exists()
#
#
#
#						
#					
#			
#	5、模型类关系	（表与表之间的关系）
#	
#		1）、 一对多关系
#		
#			例： 图书类---英雄类 :		models.ForeignKey()  定义在多的类中
#			
#		2）、 多对多关系
#		
#			例： 新闻类---新闻类型类  体育新闻	国际： 		models.ManyToManyField()  定义在哪个类中都可以
#			
#		3）、 一对一关系
#		
#			例： 员工基本信息类--- 员工详细信息类.员工工号		models.OneToOneField 	定义在哪个类中都可以
#		
#		
#		
#		
#	
#	
#	6、关联查询	（一对多） 
#	
#		在一对多关系中，一对应的类我们把它叫做一类，多对应的那个类我们把它叫做多类，我们把多类中定义的建立关联的类属性叫做关联属性
#		
#		格式：
#		
#		
#			一类 BookInfo 			由一查多					多类 HeroInfo
#		
#		—————————————————————								_____________________
#		|					|	book.heroinfo_set.all()		|					|
#		|					|								|					|
#		|					| --------------------------->	|					|
#		|					|								|					|
#		|					|								|					|
#		|					|								|					|
#		|					|								|					|
#		|					| <---------------------------	|					|
#		|					|								|					|
#		|					|		hero.hbook				|					|
#		|					|								|					|
#		|					|								|					|
#		|					|								|					|
#		—————————————————————		   由多查一				—————————————————————
#		
#		
#		例如： 
#				查询 图书id为1 所有英雄的信息  （由一查多）
#					通过关联对象查询
#						b = BookInfo.objects.get(id=1)
#						b.heroinfo_set.all()
#						
#						
#					通过模型类查询
#						HeroInfo.objects.filter(hbook__id=1)
#						
#						查询英雄信息，图书天龙八部的所有英雄
#						HeroInfo.objects.filter(hbook__btitle='天龙八部')
#							
#						
#				
#				查询 id为1的英雄 关联的图书的信息	（由多查一）
#					通过关联对象查询	（hbook 关系属性）
#						h = HeroInfo.objects.get(id=1)
#						h.hbook
#						
#						
#					通过模型类查询	
#						BookInfo.objects.filter(heroinfo__id=1)
#						
#						查询图书信息，要求图书关联的英雄的描述包含'八'
#						BookInfo.objects.filter(heroinfo__hcomment__contains='八')
#						
#		
#		
#		通过模型类查询：	（1、需要查哪个表里面的，就用哪个模型类查； 2、如果类中没有 关系属性，条件需要写对应类的名。）																																																																																								
#			通过多类的条件查询一类的数据
#				一类名.objects.filter(多类名小写__多类属性名__条件名)
#			通过一类的条件查询多类的数据
#				多类名.objects.filter(关系属性__一类属性名__条件名)
#			
#
#
#
#
#
#	7、插入、更新和 删除
#	
#		
#		模型类.objects.create(name='xxx', age=20, gender='male')		插入数据
#		模型类.save()       调用一个模型类对象的 save 方法的时候就可以实现对模型类对应数据表的插入和更新
#		模型类.delete()		调用一个模型类对象的 delete 方法的时候就可以实现对模型类对应数据表数据的删除
#		
#				
#
#
#
#
#	8、自关联
#		
#		自关联是一种特殊的一对多的关系
#		
#		案例: 显示广州市的上级地区 和 下级地区
#		
#		地区表： id , tiltle , parenteid 			# parenteid 记录上下级关系的
#
#
#			例如：  12000000		广东省		null
#					12001000		广州市		12000000
#					12001001		白云区		12001000
#					12001002		天河区		12001000
#					
#	
#	
#	
#	9、管理器
#	
#		 	属性 objects 是一个管理器， 是 models.Manager类型的对象，用于与数据库进行交互。
#		 	当没有为模型类定义管理器时，django 会为每一个模型类生成一个名为objects的管理器，
#		 	自定义管理器后，django不再生成默认管理器 objects
#		 	
#		 	只要是继承 models.Manager 类的类就是管理器
#		
#		 自定义管理器类的作用：
#		 	
#		 	 	1）、修改原始查询集，重写all()方法； （查询isDelete不为1的）
#		 	 	
#		 	 	2）、向管理器类中添加额外的方法，如向数据库中插入数据
#		 	 	
#		 例子：定义---- 图书管理器
#		 	
#		 class BookInfoManager(models.Manger):
#		 	'''	 图书模型管理器类	'''
#		 	# 1、改变查询的结果集
#		 	def all(self):
#		 		# 1、调用父类的all，获取所有数据
#		 		books = super().all()			# 这是一个 QurySet
#		 		# 2、对数据进行过滤
#		 		books = books.filter(isDelete=False)
#		 		# 3、返回
#		 		return books
#		 		
#		 	 # 2、封装函数：操作模型类对应的数据表（增删改查） (可以直接在图书模型类中添加 类方法，@classmethod def create_book(cls,btitle,bpub_date))
#		 	 def create_book(self, btitle, bpub_date):
#		 	 	# 每一个模型类的对象都有一个模型类 model ; 即使模型类的名称改变了，也不影响封装的函数
#				# 创建一个模型类对象
#				model_class = self.model
#				book = model_class()
#				book.btitle = btitle
#				book.bpub_date = bpub_date
#				# 保存到数据库
#				book.save()
#				# 返回对象
#				return book		
#
#			
#						
#			BookInfo.objects.create_book('笑傲江湖','1991-1-1')						
#												
#					
#
#
#
#
#
#
#	10、元选项 ( 必要的类 )
#	
#		改应用名后对应的应用表名不会改变，会报错    例如：booktest_bookinfo  
#		
#		模型的表名不加应用名
#		
#		在模型类中定义类 Meta ，用于设置元信息， 使用 db_table 自定义表的名字
#		
#		例：
#			指定BookInfo模型类生成的数据表为 bookinfo
#			
#			class BookInfo(models.Model):
#				...
#				
#				# 定义元选项
#				class Meta:
#				
#					db_table='bookinfo' # 指定BookInfo生成的数据表名为 bookinfo
#					verbose_name_plural = verbose_name = '书名'		#  后台显示的别名
#					ordering = ['id']			# 排序 ，默认的是由小到大 ，从大到小 '-id', 也可以多项排序 ['id', 'age']	
#					
#					
#					
#		
#		
#		
#		
#					 从模型提取					传递给上下文		 交给模板
#	 Model(database)------------->  QuerySet(views-----> context) ------------> templates(html)
#	 
#	 模型中建立的类，就有一个 queryset 对象， 类.objects.all()