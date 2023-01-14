#include <iostream>

#include "omp.h"

using namespace std;

// ������� ������

struct node {
    int number;

    unsigned long int fib_number;

    struct node* next;
};

// ����������� ������� ���������� n-�� ����� ��������

int fibonacci(int n) {
    if (n < 2)

    {
        return (n);

    }

    else

    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// ������� ����������� ����������� �������� ��� ��������� ������

void independent_work(struct node* list) {
    int n;

    n = list->number;

    list->fib_number = fibonacci(n);
}

// ������� �������� � ������������� ������

struct node* init_list(int n) {
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

    {
        list = head_list;

        while (list != NULL)  // ������� ��������� ������

        {
            count++;

            list = list->next;
        }

        list = head_list;

        node** arrd = new node*[count];  // ��������� ������ ��� ������,
                                         // �������� ������ ��������� ������

        for (int i = 0; i < count;
             i++)  // ��������� � ������ ������� ��������� ������

        {
            arrd[i] = list;

            list = list->next;
        }

#pragma omp parallel num_threads(4)  // ������������ ��������� ��������� ������

        {
#pragma omp for schedule(runtime)

            for (int i = 0; i < count; i++)

            {
                independent_work(arrd[i]);
            }
        }
    }

    end = omp_get_wtime();

    list = head_list;

    while (list != NULL)  // ����� ��������� ������ � ������������ ������

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