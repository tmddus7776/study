import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
print(np.arange(10)) #-> 배열생성
print(arr.dtype) #-> int
print(arr.shape) #-> (6,):배열의 크기
print(arr.reshape(2,3)) #->배열크기 재설정
print(arr.reshape(2,3).T) #-> T: 행과 열의 크기를 바꿈 (다른것: np.transpose(arr), np.swapaxes(arr, 0, 1))

print("Z_O======================================")
print(np.zeros((3,5))) #-> 값이 전부 0
print(np.ones(10)) #-> 값이 전부 1

print("broadcasting=============================")
print(arr + arr)
print(arr.reshape(2,3) + np.arange(3))

print("indexing=================================")
print(arr[:]) #-> 모든 값 출력
print(arr[2:5]) #-> 인덱스 값이 2부터 4까지 출력
arr2 = np.arange(15).reshape(3,5)
print(arr2)
print(arr2[1,:]) #-> 1행의 모든 값 출력
print(arr2[:,2]) #-> 2열 모든 값 출력

print("boolean============================================")
arr3 = np.array(["kim", "kim", "park", "choi"])
data = np.random.randn(4,4) #-> 기댓값이 0이고 표준편차가 1인 정규분포를 따르는 난수를 랜덤 발생
print(arr3) 
print(arr3 == "kim") #-> kim인 값만 True
print(data)
print(data[arr3=="kim",:]) #-> kim값을 가진 인덱싱 값의 행만 출력
print(data[:,arr3=="kim"]) #-> kim값을 가진 인덱싱 값의 열만 출력
print(data[:,0] < 0) #-> 0번째 열중 0보다 작은 값을 boolean값으로 출력
print(data[data[:,0]<0,:]) #-> 0번째 열중 0보다 작은 값을 인덱싱으로 써서 출력

print("numpy_func=========================================")
print(np.abs(data)) #-> abs: 절댓값
print(np.sqrt(data)) #-> sqrt: 제곱근 -값을 가졌으면 nan
print(np.square(data)) #-> square: 제곱
print(np.exp(data)) #-> exp: 무리수 e의 지수로 삼은 값 
print(np.sign(data)) #-> sign: 부호
print(np.ceil(data)) #-> ceil: 소수 첫번째 자리에서 올림
print(np.floor(data)) #-> floor: 소수 첫번째 자리에서 내림
print(np.isnan(data)) #-> isnan: nan인경우 True 아닌경우 False
print(np.isinf(data)) #-> isinf: 무한대인 경우 True

#배열2개일 때 함수: add, subtract, multiply, divide, maximum, minimum
print("통계_func==========================================")
print("===arr1==")
print(arr)
print(np.sum(arr))
print(np.mean(arr)) #->평균
print(np.argmin(arr)) #-> 최소값의 인덱스
print(np.cumsum(arr)) #-> 누적합
print(np.cumprod(arr)) #-> 누적곱
print("===arr2===")
print(arr2)
print(np.sum(arr2, axis=0)) #-> 행간의 합
print(np.sum(arr2, axis=1)) #-> 열간의 합

print("졍렬_func==========================================")
arr4 = np.array([5,2,4,6,8, 6,3,7,5,4,1,0,3,5,9]).reshape(3,5)
print(arr4)
print(np.sort(arr4)[::-1]) #->?????
print(np.sort(arr4, axis=0)) #-> 열로 오름차순
print(np.sort(arr4, axis=1)) #-> 행으로 오름차순
