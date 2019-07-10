

#	M : 模型，和数据库进行交互
#	V ：接收请求，交互处理，返回应答
#	T ：模板，产生html页面
#
#
# 虚拟环境解决不同版本同时存在
# 
# pip install django  安装django
# 
# pip freeze 查看版本
# 
# 
# 
# 	新建项目：
# 		
# 		1、django-admin startproject 项目名(test1)
# 		
# 			
# 		test1 文件夹
# 		|	
# 		|———— 	manage.py 	项目管理文件，管理项目
# 		|————	test1 	文件夹
# 				|__ _init_.py 	空文件。作用是这个目录可以当作包使用
# 				|__ setting.py 	项目的整体配置文件
# 				|__ urls.py 	项目的URL配置文件
# 				|__ wsgi.py 	web服务器和django交互的入口
# 				
# 		
# 		在django中，每一模块使用一个django应用来开发。 （用户模块， 商品模块，购物车模块，订单模块）
# 		一个项目由多个应用组成的，每一个应用完成一个特定的功能。
# 		
# 		2、新建应用：
# 			
# 			python manage.py startapp 应用名(booktest)
# 		
# 			booktest
# 			|
# 			|__ __init__.py 	说明目录是个python模块
# 			|
# 			|__ admin.py 		网站后台管理相关的文件
# 			|
# 			|__ models.py 		写和数据库项目的内容 ； 设计和表对应的类，模型类，
# 			|
# 			|__ views.py 		定义处理函数，视图函数	
# 			|
# 			|__ tests.py 		写测试代码的文件 
# 			|			
# 			|__ apps.py
# 			|
# 			|__ migrations 		迁移文件夹
# 				|
# 				|__ __init__.py
# 				
# 				
# 		3、建立应用和项目之间的联系，需要对应用进行注册
# 		
# 			修改项目的配置文件 setting.py 中的 INSTALLED_APPS 配置项
# 			添加应用一项：
# 				 'booktest', # 进行应用的注册
# 				 
# 				 
# 		4、运行开发web服务器：
# 			
# 			  python manage.py runserver
# 			  
# 			  
# 			  
# 
# -----------------------
# 
#  	ORM 框架    
#  	
# -----------------------
# 
# 	O  ---   Object , 对象，类
# 	R  ---   Relations , 关系， 关系数据库中的表
# 	M  ---   Mapping, 映射
# 	
# 	
# 		作用： 通过类和对象操作对应的数据表，不需要写sql语句。
# 	
# 		另一个作用： 根据在 models.py 中设计的类自动生成数据库中的表。
# 		
# 		django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作
# 		
# 		
# 		
# 		
# ------------------------------=----
# 
# 
# 		模型类  models.py
# 		
# 			
# -----------------------------------
# 					
# 					
# 		数据库开发的步骤：
# 		
# 			1、在 models.py 中定义模型类 (只有继承自 models.Model 才是一个模型类)
# 			
# 			2、迁移：
# 				1）、生成迁移文件： 	python manage.py makemigrations
# 				2）、执行迁移生成表: 	python manage.py migrate
# 				
# 			3、通过模型类和对象完成数据增删改查操作：
# 				python manage.py shell
# 				from booktest.models import BookInfo
# 				b = BookInfo()		# 实例化类属性
# 				b.btitle = '天龙八部'	# 实例属性
# 				from datetime import date
# 				b.bpub_date = data(1990,1,1)
# 				b.save()						# 插入到数据表
# 				b2 = BookInfo.objects.get(id=1)	  # 查找数据，存放到对象b2中   类名.objects.get(条件名); 查所有: 类名.objects.all()
# 				b2.btitle		# '天龙八部'
# 				b2.bpub_date = date(1990,10,10) 	# 更改数据，必须要save()才会更新
# 				b2.save()					# 必须执行这步才会更新数据	
# 				b2.delete()					# 删除表数据
# 				
# 				查询一对多的信息
# 				b.heroinfo_set.all()
# 				查询多对一的信息
# 				h.hbook.属性
# 				
# 				

