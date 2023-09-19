#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS
//구조체 선언
struct birth {
	int year;
	int month;
	int day;
};

//구조체 안에 구조체 포함
struct student {
	char name[100];
	int number;
	struct birth data;
};
struct point {
	int x;
	int y;
};

int main()
{
	//구조체 변수 선언
	struct student s1;
	printf("학번: ");
	scanf("%d", &s1.number); //구조체 멤버 전달
	printf("이름: ");
	scanf("%s", s1.name);
	s1.data.year = 21;
	s1.data.month = 11;
	s1.data.day = 2;
	printf("학번: %d, 생년월일: %d년 %d월 %d일\n", s1.number, s1.data.year, s1.data.month, s1.data.day);

	//배열과 구조체
	struct student list[2];
	list[0].number = 200;
	list[0].data.month = 5;
	printf("배열로 정의된 구조체 학번: %d, 태어난 달: %d\n", list[0].number, list[0].data.month);

	//포인터와 구조체
	struct point* p;
	struct point x_y = { 10, 20 };
	p = &x_y;
	printf("x = %d, y = %d\n", p->x, p->y);

	return 0;
}
