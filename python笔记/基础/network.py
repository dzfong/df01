#coding=utf-8



#网络编程
#网络通信就是两个进程之间在通信
#Socket是网络编程的一个抽象概念
#打开一个Socket需要在的目标计算机的IP地址和端口号，再指定协议类型即可

#TCP编程
#大多数连接都是可靠的TCP连接，创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
#IPv4 是32位的整数  192.168.0.1
#IPv6 是128位的整数  2001:0db8:85a3:0042:1000:8a2e:0370:7334


#导入socket库
import socket
#创建一个socket:  AF_INET指定使用IPv4协议， AF_INET6指定为IPv6， SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接：   注意参数Tuple包含了地址和端口号
s.connect(('www.sina.com.cn',80))
#发送数据：发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据:
buffer = []
while True:
	#每次最多接收1K字节：
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
#关闭连接：
s.close()
#接收到的数据包含HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收到的数据写入文件：
with open('sina.html','wb') as f:
	f.write(html)