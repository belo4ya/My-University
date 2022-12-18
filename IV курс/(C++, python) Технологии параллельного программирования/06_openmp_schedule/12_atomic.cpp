#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int count = 0;

    omp_set_num_threads(50);

#pragma omp parallel

    {
#pragma omp atomic

        count++;
    }

    printf("Число потоков: %d\n", count);
}