import numpy as np
import pandas as pd
print("기초============================================")
# 1. Series: 1차원 데이터 처리하기
a = pd.Series([4,-5,8,2])
print(a)
print(a.values) #-> 값만 확인
print(a.index) #-> 인덱싱만 확인 (시작, 끝, 스텝)
print(a.dtype)

print("\n설정============================================")
b = pd.Series([4,-5,8,2], index = ['a', 'b', 'c', 'd']) #->인덱싱 설정
print(b)
data = {"kim":1000, "park":2000, "choi": 3000} #-> 딕셔너리 형태
c = pd.Series(data)
c.name = "Salary" #-> 표이름 설정 
c.index.name = "Names" #-> 인덱스 이름 설정
print(c)

print("\nDataFrame=======================================")
# 2. Series: 2차원 데이터 처리하기
data2 = {'name':["kim", "kim", "park", "choi"],
        'class': [10, 20, 30, 40],
        'gpa': [2.5, 3.6, 4.2, 3.4]}
d = pd.DataFrame(data2)
print(d)
print(d.index) #-> 행방향 인덱스
print(d.columns) #-> 열방향 인덱스
print(d.values) #-> 행렬의 값만 출력
d.index.name = 'order' #-> 행이름
d.columns.name = 'info' #-> 열이름
print(d)
d2 = pd.DataFrame(data2, columns = ['class', 'name', 'gpa', 'penalty']) #->설정값이 없는 것은 Nan으로 채워짐
print(d2)
print(d2.describe()) #->숫자로 설정된 모든 데이터 값을 분석
print(d2['class'])
print(d2.name) #-> 결과값은 동일함
print(d2[['name', 'gpa']]) #-> name, gpa값만 출력
d2.penalty = [0,-1,-2,0] #-> 값 설정
print(d2)
val = pd.Series([1,1], index=[0,2]) #-> 새로운 열추가 Series 사용
d2['point'] = val
print(d2)
del d2['point'] #-> 열삭제
print(d2)

print("\nDataFrame_index==================================")
d2.index = [1,2,3,4]
print(d2)
print(d2[0:3]) #->0부터 2행 출력
print(d2.loc[2]) #-> 2행 출력
print(d2.loc[:, 'name']) #-> 모든 행의 이름만 출력
print(d2.loc[0:2, 'class':'gpa']) #-> data.loc[행범위, 열범위]
d2.loc[5,:] = [50, 'Jun', 4.5, -3] #->행삽입
print(d2)
print(d2.iloc[3]) #->인덱스값으로 가져오기
print(d2['gpa'] > 3.5)
print(d2.loc[d2['gpa'] > 3.5, :])
print(d2.loc[d2['name']=='kim', ['name','penalty']])

print("\nDataFrame_처리함수==================================")
e = pd.DataFrame(np.random.randn(6,4)) #-> pd.DataFrame(np.random.randn(m,n)): 랜덤으로 숫자 생성
print(e)
e.columns = ['A', 'B', 'C', 'D']
e.index = pd.date_range('20210701', periods = 6) #-> date_range('20211102', periods = N): 날짜를 써주는 함수
print(e)
e['F'] = [1,np.nan, 3, np.nan, 5, 6] #-> np.nan: nan값으로 설정
print(e)
print(e.dropna(how='any')) #-> df.dropna(how='any'): nan값 없애기 (any:행 값중 하나라도 nan이면 삭제, all:행의 모든 값이 nan이면 삭제)
print(e.fillna(value = 0)) #-> df.fillna(value = N): nan값 채우기
print(e.isnull()) #-> nan값인지 확인하여 boolean형태로 출력
print(e.loc[e.isnull()['F'],:]) #-> nan값인지 확인하여 행의 값 전부 출력
print(e.drop(pd.to_datetime('20210701'))) #-> data.drop(pd.to_datetime('날짜')): 특정 행 삭제
print(e.drop('F', axis=1)) #-> data.drop('열의 인덱스 이름', axis=1): 특정 열 삭제

print("\nDataFrame_분석함수==================================")
data = [[1,np.nan], [7,3], [np.nan, np.nan], [5, 2]]
df = pd.DataFrame(data, columns = ['one', 'two'], index = ['A', 'B', 'C', 'D'])
print(df)
print(df.sum(axis = 0)) #-> 행방향으로 합
print(df.sum(axis = 1)) #-> 열방향으로 합
print(df.sum(axis=1, skipna = False)) #-> skipna=False: nan값도 포함된 값은 nan으로 계산
print("열_one: ", df['one'].sum()) #-> 특정 행또는 열에 대해서 값 출력
print("행_B: ", df.loc['B'].sum())
