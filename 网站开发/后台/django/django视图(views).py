

#----------------------------------------------
#
#			视图管理 V  views.py
#		
#----------------------------------------------
#
#
# 	接收请求，进行处理，与 M 和 T 进行交互，返回应答
# 	返回html内容 HttpResponse, 也可能重定向 HttpResponseRedirect, 还可能是 JsonResponse
# 	
# 	1、 使用：
# 	
# 		1）、定义视图函数： request 参数必须有， 是一个HttpRequest类型的对象，参数名可以变化，但不要更改
# 		
# 		2）、配置url：	建立url和视图函数之间的对应关系
# 		
# 		
#	2、 url 配置的过程
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
#		注意： 如果是网页需要重定向，需要导入包 HttpResponseRedirect		
#			from django.http import  HttpResponseRedirect
#			然后返回 到重定向页面，（相对于地址不变，刷新了下网页）
#			return HttpResponseRedirect('/books')
#			
#			页面重定向： 服务器不返回页面，而是告诉浏览器再去请求其他的url地址
#			
#
#
#	3、错误视图
#
#		404 页面 ： 找不到页面，路径（url）有问题
#		
#			关闭 debug   : setting.py   中 设置 DEBUG = False
#			更改了debug 需要设置ALLOWED_HOSTS ，允许哪些地址访问； 允许所有那么 ALLOWED_HOSTS = ['*']
#			自定义404页面：
#				1、如果所有应用的404页面一样：在模板文件夹下(templates, 不是booktest文件夹) 新建404.html 不需要引用，django自动会使用自定义404页面
#				2、如果所有应用的404页面不一样：在模板文件夹应用文件夹下 新建404.html , 
#					然后在视图views.py中定义函数并渲染，接着在urls.py中导包 form django.conf.urls import handler404，
#					不要在调度器urlpatterns 中声明。 直接赋值 handler404 = views.函数名 ， 记住没有()，不然就是调用
#			 
#		500 页面 ： 服务器端的错误， 视图函数错误 ，代码问题
#		
#		
#		400 页面 ： 无效的请求
#		
#		
#		403 页面 : 	禁止访问，无权限
#		
#		
#		405 页面 ： 请求方法不允许
#		
#		
#		200 ok ： 请求、成功
#		
#			 
#			 
#			 
#	4、捕获url参数
#	
#		1）、位置参数：
#			位置参数，参数名可以随意指定
#			
#		2）、关键字参数：
#			在位置参数的基础上给正则表达式组命名即可
#			?P<组名>
#			
#		
#		
#	5、request 参数
#	
#		request 就是 HttpRequest类型的对象
#		request 包含浏览器请求的信息
#		
#		request.method 可以得到是 post 还是 get 请求
#			1)、request.POST 保存的是 post 方式提交的参数
#				类型是 QueryDict
#				q = QueryDict('a=1&b=2&c=3')
#				取值：q.get('a')
#				也可以设置默认值： q.get('d', 'default')
#				如果 ‘d’ 有值，返回的是值，如果没值 返回的是 default
#				QueryDict 的 键可以对应多个值，默认取得是最后的值
#				取多值使用列表： q.getlist('a') 
#			
#			2)、request.GET 保存的是get方式提交的参数
#				
#		request.path  可以得到请求页面的完整路径， 不包含域名和参数部分
#			
#		request.encoding 	提交的数据编码方式
#			
#		request.FILES	包含所有的上传文件
#		
#		request.COOKIES 	一个标准的python字典。包含所有的cookie ， 键和值都为字符串
#		
#		request.session		一个即可读又可写的类似于字典的对象，表示当前的会话，只有当django启用会话的支持时才可用
#		
#		
#		
#		
#		
#	6 、ajax
#		
#		异步的javascript	
#		作用： 在不重新加载页面的情况下，对页面进行局部的刷新 （注册页面经常用到）
#		
#		$.ajax({
#			'url': 请求地址,
#			'type': 请求方式,
#			'dataType': 预期返回的数据格式(json),
#			'data': 参数
#		}).success(function(data)){
#			//请求成功后的 回调函数
#		}
#		
#		
#		
#		
#		
#	7、HttpResponse: （用的少，基本上都是用渲染，render() ）
#		
#		HttpResponse(content, content_type=None, status=None, charset=None, reason=None, *args, **kwargs)
#			content --- 返回给视图函数的内容
#			content_type  --- 内容类型:
#				1、 text/html HTML文本字符串 ;
#				2、 text/plain 纯文本； 
#				3、 text/css
#				4、 text/javascript;
#				5、 application/xml  xml文本
#				6、 application/json json文本
#				7、 multipart/form-data 上传文本
#			status ---  html的响应代码
#				200 成功
#				404 找不页面
#				500 服务器参数
#			charset --- 字符编码设置
#			reason --- 返回一个语句，基本不用
#			
#			
#			
#			
#	
#	8、 Request:
#	
#		request.scheme   		请求协议		http
#		request.gt_host()		主机地址		127.0.0.1:8000
#		request.get_port()		获取端口		8000
#		request.method			请求方式		get
#		request.get_raw_uri		完整的url地址	http://127.0.0.1:8000/welcome
#		request.encoding		获取编码		None	
#		request.get_full_path()	完整路径 		/welcome
#		request.GET.get()
#	
#	
#	
#	
#	9、 视图装饰器
#	
#		导包： from django.views.decorators.http import require_http_methods
#		
#		定义装饰器：允许请求的方式
#			@require_http_methods(['GET','POST'])
#			
#		
#		require_GET() --- 只允许使用get方式进行请求
#		require_POST() --- 只允许使用post方式进行请求
#		require_safe() --- 只允许使用get方法和head方法的装饰器
#		
#			
#		
#		
#	10、视图渲染模板
#	
#		导包： from django.shortcuts import render
#		
#		render(<request>, <template_name>, context=None, content_type=None, status=None, using=None)
#		必选参数：
#			request 生成HttpRequest对象
#			template_name 	指定你需要渲染的模板名称
#		可选参数：
#			context 上下文，必须是个字典，我们在HTML文件中使用它的key，通过key展示对应的value, 传参
#			content_type 指定上下文的类型	
#				1、 text/html HTML文本字符串 ;
#				2、 text/plain 纯文本； 
#				3、 text/css
#				4、 text/javascript;
#				5、 application/xml  xml文本
#				6、 application/json json文本
#				7、 multipart/form-data 上传文本
#			status 响应的状态码
#				200 成功
#				404 找不页面
#				500 服务器参数			
#			using 用于加载模板的引擎名称
#				django templates language
#				jinjia2		
#			
#	
#	
#	
#	11、 类视图
#	
#		在视图views.py中
#		导包： from django.views import View
#		
#		class IndexView(View):
#		
#			# get请求
#			def get(self, request):
#				return render(request, 'index.html')
#			
#			# post请求
#			def post(self, request):
#				return render(request, 'login.html')
#				
#		在urls.py中定义路径
#			path('', views.IndexView.as_view(), name='index')
#			
#				
#		
#		