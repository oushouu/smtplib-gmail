#使用谷歌邮箱
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


#subject = input('请输入邮件标题：')
#text = input('请输入正文：')
receiver = input('请输入收件人邮箱，并用英文空格隔开（若多人）：')
to = receiver.split()
subject = 'Use Python to Send A Email3'
subject = 'Subject:' + subject
text = "Hi, This is the mail sent by Python code. It's cool, right?"


#发送邮件
result = gmail.sendmail(user,to,subject + '\n\n' + text)
print(result)

#关闭连接
gmail.close()
