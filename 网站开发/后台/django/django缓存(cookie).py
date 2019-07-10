#
# 
# -------------------------------------
# 
# 	cookie	缓存
# 	
# -------------------------------------
# 
# 
# 
# 	记录信息的一种方式
# 	
# 		Cookie是由服务器端生成，发送给User-Agent（一般是浏览器），浏览器会将Cookie的key/value保存到某个目录下的文本文件内，
# 		下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。
# 		Cookie名称和值可以由服务器端开发自己定义，这样服务器可以知道该用户是否是合法用户以及是否需要重新登录等。
# 		服务器可以利用Cookies包含信息的任意性来筛选并经常性维护这些信息，以判断在HTTP传输中的状态。
# 		Cookie是存储在浏览器中的一段纯文本信息。
# 		
# 		Cookies最典型记住用户名
# 		 		
# 		
# 		特点：
# 		
# 			1）、以键值对方式进行存储
# 			2）、通过浏览器访问一个网站时，会将浏览器存储的跟网站相关的所有cookie信息发送给该网站的服务器。 保存在 request.COOKIES 对象中
# 			3）、cookie是基于域名安全的
# 			4）、cookie是有过期时间的，如果不指定，默认关闭浏览器之后cookie就会过期
# 			
# 			
# 		设置cookie： 需要一个HttpResponse类的对象或者是它子类的对象。 set_cookie
# 		读取cookie:  浏览器发给服务器得cookie 保存request对象的COOKIES
# 		
# 		
# 		# /cookie_set
#		 def cookie_set(request):
# 			''' 
# 				设置cookie信息
# 			'''
# 			response = HttpResponse("设置cookie，在表头查看")
# 			# 设置一个cookie信息，名字为name,值为value
# 			# max_age=14*24*3600 设置多少秒过期； expires = datetime.now() + timedelta(days=14) 两周过期
# 			response.set_cookie('name', 'value')		
# 			#  返回response . request.COOKIES 读取cookie
# 			print(request.COOKIES)
# 			return response
# 	
# 	
# 	
# 	
# 	
# 	
# 	
# 	
# --------------------------------------
# 
# 	session  会话
# 	
# --------------------------------------
# 
# 
# 	保存在服务器端   表 : django_session
# 	
# 		session的特点：
# 		
# 			1）、session是以键值对方式进行存储的
# 			2）、session依赖于cookie的。保存在cookie中   sessionid:唯一标识码 
# 			3）、session是有过期时间的，如果不指定，默认两个星期 14天
# 			
# 	
# 		设置session: request.session['username'] = 'admin'
# 		读取session：request.session['username']   也可以 request.session.get('键',默认值)
# 		清除session: request.session.clear()	清除的是设定的内容，值部分
# 					 request.session.flush()	删除session的整条数据
# 		删除指定的键及值  del request.session['键']
# 		设置session会话的超时时间，如果没有指定过期时间则 两个星期后过期(14days)
# 		request.session.set_expiry(value)
# 				value是个整数，会话的session_id cookie将在value秒后过期
# 				value为0 ，会话的session_id cookie将在关闭浏览器时过期
# 				value为None，会话的session_id cookie两周后过期
# 				
# 		/set_session
#		def set_session(request):
#			'''
#				设置session
#			request.session['username'] = 'admin'
#			request.session['age'] = 18
#			return HttpResponse('设置session')
#			
#			
#			
#		记住用户的登录状态	
#			
#			
#			
#			


###
#		应用场景：
###
#
#
# 	cookie: 记住用户名；安全性要求不高
# 	session: 涉及到安全性要求比较高的数据，银行卡账号，密码
# 	