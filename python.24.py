import.random
count=0
dice1,dice2,dice3=0,0,0

while True:
    count +=1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    
    if (dice1 == dice2) and (dice2 == dice3) :
        print("3개 주사위는 모두 %d 입니다. " %dice1)
        print("같은 숫자가 나오기까지 %d번 던졌습니다." %count)
        break