#
# ----------------------------------
# 
# 		后台管理 admin.py
# 		
# ----------------------------------
# 
# 	数据表的内容可以通过后台管理进行编辑
# 	
# 	后台管理文件  admin.py
# 	
# 	1、本地化
# 	
# 		语言和时区的本地化  修改 setting.py 文件
# 		LANGUAGE_CODE = 'zh-hans'			# 语言
# 		TIME_ZONE = 'Asia/Shanghai'			# 时区
# 	
# 	2、创建管理员
# 	
# 		python manage.py createsuperuser
# 		
# 	3、注册模型类
# 	
# 		在应用下的 admin.py 中注册模型类
# 		（在 booktest 中 显示的是 BookInfo object 而不是 书名‘天龙八部’
# 		由于返回的是个 object 类型，所以需要在 models.py 中的 BookInfo 模型类中  重写 __str__ 方法）
# 		
# 	4、自定义管理页面
# 	
# 		1）、在admin.py 中 自定义模型管理类 通常是模型类名+Admin ,继承自 admin.ModleAdmin  # AreaInfoAdmin(admin.ModelAdmin)
# 				显示列表的属性名 list_display 是个列表(可以是模型属性，也可以是模型方法)；
# 				每页显示的数据 list_per_page = 10 ；
# 				然后在 注册模型类中注册 自定义模型管理类。
# 				
# 		2）、在后台显示模型别名，需要在 models.py 模型类 元选项中定义  verbose_name_plural 和 verbose_name
# 			（元选项里面定义的别名是后台显示表的名字，属性里面定义的别名是后台显示的表列名）
# 			  排序在元选项中定义： ordering = ['id']
# 			
# 		
# 		3）、在下方也显示删除列表框： 在admin.py模型管理类中添加属性
# 				actions_on_bottom = True
# 		
# 		4）、列表页右侧添加过滤栏：在admin.py模型管理类中添加属性
# 				list_filter = []  # 是个列表，可以写多个过滤字段
# 		
#		5）、列表页上方的搜索框：在admin.py模型管理类中添加属性
#				search_fields = []
#		
#		6）、 编辑页选项：在admin.py模型管理类中添加属性 (只能同时显示1个，2选1)
#		
#				显示字段顺序； 
#					fields = ['bpub_date','btitle']
#					
#				分组显示：
#					fieldsets = {
#						('基本', {'fields': ['btitle']}),
#						('高级', {'fields': ['bread']})
#					}
#					
#				关联对象：
#					在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式有两种： 表格、块
#					类型 InlineModelAdmin: 表示在模型的编辑页面嵌入关联模型的编辑
#					子类 TabularInline: 以表格的形式嵌入
#						a、class BookTabularInline(admin.TabularInline):
# 								# 多类
# 								model = HeroInfo
# 								# 修改默认的3格空行为1格
# 								extra = 1 	
# 						b、然后在一类的管理类中定义属性, 是个列表，里面放定义的类
#							 	inlines = [BookTabularInline]
# 				
#					子类 StackedInline: 以块的形式嵌入
#						a、class BookStackedInline(admin.StackedInline):
#								# 多类的名字
#								model = HeroInfo
#						b、然后在一类的管理类中定义属性, 是个列表，里面放定义的类
#							 	inlines = [BookStackedInline]
#				
#					
#		 7）、 重写后台模板
#		 	
#		 		python -- Lib -- site-packages -- django -- contrib -- admin -- templates -- admin -- base_site.html
#		 		
#		 		把这个base_site.html 文件复制到  模板文件夹templates中的admin文件夹下
#		 		
#		 		修改base_site.html文件。
#		 		
#		 		默认的会加载修改的base_site.html文件
#		 		
#		 
#		 		







