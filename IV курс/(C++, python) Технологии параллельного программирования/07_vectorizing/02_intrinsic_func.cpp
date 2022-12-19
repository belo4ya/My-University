#include <immintrin.h>

#include <iostream>

using namespace std;

int main()

{
    double __declspec(align(32)) A[16], B[16], C[16];

    for (int i = 0; i < 16; i++)

    {
        A[i] = i;

        B[i] = i;
    }

    for (int i = 0; i < 16; i += 4) {
        __m256d a = _mm256_load_pd(&A[i]);

        __m256d b = _mm256_load_pd(&B[i]);

        __m256d c = _mm256_add_pd(a, b);

        _mm256_store_pd(&C[i], c);
    }

    for (int i = 0; i < 16; i++)

    {
        cout << "C[" << i << "]=" << C[i] << endl;
    }

    return 0;
}