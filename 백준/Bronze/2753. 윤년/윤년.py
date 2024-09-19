a=int(input())

if (a%4==0 and a%100 !=0) or (a%400 == 0) :
    a = 1
else:
    a = 0

print(a)
    
    