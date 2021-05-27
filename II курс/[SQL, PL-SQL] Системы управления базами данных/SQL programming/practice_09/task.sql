/*Pract 5-1*/
-- Task 1
SELECT last_name, TO_CHAR(birthdate, 'Month DD, YYYY') AS "birthdate"
FROM f_staffs;

-- Task 2
SELECT TO_CHAR(TO_DATE('January 3, 04', 'Month DD YY'), 'DD-Mon-YYYY') AS res
FROM dual;

-- Task 3
SELECT 'The promotion began on the ' || TO_CHAR(start_date, 'ddTHSP "of" Month YYYY') AS res
FROM f_promotional_menus
WHERE code = 110;;

-- Task 4
SELECT 'Today is the ' || TO_CHAR(SYSDATE, 'ddTHSP "of" Month, Year') AS today
FROM dual;

-- Task 5
SELECT id, first_name, TO_CHAR(salary, '$999999.99') AS salary
FROM f_staffs;

-- Task 6
SELECT first_name, last_name, TO_CHAR(salary, '$999999.99') AS salary, TO_CHAR(salary + 2000, '$9999999.99') AS "New Salary"
FROM employees
WHERE first_name ||' '|| last_name = 'Ellen Abel';

-- Task 7
SELECT TO_CHAR(start_date, 'fmdd-Mon-YYYY (Day)') AS "date"
FROM f_promotional_menus
WHERE  code = 110;

-- Task 8
SELECT TO_CHAR(TO_DATE('25-Dec-2004', 'dd-Mon-yyyy'), 'Month ddth, yyyy') AS "date capitalize",
TO_CHAR(TO_DATE('25-Dec-2004', 'dd-Mon-yyyy'), 'MONTH DDth, yyyy') AS "date upper",
TO_CHAR(TO_DATE('25-Dec-2004', 'dd-Mon-yyyy'), 'ddth month, yyyy') AS "date lower"
FROM dual;

-- Task 9
SELECT code, TO_CHAR(low_range,'$999999.99') AS low_range, TO_CHAR(high_range,'$999999.99') AS high_range
FROM d_packages;

-- Task 10
SELECT TO_DATE('JUNE192004','fxMONTHddyyyy') AS "date"
FROM dual;


/*Pract 5-2*/
-- Task 1
SELECT name, start_date, end_date, NVL2(end_date, 'end in two weeks', TO_CHAR(SYSDATE, 'DD-Mon-YYYY')) AS res
FROM f_promotional_menus;

-- Task 2
SELECT last_name, NVL(overtime_rate, 0) AS "Overtime Status"
FROM f_staffs;

-- Task 3
SELECT last_name, TO_CHAR(NVL(overtime_rate, 5), '$99999999.99') AS "Overtime Status"
FROM f_staffs;

-- Task 4
SELECT last_name, NVL(manager_id, 9999) manager_id
FROM f_staffs;

-- Task 5
SELECT nullif(v_sal, 50) FROM emp;

-- Task 6
-- Если last_name не null значение, функция вернет last_name.
-- Если null вернет строку с manager_id

-- Task 7
-- A
SELECT first_name, last_name, TO_CHAR(hire_date, 'Month') as "month of hire"
FROM employees;
-- B
SELECT first_name, last_name, NULLIF(TO_CHAR(hire_date, 'Month'), 'September') as "month of hire"
FROM employees;

-- Task 8
SELECT first_name, NVL(specialty, 'No Specialty') as specialty
FROM d_partners;


/*Pract 5-3*/
-- Task 1
SELECT title,
CASE
WHEN TO_NUMBER(REPLACE(NVL(duration, '0 min'), ' min', '')) = 2 THEN 'shortest'
WHEN TO_NUMBER(REPLACE(NVL(duration, '0 min'), ' min', '')) = 10 THEN 'longest'
ELSE NVL(duration, '0 min') END AS "Play Times"
FROM d_songs;

-- Task 2
SELECT NVL(TO_CHAR(department_id), 'nullable') department_id , last_name, NVL(salary, 0) salary,
CASE department_id
WHEN 10 THEN 1.25 * NVL(salary, 0)
WHEN 90 THEN 1.5 * NVL(salary, 0)
WHEN 130 THEN 1.75 * NVL(salary, 0)
ELSE NVL(salary, 0)
END
as "New Salary"
FROM employees;

-- Task 3
SELECT first_name, last_name, manager_id, commission_pct,
COALESCE(manager_id, commission_pct, 99999)
as "Review"
FROM employees
WHERE department_id in (80, 90);
