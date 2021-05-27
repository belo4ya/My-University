-- Задача 1
-- Создайте запрос, чтобы показать текущую дату. Отобразите поле Дата.
select CURRENT_DATE from dual;

-- Задача 2
-- Отдел нуждается в отчете, который показывает номер сотрудника,
-- фамилию, зарплату, и увеличение зарплаты на 15.5 % (выраженная в
-- целом числе) для каждого сотрудника. Озаглавьте поле New Salary.
select EMPLOYEE_ID, LAST_NAME, SALARY, ROUND(SALARY * 1.155) NEW_SALARY from EMPLOYEES;

-- Задача 3
-- Измените свой запрос lab_03_02.sql, чтобы добавить поле, которое
-- вычитает старую зарплату из новой зарплаты. Озаглавьте поле Increase.
with TBL_WITN_NEW_SALARY as (select EMPLOYEE_ID, LAST_NAME, SALARY,
                                    ROUND(SALARY * 1.155) NEW_SALARY from EMPLOYEES)
select EMPLOYEE_ID, LAST_NAME, SALARY, NEW_SALARY, NEW_SALARY - SALARY INCREASE
from TBL_WITN_NEW_SALARY;
-- что эффективнее?
select EMPLOYEE_ID, LAST_NAME, SALARY, ROUND(SALARY * 1.155) NEW_SALARY,
       ROUND(SALARY * 1.155) - SALARY INCREASE
from EMPLOYEES;

-- Задача 4.1
-- Напишите запрос, который показывает фамилию (с первыми прописными буквами
-- и всеми другими строчными буквами) и длину фамилии для всех сотрудников,
-- фамилия которых начинается с букв J, A, или М. Дайте каждому полю
-- соответствующую метку. Отсортируйте результаты по фамилии сотрудников.
-- Эцио Аудиторе да Фиренце
select (UPPER(SUBSTR(LAST_NAME, 1, 1)) || LOWER(SUBSTR(LAST_NAME, 2))) "P_LAST_NAME",
       LENGTH(LAST_NAME) "LAST_NAME_LEN"
from EMPLOYEES where REGEXP_LIKE(UPPER(LAST_NAME), '^[JAM]') order by LAST_NAME;
-- LENGTH, LENGTH2, LENGTH4, LENGTHB, LENGTHC?

-- Задача 4.2
-- Перепишите запрос так, чтобы пользователь был вынужден ввести букву,
-- с которой начинается фамилия. Например, если пользователь вводит H,
-- то результат должен показать всех сотрудников, фамилия которых начинается с буквы H.
select (UPPER(SUBSTR(LAST_NAME, 1, 1)) || LOWER(SUBSTR(LAST_NAME, 2))) "P_LAST_NAME",
       LENGTH(LAST_NAME) "LAST_NAME_LEN"
from EMPLOYEES where UPPER(LAST_NAME) like UPPER(:first_letter) || '%' order by LAST_NAME;

-- Задача 4.3
-- Перепишите запрос так, чтобы пользователь был вынужден ввести букву,
-- с которой начинается фамилия. Например, если пользователь вводит h, то результат
-- должен показать всех сотрудников, фамилия которых начинается с буквы H.
select (UPPER(SUBSTR(LAST_NAME, 1, 1)) || LOWER(SUBSTR(LAST_NAME, 2))) "P_LAST_NAME",
       LENGTH(LAST_NAME) "LAST_NAME_LEN"
from EMPLOYEES where UPPER(LAST_NAME) like UPPER(:first_letter) || '%' order by LAST_NAME;

-- Задача 5
-- Отдел кадров хочет найти время работы каждого сотрудника.
-- Для каждого сотрудника, покажите фамилию и вычислите число месяцев
-- между сегодня и датой приема на работу. Озаглавьте поле MONTHS_WORKED.
-- Отсортируйте результат по количеству рабочих месяцев.
-- Округлите количество месяцев до самого близкого целого числа.
select LAST_NAME, HIRE_DATE, ROUND(MONTHS_BETWEEN(SYSDATE, HIRE_DATE)) "MONTHS_WORKED"
from EMPLOYEES order by MONTHS_WORKED desc;

-- Задача 6
-- Создайте отчет, который отображает следующее сообщение для каждого сотрудника:
-- <employee last name> earns <salary> monthly but wants <3 times salary>.
-- Озаглавьте поле Dream Salaries.
-- А эти задачки из ORACLE ACADEMY?
select LAST_NAME || ' earns ' || SALARY || ' monthly but wants ' || 3 * SALARY "Dream Salaries"
from EMPLOYEES;

-- Задача 7
-- Отобразите фамилию каждого сотрудника, дату приема на работу,
-- и дату выплаты зарплаты, которая является первым понедельником
-- после шести месяцев работы. Озаглавьте поле REVIEW. Отформатируйте даты,
-- чтобы дата отображалась в формате, подобном “понедельник, тридцать первого июля 2000.”
select LAST_NAME,
       TO_CHAR(HIRE_DATE,
               'DAY, DD MONTH YYYY',
               'nls_date_language=russian') "HIRE DATE",
       TO_CHAR(NEXT_DAY(ADD_MONTHS(HIRE_DATE, 6), 'Понедельник'),
               'DAY, DD MONTH YYYY',
               'nls_date_language=russian') "REVIEW"
from EMPLOYEES;

-- Задача 8
-- Отобразите фамилию, дату приема на работу, и день недели, в которую
-- начал работу сотрудник. Озаглавьте поле DAY. Отсортируйте результаты
-- по дням недели, начиная с понедельника.
select LAST_NAME, HIRE_DATE,
       TO_CHAR(HIRE_DATE, 'DAY', 'nls_date_language=russian') "DAY"
from EMPLOYEES order by TO_CHAR(HIRE_DATE, 'D');

-- Задача 9
-- Создайте запрос, который показывает фамилии сотрудников и процент комиссионных.
-- Если сотрудник не получает комиссионные, отобразите “No Commission.” Озаглавьте поле COMM.
select LAST_NAME, NVL(TO_CHAR(COMMISSION_PCT * 100), 'No Commission') "COMM" from EMPLOYEES;

-- Задача 10
-- Создайте запрос, который показывает первые восемь символов фамилий
-- сотрудников и указывает количество их зарплат со звездочками.
-- Каждая звездочка показывает тысячу долларов. Отсортируйте данные в
-- порядке убывания зарплаты. Озаглавьте поле EMPLOYEES_AND_THEIR_SALARIES.
select RPAD(SUBSTR(LAST_NAME, 1, 8), 8, ' ') ||
       RPAD('*', FLOOR(SALARY / 1000), '*') "EMPLOYEES_AND_THEIR_SALARIES"
from EMPLOYEES order by SALARY desc;

-- Задача 11
-- Используя функцию DECODE, напишите запрос, который
-- отображает уровень всех сотрудников, основанных на значениях
-- поля JOB_ID, используя следующие данные:
select LAST_NAME, JOB_ID,
       DECODE(JOB_ID, 'AD_PRES', 'A',
                      'ST_MAN', 'B',
                      'IT_PROG', 'C',
                      'SA_REP', 'D',
                      'ST_CLERK', 'E',
                      '0') "GRADE"
from EMPLOYEES;
