x='toot'
str1=''
for s1 in range(0,len(x)):
    str1+=x[s1]
str2=''
for s2 in range(len(x)-1,-1,-1):
    str2+=x[s2]
if str1==str2:
     print('polyndrome')    