#----------------------------------------------
#
#			视图管理  views.py
#		
#----------------------------------------------
#
#
#	在 Django 中， 通过浏览器去请求一个页面时，使用视图函数来处理这个请求的，
#	视图函数处理之后，要给浏览器返回页面内容
#	
#	
#		视图函数的使用
#		
#		
#		1、在view.py 中定义视图函数，普通函数，但是必须有一个参数 request
#		# 就是普通的函数，但是必须有个 request 参数
#		
#			def index(request):
#				'''
#					进行处理，请求和返回，和M 和T 进行交互
#				'''
#				# HttpResponse 必须要导入库
#				return HttpResponse("hello world")
#				
#		
#		2、 进行 url 配置
#		
#			注意是在 当前应用下去 新建一个 urls.py 文件去配置
#			调用 from django.urls import path
#			并且调用本应用的视图 from . import views
#			设置urlpatterns 属性。
#			这是个列表，把每个路径 视图的路径都添加进去
#			path('', views.index),	
#			
#			然后在 项目的 urls.py 文件中
#			导入应用的urls
#			from booktest import urls
#			导入包含的包
#			from django.urls import include
#			添加配置应用， index 是目录文件夹，'' 是根目录
#			path('index/', include(urls)),		
#			
#			
#			在进行地址配置时，一定要用/ 开始。 比如 <a href='/create'>
#					
#		
#				
#	注意： 如果是网页需要重定向，需要导入包 HttpResponseRedirect		
#			from django.http import  HttpResponseRedirect
#			然后返回 到重定向页面，（相对于地址不变，刷新了下网页）
#			return HttpResponseRedirect('/books')
#			
#			页面重定向： 服务器不返回页面，而是告诉浏览器再去请求其他的url地址
#			
#
#
#-------------------------------------------
#
#
#		模板   T  templates文件夹
#		
#	
#-------------------------------------------
#
#	
#		将前端的内容定义在模板中，然后再把模板交给视图调用，各种漂亮、炫酷的效果就出现了
#		
#		模板不仅仅是一个 html 文件
#		不仅可以使用变量 还可以使用编程语言代码
#		
#		
#		1、创建模板文件夹
#		
#			一般是建立  templates 
#			然后在模板文件夹下面建立应用文件夹, 使
#			把每个模板放到应用文件夹中
#			
#		2、配置模板文件
#		
#			在 setting.py 中设置模板文件夹的路径
#			把项目文件路径和模板文件夹拼接起来 os.path.join(BASE_DIR, 'templates')
#			TEMPLATES = [
#				'DIRS': [os.path.join(BASE_DIR, 'templates')],
#			]
#				
#		
#		3、使用模板文件	（views.py中）
#		
#			1）、加载模板文件		
#				去模板目录下面获取html的文件内容，返回一个模板对象
#				导入包： from django.template import loader
#				temp = loader.get_template('booktest/index.html')		# templates路径下的
#				
#			2）、定义模板上下文
#				向模板文件传递数据
#				变量名：{{ dict_key }}     {{ 之间不能有空格
#				代码： {% 代码段 %}   
#				导入包： from django.template import RequestContext
#				context = RequestContext(request, {} )		# 第一个参数是 视图函数的参数，第二个参数是传递的数据，是个字典
#				
#			3）、渲染模板 （变量替换掉）
#				得到一个标准的html内容
#			
#			上面的步骤django 已经封装好了，导入包 from django.shortcuts import render
#			
#			return render(request, 'booktest/index.html', {'dict_key ':' dict_value'})
#				
#			
#			
#		如果使用的是静态文件，如 js 、 css、 image 都是静态文件 ； 需要建立一个静态文件夹
#		在 项目下 新建一个 static 目录，然后在 setting.py 中添加一个配置
#		STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]		# 设置静态文件的保存目录
#		



