#include <iostream>

#include "omp.h"

using namespace std;

// Элемент списка

struct node {
    int number;

    unsigned long int fib_number;

    struct node* next;
};

// Рекурсивная функция вычисления n-го числа Фибоначи

int fibonacci(int n)

{
    if (n < 2)

    {
        return (n);

    }

    else

    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// Функция выполняющая независимое действие над элементом списка

void independent_work(struct node* list)

{
    int n;

    n = list->number;

    list->fib_number = fibonacci(n);
}

// Функция создания и инициализации списка

struct node* init_list(int n)

{
    struct node* list;

    struct node* head_list = NULL;

    struct node* temp = NULL;

    head_list = (struct node*)malloc(sizeof(struct node));

    list = head_list;

    list->number = 10;

    list->fib_number = 0;

    for (int i = 0; i < n; i++) {
        temp = (struct node*)malloc(sizeof(struct node));

        list->next = temp;

        list = temp;

        list->number = 10 + i;

        list->fib_number = 0;
    }

    list->next = NULL;

    return head_list;
}

int main(int argc, char* argv[]) {
    double start, end;

    struct node* list = NULL;

    struct node* temp = NULL;

    struct node* head_list = NULL;

    int count = 0;

    const int n = 36;

    head_list = init_list(n);

    start = omp_get_wtime();

#pragma omp parallel  // параллельная обработка элементов списка  с
                      // использованием task

    {
#pragma omp single nowait

        {
            list = head_list;

            while (list) {
#pragma omp task firstprivate(list)

                { independent_work(list); }

                list = list->next;
            }
        }
    }

    end = omp_get_wtime();

    list = head_list;

    while (list != NULL)  // Вывод элементов списка и освобождение памяти

    {
        printf("%d : %d\n", list->number, list->fib_number);

        temp = list->next;

        free(list);

        list = temp;
    }

    free(list);

    printf("Compute Time: %f seconds\n", end - start);

    return 0;
}