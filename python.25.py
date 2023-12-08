coffee, money=10,0

while True:
    coffee-=1
    money=int(input("돈을 넣어주세요 : "))
    if coffee >0:
        if money > 300 :
            print("거스름돈",(money-300),"을 주고 커피를 줍니다.")
            print("남은 커피의 양은 %d개입니다." %coffee)

        elif money == 300:
            print("커피를 줍니다.")
            print("남은 커피의 양은 %d개입니다." %coffee)
                
        else :
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    else:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break;
