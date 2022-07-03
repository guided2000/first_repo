#in this app asks the user for a some number as the age of people
# then returns the age of the oldest.
age_list=[]
while True:
    age= int (input())
    
    age_list .append(age)
    age_list.sort()
    
    if age==-1:
#when user inter "-1"stop loop
        print(age_list[-1])
        break
