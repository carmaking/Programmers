#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
    char* s = "수";
    char* p = "박";
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer = (char*)malloc(n * sizeof(char) * 3);
    strcpy(answer, "\0");
    
    for(int i=0; i < n; i++){
        if(i%2)
            strcat(answer, p);
        else
            strcat(answer, s);
    }
    
    return answer;
}
