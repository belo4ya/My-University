#include <omp.h>
#include <stdio.h>

#include <locale>

int main() {
    setlocale(LC_ALL, "Russian");

    int n = 1;

    printf("Значение n в начале: %d\n", n);
#pragma omp parallel firstprivate(n)
    {
        printf("Значение n в потоке (на входе): %d\n", n);
        n = omp_get_thread_num();  //  Присвоим переменной n порядковый номер
                                   //  потока
        printf("Значение n в потоке (на выходе): %d\n", n);
    }
    printf("Значение n в конце: %d\n", n);
}