-- 8-1

-- 2
SELECT ROUND(AVG(cost), 2) as "avg cost"
FROM d_events;

-- 3
SELECT TO_CHAR(ROUND(AVG(salary), 2), '$999999.99') as "avg salary"
FROM f_staffs
WHERE manager_id = 19;

-- 4
SELECT TO_CHAR(ROUND(SUM(salary), 2), '$999999.99') as "total salary"
FROM f_staffs
WHERE id in (12, 19);

-- 5
SELECT MIN(salary)    "lowest salary",
       MAX(hire_date) "most recent hire date",
       MIN(last_name) "top last name",
       MAX(last_name) "bottom last name"
FROM employees
WHERE department_id in (50, 60);

-- 9
SELECT AVG(NVL(order_total, 0)) as "Average"
FROM f_orders
WHERE order_date BETWEEN TO_DATE('January 1, 2002', 'fmMonth DD, YYYY')
          AND TO_DATE('December 21, 2002', 'fmMonth DD, YYYY');

-- 10
SELECT MAX(hire_date) as "the last"
FROM employees;

-- 8-2

-- 1
SELECT COUNT(*)
FROM d_songs;

-- 2
SELECT COUNT(DISTINCT venue_id)
FROM d_events;

-- 3
SELECT COUNT(song_id) AS "songs", COUNT(distinct cd_number) "dist songs"
FROM d_track_listings;

-- 4
SELECT COUNT(email) "emails"
FROM d_clients;

-- 5
SELECT (COUNT(*) - COUNT(auth_expense_amt)) "partners"
FROM d_partners;

-- 7
SELECT TO_CHAR(ROUND(AVG(NVL(auth_expense_amt, 100000)), 2), '$999999.99') as "total"
FROM d_partners;

/*Pract9-1*/
-- 2
-- A
SELECT manager_id, AVG(salary)
FROM employees
GROUP BY manager_id
HAVING AVG(salary) < 16000;
-- B
SELECT COUNT(*)
FROM d_cds
WHERE cd_number < 93;
-- C
SELECT type_code, MAX(TO_NUMBER(REPLACE(duration, ' min', ''))) || ' min' as "max duration"
FROM d_songs
WHERE duration IN ('3 min', '6 min', '10 min')
  AND id < 50
GROUP BY type_code;

-- 3
SELECT track, MAX(song_id)
FROM d_track_listings
WHERE track IN (1, 2, 3)
GROUP BY track;

-- 5
SELECT ROUND(MAX(AVG(salary)), 2) as "Max Value",
       ROUND(MIN(AVG(salary)), 2)    "Min Value"
FROM employees
GROUP BY department_id;

-- 6
SELECT AVG(MAX(salary)) "Avg Max Salary"
FROM employees
GROUP BY department_id;