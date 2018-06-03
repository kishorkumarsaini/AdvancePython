#!/usr/bin/python3
import os

a=10
b=0

try:
  v=a/b    
  print(v)
except:
     os.system('echo "aap se nahi hogaa bhai" | festival --tts')


finally:
		print("always print")