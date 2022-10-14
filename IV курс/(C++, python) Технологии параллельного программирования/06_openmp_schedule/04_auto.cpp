#include <omp.h>
#include <stdio.h>
#include <windows.h>

#include <chrono>
#include <iostream>
#include <locale>
#include <thread>

using namespace std;
using namespace chrono_literals;

int main()

{
    setlocale(LC_ALL, "Russian");

    int i;

    double time = omp_get_wtime();

#pragma omp parallel private(i) num_threads(4)
    {
#pragma omp for schedule(auto)
        for (i = 0; i < 200; i++) {
            printf("Поток %d выполнила итерацию %d\n", omp_get_thread_num(), i);
            Sleep(100 * (omp_get_thread_num() + 1));
        }
    }

    cout << "Time = " << (omp_get_wtime() - time) << endl;
}