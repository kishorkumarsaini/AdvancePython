#!/usr/bin/python3

#create a file in read and write mode

file=open('geek.txt','r+')
#write in file
file.write("hello this is file is created and write")
# read a file content
file.read()
file.write("hello i am again write in file")

file.write("\npython is easy to learn but hard to mastering")
file=open('geek.txt','r')
print(file.read())
file.seek(0,0)
print(file.read())
#close a file
file.close()
