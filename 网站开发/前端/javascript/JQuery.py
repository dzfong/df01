jQuery

		实际开发中很少用到原生js的，一般都是用jQuery库，是目前使用最广泛的javascript函数库; 

		jQuery库是前后端通用的；


		加载jQuery:

			<script type="text/javascript" src="js/jquery-1.12.2.js"></script>
			<script> </script>
			不能直接在jquery的引入标签里写js代码；需要另外写个script标签，在这个标签里面写js代码



		完整写法：				
					$(document).ready(function(){		// 页面加载
						var $div = $('#div1');			// 获取元素 , 和css样式规则一样
						alert('jquery弹出的' + $div);
						})

		ready的简写：
					$(function(){
						var $div = $('#div1');			
						alert('jquery弹出的' + $div);
						})




		对象一般用 $开头去写 ; 一般都是用简写的方法

		----------------------------------------------------------------------------------------

			$(document).ready(function(){}); 功能和原生的 window.onload = function(){}; 一样
			$(function(){});	

		-----------------------------------------------------------------------------------------

			但是比原生的window.onload 加载速度快;
				ready是等标签加载完就执行了；
				onload是等标签加载完后，再渲染之后才运行；


			


							

	一、 选择器：

			1、jquery选择器可以快速地选择元素，选择规则和css样式相同()，使用length属性判断是否选择成功。
				jquery有容错机制，即使没有找到元素，也不会出错，可以用length属性来判断是否找到了元素,
				length等于0，就是没选择到元素，length大于0，就是选择到了元素。

				$('#myId') 		//选择id为myId的网页元素

				$('.myClass') 	// 选择class为myClass的元素

				$('li') 		//选择所有的li元素

				$('#ul1 li span') //选择id为为ul1元素下的所有li下的span元素

				$('input[name=first]') // 选择name属性等于first的input元素


				写属性，等同于字典 json 数据
				jquery可以批量修改css样式

					$div = $('#myId');
					$div.css({'background-color':'red'});	// background-color 写成 backgroundColor 可以不加引号

				如果只是使用一次，可以不定义，直接设置，如：
					$('div').css({'background-color':'red'});		// 设置所有选择器为 div的 



			2、 对选择集进行过滤：


				$('div').has('p'); 		// 选择包含p元素的div元素

				$('div').not('.myClass'); 	//选择class不等于myClass的div元素

				$('div').filter('.myClass'); 	//选择class等于myClass的div元素

				$('div').eq(5); 	//选择第6个div元素(从0开始的)	 比较常用	


			3、 选择集转移：

				$('div').prev(); 	// 选择div元素前面紧挨的同辈元素

				$('div').prevAll();		// 选择div元素之前所有的同辈元素

				$('div').next(); 	// 选择div元素后面紧挨的同辈元素

				$('div').nextAll();		// 选择div元素后面所有的同辈元素

				$('div').parent();	// 选择div的父元素

				$('div').children();	// 选择div的所子元素

				$('div').siblings();	// 选择div的同级元素

				$('div').find('.myclass');	// 选择div内的class等于myclass的元素






	二、 样式操作：


		jquery用法思想一 		
				选择某个网页元素，然后对它进行某种操作

		jquery用法思想二
				同一个函数完成取值和赋值


			1、	操作行间样式；

					如果没有定义的css属性也能读取默认的，原生的js无法读取
					选择器获取的多个元素，获取信息获取的是第一个。

					// 获取div的样式
					$("div").css("width");
					$("div").css("color");

					//设置div的样式
					$("div").css("width","30px");
					$("div").css("height","30px");
					$("div").css({fontSize:"30px",color:"red"})


			2、	操作样式类名：

					$("#div1").addClass("divClass2") 	//为id为div1的对象追加样式divClass2 （名称不是选择器所以不用加"."）

					$("#div1").removeClass("divClass")  //移除id为div1的对象的class名为divClass的样式

					$("#div1").removeClass("divClass divClass2") //移除多个样式

					$("#div1").toggleClass("anotherClass") //重复切换anotherClass样式







	三、 绑定click事件：


			给元素绑定click事件，
				$bt1.click(function(){});

			jQuery的click事件
				$('#btn1').click(function(){

				    // 内部的this指的是原生对象

				    // 使用jquery对象用 $(this)  就是 $('#btn1')

				})		


			原生的click事件：
				oBtn1.onclick = function(){};




		获取元素的索引值 ：

			有时候需要获得匹配元素相对于其同胞元素的索引位置，此时可以用index()方法获取；
			索引值是从0开始的

			var $li = $('.list li').eq(1);
			alert($li.index()); // 弹出1
			......
			<ul class="list">
			    <li>1</li>
			    <li>2</li>
			    <li>4</li>
			    <li>5</li>
			    <li>6</li>
			</ul>






	四、 jQuery特殊效果：			

		display:none;  block的切换

		1、 fadeIn()  	// 淡入 		

		2、 fadeOut() 	// 淡出

		3、 fadeToggle()	// 切换淡入淡出

		4、 hide()		// 隐藏元素

		5、 show()		// 显示元素

		6、 toggle()	// 切换元素的可见状态

		7、 slideDown()		//	向下展开

		8、 slideUp()		// 向上卷起

		9、 slideToggle()	// 依次展开或卷起某个元素


			例如：
				    $btn.click(function(){

				        $('#div1').fadeIn(1000,'swing',function(){		// 动画时间、 动画曲线(可写可不写)、 回调函数
				            alert('done!');
				        });

				    });





	五、 jquery链式调用：		（见 层级式菜单 案例）


		jquery对象的方法会在执行完后返回这个jquery对象，所有jquery对象的方法可以连起来写：


		$('#div1').children('ul').slideDown('fast').parent().siblings().children('ul').slideUp('fast')

			$('#div1') // id为div1的元素
			.children('ul') //该元素下面的ul子元素
			.slideDown('fast') //高度从零变到实际高度来显示ul元素
			.parent()  //跳到ul的父元素，也就是id为div1的元素
			.siblings()  //跳到div1元素平级的所有兄弟元素
			.children('ul') //这些兄弟元素中的ul子元素
			.slideUp('fast');  //高度实际高度变换到零来隐藏ul元素


		
		层级式菜单：

				会用到选择集转移
				通过stop() 可以修正反复点击导致的持续动画的bug(具体见实例)


				$('.level1').click(function(){

					// next()选择div元素后面紧挨的同辈元素ul 放下来slideDon; 同时需要把其他的ul卷起来
					// 跳出当前元素a ,返回到父级parent()元素li ，然后选择其他同级元素siblings() 下的子集children('ul')元素ul 卷起来
					// $(this).next().slideDown().parent().siblings().children('ul').slideUp();
					 
					// 如果使用slideToggle() 连续点会出现往返的bug，是因为动画有延迟，所以需要在前面加个 stop()
					$(this).next().stop().slideToggle().parent().siblings().children('ul').slideUp();

				});






	六、 jquery动画:		（见 动画选项卡 案例）

		通过animate方法可以设置元素某属性值上的动画，可以设置一个或多个属性值，动画执行完成后会执行一个函数。

			默认是缓冲运动：
			如果不同时动，可以在回调函数里面写其他的动画方式

				$('#div1').animate({
				    width:'+=100',				// 每点一次加100，带单位需要加引号 ""
				    height:300
				},1000,'swing',function(){
				    alert('done!');
				});





	七、 尺寸相关、 滚动事件： （见 悬顶菜单 案例）


		1、 获取个设置元素的尺寸：

			width() 、 height() 	获取元素width 和 height （获取和设置）
			innerWidth() 、 innerHeight()	包括 padding 的width和height	（只能获取）
			outerWidth() 、 outerHeight() 	包括 padding 和 border 的width和height	(常用，盒子的真实尺寸)
			outerWidth(true) 、 outerHeight(true) 包括padding 和 border 以及 margin的width和height


		2、 获取元素相对页面的绝对位置		（见 购物车 案例）

			offset()

		3、 获取浏览器可视区宽度高度：

			$(window).width();
			$(window).height();

		4、 获取页面文档的宽度高度：

			$(document).width();
			$(document).height();

		5、获取页面滚动距离：

			$(document).scrollTop();  
			$(document).scrollLeft();

		6、 页面滚动事件：（高频触发事件）

			$(window).scroll(function(){  
			    ......  
			})



	八、 jQuery属性操作		(见 手风琴 案例)

		隔行换色可以用到循环

		1、 html() 取出或设置html内容：	同innerHTML ; 
				$('.text').html('<span>添加文字</span>');

		2、 prop() 取出或设置某个属性的值
				$('.images').prop({src:'test.jpg', alt:'test image'});



		对jquery选择的对象集合分别进行操作，需要用到jquery循环操作，此时可以用对象上的each方法

			$(function(){
			    $('.list li').each(function(i){
			        $(this).html(i);
			    })
			})

			......
			<ul class="list">
			    <li></li>
			    <li></li>
			    <li></li>
			    <li></li>
			    <li></li>
			    <li></li>
			</ul>





	九、 jquery事件

			事件函数列表：

				blur() 		元素失去焦点	获得input 元素的value值用 val(); 通常用做验证
				focus()		元素获得焦点	（input框上）
				keyup() 	输入时候	键盘放开立即触发该事件

				click()		鼠标单击

				mouseover()		鼠标进入（进入子元素也触发）	触发很多次
				mouseout()		鼠标离开（离开子元素也触发）

				mouseenter()	鼠标进入（进入子元素不触发）	在元素内操作不会再触发
				mouseleave()	鼠标离开（离开子元素不触发）

				hover()		同时为mouseenter和mouseleave事件指定处理函数
							$('.div1').hover(function(){'移入函数'},function(){'移除函数'});

				ready()		DOM加载完成		$(document).ready(function(){...}); （可以简写）$(function(){...});

				resize()	浏览器窗口的大小发生改变 （绑在windows上） $(window).resize(function(){...});

				scroll()	滚动条的位置发生变化	（绑在windows上） $(window).scroll(function(){...});

				submit()	用户递交form表单	(阻止默认行为，用ajax发送到数据库)


			
			绑定事件的其他方法：（可以同时操作多种事件,事件和事件空格隔开）

				$(function(){
				    $('#div1').bind('mouseover click', function(event) {
				        alert($(this).html());
				    });
				});


			取消绑定事件：

				绑定执行后，在绑定函数内解绑， $(thins).unbind('mouseover');





	十、 事件冒泡： （见 弹窗 事件冒泡 案例）

		什么是事件冒泡：

			在一个对象上触发某类事件（比如单击onclick事件），
			如果此对象定义了此事件的处理程序，那么此事件就会调用这个处理程序，
			如果没有定义此事件处理程序或者事件返回true，那么这个事件会向这个对象的父级对象传播，
			从里到外，直至它被处理（父级对象所有同类事件都将被激活），
			或者它到达了对象层次的最顶层，即document对象（有些浏览器是window）。


		事件冒泡的作用 ：（代理机制）

			事件冒泡允许多个操作被集中处理（把事件处理器添加到一个父级元素上，避免把事件处理器添加到多个子级元素上），
			它还可以让你在对象层的不同级别捕获事件。


			阻止事件冒泡 ：

				事件冒泡机制有时候是不需要的，需要阻止掉，通过 event.stopPropagation() 来阻止，event是事件函数参数；

			阻止默认行为 ：

				event.preventDefault();


		合并阻止操作 ：
			
			实际开发中，一般把阻止冒泡和阻止默认行为合并起来写，合并写法可以用

			return false;	





 	十一、 事件委托：	（见 层级菜单 案例）


 			事件委托就是利用冒泡的原理，把事件加到父级上，通过判断事件来源的子集，执行相应的操作，
 			事件委托首先可以极大减少事件绑定次数，提高性能；其次可以让新加入的子元素也可以拥有相同的操作。

 				// delegate 的第一个参数是 选择器； 第二个参数是 事件； 第三个参数是 函数；
	 			$('.list').delegate('li', 'click', function() {
			        $(this).css({background:'red'});
			    });

	 		如果不是用的代理，当添加元素时，那么添加进去的元素是没有事件的





	 十二、 jquery元素节点操作	 (见 to do list 案例 )

	 			原生的js中很多浏览器不兼容，需要做兼容适配；

	 		1、 创建节点：

	 				a）、 通过 $('#div1').html('<a href="#">链接</a>'); 字符串的方式添加节点性能最高；
	 					（缺点： 会覆盖掉原先的内容，应该先获取原来的内容然后加上新添加的节点内容）

	 				b）、 $a = $('<a>'); 	创建空的元素标签
	 					  

	 				c）、 $a = $('<a href="#">链接</a>');	创建带属性的元素标签


	 		2、 插入节点：

	 				子级：
		 				a）、  $("#div1").append($a); 在元素内部的后面插入新添加的节点内容	（父元素添加子元素）
		 				b）、  $a.appendTo($("#div1")); 把创建的节点内容放到div1 标签内部最后（子元素放到父元素）

		 				c）、  $("#div1").prepend($a); 在元素内部的前面插入新添加的节点内容
		 				d）、  $a.prependTo($("#div1")); 子元素放到父元素内部的前面

		 			同级：（也可以对已有的标签进行位置更改）
		 				e）、  $('#div1').after($a);	在div1后面插入新添加的节点内容，（同级的）
		 				f）、  $a.insertAfter($('#div1')); 把新添加的节点内容添加到div1后面；

		 				g）、  $('#div1').before($a);	在div1前面插入新添加的节点内容，
		 				h）、  $a.insertBefore($('#div1')); 把新添加的节点内容添加到div1前面；



	 		3、 删除节点：

	 				$a.remove();	// 自己删自己，不用通过父类来删除




	 十三、 滚轮事件 与 函数节流


	 	jquery.mousewheel.js

	 		jquery中没有鼠标滚轮事件，原生js中的鼠标滚轮事件不兼容，可以使用jquery的滚轮事件插件	jquery.mousewheel.js
	 		
	 		高频触发事件；

	 		$(window).mousewheel(function(event,dat){...})	// dat值 鼠标向上划为-1 ，向下划为1；

	 	函数节流 ： 解决高频事件的

	 		javascript中有些事件的触发频率非常高，比如onresize事件(jq中是resize)，onmousemove事件(jq中是mousemove)以及上面说的鼠标滚轮事件，
			在短时间内多处触发执行绑定的函数，可以巧妙地使用定时器来减少触发的次数，实现函数节流。

			clearTimeout(timer);			// 函数进去后先清空定时器，然后在触发这样就是200ms之内执行最后一个事件
			timer = setTimeout(function(){...}, 200);	//把滚轮或高频事件放进函数中



		限制显示一屏，用固定定位（fixed），高度100%；


		幻灯片案例：  (见 幻灯片 案例)

			每次滑动只滑动一片，不管中间隔着几个画面；

				第一张放在原始位置，其他的重叠在一起放在右边 （每张图片全部定位）；
				当第一张往左运动时，不管第二张在不在右边，先把第二张放到右边，然后往左移动，占据显示框 1-2
				当第二张往左移动时，不管第四张在不在右边，先把第四张放到右边，然后往左移动，占据显示框 2-4
				当第四张往右移动时，不管第三张在哪里，先把第三张放到左边，然后往右移动； 占据显示框 4-3




	十四、 json

		json 是 JavaScript Object Notation的首字母缩写，单词的意思是javascript对象表示法，这里说的json指的是类似于JavaScript对象的一种数据格式；
		目前这种数据类型比较流行，逐渐替换掉了传统的xml数据格式。

			javascript自定义对象： 
				var oMan = {
				    name:'tom',
				    age:16,
				    talk:function(s){
				        alert('我会说'+s);
				    }
				}


			json格式的数据：
				{
				    "name":"tom",
				    "age":18
				}

		与javascript对象不同的是，json数据格式的属性名称和字符串值需要用双引号引起来，用单引号或者不用引号会导致读取数据错误。


		json的另外一个数据格式是数组，和javascript中的数组字面量相同

			["tom",18,"programmer"]






	十四、 ajax 和 jsonp

		安全性： js不能读写文件；

		ajax 技术的目的是让javascript发送http请求，与后台通信，获取数据和信息。  跳过了浏览器的地址栏，自己就可以发送

		ajax技术的原理是实例化xmlhttp对象，使用此对象与后台通信。

		ajax通信的过程不会影响后续javascript的执行，从而实现异步。


		同步和异步:
			现实生活中，同步指的是同时做几件事情，异步指的是做完一件事后再做另外一件事，
			程序中的同步和异步是把现实生活中的概念对调，也就是程序中的异步指的是现实生活中的同步，程序中的同步指的是现实生活中的异步。

		局部刷新和无刷新 ：
			ajax可以实现局部刷新，也叫做无刷新，无刷新指的是整个页面不刷新，只是局部刷新，
			ajax可以自己发送http请求，不用通过浏览器的地址栏，所以页面整体不会刷新，
			ajax获取到后台数据，更新页面显示数据的部分，就做到了页面局部刷新。

		同源策略：
			ajax请求的页面或资源只能是同一个域下面的资源，不能是其他域的资源，这是在设计ajax时基于安全的考虑。



		$.ajax使用方法 ：

			$.ajax({
				// 参数
			    url: 'js/data.json',
			    type: 'GET',
			    dataType: 'json',
			    data:{'aa':1}
			})	// 不要加; 是紧接在后面调用的
			// 成功时的回调函数
			.done(function(data) {
			    alert(data.name);
			})
			// 失败的回调函数
			.fail(function() {
			    alert('服务器超时，请重试！');
			});

			常用参数：

				1、 url请求地址； 

				2、 type 请求方式， 默认是'get', 常用的还有'post';

				3、 dataType 设置返回的数据格式，常用的是'json'格式，也可以设置为'html'；

				4、 data 设置发送给服务器的数据；

				5、 success 设置请求成功后的回调函数；

				6、 error 设置请求失败后的回调函数；

				7、 async 设置是否异步，默认值是'true'，表示异步；



		jsonp 

			ajax只能请求同一个域下的数据或资源，有时候需要跨域请求数据，就需要用到jsonp技术，

			jsonp可以跨域请求数据，它的原理主要是利用了<script>标签可以跨域链接资源的特性。jsonp和ajax原理完全不一样，不过jquery将它们封装成同一个函数。


				$.ajax({
				    url:'js/data.js',
				    type:'get',
				    dataType:'jsonp',
				    jsonpCallback:'fnBack'
				})
				.done(function(data){
				    alert(data.name);
				})
				.fail(function() {
				    alert('服务器超时，请重试！');
				});

				// data.js里面的数据： fnBack({"name":"tom","age":18});



			empty() 清空元素；




	十五、 本地存储

		本地存储分为cookie，以及新增的localStorage和sessionStorage

		1、 cookie 存储在本地，容量最大4K ，在同源的http请求时携带传递，损耗带宽，可设置访问路径，只有此路径及此路径的子路径才能访问此cookie，在设置的过期时间之前有效

				引用插件 库 ： jquery.cookie.js

				jquery 设置cookie
					$.cookie('mycookie','123',{expires:7,path:'/'});		// 名称， 值， 设置参数
				jquery 获取cookie
					$.cookie('mycookie');

				只弹一次的弹框（见  弹一次弹框 案例）


		2、	localStorage 存储在本地，容量为5M或者更大，不会在请求时候携带传递，在所有同源窗口中共享，数据一直有效，除非人为删除，可作为长期数据。
			(H5新增的属性，不需要依赖jquery, 可以直接写)

				//设置：
				localStorage.setItem("dat", "456");
				localStorage.dat = '456';

				//获取：
				localStorage.getItem("dat");
				localStorage.dat

				//删除
				localStorage.removeItem("dat");


		3、  sessionStorage 存储在本地，容量为5M或者更大，不会在请求时候携带传递，在同源的当前窗口关闭前有效。(H5新增的属性，不需要依赖jquery, 可以直接写)


				localStorage 和 sessionStorage 合称为Web Storage , 
				Web Storage支持事件通知机制，可以将数据更新的通知监听者，Web Storage的api接口使用更方便。

				iPhone的无痕浏览不支持Web Storage，只能用cookie。






	十六、 jqueryUI   插件


		jQuery UI是以 jQuery 为基础的代码库。包含底层用户交互、动画、特效和可更换主题的可视控件。

		我们可以直接用它来构建具有很好交互性的web应用程序。


			插件：  jquery-ui.min.js 


			拖拽： 
				 $('.box').draggable({
					// 限制在x轴
					axis:'x',
					// 限制范围， 只能在父级拖动
					containment:'parent',
					// 拖动时透明值
					opacity:0.6,
					// 设置效果，ev是对象，ui是偏移值等等其他效果
					drag:function(ev,ui){
						// 拖拽的值
						$('.slide_count').val(parseInt(ui.position.left*100/600));
						// 拖拽后的样式
						$('.progress').css({width:ui.position.left});

					}
				})


			