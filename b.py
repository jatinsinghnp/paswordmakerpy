# test_str = "hellow $ echo i am hacker"
  

# print("The original string is : " + str(test_str))
  

# res = ''.join(format(ord(i), '08b') for i in test_str)
 
# print( str(res))

import random
import string
length=int(input('enter the length of the number '))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbol=string.punctuation
all=lower+upper+num+symbol

temp=random.sample(all,length)
password="".join(temp)
print(password)

