
一、 git安装

	https://git-scm.com/download/win


		git bash here 可以从当前文件夹打开git命令行界面
		git GUI here 可以打开图形界面


	查看是否安装成功

		打开 git bash here :  git version


二、 连接github

	1、 在github官网建立一个仓库

	2、 配置ssh key

		1）、 $ ls ~/ .ssh/ 	#检查本机是否已经存在ssh秘钥； 
		2）、 $ ssh-keygen -t rsa -C "邮箱账号"		# 如果不存在ssh秘钥； 按3次回车，会生成一个.ssh目录在用户目录下
		3）、 打开用户目录，找到 .ssh/id_rsa.pub 文件，复制里面的内容 粘贴到github中用户设置settings -- SSH and GPG keys中，title随便填

	3、 测试配置ssh秘钥是否成功：$ ssh -T git@github.com 	
		# 注意邮箱地址不用改，如果提示Are you sure you want to continue connecting (yes/no)?，输入yes

	4、 从github克隆项目： git clone git@github.com:dzfong/df01.git  
		# 如果克隆出错，执行 eval "$(ssh-agent -s)"   、 ssh-add 就没问题了

	5、 git配置用户信息

		1）、 设置用户名 ： $ git config --global user.name '这里填写自己的用户名'
		2）、 设置用户邮箱： $ git config --global user.email '1071184870@qq.com'
		3）、 查看配置信息： $ git config --list

	6、 推送代码：

		1）、 查看分支： $ git branch
		2）、 创建分支： $ git checkout -b 分支名
		3）、 开发文件： views.py
		4）、 查看当前git状况： $ git status
		5）、 提交文件到git暂存区： $ git add views.py
		6）、 提交暂存区文件到git仓库： $ git commit -m '说明信息：创建视图'
		7）、 添加远程仓库：$ git remote add origin git@github.com:dzfong/df01.git 
		8）、 把本地库的内容推送到远程库分支上： $ git push -u origin 分支名(没建分支也可以是master) # 这是第一次推送
				$ git push origin 分支名(没建分支也可以是master) # 推送修改的内容
		9）、 刷新github仓库就能看到文件上传成功


	7、 将本地分支跟踪服务器分支

		1）、 $ git branch --set-upstream-to=origin/远程分支名称 本地分支名称

		2）、 $ git status  # 就可以看到 您的分支与上游分支 'origin/分支名' 一致

		3）、 $ git push  #提交到仓库


	8、 从远程分支上拉取代码：

		$ git pull origin 分支名称




问题：
	1、 'fatal: Not a git repository (or any of the parent directories): .git'

		解决： git init就可以了；提示说没有.git这样一个目录



	2、 error: failed to push some refs to 'git@github.com:yangchao0718/cocos2d.git'

		解决：  git pull --rebase origin master
				执行上面代码后可以看到本地代码库中多了README.md文件
				此时再执行语句 git push -u origin master即可完成代码上传到github



	3、 'fatal:remote origin already exists'

		解决： $ git remote rm origin



	4、 执行git push出现"Everything up-to-date"

		解决：  1）没有git add; 
				2）git add 了，但忘了git commit -m “提交信息”。