# 
# =========================================
# 
# 		配置使用 mysql 数据库
# 	
# =========================================
# 
# 		
# 	1、	setting.py 中找到 DATABASES 项
# 		
# 	2、 在 'default' 字典中 注销默认的数据库
# 		
# 		添加项：
# 			'ENGINE': 'django.db.backends.mysql',
# 			'NAME': 'dbname',	# 数据库名称， 数据库必须手动创建，表不用手动创建
# 			'USER': 'root' ,	# 数据库用户
# 			'PASSWORD': 'password',		# 密码
# 			'HOST': 'localhost', # 指定mysql数据库所在电脑ip
# 			'PORT': 3306,		# 数据库端口
# 		
# 	3、 安装 MySQLdb :   pip install pymysql
# 	
# 	4、配置项目文件夹下 __init__.py:
# 		添加：
# 			import pymysql
# 			pymysql.install_as_MySQLdb
# 	
# 	
# 	5、 数据库操作
# 	
# 	
# 			mysql -u root -p 				进入mysql 数据库
# 	
# 			show databases;					显示数据库
# 			create database xxx charset='utf8';			创建数据库
# 			use xxx;			进入创建的数据库
# 			show tables;		显示数据表
# 			create table xxxx(id int primary key auto_increment not null, name varchar(20), age int default 20);	创建表
# 			show create table xxxx;		显示创建表属性
# 			desc xxxx;		表结构
# 			insert into xxxx (name,age) values ('tom', 22); 		插入数据
# 			select * from xxxx;			查询表数据
# 			update xxxx set age= 18 where name = 'tom';		修改数据
# 			delete from xxxx WHERE name='tom';		删除数据
# 			drop database xxx;		删除数据库
# 			exit;				退出mysql
# 	
# 	
# 	
# 	





#========================================================		
#		
#	 csrf攻击： 跨站请求伪造
#	 
#========================================================
#
#
#	
#		在进行网站开发的时候，有些页面是用户登录之后才能访问的，假如用户访问了这个地址，需要进行登录判断
#		如果用户已登录，可以进行后续的操作； 如果没有登录，跳转到登录页面
#		
#		针对判断登录有两种操作方式：
#		
#			1）、可以把判断的方法定义个函数，在一些需要权限的页面调用
#			
#			2）、可以定义个登录装饰器 （经常用的）
#			
#				def login_required(view_func):
#					''' 登录判断装饰器 '''
#					def wrapper(request, *view_args, **view_kwargs):
#						# 判断是否登录
#						if request.session.has_key('islogin'):
#							# 用户已登录，调用对应的视图
#							return view_func(request, *view_args, **view_kwargs)
#						else:
#							# 用户未登录，跳转到登录页
#							return redirect('/login')			
#					return wrapper
#					
#			然后在需要判断是否登录的函数前装饰：   @login_required
#			
#			
#			
#			
#			csrf 能伪造成功的关键点：
#				
#				1）、 登录正常网站之后，你的浏览器保存的sessionid，你没有退出
#				2）、 访问另外一个网站，并且点击了页面上的按钮
#			
#		
#			
#					
#				django默认开启了csrf中间件 防护，只针对post提交，
#				网页凡是使用post提交的表单，必须要加个标签 
#				{% csrf_token %}
#		
#		
#		
#				防御原理：
#		
#					1）、 渲染模板文件时在页面生成一个名字叫 csrfmiddlewaretoken 的隐藏域
#					2）、 服务器交给浏览器保存一个名为 csrftoken的 cookie信息
#					3）、 提交表单时，两个值都会发给服务器，服务器进行比对，如果一样，则csrf验证通过，否则失败
#			





#========================================									
#	
#	 验证码
#	 
#========================================
#
#	 
#	 	 	 
#	
#		在用户注册、登录页面，为了防止暴力请求，可以加入验证码功能，如果验证码错误，则不需要继续处理，
#		可以减轻业务服务器、数据库服务器的压力。
#		
#		
#		手动实现验证码
#		
#			1）、安装包 Pillow
#				
#					pip install pillow
#					
#			2)、 在views.py文件中 ，创建视图 verify_code
#			
# 					from PIL import Image, ImageDraw, ImageFont
# 					from django.utils.six import BytesIO
					
