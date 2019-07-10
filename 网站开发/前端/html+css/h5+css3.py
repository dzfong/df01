
H5

		应对手机APP开发，移动端页面

		手机上都支持H5+CSS3,浏览器都是最新版本的


	一、 CSS3新增选择器(新特性)：

		1、css3 圆角 、阴影、 文字效果：

			1）、 圆角 

				a）、 设置某一个角的圆角，比如设置左上角的圆角：
						border-top-left-radius:30px 60px;

				b）、 同时分别设置四个角：
						border-radius:30px 60px 120px 150px;

				c）、 设置四个圆角相同：
						border-radius:50%;


			2）、 盒阴影box-shadow：

				box-shadow: 10px 10px 5px #888888  inset(内部阴影，缺省默认外部);	# 水平 垂直 深度(越大越模糊) 阴影颜色

			3）、 文字阴影text-shadow：

				text-shadow：5px 5px 5px #FF0000;

			4）、 文字自动换行

					word-wrap: word-break: normal|break-all|keep-all;

					p{word-wrap:break-word;}

			5）、 字体：@font-face 规则中定义

				@font-face{
					font-family: myFirstFont;
					src: url('Sansation_Light.ttf'),
						 url('Sansation_Light.eot'); /* IE9+ */
				}
				您必须为粗体文本添加另一个包含描述符的 @font-face：
				@font-face{
					font-family: myFirstFont;
					src: url('Sansation_Bold.ttf'),
						 url('Sansation_Bold.eot'); /* IE9+ */
					font-weight:bold;			/* 加粗选择这个字体库 */
				}

				引用：
					div{
					font-family:myFirstFont;
					}

			6）、 框大小:box-sizing 

				a）、 box-sizing 属性可以设置 width 和 height 属性中包含了 padding(内边距) 和 border(边框)。
						box-sizing : content-box: 元素的填充和边框布局和绘制指定宽度和高度除外；
									 border-box: 对元素指定宽度和高度包括了 padding 和 border；
								 	 inherit: 从父元素继承；
						{ box-sizing: border-box; }

				b）、 调整尺寸：
						resize属性指定一个元素是否应该由用户去调整大小
						resize: none：用户无法调整元素的尺寸(默认)
								both：用户可调整元素的高度和宽度。
								horizontal：用户可调整元素的宽度。
								vertical: 用户可调整元素的高度。
						div{resize:both; overflow:auto;}

				c）、 外形修饰：
						outline-offset 属性对轮廓进行偏移，并在超出边框边缘的位置绘制轮廓。
						轮廓与边框有两点不同：轮廓不占用空间； 
											  轮廓可能是非矩形。
						div{ border:2px solid black; outline:2px solid red; outline-offset:15px;}



		2、  rgba:

			1）、 盒子透明度表示法：	（会改变盒子里面的字体颜色）

				opacity: 0.1;
				filter:alpha(opacity=10);		# 兼容IE浏览器

			2）、 背景透明： rgba(0,0,0,0.1)：	（不会改变字体颜色，只是在背景颜色上做改变）

				前三个数值表示颜色(0-255)，第四个数值(小数)表示颜色的透明度。

			3）、 边框透明度：
			
				border: 1px solid rgba(0, 0, 0, 0.1)



		3、 transition动画：（需要触发的）

			专题网站，炫酷的效果，主站很少用到动画：

			1）、 transition-property 设置过渡的属性，比如：width height background-color；

			2）、 transition-duration 设置过渡的时间，比如：1s 500ms；

			3）、 transition-timing-function 设置过渡的运动方式，常用有 linear(匀速)|ease(缓冲运动)；

			4）、 transition-delay 设置动画的延迟；

			5）、 transition: property duration timing-function delay 同时设置四个属性；

			多个动画之间用逗号隔开；
				transition: width 2s ease , height 1s ease 1s ;
			如果所有动画没有延迟，可以简写：
				transition: all 1s ease;



		4、 transform变换：

			1）、translate(x,y) 设置盒子位移； 位移像素(30px,50px) 30px是横向，50px是纵向

			2）、scale(x,y) 设置盒子缩放; 	等比缩放(1,2) 1是x轴保存原始尺寸，2是y轴放大2倍

			3）、rotate(deg) 设置盒子旋转；	绕着Z轴旋转(0deg) 0是角度 单位是deg	

			4）、skew(x-angle,y-angle) 设置盒子斜切； 倾斜的角度(45deg,0), x轴45度角往左倾斜，正数方向左和上

			5）、perspective(800px) 设置透视距离； 近大远小(景深) , perspective(800px) 效果是最好的

			6）、transform-style flat | preserve-3d 设置盒子是否按3d空间显示； 3维空间旋转(默认平面的旋转)

			7）、translateX、translateY、translateZ 设置三维移动

			8）、rotateX、rotateY、rotateZ 设置三维旋转；默认是绕着Z轴旋转(对着操作人员)

			9）、scaleX、scaleY、scaleZ 设置三维缩放

			10）、tranform-origin 设置变形的中心点；( tranform-origin: left top)或者 (transform-origin: 15px 30px)

			11）、backface-visibility 设置盒子背面是否可见 ； 默认是可见的(visible); 不可见：hidden

				如果需要动画变形时，在类属性中需要设置初始值(不设会出现跳变的bug)及动画过程，然后在hover中设置变换值
				如果需要围绕X、Y轴旋转，那么需要设置景深； transform: perspective(800px) rotateY(45deg)
				旋转的轴向：	判断旋转的方向，让轴向对着自己，顺时针方向
						X轴： 从左往右
						Y轴： 从上往下
						Z轴： 从屏幕内往外
				图片翻面和文字叠加起来、设置盒子背面不可见，有翻面结合的效果



		5、 animation动画： （设置元素自动，不需要触发）

			1）、@keyframes 定义关键帧动画
			2）、animation-name 动画名称
			3）、animation-duration 动画时间
			4）、animation-timing-function 动画曲线 linear(匀速)|ease(缓冲)|steps(步数)
			5）、animation-delay 动画延迟
			6）、animation-iteration-count 动画播放次数 n|infinite(无限次)	(如果设置了返回，一次一回算两次)
			7）、animation-direction 动画结束后是否反向还原 normal|alternate
			8）、animation-play-state 动画状态 paused(停止)|running(运动)
			9）、animation-fill-mode 动画前后的状态 none(缺省)|forwards(结束时停留在最后一帧)|backwards(开始时停留在定义的开始帧)|both(前后都应用)
			10）、animation:name duration timing-function delay iteration-count direction;同时设置多个属性


		需要先定义动画，用关键字 @keyframes 动画名称, 然后去在样式里引用：
			@keyframes moving{
				from{
					width:100px;
				}

				to{
					width:500px;
				}
			}

		然后去在样式里引用：
			.box{
				width:100px;
				height:100px;
				background-color:gold;

				animation: moving 1s ease 0s 5 alternate;
			}

			.box:hover{
				animation-play-state: paused;
			}


		6、 新增选择器：

			1）、 E:nth-child(n)  

				匹配元素类型为E且是父元素的第n个子元素
				例如： .con div:nth-child(5){}			# .con中的第5个div

			2）、E:first-child：匹配元素类型为E且是父元素的第一个子元素

				如果没有定义元素，那么所有元素中的 E属性的第一个子元素都生效
				例如： p:first-child{ } ---针对body div content的第一个P属性  

			3）、E:last-child：匹配元素类型为E且是父元素的最后一个子元素

				同 E:first-child

			4）、E > F E元素下面第一层子集

				元素下面的第一层子集
				例如： div>div{}  --- 第二层的div样式	如果是 .con div>div{}  那么就是第三层

			5）、E ~ F E元素后面的兄弟元素

				 不包含第一个，也不会跳出E
				 例如： .con div~div{}	--- 第二层的div从第2个元素开始	

			6）、E + F 紧挨着的后面的兄弟元素

				 同 E ~ F 但是跳出了E，还包括了 E 后面的元素，结构相同，都是二层的
				 例如： div+div{}	


		7、 属性选择器：	

			1）、 E[attr] 含有attr属性的元素

				div[data-attr='ok']{ }

			2）、 E[attr='ok'] 含有attr属性的元素且它的值为“ok”

				div[data-attr='ok']{ }			<div data-attr='ok'> </div>

			3）、 E[attr^='ok'] 含有attr属性的元素且它的值的开头含有“ok”

				div[data-attr^='ok']{ }			<div data-attr='ok123'> </div>

			4）、 E[attr$='ok'] 含有attr属性的元素且它的值的结尾含有“ok”

				div[data-attr$='3']{ }			<div data-attr='ok123'> </div>

			5）、 E[attr*='ok'] 含有attr属性的元素且它的值中含有“ok”

				div[data-attr*='1']{ }			<div data-attr='ok123'> </div> 

		

		

		8、 多背景与渐变：

			1）、 多背景：CSS3中可以通过background-image属性添加背景图片。
					不同的背景图像和图像用逗号隔开，所有的图片中显示在最顶端的为第一张。

				background-image ： url(img_flwr.gif), url(paper.gif); 
				background-size ：100% 100%;  或者（80px 60px;） 缺省值是图片的真实大小
								 cover :将背景图像等比缩放到(完全覆盖)容器，背景图像有可能超出容器
								 contain：将背景图像等比缩放到宽度或高度与容器的宽度或高度相等，背景图像始终被包含在容器内。
				background-origin：content-box, padding-box,和 border-box区域内可以放置背景图像。
				background-clip： 从指定位置裁切， content-box, padding-box,和 border-box

				background ： [background-color] | [background-image] | [background-position][/background-size] 
				| [background-repeat] | [background-attachment] | [background-clip] | [background-origin],...


			2）、 CSS3 定义了两种类型的渐变（gradients）：

				a、线性渐变（Linear Gradients）- 向下/向上/向左/向右/对角方向

					background: linear-gradient(direction, color-stop1, color-stop2, ...); /*默认从上到下*/
					background: linear-gradient(angle, color-stop1, color-stop2);

					如：
					background: linear-gradient(to bottom right, red , blue); /* 从左上角开始到右下角  */
					background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); /* 多色渐变 */
					background: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1)); /* 使用透明度 */
					background: linear-gradient(180deg, red, blue); /* 指定角度的渐变 */
					background: repeating-linear-gradient(red, yellow 10%, green 20%);	/* 10%是颜色占比，20%是100/20=5行 */

				b、 径向渐变（Radial Gradients）- 由它们的中心定义

					background: radial-gradient(center, shape size, start-color, ..., last-color);
						shape 参数定义了形状。它可以是值 circle 或 ellipse。
							circle 表示圆形，ellipse 表示椭圆形。默认值是 ellipse。

					如：
					background: -webkit-radial-gradient(red, green, blue);	 /* Safari 5.1 - 6.0 */
					background: radial-gradient(red, green, blue);	 /* 均匀渐变分布*/
					background: radial-gradient(red 5%, green 15%, blue 60%); 	/* 不均匀渐变分布 */
					background: radial-gradient(60% 55%, closest-side,blue,green,yellow,black);		/* 同尺寸大小关键字的径向渐变 */
					background: radial-gradient(60% 55%, farthest-side,blue,green,yellow,black);	/* 同尺寸大小关键字的径向渐变 */
					background: repeating-radial-gradient(red, yellow 10%, green 15%);		/* 重复的径向渐变 */




		9、 css3前缀 （兼容性）

				sublime 安装 autoprefixer 设置快捷键
				然后电脑上安装 node.js

				一般加上CSS3特性前加上 -webkit-

				如： 
					.box{
						-webkit-transition:all 1s ease;
						transition: all 1s ease;
						-webkit-transform:rotate(45deg);
						transform:rotate(45deg);
					}



		10、 css3多列属性：

				column-count   	: 分列的数量
				column-gap		: 每列之间的距离
				column-rule		: 设置间隔的线及线的颜色 column-rule: 5px outset #ff0000;	


		11、 瀑布流：

				宽度相同，高度不同；
				设置列的宽度:	 	column-width: 250px;
									-webkit-column-width: 250px;
				列间距：			column-gap: 5px;
									-webkit-column-gap: 5px;

				设置每张图片的属性  width:250px;
									margin:5px 0;						


	二、 H5 新增标签

		1、 语义标签：

			1）、<header> 页面头部、页眉

			2）、<nav> 页面导航

			3）、<article> 一篇文章

			4）、<section> 文章中的章节

			5）、<aside> 侧边栏

			6）、<footer> 页面底部、页脚


		2、 音、视频：

			1）、 <audio> 

			2）、 <video>  不支持 flv 格式 ；直接用其他程序的插件



		低版本的浏览器兼容H5新标签的方法，在页面中引入js文件：

			<script type="text/javascript" src="//cdn.bootcss.com/html5shiv/r29/html5.js"></script>


		3、 表单控件

			网址:url	<label>网址:</label><input type="url" name="" required><br><br> 
			邮箱:email	<label>邮箱:</label><input type="email" name="" required><br><br> 
			日期:date	<label>日期:</label><input type="date" name=""><br><br> 
			时间:time	<label>时间:</label><input type="time" name=""><br><br> 
			星期:week	<label>星期:</label><input type="week" name=""><br><br> 
			数量:numbe	<label>数量:</label><input type="number" name=""> <br><br>
			范围:range	<label>范围:</label><input type="range" name=""><br><br> 
			电话:tel	<label>电话:</label><input type="tel" name=""><br><br> 
			颜色:color	<label>颜色:</label><input type="color" name=""><br><br> 
			搜索:search	<label>搜索:</label><input type="search" name=""><br><br>	

			表单控件属性：

				1）、 placeholder	设置文本框默认提示文字 ： （placeholder="搜索"）
				2）、 autofocus 自动获得焦点	： 自动跳到焦点（用户体验属性）								
				3）、 autocomplete 联想关键词	： 一般都是关闭这个,自定义个 (autocomplete="off")


		4、 canvas标签：

			<canvas></canvas>
			canvas 标签只是图形容器，必须通过脚本(通常是javascript)来绘制图形；
			可以通过多种方法使用canva绘制路径、盒、圆、字符及添加图像。
			




		案例见： csstest.html