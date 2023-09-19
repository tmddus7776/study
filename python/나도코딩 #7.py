#_7) 표준입출력
print("python", "java", sep=" vs ") #sep는 중간에 ,를 넣어줌 원래는 띄어쓰기!
print("python", "java", sep=", ", end="?")
print("무엇이 더 재미있을까요?") #연결되어서 나옴

import sys
print("python", "java", file=sys.stdout) #표준출력_잘출력
print("python", "java", file=sys.stderr) #표준에러_확인해서 프로그램코드 수정해야함!

scores = {"수학": 0, "영어": 50, "코딩": 100} #items는 key, value 전부 출력
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽 정렬 8칸 띄어쓰기, 오른쪽 정렬 4칸 확보

for number in range(1, 21):
    print("대기번호 : " + str(number).zfill(3)) #3자리수로 만들기 값이 없으면 0으로 채운다.

answer = input("아무 값이나 입력하세요 : ") #무조건 문자열로 받음
print(type(answer)) 
print("입력하신 값은 " + answer + "입니다.")

#_7) 다양한 출력 포맷
print("{0: >10}".format(500)) #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >+10}".format(500)) #양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >-10}".format(500))
print("{0:_<+10}".format(500)) #왼쪽 정력하고, 빈칸을 _로 채움
print("{0:,}".format(10000000000)) #세 자리마다 콤마 찍기
print("{0:+,}".format(10000000000))#세 자리마다 콤마 찍기, 부호 포함
print("{0:-,}".format(10000000000))
print("{0:^<+30,}".format(100000000000)) #세 자리마다 콤마 찍기, 부호 포함, 자리수 확보
print("{0:f}".format(5/3)) #소수점 출력
print("{0:.2f}".format(5/3)) #소수점 특정 자릿수 만큼만 출력(소수점 3번째 자리에서 반올림)

#_7) 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") #utf8은 한글을 읽는 능력임
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #w는 쓰기, a는 고쳐쓰기
score_file.write("과학 : 80") #줄바꿈이 없음
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기 동작 실시, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline()) #한줄씩 읽기 동작
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #리스트 형태로 저장 모든 텍스트 출력
for line in lines:
    print(line, end="")
score_file.close

#_7) pickle
import pickle
profile_file = open("profile.pickle", "wb") #pickle에서는 w=wb이고, encoding은 설정하지 않아도 됨
profile = {"이름":"박명수", "나이": 30, "취미":["축구", "야구", "농구"]}
print(profile)
pickle.dump(profile, profile_file) #profile의 정보를 file에 저장가능
profile_file.close()

import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #file의 정보를 profile에 불러오기:load
print(profile)
profile_file.close

#_7) with
import pickle
with open("profile.pickle", "rb") as profile_file: #file을 profile_file로 저장
    print(pickle.load(profile_file)) #load로 file열기, close사용 필요 없음

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요") #파일에 문장넣기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

#_Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
#보고서는 항상 아래와 같은 형식으로 출력되어야 합니다.

# ---x주차 주간보고---
#부서:
#이름:
#업무요약:

#1주차부터 50주차까지 보고서 파일을 만드는 프로그램을 작성하시오.
#조건: 파일명은 '1주차.txt'...와 같이 만들어야 함.
for i in range(1, 51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as week_file:
        week_file.write("---{0}주차 주간보고---".format(i))
        week_file.write("\n부서 : ")
        week_file.write("\n이름 : ")
        week_file.write("\n업무요약 : ")
      