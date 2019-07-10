#
#-----------------------------------
#
#	模板 T templates
#	
#-----------------------------------
#
#	
#	
#	模板的功能： 产生html文件，控制页面上展示的内容，模板文件不仅仅是一个html文件
#	
#	模板文件包含两部分内容：
#	
#		1）、静态内容： css  js html
#		2）、动态内容： 用于动态去产生一些网页内容，通过模板语言来产生
#		
#		
#		
#	使用步骤：
#		
#		1）、 在views.py中 加载模板文件(导包)， 获取一个模板对象   from django.template import loader
#		
#		2）、 定义模板上下文，给模板文件传数据
#		
#		3）、 模板渲染，产生一个替换后的html内容
#		
#		
#		
#			# # 使用模板文件
			# # 1、加载模板文件,	返回模板对象
			# temp = loader.get_template('booktest/index.html')

			# # 2、定义模板上下文， 给模板文件传递数据
			# # 需要导入包。 RequestContext
			# # 第一个参数是request 第二个参数是 传递的数据 是个字典，键值队
			# context = RequestContext(request, {'':''})

			# # 3、模板渲染 ： 产生标准的html内容
			# res_html = temp.render(context)
			
			# # 4、返回给浏览器
			# return HttpResponse(res_html)
			# 
			# 
			# 
