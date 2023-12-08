
for i in range(1,11,1):
    money= int(input("돈을 넣어주세요 : "))
    if money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
        
    elif money == 300:
        print("커피를 줍니다.")
        
    elif money < 300 :
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        
    print("남은 커피의 양은 %d개 입니다." %(10 - i))
    print()

    if i==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
