#include<stdio.h>
#include<stdlib.h>

int sub(int, int);
int add(int, int);

int values[] = { 52,43,60,19,28 };
int compare(const void* a, const void* b)
{
	return (*(int*)a - *(int*)b);
}

void print_equal(int a, int b, int (*func)(int, int))
{
	if (func(a, b)) // 함수 한번 더 호출
		printf("equal\n");
	else
		printf("different\n");
}
int abs_comp(int a, int b)
{
	return abs(a) == abs(b) ? 1 : 0;
}

int main()
{
	//이중포인터
	int i = 10;
	int* p = &i; // *p = 10
	int** q = &p; // **q = 10

	//포인터 배열
	int a = 10, b = 20, c = 30, d = 40, e = 50;
	int* pa[5] = { &a, &b, &c, &d, &e };
	int num;
	char* pc[] = {
		"apple",
		"banana",
		"orange"
	};
	num = sizeof(pc) / sizeof(pc[0]); // -> 배열 원소 개수 계산
	print("%s\n", pc[0]); // 출력은 배열 인덱스 값으로...

	//배열 포인터
	int b[3] = { 1,2,3 };
	int(*pb)[3] = &b; // (*pb): pb는 포인터 [3]:배열을 가리킴

	//함수 포인터
	int num1 = 10, num2 = 20, result;
	int (*pf)(int, int); // -> int값 2개를 인자로 받고 하나의 int값을 반환하는 함수를 (*pf)포인터로 가리킨다.
	pf = sub; // 함수 이름을 함수 포인터에 대입
	result = pf(num2, num1); // 함수 호출

	//함수 포인터의 배열
	int result_add, result_sub;
	int (*pf_arr[2])(int, int) = {add, sub}; // 배열 안에 함수의 주소가 저장됨.
	result_add = pf_arr[0](num1, num2);
	result_sub = pf_arr[1](num2, num1);

	//함수 인자로서의 함수 포인터
	int x = 30, y = -30;
	print_equal(x, y, abs_comp); // 함수 호출

	//qsort() 함수 사용하기
	//void qsort(정렬하고 싶은 배열 이름, 배열의 크기, sizeof(int ..), 호출할 함수 주소)
	qsort(values, 5, sizeof(int), compare);

	return 0;
}
int add(int a, int b)
{
	return a + b;
}

int sub(int a, int b)
{
	return a - b;
}

int main(int argc, char* argv[])
{
	//main() 함수의 인수
	// c:\cprogram> my name is BSY
	// argc = 4, argv[0] = 'my' argv[1] = 'name' argv[2] = 'is' argv[3] = 'BSY' 
	for (int i = 0; i < argc; i++) {
		printf("입력값: %s\n", argv[i]);
	}

	return 0;
}
