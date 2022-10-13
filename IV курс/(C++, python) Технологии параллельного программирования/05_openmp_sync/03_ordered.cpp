#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int i, n;

#pragma omp parallel private(i, n)
    {
        n = omp_get_thread_num();

#pragma omp for ordered
        for (i = 0; i < 5; i++) {
#pragma omp ordered
            { printf("ordered: ����� %d, �������� %d\n", n, i); }
        }
    }
}