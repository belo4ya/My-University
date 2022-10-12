#include <omp.h>
#include <stdio.h>

#include <iostream>

int main() {
    int num;

    setlocale(LC_ALL, "Russian");

#pragma omp parallel num_threads(4) private(num)
    {
        num = omp_get_thread_num();

        printf("����� ���������� single num=%d \n", num);

#pragma omp barrier

#pragma omp single copyprivate(num)
        {
            printf("������� ����� ����� : ");

            scanf("%d", &num);

            printf("������� ����� : num=%d \n", num);
        }

        printf("����� ��������� single num=%d \n", num);
    }
}