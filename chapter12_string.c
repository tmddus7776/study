#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main_12()
{
	//배열과 문자열
	char str[] = "Hello World";
	char dst[100];
	int i = 0;
	printf("str = %s\n", str);
	for (i; str[i] != NULL; i++) {
		dst[i] = str[i];
	}
	dst[i] = '\0'; //문자열의 마지막을 NULL로 설정 ('',작은 따옴표를 사용해야 함)
	printf("dst = %s\n", dst);

	//포인터와 문자열
	char* p = "Hello world"; //문자열은 임의의 공간에 저장되고 그 문자열의 주소만 가져와 p에 저장한다.
	printf("p = %s, &p = %p\n", p, p); 
	p = "Goodye";
	printf("p = %s, &p = %p\n", p, p); // hello world의 주소값과 goodbye의 주소값이 다름


	//문자 입출력 라이브러리
	//1. getchar(): 사용자로부터 문자를 입력받음, putchar(): 사용자로부터 입력받은 문자 출력 -> 문자열 아님. 문자 입출력
	int ch;
	//while ((ch = getchar()) != EOF) { //EOF: End Of File -> 정수형이므로 ch를 int형으로 받는다. EOF = ^d(종료)
	//	putchar(ch); //입력받을 때 엔터를 쳐야 출력됨 -> 키보드로 입력한 문자는 버퍼에 모아서 한번에 출력
	//}
	//버퍼를 사용하지 않는 것: _getch(), _putch()

	//2. gets_s(시작주소, 최대입력 크기 할당): 입력, puts():출력
	char name[100];
	printf("이름: ");
	gets_s(name, 100);  //한줄 입력받음
	puts(name);         //한줄 출력
	//gets() -> 입력크기를 할당받지 않아 해킹으로 악용됨. 즉 할당받지 않은 메모리에 값이 저장됨

	//문자처리 라이브러리 함수 -> 거짓이면 0, 참이면 아스키코드로 연결된 숫자??
	//isalpha(c): 영문자인가?
	//isupper(c): 대문자인가?
	//islower(c): 소문자인가?
	//isdigit(c): 숫자인가?(0-9)
	//isalnum(c): 영문자이나 숫자인가?
	//isxdigit(c): 16진수 숫자인가?
	//isspace(c): 공백문자인가?
	//ispunct(c): 구두점 문자인가?
	//isprint(c): 출력가능한 문자인가?
	//iscntrl(c): 제어문자인가?
	//isascii(c): 아스키코드인가?
	//toupper(c): 대문자로 바꾸기
	//tolower(c): 소문자로 바꾸기
	//toascii(c): 아스키코드로 바꾸기

	//문자열 입출력 라이브러리
	//strlen(s): 문자열 s의 길이를 구한다. 
	//strcpy(s1, s2): s2를 s1에 복사한다.
	//strcat(s1, s2): s2를 s1의 끝에 붙여넣는다.
	//strcmp(s1, s2): s1과 s2를 비교한다. -> 같으면 0을 반환 (s1 - s2)
	//strncpy(s1, s2, n): s2의 최대 n개 문자를 s1에 복사한다.
	//strncat(s1, s2, n): s2의 최대 n개 문자를 s1의 끝에 붙여넣는다.
	//strncmp(s1, s2, n): 최대 n개 문자까지 s1과 s2를 비교한다.       ->사이즈를 지정
	//strchr(s, c): 문자열 s에서 문자 c를 찾는다. -> c의 주솟값을 반환, 없으면 NULL값 반환
	//strstr(s1, s2): 문자열 s1에서 문자열 s2를 찾는다
	//strtok(s1, s2): s1을 s2를 기준으로 나눠라

	//문자열 수치변환
	char str[] = "100";
	float v;
	//sscanf(str, "%f", &v); -> 문자열을 수치로 변환
	//sprintf(str, "%f", v); -> 수치를 문자열로 변환


	return 0;
}
