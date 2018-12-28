#使用谷歌邮箱发送中文邮件
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

#接口设置

gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#登录邮箱:登陆之前必须开启谷歌账户‘对安全性较低的应用的访问权限’，试完代码后记得关掉
while True:
    try:
        #输入用户信息
        user = input('请输入邮箱账号：')
        password = getpass.getpass('请输入邮箱密码：')
        gmail.login(user, password)
        print('登陆成功')
        break
    except:
        choice = input('认证未通过，是否重新输入用户信息？y/n\n')
        if choice == 'y':
            continue
        else: 
            print('登陆成功')
            break

#输入发送信息
receiver = input('请输入收件人邮箱，并用英文空格隔开（若多人）：')
to = receiver.split()
subject = '使用python发送中的中文邮件测试'
text = "这次使用了email模块进行utf-8的转换，从而实现发送中文内容的邮件。"
message = MIMEText(text,'plain','utf-8')
message['Subject'] = Header(subject,'utf-8')
message['From'] = Header(user,'utf-8')


#发送邮件
result = gmail.sendmail(user,to,message.as_string())
print(result)
gmail.close()
