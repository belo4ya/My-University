#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

#pragma omp parallel

    {
        printf("��������� 1\n");

        printf("��������� 2\n");

#pragma omp barrier

        printf("��������� 3\n");
    }
}