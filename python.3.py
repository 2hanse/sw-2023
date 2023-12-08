gender=str(input("성별을 입력해 주세요 (남/여) : "))
age = int(input("나이를 입력해 주세요 : "))

if gender == "여" :
    if age >=30:
        print("적립 금액의 3배를 적립해드립니다.")
    elif age>=20:
        print("적립 금액의 2배를 적립해드립니다.")
    elif age<20:
        print("적립 금액의 1.5배를 적립해드립니다.")
else :
    print("적립 금액의 2배를 적립해드립니다.")
    
