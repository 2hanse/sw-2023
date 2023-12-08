'''
com= random.radint(1,5)

for i in range(10):
    n=int(input("게임 %d회 : 컴퓨터가 생각한 숫자는 ? ",i))

if i == com:
    print("맞혔네요. 축하합니다 !!")
    break

else :
    print("아까워요. %d였는데요. 다시 해보세요.",com)
    continue
'''

import random
com,user = 0,0

for i in range(11):
    com = random.randint(1,5)
    print("게임",i,"회: ", end=" ")
    user=int(input("컴퓨터가 생각한 숫자는 ? "))
    if com == user :
        print("맞혔네요. 축하합니다 !!")
        break
    else:
        print("아까워요.", computer, "였는데요. 다시 해보세요.")
        continue

print("게임을 마칩니다.")














