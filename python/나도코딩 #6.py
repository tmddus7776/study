#_6) 함수 
def open_account():
    print("새로운 계좌가 생성되었습니다.") #호출하기 전까지 시행되지 않음!

open_account()

#_6) 전달값과 반환값
def deposit(balance, money): #입금함수
    print("입금이 완료되었습니다. 잔액은 %s 원입니다." %(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else: 
        print("출금이 불가능 합니다. 잔액은 {} 원입니다.".format(balance))
        return balance

balance = withdraw(balance, 200)

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료
    return commission, balance - money - commission #여러개 값을 ,로 구분하여 한번에 출력

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))

#_6) 기본값
def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile(name, age=17, main_lang="파이썬"): #기본값 설정
    print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
profile("유재석")
profile("김태호")

#_6) 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang= "파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호") #섞에서 써도 키워드 값으로 출력가능

#_6) 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 25, "한국어", "중국어", "영어", "일본어", "스페인어")
profile("김태호", 20, "한국어", "스페인어", "이탈리아어", "", "") #빈칸 처리/ 함수숫자 늘이는 방법

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 25, "한국어", "중국어", "영어", "일본어", "스페인어", "이탈리아어")
profile("김태호", 20, "한국어", "스페인어", "이탈리아어")

#_6) 지역변수와 전역변수
gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun을 사용
    gun = gun - soldiers #함수 안에서 설정된 값이므로 함수내에 설정해야함
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

#Quis_6) 표준 체중을 구하는 프로그램을 작성하시오.

#*표준체중 : 각 개인의 키에 적당한 체중
#(성별에 따른 공식)
#남자 : 키(m)*키(m)*22
#여자 : 키(m)*키(m)*21

#조건1 : 표준체중은 별도의 함수 내에서 계산
#        *함수명 : std_weight
#        *전달값 : 키(height), 성별(gender)
#조건2 : 표준체중은 소수점 둘째자리까지 표시

#(출력예제)
#키 175cm 남자의 표준체중은 67.38kg 입니다.

def std_weight(gender, height):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(gender, height / 100),2)
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))

