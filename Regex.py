#Question 1

import re

emails=[]

for i in range(2):
    email = input("Enter Email Address : ")
    matcher = re.split('[@.]',email)
    #print(matcher)
    emails.append(tuple(matcher))

    
print(emails)

#Question 2

import re

Text = "Betty bought a bit of butter, But the butter was so bitter,So she bought some better butter, To make the bitter butter better."

Matcher = re.findall('[bB]\w+',Text)

count=0

if Matcher:
    for Matcher_Object in Matcher:
        count= count + 1
        print(Matcher_Object)

#Question 3
        
import re

Sent="A, very very; irregular_sentence"

s= re.sub('[\W_]',' ',Sent)

print(s)

#Question 4

import re
Tweet1 = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''


Tweet2 = re.sub('[#:@]\w*|http\S*','',Tweet1)
Tweet3= re.sub('RT|cc','',Tweet2)

print(Tweet3)
