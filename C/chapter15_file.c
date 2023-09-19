#include<stdio.h>
#include<stdlib.h>

struct student {
	int num;
	char name[10];
	double gpa;
};

int main()
{
	//표준 입출력
	printf("%05d\n", 123); //-> 00123(빈칸에 0을 채움)
	printf("%+d\n", 123); //-> +123
	printf("%d\n", -123); //-> -123
	printf("%#x\n", 0x10); //-> 0x10(앞에 0x를 출력)
	printf("%5d\n", 123); //-> __123(폭은5, 우측정렬)
	printf("%-5d\n", 123); //-> 123__(폭은5, 좌측정렬)
	printf("%10.3f\n", 123.1234); //-> ___123.123(폭은10, 우측정렬)
	//형식지정자: %d(정수), %o(8진수), %x(16진수), %p(포인터)

	//scanf
	int a, b;
	char ca, cb;
	scanf("%3d%3d\n", &a, &b); //3글자씩 나눠 읽는다.
	scanf("%c %c\n", &ca, &cb); //띄어쓰기로 나눠 읽음. a (공백)b -> a b
	scanf("%c%c\n", &ca, &cb); //띄어쓰기 없이 읽음 a(공백)b -> a (공백)
	//문자형
	//%[abc] : 대괄호에 힜는 문자로만 이루어진 문자열을 읽는다.
	//%[^abc] : 대괄호에 있는 문자만 제외하고 읽는다.
	//%[0-9] : 0-9범위에 있는 문자를 읽는다.

	//파일입출력
	//텍스트 파일 쓰기모드로 열기
	FILE* fp = NULL;
	fp = fopen("test.txt", "w"); 
	if (fp == NULL) {
		printf("failed to open\n"); //파일을 여는 데 실패
		return -1;
	}
	fprintf(fp, "My name is BSY\n"); //파일에 입력
	fclose(fp);

	//텍스트 파일 읽기모드로 열기
	fp = fopen("test.txt", "r"); 
	//한단어씩 읽기
	char buff[100];
	while (fscanf(fp, "%s", buff) != EOF) { //fscanf(파일, "형식지정자", 문자열저장)
		printf("%s\n", buff);  //EOF: 파일끝(end of file)
	}
	fclose(fp);

	//한줄씩 읽기
	fp = fopen("test.txt", "r");
	char buff2[100];
	while (fgets(buff, 100, fp) != EOF) { //fgets(문자열저장, 문자열사이즈, 파일)
		printf("%s\n", buff);
	}
	fclose(fp);
	//정리(읽기, 쓰기) 
	// fgetc(fp) <-> fputc(size, fp) 
	// fgets(buf, size, fp) <-> fputs(buf, fp) 
	// fscanf(fp, "형식지정자", buf) <-> fprintf(fp, "형식지정자", buf)


	//이진파일 쓰기모드
	fp = fopen("test.txt", "wb");
	int buffer[5] = { 10, 20, 30, 40, 50 };
	fwrite(buffer, sizeof(int), 5, fp); //메모리 주소, 항목크기(int:4by), 항목개수, 파일
	flose(fp);

	//이진파일 읽기모드
	fp = fopen("test.txt", "rb");
	int buffer[5];
	fread(buffer, sizeof(int), 5, fp);
	fclose(fp);

	//구조체 읽고 쓰기
	struct student table[3] = {
		{1, "kim", 4.3},
		{2, "park", 4.5},
		{3, "choi", 3.2}
	};
	struct student s;
	fp = fopen("test.txt", "rb");
	fwrite(table, sizeof(struct student), 3, fp);
	fclose(fp);
	fp = fopen("test.txt", "wb");
	fread(&s, sizeof(struct student), 1, fp);


	//fseek()
	fseek(fp, 0, SEEK_SET); //파일의 처음으로 이동
	fseek(fp, 2, SEEK_SET); //파일의 시작점에서 2칸 이동
	fseek(fp, 0, SEEK_END); //파일의 끝지점으로 이동 
	fseek(fp, -1, SEEK_END); //파일의 끝지점에서 -1칸 이동

	return 0;
}
