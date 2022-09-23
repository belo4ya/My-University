#include <omp.h>
#include <stdio.h>
#include <time.h>

#include <iostream>
#include <locale>
using namespace std;

int main() {
  setlocale(LC_ALL, "Russian");
  // int a[10000], b[10000], c[10000];
  std::size_t array_size = 1000000000;
  int* a = new int[array_size];
  int* b = new int[array_size];
  int* c = new int[array_size];
  clock_t start_t, end_t, total_t;
  start_t = clock();
  printf("������ ����� ������������� �������� , start_t = %ld\n", start_t);
  for (int i = 0; i < array_size; i++) {
    a[i] = i;
    b[i] = i;
  }

  end_t = clock();
  printf("����� ����� ������������� �������� , end_t = %ld\n", end_t);

  total_t = end_t - start_t;
  cout << "����� ����� ������ ���������� �� ������������� �������� "
       << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

  start_t = clock();
  printf("������ ����� �������� �������� , start_t = %ld\n", start_t);

  for (int i = 0; i < array_size; i++) c[i] = a[i] + b[i];
  end_t = clock();
  printf("����� ����� �������� �������� , end_t = %ld\n", end_t);
  total_t = end_t - start_t;
  cout << "����� ����� ������ ���������� �� �������� �������� "
       << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

  delete[] a;
  delete[] b;
  delete[] c;
  return (0);
}