#_3 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요.
"""
print(sentence3)

#_3 슬라이싱
jumin = "001102-1234567"

print("성별 : " + jumin[7]) #[]필요한 값만 가져옴
print("연 : " + jumin[0:2]) #0번째부터 2번째 미만 자리까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
print("뒷 번호 : " + jumin[7:]) #7번째부터 끝까지
print("뒷 번호(뒤에서부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지


#_3 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #소문자 처리
print(python.upper()) #대문자 처리

print(python[0].isupper()) #대문자인지 판단 : True
print(len(python)) #문자열의 길이를 세줌
print(python.replace("Python", "Java")) #문자 교체

index = python.index("n")
print(index)  #첫번째n의 위치를 알려줌
index = python.index("n", index + 1)
print(index)  #두번째n의 위치를 알려줌

print(python.find("Java")) #find에서는 원하는 값이 없으면 -1
#print(python.index("Java")) #index에서는 원하는 값이 없으면 에러
print(python.count("n")) #count는 총개수를 세줌

#_3 문자열 포멧
print("a"+"b")
print("a", "b")

#방법1
print("나는 %d살입니다." %20) # %d = 정수값
print("나는 %s을 좋아해요." %"파이썬") # %s = 문자열
print("Apple은 %c로 시작해요." %"A") # %c = 문자
# %s 는 숫자도 입력받을 수 있음.
print("나는 %s살입니다." %20)
print("sksms %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법2
print("나는 {}살 입니다.".format(20))
print("sksms {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("sksms {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("sksms {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))

#방법4 
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f=변수에 저장된 값을 불러옴

#_3 탈출문자
print("백문이 불여일견\n백견이 불여일타")  #줄바꿈 : \n
print("저는 '나도코딩' 입니다.")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.") #\" \' : 문장 내에서 따옴표

#\\ : 문장 내에서 \
#print("C:\Users\tmddu\Desktop\파이썬") #->에러가발생
print("C:\\Users\\tmddu\\Desktop\\파이썬")

# \r: 커서를 맨 앞으로 이동
print("Red apple\rpine")

# \b: 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭-띄어쓰기
print("Red\tApple")


#Quiz_3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
#규칙1 : http:// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 +글자 개수+ 글자내"e" 개수 + "!"로 구성

url = "http://naver.com"
add = url[7:]
add = add.replace(".com", "")
#다른 방법 : add = add[:add.index(".")]
password = add[:3] + str(len(add)) + str(add.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

