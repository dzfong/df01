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



	swiper 3.0版本适合移动端；是一款成熟稳定的应用于PC端和移动端的滑动效果插件，一般用来触屏焦点图、触屏整屏滚动等效果。

				除了引用js文件，还需要引用 swiper.min.css 文件，
				这个css文件必须要放在自定义的CSS前面,因为有些样式可以通过自定义css修改


				如果页面引用了jquery , 就用 swiper.jquery.min.js

				如果页面没有引用jquery ， 那么用 swiper.min.js 

				具体使用见api文档 http://www.swiper.com.cn/api/index.html


				幻灯片效果 (见案例 rem.html)





	bootstrap 框架：

			框架是大于库的； 响应式布局，移动端开发、
			Bootstrap 的所有 JavaScript 插件都依赖 jQuery，因此 jQuery 必须在 Bootstrap 之前引入。

				js/jquery.min.js 
				js/bootstrap.min.js
				css/bootstrap.min.css 
				fonts文件夹  #把字体当图标

			视口 meta:vp


			bootstrap 容器:

				1、container-fluid 流体(宽度100%) 左右有15px间距 padding-left:15px;padding-right:15px
					<div class="container-fluid">流体容器</div>

				2、container	（@media）
					<div class="container">响应式固定容器</div>

					响应区间：
						1170  	大于1200
						970		大于992 小于1200
						750		大于768 小于992
						100%	小于768
					

			bootstrap 栅格系统:  （放在容器里面的）

				bootstrap将页面横向(宽度)分为12等分，按照12等分定义了适应不同宽度等分的样式类，这些样式类组成了一套响应式、移动设备优先的流式栅格系统：