#
#		以上这些步骤django已经封装了一个render
#		
#		from django.shortcuts import render
#	
#	
#	
#	
#		模板文件加载顺序：
#		
#			1、首先去配置的模板目录下找模板文件
#			2、去INSTALL_APPS 下面的每个应用下去找模板文件，前提是应用中必须有templates文件夹
#
#
#
#
#
# setting.py 中设置 模板的路径
# 
# 	TEMPLATES
# 	        'DIRS': [os.path.join(BASE_DIR, 'templates')],       # 模板目录文件夹路径, 把项目路径和模板文件夹拼接起来,这是一个列表，可以加很多路径
#        	'APP_DIRS': True,			# 自己配置可以改成 False
#     
#   
#        	     	
#       {% 代码段 %}  ----  标签
#       
#       {{ 模板变量名 }}  ----  变量
#       	  
#       	 	 格式： 数字，字母，下划线和点组成的， 不能以下划线开头
#       	 	 
#        		 模板变量的解析顺序： {{ book.btitle }}   {{ book.1 }} 
#        		 		使用模板变量时，点(.) 前面的可能是一个字典，可能是一个对象，还可能是一个列表
#        				1）、把book当成一个字典，把btitle当成键名，进行取值    book['btitle']
#        				2）、把book当成一个对象，把btitle当成属性，进行取值  	book.btitle
#        				3）、把book当成一个对象，把btitle当成对象的方法，进行取值 book.btitle
#        		
#        	 如果解析失败，则产生内容时用空字符串填充模板变量	   	
#        	   	   	   	   	
#        	   	   	   	   	   	   	   	   	
#   
#   jinjia2模板语言：
#   
#  1、	DTL模板语言： Django Templates Language， 也就是Django自带的模板语言
#  	
#  		DTL模板是一种带有特殊语法的HTML文件，这个HTML文件可以被Django编译，可以传递参数进去，实现数据动态化，
#  		在编译完成后，生成一个普通的HTML文件，然后发送给客户端。
#  		
#  		注意：
# 			1、所有的标签都是在{%%}之间。
#			2、if标签有闭合标签。就是{% endif %}。
# 			3、if标签的判断运算符，就跟python中的判断运算符是一样的。==、!=、<、<=、>、>=、in、not in、is、is not这些都可以使用。
# 				（进行比较操作时， 比较操作符两边必须有空格）
# 			4、还可以使用elif以及else等标签。
# 			5、引用参数用 {{ 参数 }}
# 			6、调用变量是按层级来调的： 调字典里面的是通过 book_list.book_name调用的，也可以用下标调用，book_list.1;
# 										而不是通过 book_List['book_name']来调的.
# 										
# 	
# 	
# 	
# 	2、 模板的继承：extends
# 	
# 		通常把所有页面相同的内容放在母模板中，不需要放在块中，
# 		当有些位置页面内容不同时预留出 块 block
# 	
# 		Django模版引擎中最强大也是最复杂的部分就是模版继承了。
# 		模版继承可以让您创建一个基本的“骨架”模版，它包含您站点中的全部元素，并且可以定义能够被子模版覆盖的 blocks 。
# 	
# 		格式:  在子版的html文件的首行 定义变量  
# 		{% extends 'base/base.html' %}
# 		
# 		母板里写入block 块，就可以被继承 ； block和顺序没有关系
# 		例如：
# 			<div class='content'> 
# 			{% block content %}
# 			{% endblock %}
# 			</div>
# 			
# 			子版里面继承
# 			{% block content %}
# 				{{ block.super }}		# 继承母模板内容
# 				<div>
# 				<h1>,....</h1>
# 				</div>
# 			{% endblock %}
# 			
# 			
# 		
# 		注意： 如果是在子页面写CSS和JS，CSS就不是在头部了，而JS也不是在<body>之前，假如要引用jquery,子页面写的JS会在jquery引用前面，就会不生效
# 	
# 				解决方案：在模板里css 和js位置在写个block块。然后在block里引入，在这个block写自己的js和css
# 						
#  	
#  	
#  	
#  	3、 模板的导入：  include 
#  	
#  		由于子版只能单一继承，所有当需要其他模板时，重复导入，需用到 include ，
#  		其他模板可以分块定义，然后用 include 导入
#  		include 方法同 extends 
#  			
#  			<!--  导入导航文件 -->
#			{% include 'booktest/nav.html' %}
#  	
#  	
#  	4 、注释：
#  	 
#  			<!-- 单行注释  -->  也可多行，但是 不能内嵌  ；  网页源代码会显示
#  			{#  单行注释  #}								网页源代码不显示
#  			{%  comment %}  多行注释 {% endcomment %}		网页源代码不显示
#  			
#  				
#  		
#  	5、 url 标签：
#  			
#  			<a href={%url 'news:creat'%}>		# news 是实例命名空间 ； creat 是路径别名
#  			
#  			
#  			
#  
#   6、 日期 Now 标签：
#   		
#   		{% now 'Y M d H:i:s' %}  	 不需要 endnow； 可以嵌套在子版的其他 block 中； 也可以定义在母版中
#   		
#   
#   
#   7、 自动转义  autoescape 标签：
#   	
#   		默认是打开的  
#   		
#   		打开： {% autoescape on %}
#   					模板语言代码
#   				{% endautoescape %}
#   				
#   		关闭： {% autoescape off %}
#   					模板语言代码
#   				{% endautoescape %}
#   				
#   		在模板上下文中的html 标记默认是会被转义的
#   		要关闭模板上下文字符串的转义： 可以用 {{ 模板变量|safe }}
#   		
#   		模板硬编码中的字符串默认不会经过转义，如果需要转义，需要手动进行转义
#   		{{ test|default:'&lt;h1&gt;hello&lt;/h1&gt;' }}		# <h1>hello</h1>
#   		
#   		用处：编辑商品详情信息的时候，数据表总保存的是html内容，比如字体加粗 ，默认显示的是转义的
#   				
#   				
#   8、 条件判断 if :
#   
#   		if 和 block 标签是成对出现的
#   		
#   		{%  block content %}
# 				{% if age > 18 %}
# 					<h2>你允许访问此网站</h2>
# 				{% else %}
# 					<h2>未到法定年龄</h2>
# 				{% endif %}
# 			{%endblock%}
# 			
# 			
# 	9、 for 循环：
# 	
# 			查看循环次数： {{ forloop.counter }}
# 	
# 			for 循环
# 					{% for i in list %}
#						<li>{{ i }}</li>
#					{% empty %}					# 如果是空值，则调用
#						<h2>{{empty}}</h2>
#					{% endfor %}
# 	
# 	
# 	10、 with ... as .. 标签：
# 		
# 		重复调用，经常调用的可以使用with标签; 定义的参数只能在with中用
# 		
# 		{% with tutorial.english.type as t %}
# 			{{t}}
# 		{% endwith %}
# 		
# 		
# 		
# 		
# 	11、 过滤器： | 
#
# 		过滤器是对模板变量进行操作的
# 		
# 		格式：  模板变量|过滤器：参数
#   		
#  		{{ value|add:200 }}     #  |是过滤器， add是处理方式,把后面的值转化为整数，如果类型不同则返回的是空值
#  		
#  		|first ---  返回列表的第一个值
#  		|last ---	返回列表的最后个值
#  		|length --- 返回变量值的长度
#  		|linebrakebr --- 将纯文本文件中的换行符转换为HTML中的换行
#  		|linenumbers --- 显示行号
#  		|ljust --- 左对齐
#  		|rjust --- 右对齐
#  		|lower --- 全小写
#  		|upper --- 全大写
#  		|title --- 将所有首字母大写
#		|wordcount --- 统计单词数量
#		|default --- 前面为False，则返回默认值
#		
#		
#		自定义过滤器：
#		
#			应用文件夹下新建 python package ,目录名固定的 templatetags 
#			新建一个filters.py文件
#			过滤器其实就是python函数
#			导类： from django.template import Library
#			创建一个Library类的对象 	register = Library()
#			需要像内置方法一样使用，必须用Library注册它  register.filter('mm', mod)
#			
#			在使用的html文档中 加载
#			{% load fiters %}
#
#
#
#	12、 静态文件
#		
#		css\ js\ images\ 都属于静态文件
#		在项目目录下新建个静态文件夹 static 
#		在static文件夹下在建立CSS JS IMAGES 等文件夹
#		
#		1）、然后建立文件
#		
#		2）、在html中加载 静态文件
#		
#		设置：
#		
#		在setting.py 中设置 
#			STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]           # 设置静态文件的保存目录
#		
#			TEMPLATES > OPTIONS > 添加 'builtins': ['django.templatetags.static']		# 不需要在html文件导包
#			 或者（在html首行添加 {% load static %} ）
#		
#		然后在head中添加样式链接 ：
#			 static 就是static的路径
#			 <link rel="stylesheet" href={% static css/style.css %}>  
#		
#		
#		
#		
