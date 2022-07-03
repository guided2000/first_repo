def maghsoom(a):
    c=0
##    a=int(input())
    for i in range(1,a+1):
        b=a%i
        if b==0:
            c+=1
    return(c)




list1=[]
c=0
list2=[]

while True:
    a=int (input ())
    javab=maghsoom(a)
    list2=[javab,a]
    list1.append(list2)
    list3=(max(list1))
    c=c+1
    if c==20:
        print(list3[1],list3[0])
##        print(list1)
        break

        

     
 

