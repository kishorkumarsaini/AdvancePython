#!/usr/bin/python3
import poplib

host='pop.gmail.com'
username=input("Please Enter your email=")
password=input("Please Enter your password=")

pop3server=poplib.POP3_SSL(host,995)
print(pop3server.getwelcome())
pop3server.user(username)
pop3server.pass_(password)
#access mailbox status
pop3info=pop3server.stat()
mailcount=pop3info[0]
print("Total no of Email:",mailcount)
print("\nstart reading message")
for i in range(mailcount):
	for message in pop3server.retr(i+1)[1]:
		print(message)
pop3server.quit()