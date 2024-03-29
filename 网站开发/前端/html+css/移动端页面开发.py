
移动端页面开发



	视口

		视口是移动设备上用来显示网页的区域，一般会比移动设备可视区域大，宽度可能是980px或者1024px，
		目的是为了显示下整个为PC端设计的网页，这样带来的后果是移动端会出现横向滚动条，
		为了避免这种情况，移动端会将视口缩放到移动端窗口的大小。
		这样会让网页不容易观看，可以用 meta 标签，name=“viewport ” 来设置视口的大小，
		将视口的大小设置为和移动设备可视区一样的大小。


		设置方法： 快捷方式：meta:vp + tab



	retina屏幕 (视网膜屏)

		视网膜屏幕指的是屏幕的物理像素密度更高的屏幕，物理像素可以理解为屏幕上的一个发光点，无数发光的点组成的屏幕，
		视网膜屏幕比一般屏幕的物理像素点更小，常见有2倍的视网膜屏幕和3倍的视网膜屏幕，
		2倍的视网膜屏幕，它的物理像素点大小是一般屏幕的1/4,
		3倍的视网膜屏幕，它的物理像素点大小是一般屏幕的1/9。

		通常ui在设计的时候把页面放大到2倍，然后通过CSS改变大小；
		背景图强制改变大小，缩放可以使用background新属性 : background-size:



	PC及移动端页面适配方法：

		1、 全适配： 响应式布局+流体布局 （一个页面同时适配PC、平板、手机端的）

		2、 移动端适配：	
					1）、 流体布局+少量响应式	（不流行）
					2）、 基于rem的布局： 	 	（流行）



	流体布局：

		就是使用百分比来设置元素的宽度，元素的高度按实际高度写固定值，
		流体布局中，元素的边线无法用百分比，可以使用样式中的计算函数 calc() 来设置宽度，
		或者使用 box-sizing 属性将盒子设置为从边线计算盒子尺寸。

		calc() 
			可以通过计算的方式给元素加尺寸，
			比如： width：calc(25% - 4px);  # 一定要空格



	响应式布局：

		就是使用媒体查询的方式，通过查询浏览器宽度，
		不同的宽度应用不同的样式块，每个样式块对应的是该宽度下的布局方式，从而实现响应式布局。
		响应式布局的页面可以适配多种终端屏幕（pc、平板、手机）。

		@media (max-width:960px){
		    .left_con{width:58%;}
		    .right_con{width:38%;}
		}
		@media (max-width:768px){
		    .left_con{width:100%;}
		    .right_con{width:100%;}
		}
		


	基于rem的布局：

		em单位是参照元素自身的文字大小来设置尺寸(chrome文字最小的为12px)。font-size: 14px; width: 20em  	# width: 280px;
		用的最多的是首行缩进；

		rem是css的单位	
		rem指的是参照根节点的文字大小，根节点指的是html标签，设置html标签的文字大小，
		其他的元素相关尺寸设置用rem，这样，所有元素都有了统一的参照标准，
		改变html文字的大小，就会改变所有元素用rem设置的尺寸大小。

		通过js根据屏幕大小改变html的font-size，来缩放宽高(rem单位)达到整体缩放 ；

		cssrem插件可以动态的将px尺寸换算成rem尺寸






	案例见： rem.html