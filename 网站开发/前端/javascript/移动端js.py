移动端js


	移动端的操作方式和PC端是不同的，移动端主要用手指操作，所以有特殊的touch事件，touch事件包括如下几个事件

		1、touchstart: //手指放到屏幕上时触发

		2、touchmove: //手指在屏幕上滑动式触发

		3、touchend: //手指离开屏幕时触发

		4、touchcancel: //系统取消touch事件的时候触发，比较少用


		移动端一般有三种操作，点击、滑动、拖动，这三种操作一般是组合使用上面的几个事件来完成的，
		所有上面的4个事件一般很少单独使用，一般是封装使用来实现这三种操作，可以使用封装成熟的js库。


		zeptojs (基本上不用了，手机端直接用jquery)：是一个轻量级的针对现代高级浏览器的JavaScript库， 它与jquery有着类似的api。 
					精简的类似jquery的js库；



	一、swiper 3.0版本适合移动端；是一款成熟稳定的应用于PC端和移动端的滑动效果插件，一般用来触屏焦点图、触屏整屏滚动等效果。

				除了引用js文件，还需要引用 swiper.min.css 文件，
				这个css文件必须要放在自定义的CSS前面,因为有些样式可以通过自定义css修改


				如果页面引用了jquery , 就用 swiper.jquery.min.js

				如果页面没有引用jquery ， 那么用 swiper.min.js 

				具体使用见api文档 http://www.swiper.com.cn/api/index.html


				幻灯片效果 (见案例 rem.html)





	二、bootstrap 框架：

			https://www.bootcss.com/ 
			https://v3.bootcss.com/css
			https://v3.bootcss.com/javascript

			框架是大于库的； 响应式布局，移动端开发、
			Bootstrap 的所有 JavaScript 插件都依赖 jQuery，因此 jQuery 必须在 Bootstrap 之前引入。

				js/jquery.min.js 
				js/bootstrap.min.js
				css/bootstrap.min.css 
				fonts文件夹  #把字体当图标

			视口 meta:vp


			1、bootstrap 容器:

				1、container-fluid 流体(宽度100%) 左右有15px间距 padding-left:15px;padding-right:15px
					<div class="container-fluid">流体容器</div>

				2、container	（@media）
					<div class="container">响应式固定容器</div>

					响应区间：
						1170  	大于1200 				col-lg- 	大于一行，小于各占一行
						970		大于992 小于1200		col-md- 	大于一行，小于各占一行		(ipad pro)
						750		大于768 小于992			col-sm- 	大于一行，小于各占一行		(ipad)
						100%	小于768					col-xs- 	始终排成一行				(手机)
		


			2、bootstrap 栅格系统:  （放在容器里面的）

				bootstrap将页面横向(宽度)分为12等分，按照12等分定义了适应不同宽度等分的样式类，
				这些样式类组成了一套响应式、移动设备优先的流式栅格系统：

				最好的是  6、4 、3 、2 、1


				
				列偏移： 当不能被12等分的时候，就不会居中，所以要设置偏移量
					col-lg-offset-
					col-md-offset-
					col-sm-offset-
					col-xs-offset-


				隐藏类： 当缩小时，大图片的栅格隐藏
					hidden-xs
					hidden-sm
					hidden-md
					hidden-lg


			3、bootstrap 按钮：	（颜色亮度一样，调和过的）

					1、btn 	    	声明按钮
					2、btn-default  默认按钮样式
					3、btn-primay   蓝色背景的按钮
					4、btn-success	绿色背景的按钮
					5、btn-info		天蓝色
					6、btn-warning	黄色
					7、btn-danger	红色
					8、btn-link		无背景色，随便放上有横杠
					9、btn-lg		按钮尺寸大
					10、btn-md		中
					11、btn-xs		小
					12、btn-block 	宽度是父级宽100%的按钮 （一般是做移动端的）
					13、active		默认响应的效果
					14、disabled	失效的按钮
					15、btn-group 	定义按钮组		可以做步骤 btn-group-justified是宽度100%显示


			4、 bootstrap 表单：

					1、form 	 		 声明一个表单域
					2、form-inline 		 内联表单域
					3、form-horizontal   水平排列表单域
					4、form-group 		 表单组、包括表单文字和表单控件
					5、form-control 	 文本输入框、下拉列表控件样式
					6、checkbox checkbox-inline  多选框样式
					7、radio radio-inline 单选框样式
					8、input-group 		 表单控件组
					9、input-group-addon 表单控件组物件样式
					10、input-group-btn	 表单控件组物件为按钮的样式
					11、form-group-lg 	 大尺寸表单
					12、form-group-sm 	 小尺寸表单




			记忆曲线： 5分钟 、 半小时、 12小时、 1天、  2天、 4天、 7天、 15天



			5、 导航条：

				先写导航条，把 container包含进去

					1、navbar 			声明导航条（设置nav元素为导航条组件）
					2、navbar-default 	声明默认的导航条样式
					3、navbar-inverse 	声明反白的导航条样式（指定导航条组件为黑色主题）
					4、navbar-static-top 去掉导航条的圆角
					5、navbar-fixed-top 固定到顶部的导航条（设置导航条组件固定在顶部）
					6、navbar-fixed-bottom 固定到底部的导航条（设置导航条组件固定在底部；）
					7、navbar-header 	申明logo的容器（主要指定div元素为导航条组件包裹品牌图标及切换按钮）
					8、navbar-brand 	针对logo等固定内容的样式（默认是放文字的,也可以放图片，但必须是小图片,如果图片太大，位置就会靠下）
					11、nav navbar-nav	定义导航条中的菜单
					12、navbar-form 	定义导航条中的表单
					13、navbar-btn 		定义导航条中的按钮
					14、navbar-text 	定义导航条中的文本
					15、navbar-left 	菜单靠左
					16、navbar-right 	菜单靠右
					17、navbar-toggle	设置button元素为导航条组件的切换钮；元素为在视口小于768px时才显示；
					18、collapsed navbar-collapse  设置元素显示768显示，小于隐藏	
					19、data-toggle		指以什么事件触发，常用的如modal,popover,tooltips等，data-target指事件的目标。


			6、 模态框：（弹框 有js点击事件）

					1、modal 			声明一个模态框
					2、modal-dialog 	定义模态框尺寸
					3、modal-lg			定义大尺寸模态框
					4、modal-sm 		定义小尺寸模态框
					5、modal-header		头部
					6、modal-body		主题
					7、modal-foot		底部



			7、 路径导航：breadcrumb 爬虫会爬取

				<ol class="breadcrumb">
				  <li><a href="#">Home</a></li>
				  <li><a href="#">Library</a></li>
				  <li class="active">Data</li>
				</ol>




			8、 bootstrap 下拉菜单

					1、dropdown-toggle
					2、dropdown-menu


			9、 图片响应式

					img-responsive 声明响应式图片
					class="img-responsive"