# 					def verify_code(request):
# 					    #引入随机函数模块
# 					    import random
# 					    #定义变量，用于画面的背景色、宽、高
# 					    bgcolor = (random.randrange(20, 100), random.randrange(
# 					        20, 100), 255)
# 					    width = 100
# 					    height = 25
# 					    #创建画面对象
# 					    im = Image.new('RGB', (width, height), bgcolor)
# 					    #创建画笔对象
# 					    draw = ImageDraw.Draw(im)
# 					    #调用画笔的point()函数绘制噪点
# 					    for i in range(0, 100):
# 					        xy = (random.randrange(0, width), random.randrange(0, height))
# 					        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
# 					        draw.point(xy, fill=fill)
# 					    #定义验证码的备选值
# 					    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
# 					    #随机选取4个值作为验证码
# 					    rand_str = ''
# 					    for i in range(0, 4):
# 					        rand_str += str1[random.randrange(0, len(str1))]
# 					    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
# 					    # windows 字体路径： 'c:\Windows\Fonts\msyh.ttf'
# 					    font = ImageFont.truetype('FreeMono.ttf', 23)
# 					    #构造字体颜色
# 					    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
# 					    #绘制4个字
# 					    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
# 					    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
# 					    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
# 					    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
# 					    #释放画笔
# 					    del draw
# 					    #存入session，用于做进一步验证
# 					    request.session['verifycode'] = rand_str
# 					    #内存文件操作
# 					    buf = BytesIO()
# 					    #将图片保存在内存中，文件类型为png
# 					    im.save(buf, 'png')
# 					    #将内存中的图片数据返回给客户端，MIME类型为图片png
# 					    return HttpResponse(buf.getvalue(), 'image/png')
# 		
#			
#			
#			
#			3) 、配置url
#			
#			4）、 登录检验页面 调用验证码和 session验证
#			
#			
#			







#============================================ 		
# 		
# 		中间件
# 	
#=============================================
#
#
#
# 	
# 		中间件函数是 django 框架给我们预留的函数接口，让我们可以干预请求和应答的过程
# 			
# 			获取浏览器端的ip地址:
# 				request.META['REMOTE_ADDR']		
# 				
# 			
# 				禁止某些ip访问网站：
# 					1）、禁止列表
# 					2）、定义装修器函数 判断
# 					3）、页面函数前添加装饰器
# 				这样是可以操作，但是太麻烦，必须每个页面前面都要加上装饰器：	
# 				
# 			
# 		所以用到中间件，每个视图调用之前执行中间件
# 			
# 			1)、在应用下去新建 middlewae.py 文件
# 			
# 			2）、定义中间件类，  class BlockedIPSMiddleware(object):
# 			
# 			3）、定义中间件函数,名字是预留的，下面的函数就是服务器响应的顺序
# 			
# 				__init__(self, get_response): 服务器响应第一个请求的时候调用，只调用一次，重启后会再调用一次
# 				
# 				__call__(self, request):	调用函数或类，调用的就是__call__方法， 有返回值
# 				
# 				process_request(self, request): 是在产生request对象， 进行url匹配之前调用。
# 				
# 				process_view(self, request, view_func, *view_args, **view_kwargs): 是url匹配之后，调用视图函数之前
# 				
# 				process_response(self, request, response): 视图函数调用之后，内容返回给浏览器之前 , 把参数返回去 ；有返回值
# 				
# 				process_exception(self, request, exception): 视图函数出现异常，会调用这个函数
# 				
# 				如果注册的多个中间件类中包含 process_exception 函数的时候，调用的顺序跟注册的顺序是相反的
# 				注册多个异常类的时候：先注册的后调用，后注册的先调用
# 				
# 				
# 					# 新版本的中间件设置 ：中间件类必须接受一个get_response参数
# 						def __init__(self, get_response):
# 			 				self.get_response = get_response
#
# 						def __call__(self, request):
# 							return self.get_response(request)	
# 									
# 				
# 			4）、 在setting 的 MIDDLEWARE_CLASSES 项中注册自定义的中间件类
# 				
# 				'booktest.middleware.BlockedIPSMiddleware'
# 				 
# 				 格式： 应用名.middleware.中间件类名
# 				
# 			
# 			



