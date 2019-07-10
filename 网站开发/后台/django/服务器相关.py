#
## 
#
# nginx
# 	
# 		web服务器
# 		nginx 是个代理服务器，支持高并发，它是代理，本身并不执行，是个传话筒，把用户提交的请求转发给web服务器，再把web服务器的结果转发给用户。
# 		
# 		nginx 接收到浏览器发送过来的http请求，将包进行解析，分析url：
# 		1）、如果是静态文件请求就直接访问用户给nginx配置的静态文件目录，直接返回用户请求的静态文件；
# 		
# 		2）、如果不是静态文件，而是一个动态的请求，那么nginx就将请求转发给uwsgi,
# 		uwsgi 接收到请求之后将包进行处理，处理成wsgi可以接受的格式，并发给wsgi,
# 		wsgi 根据请求调用应用程序的某个文件，某个文件的某个函数，最后处理完将返回值再次交给wsgi,
# 		wsgi将返回值进行打包，打包成uwsgi能够接收的格式，
# 		uwsgi接收wsgi 发送的请求，并转发给nginx,nginx最终将返回值返回给浏览器。
# 		
# 		
# 		
# 		正向代理，"它代理的是客户端，代客户端发出请求"
# 		
# 		反向代理，"它代理的是服务端，代服务端接收请求"
# 		
# 		
# 		Nginx可以作为反向代理进行负载均衡的实现.
# 		
# 		
# 		
# uWSGI
# 
# 		是实现了WSGI协议的一个web服务器；即用来接受客户端请求，转发响应的程序。
# 		实际上，一个uWSGI的web服务器，再加上Django这样的web框架，就已经可以实现网站的功能了。那为什么还需要Nginx呢？	
# 		
# 		一个普通的个人网站，访问量不大的话，当然可以由uWSGI和Django构成。但是一旦访问量过大，客户端请求连接就要进行长时间的等待。
# 		这个时候就出来了分布式服务器，我们可以多来几台web服务器，都能处理请求。但是谁来分配客户端的请求连接和web服务器呢？
# 		Nginx就是这样一个管家的存在，由它来分配。
# 		这也就是由Nginx实现反向代理，即代理服务器
#	
# 
# uwsgi
# 
# 		与WSGI一样，是uWSGI服务器的独占通信协议，用于定义传输信息的类型(type of information)。
# 		每一个uwsgi packet前4byte为传输信息类型的描述，与WSGI协议是两种东西，据说该协议是fcgi协议的10倍快。		
# 	
# 	
# 	
# 		
# WSGI
# 	
# 		WSGI的全称是Web Server Gateway Interface（Web服务器网关接口），
# 		它不是服务器、python模块、框架、API或者任何软件，
# 		只是一种描述web服务器（如nginx，uWSGI等服务器）如何与web应用程序（如用Django、Flask框架写的程序）通信的规范。
# 		
# 		web服务器必须具备WSGI接口，所有的现代Python Web框架都已具备WSGI接口，它让你不对代码作修改就能使服务器和特点的web框架协同工作
# 	
# 	
# 		WSGI协议的流程：
# 		
# 										Nginx uWSGI												Django
# 							
# 		【浏览器】 1、请求动态资源 --> 【web服务器】 2、通过wsgi调用  --------------------> 【应用程序框架】 里面的 application(env func_p) 函数	
# 			|							|														|	env 是字典， func_p是函数
# 			|							|														|		|
# 			|							3、通过引用调用web服务器的方法，						|		|
# 			|							|	设置返回的状态和头信息				<----------------		|
# 			|							|																|
# 			|							设定一个函数，													|
# 			|							把函数的引用传递给application里的func_p函数 					|	
# 			|							保存header														|	application 继续执行代码	
# 			|							|																|
# 			|							|																|
# 			|							|																|
# 			|							4、调用返回														|
# 			|							此时web服务器端保存了刚刚设置的信息 	----------------> 5、查询数据库等，生成动态页面的body信息
# 			|							|														|		|	
# 			|							|														|		return body
# 			|							|														|		|
# 			|							6、把生成的body信息返回给web服务器的调用	<------------		|
# 			|							|																|
# 			|							|																|
# 			7、web服务器把数据返回给浏览器								 								
# 			|					
# 								
# 		
# django 
# 
# 		web框架
# 		框架的作用在于处理request和 reponse，其他的不是框架所关心的内容。
# 		所以如何部署Django不是Django所需要关心的。
# 		
# 		
# 		
# 		
# 
# 

# 访问过程
# 
# 
# 
# 		 	HTTP			uwsgi 			  uwsgi 							WSGI		
# 浏览器 --------> Nginx ----------> uWSGI -----------> python WSGI module -------------> python application