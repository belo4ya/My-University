#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int count;
    omp_set_num_threads(50);

#pragma omp parallel

    {
#pragma omp critical

        { count++; }
    }

    printf("Число потоков: %d\n", count);
}