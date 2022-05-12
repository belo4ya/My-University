-- Задача 1
-- Создайте запрос для отдела кадров, чтобы отобразить адреса всех отделов.
-- Используйте таблицы LOCATIONS и COUNTRIES. Покажите территориальное расположение,
-- улицу, город, государство или область, и страну на выходе.
-- Используйте NATURAL JOIN , чтобы отобразить результат.
select DEPARTMENT_NAME, STREET_ADDRESS,
       CITY, STATE_PROVINCE, COUNTRY_NAME from DEPARTMENTS
           natural join LOCATIONS
           natural join COUNTRIES;

-- Задача 2
-- Отделу кадров необходим отчёт обо всех сотрудниках. Создайте запрос, чтобы
-- отобразить фамилии, номера отделов и названия отделов для всех сотрудников.
select LAST_NAME, DEPARTMENT_ID, DEPARTMENT_NAME from EMPLOYEES natural join DEPARTMENTS;

-- Задача 3
-- Отделу кадров необходим отчёт обо всех сотрудниках в Торонто.
-- Отобразите фамилию, должность, номер отдела и название отдела для всех сотрудников,
-- которые работают в Торонто.
select LAST_NAME, JOB_TITLE, DEPARTMENT_ID, DEPARTMENT_NAME from EMPLOYEES
    natural join JOBS
    natural join DEPARTMENTS
    natural JOIN LOCATIONS
where CITY like 'Toronto';

-- Задача 4
-- Создайте отчёт, чтобы отобразить фамилии сотрудников и
-- номера сотрудников наряду с фамилиями их начальников и номерами
-- начальников. Назовите поля Employee, Emp#, Manager и Mgr#, соответственно.
select E.LAST_NAME "Employee",
       E.EMPLOYEE_ID "Emp#",
       M.LAST_NAME "Manager",
       M.EMPLOYEE_ID "Mgr#"
from EMPLOYEES E join EMPLOYEES M on E.MANAGER_ID = M.EMPLOYEE_ID;

-- Задача 5
-- Измените lab_05_04.sql, чтобы отобразить всех сотрудников,
-- включая King, у которых нет начальника. Отсортируйте результат
-- по номеру сотрудника.
select LAST_NAME, EMPLOYEE_ID from EMPLOYEES
where MANAGER_ID is null order by EMPLOYEE_ID;

-- Задача 6
-- Создайте отчёт для отдела кадров, чтобы отобразить фамилии сотрудников,
-- номера отделов и всех коллег сотрудников. Дайте каждому полю
-- соответствующее название.
select E.DEPARTMENT_ID, C.LAST_NAME EMPLOYEE, E.LAST_NAME COLLEGUE
from EMPLOYEES E join EMPLOYEES C on E.DEPARTMENT_ID=C.DEPARTMENT_ID
where C.LAST_NAME not like e.LAST_NAME order by E.DEPARTMENT_ID;

-- Задача 7
-- Отдел кадров нуждается в отчете относительно рабочих категорий и зарплат.
-- Чтобы ознакомить себя с таблицей  JOB_GRADES, сначала покажите структуру
-- таблицы JOB_GRADES. Создайте запрос, который показывает имя, должность,
-- название отдела, зарплату, и рабочую категорию для всех сотрудников.
select FIRST_NAME, JOB_TITLE, DEPARTMENT_NAME, SALARY,
       (select GRADE_LEVEL from JOB_GRADES
        where SALARY between LOWEST_SAL and HIGHEST_SAL) JOB_GRADE
from EMPLOYEES E
    join DEPARTMENTS D on D.DEPARTMENT_ID = E.DEPARTMENT_ID
    join JOBS J on E.JOB_ID = J.JOB_ID;

-- Задача 8
-- Отдел кадров хочет определить имена всех служащих, которые были
-- приняты на работу после Davies. Создайте запрос, чтобы отобразить
-- имя и дату приема на работу любого сотрудника, принятого после сотрудника Davies.
select LAST_NAME, HIRE_DATE from EMPLOYEES
where HIRE_DATE > (select HIRE_DATE from EMPLOYEES
                   where EMPLOYEES.LAST_NAME like 'Davies');

-- Задача 9
-- Отдел кадров должен найти имена и даты приема всех сотрудников,
-- которые были наняты перед их начальниками, наряду с именами их
-- начальников и датами приема.
select E.EMPLOYEE_ID, E.FIRST_NAME, E.LAST_NAME, E.HIRE_DATE, E.MANAGER_ID,
       M.EMPLOYEE_ID, M.FIRST_NAME, M.LAST_NAME, M.HIRE_DATE
from EMPLOYEES E join EMPLOYEES M on E.MANAGER_ID = M.EMPLOYEE_ID
where E.HIRE_DATE < (select M.HIRE_DATE from EMPLOYEES M where E.MANAGER_ID = M.EMPLOYEE_ID);
