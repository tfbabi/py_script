#!/usr/bin/python
#encoding:utf8
import smtplib
from email.mime.text import MIMEText
import time,sys,os
import psutil
def sendmail(reviewer,subject,msg):
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S')
    username = 'xxxxx'
    passwd = 'xxxxx'
    msg = MIMEText(msg,'plain', 'utf-8')
    msg["Subject"] = subject
    msg["From"]    = username
    msg["To"]      = reviewer
    try:
        s = smtplib.SMTP_SSL('smtp.163.com', 465)
        s.login(username,passwd)
        s.sendmail(username, reviewer, msg.as_string())
        s.quit()
        print "[%s]INFO:Email send Success!" % nowtime
    except smtplib.SMTPException,e:
            print "[%s]ERROR:Email send Falied,%s" % (nowtime,e)

def collect_os_info():
    res = "CPU逻辑个数:%s\n" %psutil.cpu_count()
    res+= "cpu物理个数:%s\n"  %psutil.cpu_count(logical=False)
    return res

if __name__ == "__main__":
    sendmail('xxxxx','服务器信息统计',collect_os_info())
