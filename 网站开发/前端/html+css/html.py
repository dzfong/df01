


	HTML

		HTML是 HyperText Mark-up Language 的首字母简写，意思是超文本标记语言，
		超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言
		
		目前常用的两种文档类型是 xhtml 1.0 和 html5
		html5新增了标签元素以及元素属性	
		
		<!-- 这是一段注释  --> 
		
		
		
		
	基本结构：	
	
			<!DOCTYPE html>  					文档说明，顶文件
			<html 'lang="zh-CN"'>				外框结构，定义语言，成对的	
				<head>							头文件，成对的，
					<meta charset="UTF-8">		定义网页编码，单标签
					<title></title>				网页标题
					<link rel="stylesheet" href="css/style.css">  	外链css样式文件
					<script src="/static/js/jquery-1.12.4.js"></script>		javascript文件
				</head>
				<body>
												网页内容
				</body>
			</html>
			
			
	


	1、html标题标签
	
		 <h1>、<h2>、<h3>、<h4>、<h5>、<h6>
		 
		 成对的<h1></h1>, 存在于 <body> 标签中 
		 
		 6种级别的标题表示文档的6级目录层级关系； 大小、间距、都是加粗的
		 
		 搜索引擎会使用标题将网页的结构和内容编制索引，所以网页上使用标题是很重要的。
		 
		 SEO搜索引擎优化，方便百度爬虫爬取
		 
	



		 
	2、段落标签、换行标签与字符实体
	
		<p> </p>	
		
			<p>标签定义一个文本段落，带有样式，一个段落含有默认的上下间距，段落之间会用这种默认间距隔开。	
			
		<br />  
		
			换行标签 , 单标签，也可以写成 <br>
			
			
		字符实体：
		
			1）、&nbsp; 	 空格。 但是不精确的，如果需要精确的需要用到样式来做
			
			2）、&lt;	<	。 符号<
			
			3）、&gt;	>	。 符号<
		



			
	3、块标签、含样式的标签
	
		<div> </div>	
		
			可定义文档中的分区或节；以把文档分割为独立的、不同的部分；
			块元素，表示一块内容，这意味着它的内容自动地开始一个新行；
			没有具体的语义，不带样式，可以嵌套其他标签；
			用 id 或 class 来标记 <div>，那么该标签的作用会变得更加有效； 
			<div class=""></div> ; 
			<div style="color:#00FF00"></div>
			支持全局属性 和 事件属性
			
			
		<span> </span>
			
			行内元素，表示一行中的一小段内容，没有具体的语义，不带任何样式；
			主要是对某段内容中的一小段进行样式处理；
			比如 ：
			<p class="tip"><span>提示：</span>... ... ...</p>
			
			p.tip span {
				font-weight:bold;
				color:#ff9955;
			}
			
		
		含样式和语义的标签
		
			1）、<em> </em>	:	行内元素， 表示语气中的强调词 ； 倾斜的样式
				
			2）、<i> </i> ： 行内元素， 表示专业词汇； 倾斜的样式
			
			3）、<b> </b> ： 行内元素，表示文档中的关键字或者产品名； 加粗的样式
			
			4）、<strong> </strong> ： 行内元素， 表示非常重要的内容；加粗的样式 通常嵌套在 <em></em>中
			
			
		语义化的标签
		
			语义化的标签，就是在布局的时候多使用有语义的标签，搜索引擎在爬网的时候能认识这些标签，理解文档的结构，方便网站的收录。
			比如：
				h1标签是表示标题，
				p标签是表示段落，
				ul、li标签是表示列表，
				a标签表示链接，
				dl、dt、dd表示定义列表等，
				语义化的标签不多。
			



		
	4、图像标签、绝对路径和相对路径
	
		
		<img />
			
			单标签，在网页上插入一张图片
			src 属性；  引用图片的地址			
			alt 属性：	图片说明	；
				当图片加载失败的时候，会显示的文字
			
			
			绝对地址在整体文件迁移时会因为磁盘和顶层目录的改变而找不到文件，相对路径就没有这个问题。
			通常用到的都是相对路径。
			相对路径： 	 ./ 当前目录 ../ 上级， ../../上上级
						src="./images/001.jpg"; src="../../images/002.jpg"
						
			绝对路径:	src="https:www.baid.com/iamges/001.jpg"
			
		
		


	5、链接标签
	
		<a> </a>
		
			双标签，可以在网页上定义一个链接地址
			href属性： 定义跳转的地址
			title属性： 定义鼠标悬停时弹出的提示文字框
			target属性： 定义链接窗口打开的位置
				target="_self" 缺省值，新页面替换原来的页面，在原来位置打开
				target="_blank" 新页面会在新开的一个浏览器窗口打开
			缺省链接： href="#"
			



	
	6、列表标签
	
		<ol> </ol>
		
			双标签，有序列表；
			在网页上定义一个有编号的内容列表可以用<ol>、<li>配合使用来实现
			
			
		<ul> </ul>
		
			双标签，无序列表；
			在网页上定义一个无编号的内容列表可以用<ul>、<li>配合使用来实现；前面显示的是 ·
			新闻列表
			
			
		<li> </li>	
			
			定义列表项目
			<li>新闻标题一</li>
			<li>新闻标题二</li>
			<li>新闻标题三</li>		
			
				写法： ul>(li>a{新闻标题})*3 然后 按 tab键
				
				
		定义列表：
		
			<dl>				: 表示列表的整体
				<dt> </dt>		：定义术语的题目
				<dd> </dd>		：定义术语的解释
			</dl>
			
				写法： dl(dt+dd)*3 然后 按 tab键
				



				
	7、 表格
	
		<table> </table>
		
			双标签，声明一个表格
			
			<tr> </tr>  # 表格中的一行
			<th> </th>  # 表头单元格
			<td> </td>  # 普通单元格
			
			表格属性：
				border 		# 边框
				width 		# 宽度
				height		# 高度
				align		# 表格水平对齐的方式
				cellpadding	# 单元边沿与其内容之间的空白
				cellspacing # 单元格之间的空白 0 就是实线
				
			单元格属性：
				align  		# 单元格内容水平对齐方式  left \ right \ center
				valign		# 单元格内容垂直对齐方式  top \ middle \ bottom
				colspan		# 单元格水平合并	数值
				rowspan		# 单元格垂直合并	数值
				
			
			
			<table border="1" width="300" height="200" align="center">		# 1个像素的边框，不写单位
			  <tr align="center">					# 表格中的一行
			    <th>Month</th>		# 表头单元格
			    <th>Savings</th>
			  </tr>
			  <tr>
			    <td>January</td>	# 普通单元格
			    <td>$100</td>
			  </tr>
			</table>

	


								
	8、页面布局

		布局也可以叫做排版，它指的是把文字和图片等元素按照我们的意愿有机地排列在页面上，布局的方式分为两种：

		1）、table布局： 传统布局，通过table元素将页面空间划分成若干个单元格，将文字或图片等元素放入单元格中，隐藏表格的边框，从而实现布局。
			目前主要使用在EDM(广告邮件中的页面)中，主流的布局方式不用这种。

				a、按照设计图的尺寸设置表格的宽高以及单元格的宽高。

				b、将表格border、cellpadding、cellspacing全部设置为0，表格的边框和间距就不占有页面空间，它只起到划分空间的作用。

				c、针对局部复杂的布局，可以在单元格里面再嵌套表格，嵌套表格划分局部的空间。

				d、单元格中的元素或者嵌套的表格用align和valign设置对齐方式

				e、通过属性或者css样式设置单元格中元素的样式


		2）、HTML+CSS布局(DIV+CSS)：主要通过CSS样式设置来布局文字或图片等元素，
			需要用到CSS盒子模型、盒子类型、CSS浮动、CSS定位、CSS背景图定位等知识来布局，它比传统布局要复杂，目前是主流的布局方式。


					
									
		
	9、表单
	
		用于搜集不同类型的用户输入，表单由不同类型的标签组成，相关标签及属性

		1）、<form> </form>
		
			action 属性：  表单数据提交的地址

			method 属性：  表单提交的方式，get 、 post  、ajax

			2）、<label> </label>

				label 元素不会向用户呈现任何特殊效果。不过，它为鼠标用户改进了可用性。
				如果您在 label 元素内点击文本，就会触发此控件。
				就是说，当用户选择该标签时，浏览器就会自动将焦点转到和标签相关的表单控件上。
				for 和 id 属性配合用，点击 字段，会触发控件
					<form>
					  <label for="male">Male</label>
					  <input type="radio" name="sex" id="male" />
					  <br />
					  <label for="female">Female</label>
					  <input type="radio" name="sex" id="female" />
					</form>


			3）、<input>

				单标签，用于搜集用户信息
				根据不同的 type 属性值，输入字段拥有很多种形式。输入字段可以是文本字段、复选框、掩码后的文本控件、单选按钮、按钮等等

				type 属性： 字段类型
					type="text" 定义单行文本输入框
					type="password" 定义密码输入框
					type="radio" 定义单选框	； name必须一样
					type="checkbox" 定义复选框
					type="file" 定义上传文件
					type="submit" 定义提交按钮
					type="reset" 定义重置按钮
					type="button" 定义一个普通按钮
					type="image" 定义图片作为提交按钮，用src属性定义图片地址; 通常会提交2次，不建议使用
					type="hidden" 定义一个隐藏的表单域，用来存储值
					type="number"	

				name 属性： 表单元素的名称，此名称是提交数据时的键名；
							这是必须要的，把这个提交到数据库里面去

				value属性： 定义表单元素的值；输入的值

			4）、<textarea>

				双标签， 定义多行文本输入框
				文本区中可容纳无限数量的文本，其中的文本的默认字体是等宽字体（通常是 Courier）。
				在文本输入区内的文本行间，用 "%OD%OA" （回车/换行）进行分隔

				name 属性： 

			5）、 <select> </select>

				双标签， 下拉的表单控件
				可创建单选或多选菜单

				name 属性：

			6）、 <option> </option>

				<option>标签 与<select>标签配合，定义下拉表单元素中的选项。

				value 属性： 

					<select>
					  <option value ="volvo">Volvo</option>
					  <option value ="saab">Saab</option>
					  <option value="opel">Opel</option>
					  <option value="audi">Audi</option>
					</select>




	
			
		
						
