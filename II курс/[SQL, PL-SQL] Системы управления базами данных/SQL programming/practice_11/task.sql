-- 6-3

-- 1
SELECT E.FIRST_NAME, E.LAST_NAME, d.DEPARTMENT_NAME
FROM EMPLOYEES E
         LEFT JOIN DEPARTMENTS D ON E.department_id = D.DEPARTMENT_ID;

-- 2
SELECT E.FIRST_NAME, E.LAST_NAME, d.DEPARTMENT_NAME
FROM EMPLOYEES E
         RIGHT JOIN DEPARTMENTS D ON E.department_id = D.DEPARTMENT_ID;

-- 3
SELECT E.FIRST_NAME, E.LAST_NAME, d.DEPARTMENT_NAME
FROM EMPLOYEES E
         FULL JOIN DEPARTMENTS D ON E.department_id = D.DEPARTMENT_ID;

-- 4
SELECT c.FIRST_NAME, c.LAST_NAME, E.event_date, E.description
FROM d_clients c
         LEFT JOIN d_events E USING (client_number);

-- 5
SELECT s.description as "description", sa.shift_assign_date as "date"
FROM f_shifts s
         LEFT JOIN f_shift_assignments sa USING (code);


-- 6-4

-- 1
SELECT E.LAST_NAME, E.employee_id as "Emp#", m.LAST_NAME as "Manager", m.employee_Id as "Mgr#"
FROM EMPLOYEES E
         JOIN EMPLOYEES m ON E.manager_id = m.employee_id;

-- 2
SELECT E.LAST_NAME, E.employee_id as "Emp#", m.LAST_NAME as "Manager", m.employee_Id as "Mgr#"
FROM EMPLOYEES E
         INNER JOIN EMPLOYEES m ON E.manager_id = m.employee_id
ORDER BY LAST_NAME;

-- 3
SELECT E.LAST_NAME, E.hire_date as "Emp Hired", m.LAST_NAME as "Manager", m.hire_date as "Mgr Hired"
FROM EMPLOYEES E
         LEFT JOIN EMPLOYEES m ON E.manager_id = m.employee_id
WHERE E.hire_date < m.hire_date
ORDER BY LAST_NAME;

-- 4
SELECT LAST_NAME, salary, department_id
FROM employees
START WITH FIRST_NAME || ' ' || LAST_NAME = 'Lex De Haan'
CONNECT BY PRIOR employee_id = manager_id;

-- 5
SELECT LAST_NAME, department_id, salary, employee_id, manager_id
FROM employees
START WITH LAST_NAME = 'King'
CONNECT BY manager_id = PRIOR employee_id;

-- 6
SELECT LPAD(LAST_NAME, LENGTH(LAST_NAME) + (LEVEL - 1) * 2, '—') as "organization chart"
FROM employees
START WITH LAST_NAME = (SELECT LAST_NAME from EMPLOYEES WHERE manager_id IS NULL)
CONNECT BY PRIOR employee_id = manager_id;

-- 7
SELECT LPAD(LAST_NAME, LENGTH(LAST_NAME) + (LEVEL - 1) * 2, '—') as "organization chart"
FROM employees
START WITH LAST_NAME = (SELECT LAST_NAME from EMPLOYEES WHERE manager_id IS NULL)
CONNECT BY PRIOR employee_id = manager_id
       AND LAST_NAME != 'De Haan';
