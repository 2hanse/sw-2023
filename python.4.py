print("사이다 - 700원, 콜라 - 800원, 물 - 1200원")
money=int(input("얼마를 입력하겠습니까 : "))
drink = int(input("선택) 1- 사이다, 2- 콜라, 3- 물 : "))
print()

if drink == 1:
    if money < 700 :
        print("음료수를 뽑을 수 없습니다.")
        print("잔돈 %d원을 반환합니다." %money)
    else:
        print("사이다가 나왔습니다.")
        print("잔돈 %d원 반환합니다." %(money - 700))
          

elif drink == 2:
    if money < 800 :
        print("음료수를 뽑을 수 없습니다.")
        print("잔돈 %d원을 반환합니다." %money)
    else:
        print("'콜라가 나왔습니다.")
        print("잔돈 %d원 반환합니다." %(money-800))

else :
    if money < 1200 :
        print("음료수를 뽑을 수 없습니다.")
        print("잔돈 %d원을 반환합니다." %money)
    else:
        print("물이 나왔습니다.")
        print("잔돈 %d원 반환합니다." %(money - 1200))

