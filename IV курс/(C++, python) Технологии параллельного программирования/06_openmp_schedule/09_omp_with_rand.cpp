#include <ctime>
#include <iostream>
#include <locale>

#include "omp.h"

using namespace std;

int main()

{
    double start, end;

    const int W = 10;

    int arr[W][W];

    start = omp_get_wtime();

#pragma omp parallel

    {
        srand(time(0) + omp_get_thread_num());

#pragma omp for schedule(dynamic, 6)

        for (int i = 0; i < W; ++i)

            for (int j = 0; j < W; ++j) arr[i][j] = rand() % 50;
    }

    end = omp_get_wtime();

    for (int i = 0; i < W; i++)

    {
        for (int j = 0; j < W; j++)

        {
            cout << arr[i][j];

            cout << ' ';
        }

        cout << "\n";
    }

    printf("Compute Time: %f seconds\n", end - start);
}