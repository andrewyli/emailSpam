# This email bot is made by Aayush Patil
# Email bot
# Follow me insta ayush_patil7
import smtplib
import config
import xlrd
import socket

# Explain why we have to do this
socket.getaddrinfo('localhost', 25)


loc = 'Emails.xlsx'
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)




class Sending_emails:

    def __init__(self, username, password, subject, msg):
        self.username = username
        self.password = password
        self.subject = subject
        self.msg = msg

    def send_email(self):

        for all_emails in range(sheet.nrows):
            try:
                print("Target set : {0}".format(sheet.cell_value(all_emails + 1, 0)))

            except IndexError:
                None
            try:
                print("We are sending email to {0}".format(sheet.cell_value(all_emails + 1, 0)))
            except IndexError:
                None

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)

            message = 'Subject: {}\n\n{}'.format(sheet.cell_value(all_emails + 1, 2),
                                                 sheet.cell_value(all_emails + 1, 1))

            try:
                server.sendmail(self.username, sheet.cell_value(all_emails + 1, 0), message)
            except IndexError:
                None
            server.quit()
            print("Email sent to: {0} ".format(sheet.cell_value(all_emails + 1, 0)))


count = 0
while count < 200:
    try:
        e = Sending_emails(config.EMAIL_ADDRESS, config.PASSWORD, sheet.cell_value(count + 1, 2),
                           sheet.cell_value(count + 1, 1))
        e.send_email()
        count = count + 1
        
    except IndexError:
        print("Done with sending emails")
        print("Congratulations we have send  emails successfully")
        break


