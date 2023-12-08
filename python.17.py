'''
i=0
j=1
for a in range(100):
    print(i)
    fibo= i+j
    i=j
    j=fibo
    if i>100:
        break
'''

i=0
j=1
fibo=0
while fibo <100:
    fibo = i+j
    print(fibo)
    i=j
    j=fibo
