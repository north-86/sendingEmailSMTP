import smtplib

domainName = input('Enter SMTP server domain name\n')
port = int(input('Enter port\n'))

if (port == 587):
    smtpObject = smtplib.SMTP(domainName, port)
    smtpObject.ehlo()
    smtpObject.starttls()
if (port == 465):
    smtpObject = smtplib.SMTP_SSL(domainName, port)
    smtpObject.ehlo()

emailOut = input('Enter your email address\n')
password = input('Enter password\n')
smtpObject.login(emailOut, password)

emailIn = input('Enter the destination email address\n')
subject = input('Enter subject\n')
text = input('Enter text\n')
message = 'Subject: ' + subject + '\n ' + text
smtpObject.sendmail(emailOut, emailIn, message)
smtpObject.quit()
input()