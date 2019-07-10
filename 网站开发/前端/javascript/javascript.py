
javascript

	运行在浏览器端的脚本语言，
	JavaScript主要解决的是前端与用户交互的问题，包括使用交互与数据交互；
	JavaScript是浏览器解释执行的，不需要编译；

	组成：
	 1、 ECMAscript javascript的语法(变量、 函数、 循环语句等语法) ： 按照这个语法规范来实现的
	 2、 DOM (Document Object Model)文档对象模型 ： 操作html和css的方法 （document.getElementById()）
	 3、 BOM (Browser Object Model)浏览器对象模型:  操作浏览器的方法 （alert() 定时器等）


	前端三大块 ：

		1）、HTML：页面结构
		2）、CSS：页面表现：元素大小、颜色、位置、隐藏或显示、部分动画效果
		3）、JavaScript：页面行为：部分动画效果、页面与用户的交互、页面功能


	JavaScript嵌入页面的方式：

		1、行间事件（主要用于事件）：
			<input type="button" name="" onclick="alert('ok！');">

		2、 页面script标签嵌入：
			<script type="text/javascript">        
			    alert('ok！');
			</script>

		3、 外部引入：
			<script type="text/javascript" src="js/index.js"></script>



	一、变量：

		1、javascript的变量类型由它的值来决定。 定义变量需要用关键字 'var'；
			同时定义多个变量可以用","隔开，公用一个‘var’关键字

				var iNum = 123, sTr='qwe', sCount='68';

		
		2、变量类型:
			5种基本数据类型：
				1）、number 数字类型
				2）、string 字符串类型
				3）、boolean 布尔类型 true 或 false
				4）、undefined undefined类型，变量声明未初始化，它的值就是undefined
				5）、null null类型，表示空对象，如果定义的变量将来准备保存对象，
					可以将变量初始化为null,在页面上获取不到对象，返回的值就是null

			1种复合类型：
				object


		3、变量、函数、属性、函数参数命名规范

			1）、区分大小写
			2）、第一个字符必须是字母、下划线（_）或者美元符号（$）
			3）、其他字符可以是字母、下划线、美元符或数字


		4、匈牙利命名风格：

			对象o Object 		比如：oDiv
			数组a Array  		比如：aItems
			字符串s String		比如：sUserName
			整数i Integer  	 	比如：iItemCount
			布尔值b Boolean  	比如：bIsComplete
			浮点数f Float  		比如：fPrice
			函数fn Function	 	比如：fnHandler
			正则表达式re RegExp 比如：reEmailCheck


		5、javascript语句与注释：

			1）、一条javascript语句应该以“;”结尾；
			2）、javascript注释
				单行注释：  //
				多行注释： /*   */





	二、获取元素方法：


		可以操作html对象， 操作html的API

		方法1：
			可以使用内置对象 document上的getElementById() 方法来获取页面上设置了id属性的元素，
			获取到的是一个html对象，然后将它赋值给一个变量
			ID是给js用的，所以一般不会给样式使用

				document.getElementById('div1').style.color = 'red';

			通常在<head></head>中嵌入js文件，默认直接写(如上)是不会被执行的，因为html运行是有顺序的，从上往下
			javascript去页面上获取元素div1的时候，元素div1还没有加载；如果需要执行，需要添加函数把上面的语句包含住

				第一种方法：将javascript语句放到 window.onload(触发的函数里面),获取元素的语句会在页面加载完后才执行。

					window.onload = function(){		
						/*
						document.getElementById('test').style.color = 'red';
						document.getElementById('test').style.fontSize = "30px";
						document.getElementById('test').style.padding = "20px";
						*/
						
						// 用变量简化代码
						var oTest = document.getElementById('test');
						var sStyle = oTest.style 	
						sStyle.color = 'red';
						sStyle.fontSize = "30px";
						sStyle.padding = "20px";

					}

				第二种方法：将javascript放到页面最下边。


			JS中的CSS样式中包含-属性的需要换成驼峰写法，JS不识别包含-样式的属性
			比如: 
				document.getElementById('div1').style.font-size = '30px';		// 错误的写法；识别不了
				document.getElementById('div1').style.fontSize = '30px';		// 正确的写法；


		方法2：

			可以使用内置对象 document上的getElementsByTagName()方法来获取页面上的某一种标签，
			获取的是一个选择集，不是数组，但是可以用下标的方式操作选择集里面的标签元素。

			
			通过标签获取元素

				<script type="text/javascript">
				    window.onload = function(){
				   		var oUl = document.getElementById('list1')
				        var aLi = oUl.getElementsByTagName('li');		// document是整个文档，oUl是取id值为 list1 的标签元素
				        // aLi.style.backgroundColor = 'gold'; // 出错！不能同时设置多个li
				        alert(aLi.length);
				        aLi[0].style.backgroundColor = 'gold';
				    }
				</script>




	三、 操作元素属性：

		获取的页面元素，就可以对页面元素的属性进行操作，属性的操作包括属性的读和写。

		1、操作属性的方法 
			1）、“.” 操作
			2）、“[ ]”操作 ; 如果把属性定义为一个变量，那么读写的时候用[] 
							 例如：var sMystyle = 'color'   oTest.style[sMystyle] = 'red'

		2、属性写法
			1）、html的属性和js里面属性写法一样
			2）、“class” 属性写成 “className”	 	oTest.className = "box2"	
			3）、“style” 属性里面的属性，有横杠的改成驼峰式，比如：“font-size”，改成”style.fontSize”

		3、innerHTML 
			innerHTML可以读取或者写入标签包裹的内容; 带有格式的会自动转换
			oTest.innerHTML = "<a href='http://www.dzfong.cn'>竹风</a>"




	四、 函数：

		函数就是重复执行的代码片。
		JavaScript解析过程分为两个阶段，先是编译阶段，然后执行阶段

		在编译阶段会将function定义的函数提前，并且将var定义的变量声明提前，将它赋值为undefined；
			预解析会把变量的声明提前，但是不会初始化(不会先赋值，值是undefind), 如果未声明的变量会出错，下面的会不执行
			预解析会让函数的声明和定义提前，（一般公共函数可以放到最后去声明定义）


			函数定义与执行：
				<script type="text/javascript">
				    // 函数定义
				    function fnAlert(){
				        alert('hello!');
				    }
				    // 函数执行
				    fnAlert();
				</script>

		
			提取行间事件：
				<script type="text/javascript">
					window.onload = function(){
						// 执行函数
						var oBtn = document.getElementById('btn');
						// 将事件属性和一个函数关联，函数不能写小括号，写了会马上执行
						oBtn.onclick = fnChange;
					}

					// 定义函数
					function fnChange(){
						var oDiv = document.getElementById('func');
						oDiv.style.color = "gold";
						oDiv.style.fontSize = '30px'
						oDiv.style.padding = "20px";
					}
				</script>



		匿名函数: 只为某一个属性做事件，不是公共的函数
				# 将上面的函数可以转换为匿名函数; 
				<script type="text/javascript">

					window.onload = function(){
						var oBtn = document.getElementById('btn');

						oBtn.onclick = function(){
						var oDiv = document.getElementById('func');
						oDiv.style.color = "gold";
						oDiv.style.fontSize = '30px'
						oDiv.style.padding = "20px";
						};
					}

				</script>


		
			网页换肤： 通过改变样式来达到换肤，操作link的href属性



		函数传参：

			    function fnChangeStyle(myid, mystyle, val){		// mystyle, val 是形参
			        var oDiv = document.getElementById(myid);
			        oDiv.style[mystyle] = val;					// 自定义的属性需要用[]
			    }
			    fnChangeStyle('div1','fontSize', '30px');			// 实参 , 
			    fnChangeStyle('div1','backgroundColor', 'pink')		// 这里也可以写成  'background-color'


		函数返回值：  return

			作用：
				1）、返回函数执行的结果
				2）、结束函数的运行
				3）、阻止默认行为			return false;


			    function fnAlert(a, b){
			    	var	c = a + b ;
			        return(c);
			        alert("aaaa");			// 这句不执行 ，上面的return就已经返回了结束啦
			    }    
			    var iResult = fnAlert(12, 34);
			    alert(iResult);


	五、 条件语句 

		通过条件来控制程序的走向，就需要用到条件语句。

		
		运算符 ：
			1、算术运算符： +(加)、 -(减)、 *(乘)、 /(除)、 %(求余)
			2、赋值运算符：=、 +=、 -=、 *=、 /=、 %= 、 ++ (+1) 、
			3、条件运算符：==(先类型转换再判断)、===(先判断类型)、>、>=、<、<=、!=、&&(而且)、||(或者)、!(否，取反)

		
		if else

			制作单个按钮点击切换元素的显示和隐藏效果

			默认的会先去行间里面取样式，如果行间距没有定义，那么取到的是空值，所以在判断的时候需要加上空条件

				var oBtn = document.getElementById('btn');
				var oDiv = document.getElementById('div1')

				oBtn.onclick = function(){
					if(oDiv.style.display=='block'||oDiv.style.display==''){	// 行间距没设，所以取到的是空值
						oDiv.style.display = 'none';
					}
					else{
						oDiv.style.display = 'block';
					}
				}



		多重if else条件语句

				if(){

				}
				else if(){

				}
				else{

				}


		switch语句：

			多重if else语句可以换成性能更高的switch语句

				var iNow = 1;
				switch (iNow){
				    case 1:
				        ...;
				        break;			// 结束当前的运行
				    case 2:
				        ...;
				        break;    
				    default:			// 前面的条件都不满足的
				        ...;
				}




		字符转整形：  pareseInt(oInput01.value)




	六、 数组

		数组就是一组数据的集合，javascript中，数组里面的数据可以是不同类型的。

		1）、 定义数组的方法：

			//对象的实例创建 （类实例化）
			var aList = new Array(1,2,3);

			//直接量创建	
			var aList2 = [1,2,3,'asd'];


		2）、 操作数组中数据的方法 

			a、 获取数组的长度（成员个数）：	aList.length；
					var aList = [1,2,3,4];
					alert(aList.length); // 弹出4

			b、 用下标操作数组的某个数据：	aList[0];
					var aList = [1,2,3,4];
					alert(aList[0]); // 弹出1

			c、 join() 将数组成员通过一个分隔符合并成字符串：数组本身不会发生变化，会返回一个字符串	
					var aList = [1,2,3,4];
					alert(aList.join('-')); // 弹出 1-2-3-4

			d、 push() 和 pop() 从数组最后增加成员或删除成员
					var aList = [1,2,3,4];
					aList.push(5);
					alert(aList); //弹出1,2,3,4,5
					aList.pop();
					alert(aList); // 弹出1,2,3,4

			e、 unshift()和 shift() 从数组前面增加成员或删除成员

			f、 reverse() 将数组反转
					var aList = [1,2,3,4];
					aList.reverse();
					alert(aList);  // 弹出4,3,2,1

			g、 indexOf() 返回数组中元素第一次出现的索引值
					var aList = [1,2,3,4,1,3,4];
					alert(aList.indexOf(1));// 弹出0 

			h、 splice() 在数组中增加或删除成员
				第一个参数是开始的位置，第二个参数是从起始位置删除多少个成员，第三个之后(包含第三个)是要增加的成员的值
					var aList = [1,2,3,4];
					aList.splice(2,1,7,8,9); //从第2个元素开始，删除1个元素，然后在此位置增加'7,8,9'三个元素
					alert(aList); //弹出 1,2,7,8,9,4


		3）、 多维数组：

			多维数组指的是数组的成员也是数组的数组。

					var aList = [[1,2,3],['a','b','c']];	//二维数组

					alert(aList[0][1]); //弹出2;


	七、 循环语句 

		不同于python, python中常用 while 循环， js经常用for 循环

			for 循环：

				var aList = ['a', 'b', 'c', 'd', 'e'];
				var iLen = aList.length;

				for(var i=0; i<iLen; i++){
					alert(aList[i]);
				}

			while 循环：

				var i=0;
				while(i<8){
					......
					i++;
				}


			数组去重：

				var aList = [1,2,3,4,4,3,2,1,2,3,4,5,6,5,5,3,3,4,2,1];
				var aList2 = [];
				var iLen = aList.length;

				//aList[i]是数组的值，然后通过indexOf取这个值的下标，
				//如果这个下标=i 就不是重复数

				for(var i=0; i<iLen; i++){

				    if(aList.indexOf(aList[i])==i){	
				        aList2.push(aList[i]);
				    }
				}

				alert(aList2);





	八、 字符串处理方法：

		js针对字符串操作不是太多，后台操作字符串比较强，一般都是后台处理干净才传给前端

			1、 字符串合并操作：“ + ”

			2、 parseInt() 将数字字符串转化为整数

			3、parseFloat() 将数字字符串转化为小数

			4、split() 把一个字符串分隔成字符串组成的数组

			5、charAt() 获取字符串中的某一个字符

			6、indexOf() 查找字符串是否含有某字符		// 不存在则返回 -1  ；

			7、substring() 截取字符串 用法： substring(start,end)  // 不包括end , 如果括号内只有1个参数，那么就是从这个数到末尾

			8、toUpperCase() 字符串转大写		// 不会改变本身，有返回值

			9、toLowerCase() 字符串转小写		// 不会改变本身，有返回值


		字符串反转：

			var str = 'asdfj12jlsdkf098';
			var str2 = str.split('').reverse().join('');	//把字符串转成数组，数组反转，然后把数组元素拼接成字符串




	九、 定时器

		作用：
			1、 制作动画 
			2、 异步操作
			3、 函数缓冲与节流


			定时器：
				1、 只执行一次的定时器：  	setTimeout()   、  关闭只执行一次的定时器： 	clearTimeout
				2、 反复执行的定时器： 		setInterval()  、  关闭反复执行的定时器： 	clearInterval

					function myalert(){
						alert('hello world!');
					}

					// 只执行一次的定时器，第一个参数是函数名，或者是匿名函数，第二个参数是时间，单位默认是ms
					// 赋值给变量 同样会执行
					var timer01 = setTimeout(myalert, 2000);

					// 关闭只执行一次的定时器
					clearTimeout(timer01);			// 由于关闭了，所以不会执行上面的定时器


			动画的时间30ms 是最佳时间


			无缝滚动： 把图片放在一个ul里，然后复制一个ul 拼接起来。让ul滚动


			制作时钟：  从0到6 ，而且是阿拉伯数字；
						月份是从0到11, 0表示1月份；
						定义函数星期的阿拉伯数字改成大写；
						定义函数把小时、分钟、秒钟 单数变双数；
						需要反复执行的， 封装在一个函数内；
						重复执行的函数先调用一次， 如果不调用，默认的会等待一秒钟，才会调用；
						设置反复执行的定时器，一秒钟刷新一次；



			倒计时：


	


	十、 变量作用域：

		变量作用域指的是变量的作用范围，javascript中的变量分为全局变量和局部变量。

		1、全局变量：在函数之外定义的变量，为整个页面公用，函数内部外部都可以访问。
		2、局部变量：在函数内部定义的变量，只能在定义该变量的函数内部访问，外部无法访问。





	十一、 封闭函数：

		封闭函数是javascript中匿名函数的另外一种写法，创建一个一开始就执行而不用命名的函数。

		封闭函数的好处 
			封闭函数可以创造一个独立的空间，在封闭函数内定义的变量和函数不会影响外部同名的函数和变量，
			可以避免命名冲突，在页面上引入多个js文件时，用这种方式添加js文件比较安全。


			定义函数和执行函数：

				function myalert(){
				    alert('hello!');
				};
				myalert();


			封闭函数：()()

				(function myalert(){
				    alert('hello!');
				})();


			通常在开发中，后期添加js ，可以用封闭函数，不会改变其他变量，只在自己定义的函数中起效果


			封闭函数第二种写法：在函数定义前加上“~”和“!”等符号来定义匿名函数

				!function myalert(){
				    alert('hello!');
				}()

				~function myalert(){
				    alert('hello!');
				}()


			在封闭函数前加“ ; ” 防止js压缩成一行时出错。



	十二、 常用内置对象

		1、 document 

			document.getElementById  // 通过id获取元素
			document.getElementsByTagName 	// 通过标签名获取元素
			document.referrer			// 获取上一个跳转页面的地址(需要服务器环境)  var sUrl = document.referrer


		2、 location 

			window.location.href 	// 获取或重定url地址  window.location.href = sUrl
			window.location.search 	// 获取地址参数部分 (?)	var sSearch = window.location.search
			window.location.hash	// 获取页面锚点或叫哈希值 (#) 

		3、 Math

			Math.random()   // 获取0-1的随机数, 不包含1
			Math.floor()	// 向下取整 ; 直接去掉小数	5.6 ---》 5
			Math.ceil()		// 向上取整 ；整体 + 1 		5.2 ---》 6

			
			例： 取10-20的随机数:
				var iN01 = 10;
				var iN02 = 20;
				var arr2 = [];
				for(var i=0;i<40;i++){
					var iNum02 = Math.floor((iN02-iN01+1)*Math.random()) + iN01;
					arr2.push(iNum02);
				} 
				console.log(arr2);




	十三、 调试程序


		1、 alert()		：  直接弹窗

		2、 console.log()  :  在浏览器的---检查-- console 里面看

		3、 document.title() :	改变 <title> 的值






	案例见： csstest.html











				


