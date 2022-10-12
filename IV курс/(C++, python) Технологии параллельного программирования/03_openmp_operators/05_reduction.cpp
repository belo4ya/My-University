#include <iostream>
#include <locale>
#include <string>

#include "omp.h"

using namespace std;
int main() {
    setlocale(LC_ALL, "Russian");
    int x = 0;
    printf("x � ���������������� ������� (������): %d\n", x);
#pragma omp parallel reduction(+ : x) num_threads(30)
    {
        printf("�������� x � ������ (�� �����): %d\n", x);
        x += 1;
        printf("�������� x � ������ (�� ������): %d\n", x);
    }
    cout << "x = " << x << endl;
    return 0;
}