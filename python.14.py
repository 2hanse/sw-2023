sum=0

for i in range(100):
    i+=1
    sum+=i
    print("n : ", i)
    print("sum : ", sum)
    if sum>1000:
        break
print("last n: ",i)
