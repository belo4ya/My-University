#include <omp.h>
#include <stdio.h>

#include <iostream>

int main() {
    setlocale(LC_ALL, "Russian");

    double k = 0;

#pragma omp parallel num_threads(4) firstprivate(k)
    {
        printf("Перед директивой single 1 без nowait Поток %d \n",
               omp_get_thread_num());

#pragma omp single
        {
            // Данный цикл добавлен для того, чтобы поток выполнил какую-нибудь
            // работу

            for (int i = 0; i < 100000; i++)

            {
                k += (double)i / (i + 1);
            }

            printf("В директиве single 1 Поток %d \n", omp_get_thread_num());
        }

        printf(
            "После директивы single 1 без nowait. Это сообщение никогда не "
            "будет раньше предыдущих, напечатанных в директиве single. k = %f "
            "Поток %d \n",
            k, omp_get_thread_num());

#pragma omp barrier  // Данная директива синхронизирует потоки, в следующих
                     // лекциях она будет рассмотрена.

        printf("Перед директивой single 2 c nowait Поток %d \n",
               omp_get_thread_num());

#pragma omp single nowait
        {
            // Данный цикл добавлен для того, чтобы поток выполнил какую-нибудь
            // работу

            for (int i = 0; i < 100000; i++)

            {
                k += (double)i / (i + 1);
            }

            printf("В директиве single 2 Поток %d \n", omp_get_thread_num());
        }

        printf(
            "После директивы single 2 c nowait. Это сообщение может быть "
            "раньше предыдущих, напечатанных в директиве single. k =  %f Поток "
            "%d \n",
            k, omp_get_thread_num());
    }

    return 0;
}