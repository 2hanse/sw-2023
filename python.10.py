n=int(input("N의 숫자를 입력 : "))
sum=0

for step in range(1,n+1,2):
    sum=sum+step
print("'1~%d까지 홀수의 합은 %d입니다." %(n,sum))
