#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct book {
	int num;
	char title[50];
};

typedef struct node {
	int score;
	struct node* next;
} node_t;

int main()
{
	//동적할당
	//integer
	int* list;
	list = (int*)malloc(3 * sizeof(int)); 
	list[0] = 10;
	list[1] = 20;
	list[2] = 30;
	free(list);

	//struct
	struct book* p;
	p = (struct book*)malloc(2 * sizeof(struct book)); //중간에 * 는 곱하기임
	p[0].num = 1;
	strcpy(p[0].title, "programming1");
	p[1].num = 2;
	strcpy(p[1].title, "programming2");
	free(p);

	//배열->문자열
	char* str[3];
	for (int i = 0; i < 3; i++) {
		str[i] = (char*)malloc(100 * sizeof(char)); // 100:문자열 길이
		if (str[i] == NULL) {
			printf("malloc 실패\n");
			return -1;
		}
		strcpy(str[i], "test");
	}

	//연결리스트
	//노드생성
	node_t* new_node;
	node_t* list_head = NULL;
	node_t* tmp;
	new_node = (node_t*)malloc(sizeof(node_t));
	new_node->next = NULL;
	new_node->score = 100;
	list_head = new_node;

	//노드연결
	new_node = (node_t*)malloc(sizeof(node_t));
	new_node->next = list_head;
	new_node->score = 200;
	list_head = new_node;

	//노드해제
	while (list_head) {
		tmp = list_head;
		list_head = list_head->next;
		free(tmp);
	}


	return 0;
}
