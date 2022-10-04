#include <iostream>
#include <locale>
#include <string>

#include "omp.h"

using namespace std;
int main() {
    setlocale(LC_ALL, "Russian");
    int x = 0;
    printf("x в последовательной области (начало): %d\n", x);
#pragma omp parallel reduction(+ : x) num_threads(30)
    {
        printf("Значение x в потоке (на входе): %d\n", x);
        x += 1;
        printf("Значение x в потоке (на выходе): %d\n", x);
    }
    cout << "x = " << x << endl;
    return 0;
}