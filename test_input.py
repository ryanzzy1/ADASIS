from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication  #附件

import smtplib #发送邮件

input("pls input ")

#准备发送邮件的参数
sender = "838750084@qq.com"
#收件人
to_list = ["838750084@qq.com",
           "ryan_zhang310@163.com"
]

#抄送人
cc_list = [
    "838750084@qq.com",
    "ryan_zhang310@163.com"
]

subject = "This is a test today "
#授权密码，链接邮箱smtp
auth_pwd = 'rrskrbnpqkgmbbjj'

#写邮件
#创建邮件
em = MIMEMultipart() #em 其实是message.Message 的子类的对象
em['Subject'] = subject
em['From'] = sender
em['To'] = ",".join(to_list)
em['Cc'] = ','.join(cc_list)

#邮件内容
'''
content = MIMEText("This is a test for python send email!")
em.attach(content)
 '''
#发送html 代码

content = MIMEText("<a href='http://www.baidu.com'><img src='cid:Python'/></a>", _subtype="html")
em.attach(content)

#发送图片
img = MIMEImage(open("OIP.jpg",mode="rb").read())
img.add_header("Content-ID","Python") # 给图片设置id值
em.attach(img)

#发送附件
app = MIMEApplication(open("OIP.jpg", mode='rb').read())
app.add_header('content-disposition', 'attachment', filename='test.jpg')
em.attach(app)
# 发送邮件
#1.链接smtp 服务器

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
#2.登录
smtp.login(sender,auth_pwd)
#3.发送邮件
smtp.send_message(em) #msg 必须是message.Message 的对象，fromaddr 和 to_addr 都不用提供，smtp.send_message(em,from_addr=None, to_addrs=None)
# smtp.sendmail() #必须是字符串

#4.关闭链接
smtp.close()