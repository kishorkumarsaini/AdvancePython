#!/usr/bin/python3
import smtplib

sender=input("Please Enter the sender email=")
SenderPassward=input("plses Enter your password=")
receiver=input("Please Enter the receiver email=")

From=sender
To =receiver
Subject=input("Enter your message=")
message=" Message\n{0}\n{1}\n{2}".format(From,To,Subject)

try:
	#create SMTP session
	smtpobj=smtplib.SMTP('smtp.gmail.com',587)
	#start TLS for security
	smtpobj.starttls()
	#Authentication
	smtpobj.login(sender,SenderPassward)
	smtpobj.sendmail(sender,receiver,message)
	print("Successfully send email")
except SMTPException:
	print("Error unable to send email")