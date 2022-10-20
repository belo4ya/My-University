#include <iostream>

#include "omp.h"

using namespace std;

// ������� ������

struct node {
    int number;  // ����� ����� �����

    unsigned long int fib_number;  // ����� ��������

    struct node* next;  // ��������� �� ��������� ������� ������

    //	node* next; // ��������� �� ��������� ������� ������
};

// ����������� ������� ���������� n-�� ����� ��������

int fibonacci(int n) {
    if (n < 2) {
        return (n);
    } else {
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

    // node* list;

    // node* head_list = NULL;

    // node* temp = NULL;

    head_list = (struct node*)malloc(sizeof(struct node));

    // head_list = new node();

    list = head_list;

    list->number = 10;

    list->fib_number = 0;

    for (int i = 1; i < n; i++) {
        //	temp = (struct node*)malloc(sizeof(struct node));

        temp = new node();

        list->next = temp;

        list = temp;

        list->number = 10 + i;

        list->fib_number = 0;
    }

    list->next = NULL;

    return head_list;
}

int main(int argc, char* argv[]) {
    struct node* list = NULL;

    struct node* temp = NULL;

    struct node* head_list = NULL;

    int count = 0;

    const int n = 36;  // ����� ��������� � ������

    head_list = init_list(n);  // ������������� ������

    double time = omp_get_wtime();

    list = head_list;

    while (list !=
           NULL)  // �������� ���� �� ���������� �������� ��� ���������� ������

    {
        independent_work(list);

        list = list->next;
    }

    time = omp_get_wtime() - time;

    list = head_list;

    while (list != NULL)  // ����� ��������� ������ � ������������ ������

    {
        printf("%d : %d\n", list->number, list->fib_number);

        temp = list->next;

        free(list);

        list = temp;
    }

    head_list = NULL;

    cout << "Time=" << time << endl;
}