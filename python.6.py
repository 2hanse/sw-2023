i=0
j=1
m=int(input("원하는 수열 항목 수 입력 > "))

for a in range(m):
    print(i,end="")
    fibo=i+j
    i=j
    j=fibo
