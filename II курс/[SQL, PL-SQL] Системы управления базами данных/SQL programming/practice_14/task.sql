-- 9-2

-- 1
select MANAGER_ID, JOB_ID, sum(SALARY) from EMPLOYEES group by rollup (MANAGER_ID, JOB_ID);

-- 2
select MANAGER_ID, JOB_ID, sum(SALARY) from EMPLOYEES group by rollup (JOB_ID), MANAGER_ID;

-- 3
select DEPARTMENT_ID, MANAGER_ID, JOB_ID, sum(SALARY) from EMPLOYEES group by (DEPARTMENT_ID, MANAGER_ID, JOB_ID);
select MANAGER_ID, JOB_ID, sum(SALARY) from EMPLOYEES group by (JOB_ID, MANAGER_ID);
select DEPARTMENT_ID, MANAGER_ID, sum(SALARY) from EMPLOYEES group by (DEPARTMENT_ID, MANAGER_ID);

-- 9-3

-- 2
select EMPLOYEE_ID, JOB_ID, HIRE_DATE from EMPLOYEES
    union
select EMPLOYEE_ID, JOB_ID, START_DATE from JOB_HISTORY;

-- 3
select EMPLOYEE_ID, JOB_ID, HIRE_DATE from EMPLOYEES
    union all
select EMPLOYEE_ID, JOB_ID, START_DATE from JOB_HISTORY
    order by EMPLOYEE_ID;

-- 4
select * from EMPLOYEES where EMPLOYEE_ID not in (select EMPLOYEE_ID from JOB_HISTORY) order by EMPLOYEE_ID;

-- 5
select * from EMPLOYEES where EMPLOYEE_ID in (select EMPLOYEE_ID from JOB_HISTORY);

-- 6
select EMPLOYEE_ID, JOB_ID, SALARY from EMPLOYEES
    union
select EMPLOYEE_ID, JOB_ID, SALARY from JOB_HISTORY natural join EMPLOYEES;
