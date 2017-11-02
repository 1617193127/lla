import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'tonyemail@126.com'
msg['to'] = '2259827138@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('tonyemail@126.com', '*******')
smtp.sendmail('tonyemail@126.com', '2259827138@qq.com', str(msg))
smtp.quit()