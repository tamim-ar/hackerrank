#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    
    for (int i = 21; i <= N; i += 21) {
        printf("%d\n", i);
    }
    
    return 0;
}
