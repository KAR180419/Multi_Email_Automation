# to, cc and bcc

import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
fromaddress = input("Your Address: ") #Sender E mail

password = getpass.getpass("Your Password: ") #Password

to = input("To address: ") #Receiver E mail

cc = input("CC Addresses (Leave blank if none): ").split() #Can enter multiple E Mails

bcc = input("BCC Addresses (Leave blank if none): ").split() #Can enter multiple E Mails

sub = input("Enter Subjectline: ") #Subject line of Email

message_text = input("Message (Maximum 1 paragraph): ") #Body of Email

message = "From: %s\r\n" % fromaddress + "To: %s\r\n" % to + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % sub + "\r\n" + message_text
total = [to] + cc + bcc

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(fromaddress, password)
    server.sendmail(fromaddress, total, message)