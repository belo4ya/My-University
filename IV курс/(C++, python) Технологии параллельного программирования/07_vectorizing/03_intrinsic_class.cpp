#include <dvec.h>

#include <iostream>

#define _INC_IOSTREAM 1

#define ALIGN __attribute__((aligned(32)))

using namespace std;

int main()

{
    F64vec4 A[4], B[4], C[4];

    int i, j;

    for (i = 0, j = 0; i < 16; i += 4, j++)

    {
        A[j] = F64vec4(i, i + 1, i + 2, i + 3);

        B[j] = F64vec4(i, i + 1, i + 2, i + 3);
    }

    for (int i = 0; i < 4; i++) C[i] = A[i] + B[i];

    for (int i = 0; i < 4; i++)

    {
        for (int j = 0; j < 4; j++)

        {
            cout << "C[" << i * 4 + j << "]=" << C[i][3 - j] << endl;
        }
    }

    return 0;
}