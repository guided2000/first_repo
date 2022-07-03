import random
a=1
b=99
c=0
while True:
    print("k=adad shoma bishtar ast\nb=adad shoma kamtarast\nd=robat dorost javab dad ast")
    print("yek adad dar nazar begirid")
    print("*=====*=====*=====*=====*=====*")
    while True:
        hads=  random.randint(a,b)
        print (hads)
        h= input("aya shoma in adadra dar nazar gerefte bodid:")
        if h =="k":
            a=hads+1
        elif h=="b":
            b=hads-1
        elif h=="d":
            print ("yuuuuuhuuu!!!man bordam!!!")
            print("*======*======*=====*=====*=====*")
            break
    z= input ("aya maielid dobareh bazi konid?  y/n:")
    if z=="y":
        continue
    elif z=="n":
        break