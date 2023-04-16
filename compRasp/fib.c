// A01732610 - Dafne Vania Peña Cortés

#include <stdio.h>

void fibonacci(int n) {
    int sig = 1;
    int curr = 0;
    int temp = 0;
    for (int x = 1; x <= n; x++) {
        printf("%d, ", curr);
        temp = curr;
        curr = sig;
        sig = sig + temp;
    }
    printf("%d", curr);
}

int main()
{
    printf("Los primeros 19 números de la serie Fibonacci son:\n");
    int n = 18;
    fibonacci(n);

    return 0;
}