


CSS

	css是 Cascading Style Sheets 的首字母缩写，意思是层叠样式表；
	有了CSS，html中大部分表现样式的标签就废弃不用了，html只负责文档的结构和内容，表现形式完全交给CSS，html文档变得更加简洁。
	下面的样式会把上面的样式给覆盖，这是层叠样式表的特性

	
	一些标签会有样式，通常会把这些样式重置，在样式表前重新定义  （用到的标签就写，没用到的不要写，会影响资源）
		body,p,h1,h2,h3,h4,h5,h6,ul,dl,dt,form,input{ margin:0; padding:0}		# 去间距
		ul{ list-style: none}		# 去掉默认的小圆点
		a{ text-decoration:none }	# 去掉默认的下划线
		em{ font-style:normal }		# 设置不倾斜
		img{ border:0 }				# 去掉在IE下图片做链接时会默认生成1px的边框
		h1,h2,h3,h4,h5,h6{ font-size:100% }	# 让h标签继承body中的字体大小的设置
		/* 公共的类 */
		.clearfix:before,.clearfix:after{ content:""; display:table; }		# 清除浮动、解决margin-top 塌陷
		.clearfix:after{ clear:both; }		# 清除浮动
		.clearfix{ zoom:1 }			# IE兼容
		.fl{ float:left }			# 左浮动
		.fr{ float:right }			# 右浮动


	CSS样式的引用是有顺序的，后引进的会覆盖先引进的


	权重：

			1、!important，加在样式属性值后，权重值为 10000
			2、内联样式，如：style=""，权重值为 1000
			3、ID选择器，如：#content，权重值为100
			4、类，伪类和属性选择器，如： content、:hover 权重值为 10
			5、标签选择器和伪元素选择器，如：div、p、:before 权重值为 1
			6、通用选择器（*）、子选择器（>）、相邻选择器（+）、同胞选择器（~）、权重值为 0




	注释：
		/*
				css注释 
		*/
	




	1、css 定义方法：
	
		选择器 { 属性:值; 属性:值; 属性:值 }

			div {
				font-size:20px;
				color:red;
			}





	
	2、css页面引入方式：
	
		1）、 外联式 ： 通过 link 标签， 链接外部样式表到页面中		(常用的)
		
			<link rel="stylesheet" type="text/css" href="css/style.css">

			
		2）、 嵌入式 ： 通过 style 标签， 在网页上创建嵌入的样式表	（部分首页使用，做性能优化）
			一般放在 <head></head>标签内

			<head>
				<style type="text/css">
					div{
						 width:100px;
						 height:100px;
						 color:red
					} 
					...
				</style>
			</head>


		3）、 内嵌式 ： 通过标签的style属性，在标签上直接写样式。	（不常用，比较乱）

			<div style="width:100px; height:100px;color:red"> ... </div>






	3、常用的样式：


		1）、 color: 设置文字的颜色。 如： color:red; 

				颜色的3种表示方法：
					a、 颜色名表示： red  gold
					b、 rgb表示：红绿蓝色的光，255是最大值  rgb(255,0,0) 表示红色
					c、 16进制数值表示： #ff0000 表示红色，也可写成 #f00


		2）、 font-size: 设置文字的大小 (默认的是16px)。 如: font-size:12px;	

		3）、 font-family: 设置文字的字体(通常用英文,中文容易乱码)。 如：font-family:'微软雅黑';  font-family:'Microsoft Yahei';

		4）、 font-style: 设置文字是否倾斜(通常把倾斜的变不倾斜，用倾斜)。 如： font-style:normal; 不倾斜； font-style:italic; 倾斜

		5）、 font-weight: 设置文字是否加粗(把加粗的变不加粗)。 如： font-weight:bold; 加粗； font-weight:normal; 不加粗

		6）、 line-height: 设置文字的行高(只针对文字，其他不行)，设置行高相当于在每行文字的上下同时加间距。 如： line-height:24px;

		7）、 font: 同时设置文字的几个属性，写的顺序有兼容问题，建议按照如下顺序写：
					是否加粗、字号/行高、字体		
					如： font:normal 12px/36px 'Microsoft Yahei';

		8）、 text-decoration: 设置文字的下划线的(通常把下划线的设为没有)。	如： text-decoration:underline;下划线  none去掉下划线

		9）、 text-indent: 设置文字首行缩进(通过CSS设置的，缩进只针对首行)。 如： text-indent:24px; 缩进了2个字符，12px的字体

		10）、 text-align: 设置文字水平对齐方式(left/ center/ right; 针对于元素的宽度)。 如： text-align:center 文字水平居中 







	4、 CSS选择器：

		选择器是一种模式，用于选择需要添加样式的元素。

		1）、 标签选择器：

			标签选择器，此种选择器影响范围大，建议尽量应用在层级选择器中;
			在css中直接用标签名定义， 在body中直接引用
			* 星标签是给所有的标签设置样式
				*{
					font-size:20px;
				}


		2）、 id 选择器：（基本上不用）

			id 是所有标签的属性
			通过id名来选择元素，元素的id名不能重复，所以一个样式设置项只能对应于页面上一个元素，不能复用，
			在css中用 #idname 定义 ， 在div中用id='idname'调用
			id名一般给程序使用，所以不推荐使用id作为选择器。

				#div{
					color:blue;
				}
				<div id='div1'> 这是第一个div </div>

		
		3）、 类选择器：（最常用）

			通过类名来选择元素，一个类可应用于多个元素，一个元素上也可以使用多个类，应用灵活，可复用，
			在css中用 .classname 定义，  在div中用 class='classname' 调用,可以同时调用多个样式
			是css中应用最多的一种选择器。
				.green{color:green}
				.big{font-size:40px}
				<div class="big green"> 这是第一个div</div>



		4）、 层级选择器： （经常用的）

			主要应用在选择父元素下的子元素，或者子元素下面的子元素，可与标签元素结合使用，减少命名，
			同时也可以通过层级，防止命名冲突。
			通常结合标签和类选择器使用
			在css中用 .classname 标签名 定义。 在div中用 class='classname' 调用,可以同时调用多个样式
			层级选择器不要超过4层
				.search-bd .search-triggers .tmall-search-tab .selected{
					background-color: #c60000;
				}


		5）、 组选择器：

			多个选择器，如果有同样的样式设置，可以使用组选择器。
			多个选择器，用 逗号(,) 分开，用空格的是 层级选择器。
				.box1,.box2,.box3{width:100px;height:100px}
				.box1{background:red}
				.box2{background:pink}
				.box2{background:gold}

				<div class="box1">....</div>
				<div class="box2">....</div>
				<div class="box3">....</div>



		6）、 伪类及伪元素选择器:

			常用的伪类选择器有 hover(通常用在链接响应的时候)，表示鼠标悬浮在元素上时的状态;  
			伪元素选择器有 before和after(解决样式的bug会用到),它们可以通过样式在元素中插入内容，插入的内容是不可选的
					.box1:hover{ color:red } 		# 鼠标放上去的状态 
					.box2:before{content:'行首文字';color:red;}		# 在box2的文本前面插入一些文字，是选不中的
					.box3:after{content:'行尾文字';}		#	在box3的文本后面添加一些文字，也是不可选的






	5、 css盒子模型：

		元素(也叫标签)在页面中显示成一个方块，类似一个盒子，CSS盒子(平面的)模型就是使用现实中盒子来做比喻，帮助我们设置元素对应的样式。
		布局模型

		把元素叫做盒子，设置对应的样式分别为：
			盒子的内容(content)：
			盒子的宽度(width)： 设置盒子的宽度，此宽度是指盒子内容的宽度，不是盒子整体宽度
			盒子的高度(height)：设置盒子的高度，此高度是指盒子内容的高度，不是盒子整体高度
			盒子内的内容和边框之间的间距(padding)：  内间距内填充：padding-top /  padding-right /  padding-bottom / padding-left 
			盒子的边框(border)： 边框
			盒子与盒子之间的间距(margin)： 外间距：块与块之间的间距


				+-----------------------------------------------------------+
				|															|	
				|						margin-top							|			
				|		 _________________________________________			|							
				|		!										  !			|
				|		!				border-top				  !			|
				|		!		+=========================+	  	  !			|
				|		!		|		padding-top		  |		  !			|
				|margin-!		|		_____________ 	  |	  	  ！margin- |
				|left 	!border-|padd 	!			 !padd|border-! right   |
				|		!left 	|ing-	!	content	 !ing-|right  !			|
				|		!		|left 	!			 !left|		  !			|
				|		!		|		!____________!	  |   	  !			|
				|		!		|						  |		  !			|
				|		!		|		padding-bottom	  |		  !			|
				|		!		+=========================+       !			|
				|		!										  !			|
				|		!				border-bottom    		  !			|
				|		!_________________________________________!			|
				|															|
				|						margin-bottom						|
				+-----------------------------------------------------------+


				padding：20px 40px 0 30px;	/* 四个值按照顺时针方向，分别设置的是 上 右 下 左 ； 0表示没有值，单位可以不写 */		
				padding：20px 40px 50px; 		/* 三个值设置顶部内边距为20px，左右内边距为40px，底部内边距为50px */
				padding：20px 40px; 			/* 二个值设置上下内边距为20px，左右内边距为40px */
				padding：20px;					/* 一个值设置四边内边距为20px */ 

			margin 外边距的设置方法和padding的设置方法相同,将上面设置项中的'padding'换成'margin'就是外边距设置方法 

				border-top-color:red;    /* 设置顶部边框颜色为红色 */  
				border-top-width:10px;   /* 设置顶部边框粗细为10px */   
				border-top-style:solid;  /* 设置顶部边框的线性为实线, 实线：solid ；虚线：dashed; 点线：dotted */

			上面三句可以简写成一句：
			
				border-top:10px solid red;	/* 属性无顺序要求，是乱序的 , 中间是没有逗号的，用空格区分*/	

				border-radius: 14px;		/* 设置圆角 14px为半径 */

			四个边如果设置一样，可以将四个边的设置合并成一句：

				border:10px solid red;	

			盒子宽度 = width + padding左右 + border左右
			盒子高度 = height + padding上下 + border上下



		技巧：

			1）、margin 技巧:
				a、 设置元素水平居中： margin:x auto;	/* margin: 50px auto 60px   垂直是没有auto属性的*/
				b、 margin负值让元素位移及边框合并	/* body自带有8px的margin */

			2）、垂直外边距合并
				指的是，当两个垂直外边距相遇时，它们将形成一个外边距。（垂直外边距合并，左右外边距是不会合并的）
				合并后的外边距的高度等于两个发生合并的外边距的高度中的较大者。
					例如：  box1的margin-bottom：30px; 
					   		box2的margin-top: 20px;
					   	那么他们的外边距不是50px,而是取最大的那个30px;
					解决方式：
						a、 使用这种特性；(布局效果，上下合并 空出间距)
						b、 设置一边的外边距，一般设置margin-top;	（开发中常用）
						c、 将元素浮动或者定位

			3）、margin-top 塌陷
				在两个盒子嵌套时候，内部的盒子设置的margin-top会加到外边的盒子上，导致内部的盒子margin-top设置失败
					解决方法：
						a、 外部的盒子设置一个边框；	/*	border:1px solid black; */
						b、 外部盒子设置 属性：overflow:hidden	 /* 元素溢出；overflow:hidden; css的黑魔法  */
						c、 使用伪元素类：	/*  clearfix约定俗成的类。 */	(常用的方法)
							.clearfix:before{ content:""; display:table;}
							引用： class="外部盒子类 clearfix"



		css元素溢出：

			当子元素的尺寸超过父元素的尺寸时，需要设置父元素显示溢出的子元素的方式，设置的方法是通过overflow属性来设置。

			设置项：

				1）、 visible (默认值)。内容不会被修剪，会呈现在元素框之外。
				2）、 hidden (内容会被修剪)，并且其余内容是不可见的，此属性还有清除浮动、清除margin-top塌陷的功能。
				3）、 scroll (内容会被修剪)，但是浏览器会显示滚动条以便查看其余的内容。
				4）、 auto (如果内容被修剪)，则浏览器会显示滚动条以便查看其余的内容。
				5）、 inherit (继承父元素 overflow 属性的值)。




	6、块元素、内联元素、内联块元素

		元素就是标签，布局中常用的有三种标签，块元素、内联元素、内联块元素，了解这三种元素的特性，才能熟练的进行页面布局。

		1）、块元素 
			块元素，也可以称为行元素，布局中常用的标签如：div、p、ul、li、h1~h6、dl、dt、dd等等都是块元素

			它在布局中的行为：（特点）
				支持全部的样式
				如果没有设置宽度，默认的宽度为父级宽度100%	（不需要设宽度）
				盒子占据一行、即使设置了宽度 （换行）

		2）、内联元素
			内联元素，也可以称为行内元素，布局中常用的标签如：a、span、em、b、strong、i等等都是内联元素

			它们在布局中的行为：（特点）
				支持部分样式（不支持宽、高、margin上下、padding上下;左右是有的）
				宽高由内容决定	
				盒子并在一行
				代码换行，盒子之间会产生间距
				子元素是内联元素，父元素可以用text-align属性设置子元素水平对齐方式

				解决内联元素间隙的方法：
					a、去掉内联元素之间的换行
					b、将内联元素的父级设置font-size为0，内联元素自身再设置font-size

		3）、 内联块元素
			内联块元素，也叫行内块元素，是新增的元素类型，现有元素没有归于此类别的，
			img和input元素的行为类似这种元素，但是也归类于内联元素，
			我们可以用display属性将块元素或者内联元素转化成这种元素。

			在布局中表现的行为：
					支持全部样式
					如果没有设置宽高，宽高由内容决定
					盒子并在一行
					代码换行，盒子会产生间距 (同内联元素的解决方法)
					子元素是内联块元素，父元素可以用text-align属性设置子元素水平对齐方式。


		这三种元素，可以通过display属性来相互转化，
		不过实际开发中，块元素用得比较多，
		所以我们经常把内联元素转化为块元素，少量转化为内联块，
		而要使用内联元素时，直接使用内联元素，而不用块元素转化了。

			display属性：
				1）、none 元素隐藏且不占位置, (元素隐藏起来)
				2）、block 元素以块元素显示
				3）、inline 元素以内联元素显示
				4）、inline-block 元素以内联块元素显示




	7、 浮动

		浮动特性：
			1）、浮动元素有左浮动(float:left)和右浮动(float:right)两种

			2）、浮动的元素会向左或向右浮动，碰到父元素边界、其他元素才停下来

			3）、相邻浮动的块元素可以并在一行，超出父级宽度就换行

			4）、浮动让行内元素或块元素自动转化为行内块元素(此时不会有行内块元素间隙问题)

			5）、浮动元素后面没有浮动的元素会占据浮动元素的位置，没有浮动的元素内的文字会避开浮动的元素，形成文字饶图的效果

			6）、父元素如果没有设置尺寸(一般是高度不设置)，父元素内整体浮动的元素无法撑开父元素，父元素需要清除浮动

			7）、浮动元素之间没有垂直margin的合并	


			通常菜单都是由列表制作 ul+li 构造的			快捷键： ul.menu>(li>a{公司简介})*7  按tab键

				list-style:none；/* 去掉 li 的圆点 */   或者把全局字体设为0 ，然后在元素自定义字体大小


			清除浮动： 父元素如果没有设置尺寸(一般是高度不设置)，父元素内整体浮动的元素无法撑开父元素

				1）、 在父级上增加属性 ： overflow:hidden;

				2）、 clearfix: 	引用时把clearfix加到父级后面去	（常用）
						.clearfix:after{ content:""; display:table; clear:both; }	# 清除浮动
						.clearfix:before{ content:""; display:table; }				# margin-top 塌陷

						合二为一：(放到公共的样式里面)
							.clearfix:before,.clearfix:after{ content:""; display:table; }	# IE有时候不认
							.clearfix:after{ clear:both; }
							.clearfix{ zoom:1 ;}											# IE独有的属性，1 不放大也不缩小



			当把两个块元素并排放(放一行内),需要把这两个块元素并列，在两个块元里设置display:inline-block(转为内联块)，之间会有空隙的，
			一种是代码不换行，把两个div放在一行；另一种通过设置font-size，全局设为0，那么每个样式中都要设font-size
			还有种方式就是浮动，

			当浮动的时候设置了间距导致不能有效的排列在一行，可以在添加个父类块，把宽度设大，并设置 overflow:hidden; 这样子元素就能有效的
			排列在一行上




	8、 定位：

		文档流：
			是指盒子按照html标签编写的顺序依次从上到下，从左到右排列，块元素占一行，
			行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置。

		定位：
			我们可以使用css的 position (属性)来设置元素的定位类型.

			postion的设置项:
				1）、 relative (用的少，作为绝对的参照物，父级使用): 生成相对定位元素，元素所占据的文档流的位置保留，元素本身相对自身原位置进行偏移。

				2）、 absolute (用的多): 生成绝对定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，
						相对于上一个设置了定位的父级元素(来进行定位)，如果找不到，则相对于body元素进行定位。

				3）、 fixed (页面弹框): 生成固定定位元素，元素脱离文档流，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于浏览器窗口进行定位。

				4）、 static (可设可不设，取消定位属性): 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性。

				5）、 inherit (用的少，直接定义): 从父元素继承 postion 属性的值。


			定位元素的偏移：
				left / right / top / bottom 设置偏移值  （left:左边向右偏，top:上边往下偏）

			定位元素的层级：
				默认的层级是 后设的在上面，
				z-index属性设置元素的层级, 数值越大 定位元素越上面
				z-index:9999;		

			定位元素的特性：
				绝对定位和固定定位的块元素和行内元素会自动转为为行内块元素。（内容决定宽度）



	9、 background 属性

		负责给盒子设置背景图片和背景颜色的，background是一个复合属性；

			设置项：
				1）、 background-color(同color) 设置背景颜色
				2）、 background-image(url（路径）) 设置背景图片地址
				3）、 background-repeat(默认平铺填充) 设置背景图片如何重复平铺  （repeat-x 重复x轴。 repeat-y 重复y轴）
				4）、 background-position(水平 垂直) 设置背景图片的位置	（方位值； 也可以是数值px）
				5）、 background-attachment(默认是滚动的，fixed(浮动))设置背景图片是固定还是随着页面滚动条滚动

				background: #00FF00 url(bgimage.gif) no-repeat left center fixed
				设置项用空格隔开，有的设置项不写也是可以的，它会使用默认值。



	



	案例见： default.html


			


