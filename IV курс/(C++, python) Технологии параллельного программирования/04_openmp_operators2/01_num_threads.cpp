#include <omp.h>
#include <stdio.h>
#include <windows.h>

#include <locale>

int main() {
    SetConsoleCP(1251);
    setlocale(LC_ALL, "Russian");
    SetConsoleOutputCP(1251);

    omp_set_num_threads(2);

#pragma omp parallel num_threads(3)

    { printf("������������ ������� 1\n"); }

#pragma omp parallel

    { printf("������������ ������� 2\n"); }

    return 0;
}