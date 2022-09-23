#include <iostream>
#include <locale>

int main() {
  setlocale(LC_ALL, ".UTF8");
  printf("Seq 1\n");
#pragma omp parallel
  { printf("Concurrent\n"); }
  printf("Seq 2\n");
}
