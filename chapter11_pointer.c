#include<stdio.h>
void swap(int* a, int* b);
void add(int*b, int size);

int main_11()
{
	//포인터 선언
	int x = 10;
	int* p = NULL; //변수의 주소를 저장하는 포인터, 초기화
	p = &x; // 포인터에 변수 x의 주소를 입력(&:주소를 반환)
	*p = 20; //포인터가 가리키는 주소로 가서 값을 20으로 바꿔라!(*:포인터가 가리키는 곳의 내용을 반환)
	printf("%p\n", &x); // x의 주소 출력 = 0x20
	printf("%p\n", p); //p에 저장된 값(주소) 출력 =0x20
	printf("%d\n", x); //x의 값 출력 = 20
	printf("%d\n", *p); //p가 가리키는 주소의 값 출력 = 20
	//추가 정보: char(1바이트), int(4바이트), float(4바이트), double(8바이트)
	// p의 주소값 출력 -> %u, %d, %p 사용 가능
	
	//포인터 연산
	char* pc;
	int* pi;
	double* pd;
	pc = (char*)1000; //포인터 형변환 -> 포인터의 주소값을 임의로 1000으로 한다.
	pi = (int*)1000;
	pd = (double*)1000;
	printf("pc = %p, pi = %p, pd = %p\n", pc, pi, pd);
	// 포인터 안에 저장된 주소값을 각각 증가(주소값이 증가한 값은 변수형마다 다름)
	pc++; // -> 1001
	pi++; // -> 1004
	pd++; // -> 1008
	printf("pc = %p, pi = %p, pd = %p\n", pc, pi, pd);
	// 다른 연산자
	(*p)++; //포인터가 가리키는 값의 증가
	printf("(*p)++ = %d\n", *p);
	
	//*p++; //포인터의 주소값 증가
	//*++p; // 포인터의 주소값 증가
	++* p; // 포인터가 가리키는 값의 증가

	//참조에 의한 호출(call by regerence) vs 값에 의한 호출(call by value)
	int a = 10, b=20;
	swap(&a, &b); // 주소를 전달한다.

	//포인터와 배열
	int arr[] = { 1,2,3,4,5 };
	int* p_arr;
	p_arr = arr; // 포인터에 배열 저장
	p_arr[0] = 10;
	p_arr[1] = 20; //포인터를 통해 배열의 원소를 변경할 수 있다.
	printf("p[0] = %d, p[1] = %d, p[2] = %d, p[3] = %d, p[4] = %d\n", p_arr[0], p_arr[1], p_arr[2], p_arr[3], p_arr[4]);
	add(p_arr, 5);
	printf("p[0] = %d, p[1] = %d, p[2] = %d, p[3] = %d, p[4] = %d\n", p_arr[0], p_arr[1], p_arr[2], p_arr[3], p_arr[4]);
}

void swap(int* pa, int* pb) //공간에 와서 작업을 함.
{
	int tmp; // int형 변수
	tmp = *pa; // tmp에 pa의 값을 저장
	*pa = *pb;
	*pb = tmp;
}

void add(int *b, int size) // 포인터 매개변수
{
	b[2] = 30;
	b[3] = 40;
	b[4] = 50;
}
