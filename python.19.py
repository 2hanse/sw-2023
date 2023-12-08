'''
num=int(input("(종료 '1')구구단 몇 단을 출력할까요 : "))

if num == 1 :
    for i in range(1) :
        for j in range(1,10,1):
            print(i,"*",j,"=",i*j)
            break;
        
elif num ==2 :
    for i in range(2,3,1) :
        for j in range(1,10,1):
            print(i,"*",j,"=",i*j)
            continue
    
'''

num=0
while num !=1:
    num=int(input("(종료'1') 구구단 몇 단을 출력할까요 : "))
    i=1

    while i<10:
        print(num, "*",i, "=", num*i)
        i=i+1
