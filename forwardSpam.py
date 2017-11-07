import smtplib
import time
import random

from email.Header import Header
from email.mime.text import MIMEText
#Open a file for reading

me = 'andrewyli@gmail.com' # change to your email
p_reader = open('password.txt', 'rb') # edit for your password
cipher = p_reader.read()
recipients = ['andrewyli@gmail.com'] # enter recipients here


def spamEveryMinute():
    while (True):
        fp = open('message.txt', 'rb')
        #multipart class is for multiple recipients
        msg = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()

        thread_number = random.randint(0, 10000)
        msg['Subject'] = Header('Minutely Spam Report (randomizer: ' + str(thread_number) + ')', 'utf-8')
        msg['From'] = me
        msg['To'] = ', '.join(recipients)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, cipher)
        s.sendmail(me, recipients, msg.as_string())

        print "Email sent to: " + ', '.join(recipients)
        s.quit()
        time.sleep(60) # change rate of fire here
    
spamEveryMinute()

FindATargetOnGSuiteOpen = open ('gsuitetargets.txt', 'rb')
FindARandomTargetOnGSuitePrepare= email_list = ['jansbrid@d93mail.com', 'minzbrad@d93mail.com']

