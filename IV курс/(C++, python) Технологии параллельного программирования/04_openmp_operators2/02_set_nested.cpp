#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int n;

    omp_set_num_threads(3);

    omp_set_nested(1);  //��������� ������������� ��������� ������������
                        //�������� - ������������� ���������� ���������
#pragma omp parallel private(n)
    {
        n = omp_get_thread_num();  // ����������� ������ ������ �� �������
                                   // ������������ ������

        printf("������� ������������ ������ 1, ����� n=%d \n", n);

#pragma omp parallel
        {
            printf("��������� ������������ ������ 1, ����� %d - %d\n", n,
                   omp_get_thread_num());
        }
    }

    omp_set_nested(0);  //��������� ������������� ��������� ������������
                        //�������� - ���������� ���������� ���������

#pragma omp parallel private(n)
    {
        n = omp_get_thread_num();

        printf("������� ������������ ������ 2, ����� n=%d \n", n);

#pragma omp parallel
        {
            printf("��������� ������������ ������ 2, ����� %d - %d\n", n,
                   omp_get_thread_num());
        }
    }

    return 0;
}