#_4 리스트

#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "박명수", "조세호"]
print(subway)

#조세호가 몇 번쨰 칸에 타고 있는가?
print(subway.index("조세호"))

#하하가 다음정류장에서 탑승
subway.append("하하")   #맨 뒤에만 추가 가능
print(subway)

#정형돈을 2번째 자리에 입력
subway.insert(1, "정형돈")  #원하는 자리에 추가 가능
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형과 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)


#_4 사전
cabinet = {3:"철수", 100:"영희"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) 에러
print(cabinet.get(5)) #None으로 출력. 에러아님
print(cabinet.get(5, "사용가능"))

cabinet = {"A-3":"철수", "B-100":"영희"} #문자열로도 입력가능
print("A-3" in cabinet) #True/False
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "짱구" #기존 값 교체
cabinet["C-20"] = "영구"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#ket 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

#_4 튜플 -> 내용변경이나 추가 불가능하나 속도가 빠름

menu = ("돈까스", "우동")
print(menu[0])
print(menu[1])

#name = "철수"
#age = 20
#hobby = "코딩" 한번에 처리하기
(name, age, hobby) = "김종국", 20, "코딩"
print(name, age, hobby)

#_4 세트(집합.set) =>중복불가, 순서없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"철수", "영희", "짱구"}
python = set(["철수", "맹구"])

#교집합출력하기
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python)) #순서 랜덤

#차집합
print(java - python)
print(java.difference(python))

python.add("순이")  #추가
print(python)  

java.remove("철수")
print(java)

#_4 자료구조의 변경
menu = {"커피", "우유", "주스"} #set로 설정_{}
print(menu, type(menu)) 

menu = list(menu)
print(menu, type(menu)) #list로 바꿈_[]

menu = tuple(menu)
print(menu, type(menu)) #tuple로 바꿈_()

#Quiz_4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#추첨 프로그램을 작성하시오.

#조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
#조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복불가
#조건3 : random 모듈의 shuffle과 sample을 활용

#(출력예제)
#--- 당첨자 발표 ---
#치킨 당첨자 : 1
#커피당첨자 : [2, 3, 4]
#--- 축하합니다. ---


from random import*
lst = [1,2,3,4,5,6]
print(lst)
shuffle(lst) #lst를 섞어줌
print(lst)
print(sample(lst, 1)) #lst중에서 랜덤으로 n개를 뽑아줌

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#다른 방법 lst = range(1,21) ->type은 range이므로 list함수 사용 불가
#따라서 lst= list(range(1, 21)) 
shuffle(lst)
roopang = sample(lst, 4)

chicken = roopang[0]
coffee = roopang[1:4]
print(coffee)

print("--- 당첨자 발표 --- \n치킨 당첨자 :", chicken)
print("커피 당첨자 :", coffee) 
print("--- 축하합니다 ---")
#한번에 처리하기
#print("치킨 당첨자 :{}".format(lst[0]))















