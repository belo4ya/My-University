#include <iostream>
#include <string>

#include "omp.h"

using namespace std;

int main() {
    int x = 0;
#pragma omp parallel shared(x) num_threads(50)
    { x += 1; }
    cout << "x = " << x << endl;
    return 0;
}
