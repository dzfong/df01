#
#
#
# ---------------------------------
# 
# 		urls 配置
# 		
# ---------------------------------
# 
# 
# 一、配置
# 
# 	1、当前应用下去 新建一个 urls.py 文件
# 	
# 		调用： from django.urls import path
# 		并且调用本应用的视图： from . import views
# 		设置 urlpatterns 属性。(调度器)
# 		这是个列表，把每个路径 视图的路径都添加进去
# 		语法： path(<route>, <view>, name=None, **kwargs)
# 		route ---- 表示路径，从端口以后URL的地址，到/结束
# 		view ---- 表示route匹配成功后，需要调用的视图，view必须是函数，如果是class必须使用 as_view()转换为函数
# 		name --- 表示别名，视图的别名
# 		**kwargs --- 是一个字典
# 		path('', views.index, name='index'),
# 		
# 	2、在 项目的 urls.py 文件中
# 	
# 		导入应用的urls ：from booktest import urls
# 		导入包含的包：from django.urls import include
# 		添加配置应用， index 是目录文件夹，'' 是根目录
# 		path('index/', include(urls)),
# 
# 
# 
# 	注意：在模板里面引用地址配置时，一定要用/ 开始。 比如 <a href='/create'>
# 			
# 		匹配是按顺序的，如果两个url的路径设置的相同，那么匹配到第一个就停止了，不会继续往后匹配
# 		
# 		
# 		
# 		
# 
# 二、转换器： <>
# 		5种转换器类型：
# 				<str:string>: 	匹配的是一个非空字符串，除去“/” , 默认使用的是这种方式
# 				<int:num>:		匹配的0或正整数
# 				<uuid:uu>:		uuid格式的字符串
# 				<slug:string>:	由ASCII字母或数字组成，通过'-'连接的字符串
# 				<path:string>:	匹配的一个非空字符串，包含 “/”
# 		
# 		例如：			
# 			path("pages/<int:num>", views.page, name='page')
# 			num 是 视图views.py 中的 函数 page的参数
# 			def page(request, num):
# 				return HttpResponse('<h1>{}</h1>'.format(num))
# 
# 
# 
# 
# 三、include函数
# 
# 		项目的 urls.py 文件中 导包
# 		
# 		1、包含文件 URLconf
# 				1）、 导包： from django.urls import include, path
# 				2）、 添加路径： path('blog/', include('blog.urls'), name='blog') 		# 注意 include('blog.urls') 有引号
# 						或者 这样操作： 导包 from blog import urls
# 										path("blog/", include(urls), name='blog')
# 										
# 										
# 		2、函数views：
# 				1）、 导包： from my_app import views
# 				2）、 添加路径： path('', views.home, name='home')
# 		3、类views:
# 				1）、 导包： from other_app.views import Home
# 				2）、 添加路径： path('', Home.as_view(), name='home')	
# 		
# 						
# 				
# 		include 的三种写法：
# 		
# 			include(module, namespace=None): 最常用
# 				module ---  表示的是一个模型文件
# 				namespace --- 实例命名空间
# 			
# 			include(pattern_list)
# 				pattern_list --- 必须是一个可迭代的path() 或 re_path()清单
# 			
# 			include((pattern_list, app_namespace), namespace=None)
# 				app_namespace --- app命名空间
# 				
# 		
# 		例如： app应用urls.py
# 			
# 			from django.urls import path, include
# 			
# 			extractpatterns = [
# 				path('', views.index, name='index')
# 				path('blog/', views,blog, name='blog')
# 				path('', views.home, name='home')
# 			
# 			]
# 			
# 			urlpatterns = [
# 				path('', views.index, name='index'),			# 第一种方式
# 				path('index/', include(extractpatterns))		# 第二种方式
# 				# path('index/', include((extractpatterns, app_namespace='booktest')), name='index')	#第三种方式
# 			]
# 	
# 			
# 					
# 									
# 四、别名的作用：
# 		
# 			1、反复的调用别名，不会因为改变url而失效
# 			
# 				path('creat/', views.creat, name='creat')
# 			
# 				使用： 在模板的html 文件中的 href中把 <a href='/create'> 变成  <a href={%url 'news:creat'%}>		# news 是实例命名空间
# 	
# 	
# 			2、地址反转
# 			
# 			
# 
# 五、查询：
# 
# 		通过视图 views.py 的函数查询
# 		通常查询是通过get方法得到的， 百度通过关键字 s?wd ； 搜狗通过关键字 web?query 
# 		
# 		def search(request):
# 			search = request.GET.get('query')
# 			return HttpResponse('<h1>{}</h1>'.format(search))
# 			
# 		
# 
# 
# 
# 六、URL重定向：
# 
# 		1、页面重定向： 服务器不返回页面，而是告诉浏览器再去请求其他的url地址
# 				
# 		
# 			1）、redirect(to, permanent=False, *args, **kwargs)
# 				to --- 需要重新定位的位置，这个位置可以是一个视图，也可以是个url地址，还可以是一个模块，还可以URL的别名
# 				permanent --- 是否永久重定向，默认为False
# 				在 views.py 中导包：
# 					from django.shortcuts import redirect
# 				
# 					def index(request):
# 						return redirect("https://www.baidu.com", permanent=True)	# 永久性重定向
# 				
# 				
# 					
# 				
# 			2）、HttpResponseRedirect		（不常用。因为返回的只能是个 url地址）
#				from django.http import  HttpResponseRedirect
#				然后返回 到重定向页面，（相对于地址不变，刷新了下网页）
#				return HttpResponseRedirect('/books')
# 			
# 			
#
# 	
# 		2、反向解析： 传递参数
# 		
# 			在 views.py 中导包： from django.shortcuts import reverse
# 			reverse(viewname, urlconf=None, args=None, Kwargs=None, current_app=None)
# 			viewname --- 视图名
# 			urlconf --- URL配置文件
# 			args --- 列表
# 			Kwargs --- 字典
# 			current_app --- 当前app应用名
# 			
# 			def error(request, a, b):
# 				sum = a + b
# 				return HttpResponse('<h1 style='color:red;'>{}</h1>'.format(sum))
# 			
# 			def index(request):
# 				return redirect(reverse('loose', kwargs={'a':100, 'b':200}))
# 				
#	
#	
#			反向解析应用在两个地方：模板中的超链接，视图中的重定向
#	
#				1）、模板的超链接：
#					动态的去生成url地址，不会因为url改变而访问不了
#		
#					步骤
#						1）、	在项目的urls.py 中 添加 namespace , 通常是应用的名字
#								path('paper/', include('booktest.urls', namespace='paper'))
#			
#						2）、 	在应用的urls.py中 添加 name 别名，通常在html中应用 {% url 'paper:home' %}
#								path('home/', views.home, name='home')
#		
#	
#					位置参数：
#							{% url 'news:loose' 100 200 %}      # error/100/200
#							{% url 'news:loose' a=100 b=200 %}"	# error/100/200  带参数指定， def error(request, a, b):
#				
#		
#				
#				2）、视图中的重定向
#								
#					在重定向的时候使用 反向解析，需要导入包
#		
#					用到三个包，一个重定向redireect  一个反向解析 reverse  一个路径分离 resolve
#			
#					# 反向解析重定向
#			
# 						/rev  重定向到 /error/100/200
# 						def rev(request):
# 				
# 							# 获取路径 
# 							path = request.path
# 					
# 							# 路径分离 得到项目urls.py中应用名namespace
# 							current_namespace = resolve(path).namespace
# 					
# 							# 获取完整的url
# 							url = reverse('{}:loose'.format(current_namespace), kwargs={'a':100, 'b':200})
# 					
# 							return redirect(url)
# 											
# 		
# 		
# 		
# 		
# 		
# 		
# 		3、URL应用命名空间：
# 		
# 			多个app应用如果代码相同的情况下，默认的返回最后个代码，所以需要添加 应用名来区别
# 			
# 			在应用的 urls.py 中前面添加属性：
# 				app_name = 'news'
# 			
# 			在应用的views.py的函数别名前 加应用名：
# 				return redirect(reverse('booktest:loose', kwargs={'a':100, 'b':200}))
# 		
# 		
# 		
# 		
# 		4、URL实例命名空间：
# 			
# 			实例命名空间 是在 项目的urls.py 中的 include 使用
# 			要使用实例命名空间，必须要定义 应用命名空间
# 			
# 			当一个网页对应多个路径时 需要定义 namespace
# 			
# 				path('news/', include('booktest.urls', namespace='news')),
# 				paht('paper/', include('booktest.urls', namespace='paper')),
# 			
# 			
# 			应用views.py 中获取 路径分离
# 			导包： from django.urls import resolve
# 			
# 			def rev(request):
# 				path = request.path
# 				current_namespace = resolve(path).namespace
# 				return redirect(reverse('{}:loose'.format(current_namespace), kwargs={'a':100, 'b':200}))
# 				
# 				
# 				
# 				
# 				
# 七、URL默认值设置
# 
# 		页面的默认值设置，如果设置了默认值，那么需要在应用的urls.py中设置两个URL
# 			path('page<int:page>/', views.page),
# 			path('page/', views.page)
# 		