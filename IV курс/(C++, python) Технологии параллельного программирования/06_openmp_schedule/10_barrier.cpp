#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

#pragma omp parallel

    {
        printf("Сообщение 1\n");

        printf("Сообщение 2\n");

#pragma omp barrier

        printf("Сообщение 3\n");
    }
}