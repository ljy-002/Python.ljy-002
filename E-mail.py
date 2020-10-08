import smtplib

from email.mime.text import MIMEText

import time


mail_server = "XXX.XXX.com"#邮件提供商的smtp（上网去查查）

mail_port = 2

sender = "ljy123ljy123@dingtalk.com"#你的邮箱

sender_password = "xxxxxx"  #授权码，不一定是密码

receivers="1wh-zddx650ixl@dingtalk.com"  # input("receivers接收者邮箱:")

mytxt=input("text发送的文本:")

req=int(input("times邮件发送次数:"))

message = MIMEText(mytxt, 'plain', 'utf-8')

message['From'] = sender

message['To'] = receivers

message['Subject'] = input("Subject主题:")

a=0

while a<req:

    try:

        smtp_obj = smtplib.SMTP()

        smtp_obj.connect(mail_server, mail_port)

        smtp_obj.login(sender, sender_password)

        smtp_obj.sendmail(sender, [receivers], message.as_string())

        print('success!')

    except smtplib.SMTPException as e:

        print('failure!')

        print(e)

    a+=1