#=========================================
#
#		上传图片
#		
#=========================================
#
#
#		
#	在python中进行图片操作，需要安装包PIL
#		pip install pillow
#
#	在Django中上传图片包括两种方式：
#		
#			1）、在管理页面admin中上传图片
#			2）、自定义form表单中上传图片
#
#
#	
#		1、配置上传文件保存目录
#			
#			1）、新建上传文件保存目录
#				
#				static --- media
#		
#			2）、在 setting.py 中添加 设置上传文件的保存目录 的属性
#				
#				MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
#		
#		
#		2、后台管理页面上传图片
#		
#			1）、 设计模型类
#			
#				class PicTest(models.Model):
#					# 上传图片
#					gpic = models.ImageField(upload_to='booktest')	# upload_to 指定上传目录
#			
#			
#			2）、 迁移文件
#				
#				python manage.py makemigrations
#				
#				python manage.py migrate
#			
#			3）、 注册模型文件
#				
#				在 admin.py 中导入 模型类，并注册
#				
#				admin.site.register(PicTest)
#			
#
#
#		3、用户自定义页面上传图片
#		
#			1）、定义用户上传图片的页面upload_pic.html并显示， 是一个自定义的表单； 
#				表单的提交方式为post ， 指定编码类型为 multipart/form-data
#				<form method='post' action={% url 'news:upload_handle' %} enctype="multipart/form-data">
#					{% csrf_token %}
#					<input type='file' name="pic"><br/>
#					<input type="submit" value="上传">
#					
#			2）、定义接收上传文件的视图函数
#				 request.FILES的属性可以获取上传文件的处理对象
#				 上传文件不大于2.5M的，文件放在内存中		# <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>	
#				 上传文件大于2.5M的，文件写在一个临时文件中	# <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>
#				 
#				 
#				
#				 




#===========================================
#
#		分页
#		
#===========================================
#
#
#
#		Django提供了数据分页的类，这些类被定义在django/core/paginator.py中。
#		类Paginator用于对列进行一页n条数据的分页运算。类Page用于表示第m页的数据	
#		
#		
#		Paginator类实例对象
#		
#			方法_init_(列表,int)：返回分页对象，第一个参数为列表数据，第二个参数为每页数据的条数
#			
#			属性count：返回对象总数
#			
#			属性num_pages：返回页面总数
#			
#			属性page_range：返回页码列表，从1开始，例如[1, 2, 3, 4]
#			
#			方法page(m)：返回Page类实例对象，表示第m页的数据，下标以1开始
#			
#			
#			
#			
#		Page类实例对象
#		
# 			调用Paginator对象的page()方法返回Page对象，不需要手动构造。
# 			
# 			属性object_list：返回当前页对象的列表。
# 			
# 			属性number：返回当前是第几页，从1开始。
# 			
# 			属性paginator：当前页对应的Paginator对象。
# 			
# 			方法has_next()：如果有下一页返回True。
# 			
# 			方法next_page_number(): 返回下一页的页码
# 			
# 			方法has_previous()：如果有上一页返回True。
# 			
# 			方法previous_page_number(): 返回上一页的页码
# 			
# 			方法len()：返回当前页面对象的个数。
#
# 	
# 	
# 		from django.core.paginator import Paginator
# 		
# 		paginator = Paginator(books, 10)			
#		
#		page = paginator.page(1)
#		
#		
#		html中的 逻辑
#			<!-- 两者效果相同 -->
# 			{# {% for book in page.object_list %} #}
# 			<!-- 显示页内容，默认为第1页  -->	
# 			{% for book in page %}
# 			<li>{{ book }}</li>
# 			{% endfor %}
		

# 			<!-- 判断是否有上一页 -->
# 			{% if page.has_previous %}
# 				<a href={% url "news:showpage" page.previous_page_number %}>&lt;上一页</a>
# 			{% endif %}

# 			<!-- page_range是页码的列表 -->
# 			{% for pindex in page.paginator.page_range %}
# 				<!-- 判断是否为当前页 -->
# 				{% if pindex == page.number %}
# 					{{ pindex }}
# 				{% else %}
# 					<a href={% url "news:showpage" pindex %}>{{ pindex }}</a>
# 				{% endif  %}
# 			{% endfor %}

# 			<!-- 判断是否有下一页 -->
# 			{% if page.has_next %}
# 				<a href={% url "news:showpage" page.next_page_number %}>下一页&gt;</a>
# 			{% endif %}
# #		
#					