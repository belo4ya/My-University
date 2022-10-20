#include <omp.h>
#include <stdio.h>

#include <iostream>

int main() {
    setlocale(LC_ALL, "Russian");

    double k = 0;

#pragma omp parallel num_threads(4) firstprivate(k)
    {
        printf("����� ���������� single 1 ��� nowait ����� %d \n",
               omp_get_thread_num());

#pragma omp single
        {
            // ������ ���� �������� ��� ����, ����� ����� �������� �����-������
            // ������

            for (int i = 0; i < 100000; i++)

            {
                k += (double)i / (i + 1);
            }

            printf("� ��������� single 1 ����� %d \n", omp_get_thread_num());
        }

        printf(
            "����� ��������� single 1 ��� nowait. ��� ��������� ������� �� "
            "����� ������ ����������, ������������ � ��������� single. k = %f "
            "����� %d \n",
            k, omp_get_thread_num());

#pragma omp barrier  // ������ ��������� �������������� ������, � ���������
                     // ������� ��� ����� �����������.

        printf("����� ���������� single 2 c nowait ����� %d \n",
               omp_get_thread_num());

#pragma omp single nowait
        {
            // ������ ���� �������� ��� ����, ����� ����� �������� �����-������
            // ������

            for (int i = 0; i < 100000; i++)

            {
                k += (double)i / (i + 1);
            }

            printf("� ��������� single 2 ����� %d \n", omp_get_thread_num());
        }

        printf(
            "����� ��������� single 2 c nowait. ��� ��������� ����� ���� "
            "������ ����������, ������������ � ��������� single. k =  %f ����� "
            "%d \n",
            k, omp_get_thread_num());
    }

    return 0;
}