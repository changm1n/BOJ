#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct StackType{
    int top;
    int stack[100000];
    int size;
} StackType;

void init(StackType *S){
    S -> top = -1;
}

int is_Empty(StackType *S){
    if (S -> top == -1){
        return 1;
    }
    else {
        return 0;
    }
}

int print_top(StackType *S){
    if (is_Empty(S) == 1){
        printf("-1\n");
    }
    else {
        printf("%d\n", S -> stack[S -> top]);
    }
}

void Push(StackType *S, int c){
    S -> top++;
    S -> stack[S -> top] = c;
    S -> size++;
}

void Pop(StackType *S){
    if (is_Empty(S) == 1){
        printf("-1\n");
    }
    else {
        printf("%d\n", S -> stack[S -> top]);
        S -> top--;
        S -> size--;

    }
}
int main(){
    StackType S;
    init(&S);
    int n = 0;
    int a = 0;
    char str[10];
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%s", str);
        if (strcmp(str, "top")==0){
            print_top(&S);
        }
        else if (strcmp(str, "size")==0) {
            printf("%d\n", S.size);
        }
        else if (strcmp(str, "pop")==0){
            Pop(&S);
        }
        else if (strcmp(str, "push")==0){
            scanf("%d", &a);
            Push(&S,a);
        }
        else if (strcmp(str, "empty")==0) {
            printf("%d\n",is_Empty(&S));
        }
    }
}

/*
 * 정수 입력하라고 했으니 변수를 int형으로 받을것.
 * \n 빼먹지 말기
 * 적어도 백준에 있는 예시는 테스트 해보기
 * string.h 쓴다면 strcmp 로 문자열 비교 가능
 * strcmp(문자열1, 문자열2)
 * 문자열 1 < 문자열 2 (아스키코드값 비교) 이면 음수
 * 문자열 1 > 문자열 2 면 양수
 * 문자열 1 == 문자열 2 면 0을 반환한다.
 * return 1 이라고 했다면 프린트하면 1 나옴
 *
 * */