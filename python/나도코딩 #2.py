#_2 연산자
print(1+1) #덧셈
print(3-2) #뺄셈
print(2*10) #곱셈
print(6/2) #나눗셈

print(2**3)  #2^3이 나옴. **=^
print(5%3) # %는 나머지를 구할때 사용
print(5//3) # //는 몫을 구할때 사용

print(10>3) #True
print(4>=7) #False

print(3==3) # ==는 등호임
print(4==2) 
print(1 != 3) # !=은 같지 않다를 의미함. 

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True &=and

print((3>0) or (3>5)) #True, or은 하나만 만족하면 True
print((3>0) | (3>5))  # |는 or의 뜻을 가짐

#_2 수식
number = 2+3*4
print(number)
number = number + 2
number += 2 #두개 같은의미
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)

number %= 2
print(number)

#_2 숫자 처리 함수
print(abs(-5)) #abs = 절댓값
print(pow(4, 2)) #4^2
print(max(5, 12)) #최댓값
print(min(5, 12)) #최솟값
print(round(3.14)) #반올림
print(round(3.94))

from math import*
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근


#_2 랜덤함수
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값을 생성
print(random()*10) #0.0 ~ 10.0 미만의 값 생성
print(int(random()*10)) #0~10 미만의 값을 생성

print(int(random()*10) + 1) #1~10 이하의 값을 생성
print(int(random() * 45) +1) #1~45이하의 값을 생성

from random import *
print(randrange(1,46)) #randrange = 포함 미포함
print(randint(1, 45))  #randint = 포함 포함

# Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함.
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함.
# 조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

#(출력문) 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " +str(date)+ "일로 선정되었습니다.")
