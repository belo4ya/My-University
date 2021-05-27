/*Pract 4-1*/
-- Task 1
SELECT CONCAT('Oracle', CONCAT(CONCAT(' ', 'Internet'), CONCAT(' ', 'Academy'))) AS "The Best Class"
FROM dual;

-- Task 2
SELECT SUBSTR('Oracle Internet Academy', 13, 3)  AS "The Net"
FROM dual;

-- Task 3
SELECT LENGTH('Oracle Internet Academy')  AS "Length"
FROM dual;

-- Task 4
SELECT INSTR('Oracle Internet Academy', 'I')  AS "I Pos"
FROM dual;

-- Task 5
SELECT REPLACE(RPAD(LPAD('Oracle Internet Academy', 27, '*'),31,'*'),' ', '****')  AS "Result"
FROM dual;

-- Task 6
SELECT REPLACE('Oracle Internet Academy',' ', '$$$')  AS "Result"
FROM dual

-- Task 7
SELECT REPLACE('Oracle Internet Academy','Internet', '2013-2014')  AS "The Best Class"
FROM dual;

-- Task 8
SELECT order_date, LPAD(order_total, 7, '$') AS Total
FROM F_ORDERS;

-- Task 9
SELECT UPPER(first_name || ' ' || last_name || ' ' ||  address ||' '|| city ||', '|| state ||' '|| zip) AS Address
FROM F_CUSTOMERS;

-- Task 10
SELECT SUBSTR(first_name, 1, 1) || '.' || last_name "Name", salary, department_id
FROM employees
WHERE department_id = 20;

SELECT SUBSTR(first_name, 1, 1) || '.' || last_name "Name", salary, department_id
FROM employees
WHERE department_id = :department_id;

-- Task 11
SELECT department_id, department_name, location_id
FROM departments
WHERE LOWER(department_name)  = LOWER(:the_department_of_your_choice);

-- Task 12
SELECT first_name, last_name, hire_date, TO_CHAR(hire_date, 'MON') AS "Month"
FROM employees
WHERE TO_CHAR(hire_date, 'MON') = UPPER(:month);

/*Pract 4-2*/
-- Task 1
SELECT last_name, salary, ROUND(salary/1.55, 2) "Rounded Salary"
FROM employees
WHERE employee_id BETWEEN 100 AND 102;

-- Task 2
SELECT last_name, salary, TRUNC(salary * 1.0533, 2) "Truncated Salary"
FROM employees
WHERE department_id = 80;

-- Task 3
SELECT (CASE WHEN MOD(38873, 2) = 0 THEN 'even' ELSE 'odd' END) AS "Odd/Even"
FROM dual;

-- Task 4
SELECT ROUND(845.553, 1), ROUND(30695.348, 2), ROUND(30695.348, -2), TRUNC(2.3454, 1)
FROM dual;

-- Task 5
SELECT last_name, salary
FROM employees
WHERE MOD(salary, 3) = 0;

-- Task 6
SELECT MOD(34, 8) AS example
FROM dual;

-- Task 7
SELECT (565.784 - ROUND(565.784, 2)) * 1000 * (:ppl) AS diff
FROM dual;


/*Pract 4-3*/
-- Task 1
SELECT name, event_date, ROUND(MONTHS_BETWEEN(SYSDATE, event_date)) AS "number of months"
FROM d_events
WHERE name = 'Vigil wedding';

-- Task 2
SELECT TO_DATE('1-Sep-2020', 'dd-Mon-yyyy') - TO_DATE('30-May-2020', 'dd-Mon-yyyy') AS "Days",
ROUND(MONTHS_BETWEEN(TO_DATE('1-Sep-2020', 'dd-Mon-yyyy'), TO_DATE('30-May-2020', 'dd-Mon-yyyy')) * 30.5, 0) AS "Days 2"
FROM dual;

-- Task 3
SELECT TO_DATE('31-Dec-2021', 'dd-Mon-yyyy') - TO_DATE('01-Jan-2021', 'dd-Mon-yyyy') AS "year"
FROM dual;

-- Task 4
SELECT ROUND(SYSDATE, 'Month') AS "nearest first day of month", ROUND(SYSDATE, 'Year') AS "nearest first day of year",
TRUNC(SYSDATE, 'Month') AS "first day of current month", TRUNC(SYSDATE, 'Year') AS "first day of current year"
FROM dual;

-- Task 5
SELECT LAST_DAY(TO_DATE('01-Jun-2005', 'dd-Mon-yyyy')) AS "LAST_DAY"
FROM dual;

-- Task 6
SELECT first_name, last_name, ROUND(MONTHS_BETWEEN(SYSDATE, birthdate)/12) AS diff
FROM f_staffs
WHERE first_name || ' ' || last_name = 'Bob Miller'

-- Task 7
SELECT TO_CHAR(ADD_MONTHS(SYSDATE, 6), 'fmdd-Mon-yyyy (Day)') AS "Appointment"
FROM dual;

-- Task 8
SELECT TO_CHAR(LAST_DAY(SYSDATE),'fmdd-Mon-yyyy (Day)') AS "Deadline"
FROM dual;

-- Task 9
SELECT ROUND(MONTHS_BETWEEN(TO_DATE('01-01-2022','dd-mm-yyyy'),
TRUNC(TO_DATE('18-08-2021','dd-mm-yyyy')))) "Months"
FROM dual;

-- Task 10
SELECT TO_DATE('18-Aug-2021', 'dd-Mon-yyyy') AS "birthday", NEXT_DAY(TO_DATE('18-08-2021','dd-mm-yyyy'), 'Friday') AS "First Friday"
FROM dual;
