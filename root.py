import math
number=int(input())
tedad=0
while tedad != number :
 x=int(input())
 x=abs(x)
 tedad +=1
 a=math.sqrt(x)
 b=('%.15f'%a)
 print(b[:-11])
