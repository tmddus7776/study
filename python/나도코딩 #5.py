#_5 if

weather = input("오늘 날씨는 어떤가요?: ")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("오늘은 준비물이 필요 없습니다.")

temp = int(input("기온은 어떤가요? :"))
if temp >=30:
    print("너무 덥습니다. 나가지 마세요")
elif 30> temp >=10:
    print("괜찮은 날씨입니다.")
elif 10> temp >=0:
    print("조금 쌀쌀합니다. 겉옷을 챙겨주세요")
else:
    print("너무 춥습니다. 나가지 마세요.")

#_5 for 반복문
for waiting in range(1, 6):
    print("대기번호 : {0}".format(waiting)) #range 형태 1부터 50까지 반복
for waiting in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting)) #리스트 형태

starbucks = ["아이언맨", "토르", "캡틴 아메리카"]
for i in starbucks:
    print("{}님, 주문하신 커피가 나왔습니다.".format(i))


#_5 while 반복문
customer = "토르"
index = 5
while index >=1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -=1
    if index == 0:
        print("{0}님이 나타나지 않아 커피를 버립니다.".format(customer))

customer = "아이언맨"  #무한루프
index = 1
while True:
    print("{0}님, 주문하신 커피가 나왔습니다. 호출{1}회".format(customer, index))
    index +=1

customer = "토르"
person = "unknown"
while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되시나요? ")

#_5 continue와 break
absent = [2,5] #결석
no_book = [7]
for i in range(1,11):
    if i in absent:
        continue
    elif i in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 오세요".format(i))
        break
    print("{0}, 책을 읽어보세요.".format(i))

#_5 한줄 for
student = [1,2,3,4,5]
print(student)
student= [i+100 for i in student]
print(student)

students = ["lron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

students2 = ["lron man", "Thor", "Groot"]
students2 = [i.upper() for i in students2]
print(students2)

#Quis_5) 당신은 코코아 서비스를 이용하는 택시 기사님입니다.
#50명이 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

#조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
#조건2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭해야 합니다.

#(출력문 예제)
#[0] 1번째 손님 (소요시간 : 15분)
#...
#[ ] 50번째 손님 (소요시간 : 25분)

#총 탑승 승객 : 2분

from random import *
sum = 0
for i in range(1, 51):
    time = randint(5, 50)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        sum += 1
    else: 
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : %s분" %sum)








