#_1 숫자형 자료
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*5)
print(3*3+1)

#_1 문자형 자료
print("풍선")
print('나비')
print("ㅋㅋㅋㅋㅋ")
print("ㅋ*5")

#boolean 자료_참/거짓
print(5<10)
print(5>10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))


#_1 변수
#ex) 애완동물을 소개해 주세요~
animal = "강아지"   #문자열은 ""에 입력
name = "연탄이"
age = 4
hobby = "산책"
is_adualt = age>=3

print("우리집 "+ animal +"의 이름은 "+ name +"에요")
print(""+ name +"는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print(""+ name +"는 어른일까요? "+ str(is_adualt))

print("우리집 "+ animal +"의 이름은 "+ name +"에요")
print(name, "는 ", (age), "살이며, ", hobby,"을 아주 좋아해요")
print(name,"는 어른일까요? ", is_adualt)
#,도 사용가능! +와 달리 ,는 문자형, 숫자형 구분 안해도 됨 
# 대신, ,는 띄어쓰기가 기본으로 설정됨 
# +는 +변수+가 기본 형태이므로 이렇게 작성해야 에러가 안남.
#,나 +사이의 문자열은 무조건 ""안에 넣어야 함.


# Quiz1) 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : xx행 열차가 들어오고 있습니다.

station = "사당"
print(station,"행 열차가 들어오고 있습니다.")
print(station + "행 열차가 들어오고 있습니다.")


