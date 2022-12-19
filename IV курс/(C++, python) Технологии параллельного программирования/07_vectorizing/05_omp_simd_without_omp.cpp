#include <chrono>
#include <iostream>

using namespace std::chrono;

const int n = 6;

using namespace std;

auto start = high_resolution_clock::now();

int main()

{
    int i, j;

    float* a = new float[n * n];

    for (int i = 0; i < n * n; i++) a[i] = 1.0f;

    for (int k = 0; k < 1; k++)

    {
        for (int i = 1; i < 3; i++)

            for (int j = 0; j < n; j++)

            {
                a[n * i + j] =
                    a[n * i + j - (i + 1) - 1] /
                        (a[n * i + j - (i + 1)] * a[n * i + j - (i + 1)]) +
                    1;
            }

        for (int i = 3; i < n; i++)

#pragma omp simd safelen(4)

            for (int j = 0; j < n; j++)

            {
                a[n * i + j] =
                    a[n * i + j - (i + 1) - 1] /
                        (a[n * i + j - (i + 1)] * a[n * i + j - (i + 1)]) +
                    1;
            }
    }

    auto stop = high_resolution_clock::now();

    cout << "example2_vec" << endl;

    for (int i = 0; i < n; i++)

    {
        for (int j = 0; j < n; j++)

        {
            cout << a[i * n + j] << " ";
        }

        cout << endl;

        auto duration = duration_cast<microseconds>(stop - start);

        cout << "Time taken by function: "

             << duration.count() << " microseconds" << endl;
    }

    return 0;
}