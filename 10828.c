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