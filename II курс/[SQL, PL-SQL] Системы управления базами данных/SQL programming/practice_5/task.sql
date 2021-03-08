-- 1
select ROUND(MAX(SALARY)) "Maximum", ROUND(MIN(SALARY)) "Minimum",
       ROUND(SUM(SALARY)) "Sum", ROUND(AVG(SALARY)) "Average" from EMPLOYEES;

-- 2
select JOB_TITLE, ROUND(MAX(SALARY)) "Maximum", ROUND(MIN(SALARY)) "Minimum",
       ROUND(SUM(SALARY)) "Sum", ROUND(AVG(SALARY)) "Average" from EMPLOYEES natural join JOBS group by JOB_TITLE;

-- 3
select JOB_TITLE, COUNT(JOB_ID) "Total" from EMPLOYEES natural join JOBS group by JOB_TITLE order by "Total" desc;

-- 4
select JOB_ID, COUNT(JOB_ID) "Total" from EMPLOYEES where JOB_ID = :job_id group by JOB_ID;

-- 5
with t as
    (select MANAGER_ID, COUNT(MANAGER_ID) TOTAL from EMPLOYEES where MANAGER_ID is not  null group by MANAGER_ID)
select SUM(TOTAL) from t;

-- 6
select MAX(SALARY) - MIN(SALARY) "DIFFERENCE" from EMPLOYEES;

-- 7
select MANAGER_ID, MIN(SALARY) from EMPLOYEES
where MANAGER_ID is not null group by MANAGER_ID HAVING MIN(SALARY) > 6000;

-- 8
select COUNT(*),
       SUM(DECODE(EXTRACT(year from HIRE_DATE), 1995, 1)) "1995",
       SUM(DECODE(EXTRACT(year from HIRE_DATE), 1996, 1)) "1996",
       SUM(DECODE(EXTRACT(year from HIRE_DATE), 1997, 1)) "1997",
       SUM(DECODE(EXTRACT(year from HIRE_DATE), 1998, 1)) "1998"
from EMPLOYEES;

-- 9
select JOB_ID,
       SUM(DECODE(DEPARTMENT_ID, 20, SALARY)) "D20",
       SUM(DECODE(DEPARTMENT_ID, 50, SALARY)) "D50",
       SUM(DECODE (DEPARTMENT_ID, 80, SALARY)) "D80",
       SUM(DECODE (DEPARTMENT_ID, 90, SALARY)) "D90",
       SUM(SALARY)
FROM employees GROUP BY JOB_ID;
