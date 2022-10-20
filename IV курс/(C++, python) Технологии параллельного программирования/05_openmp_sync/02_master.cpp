#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int n;

#pragma omp parallel private(n)
    {
        n = 1;

#pragma omp master

        { n = 2; }

        printf("������ �������� n ������ %d: %d\n", omp_get_thread_num(), n);

#pragma omp barrier

#pragma omp master
        { n = 3; }
        printf("������ �������� n ������ %d: %d\n", omp_get_thread_num(), n);
    }

    return 0;
}