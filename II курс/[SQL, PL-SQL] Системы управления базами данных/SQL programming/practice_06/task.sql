-- 1
with T as (
    select DEPARTMENT_ID, LAST_NAME from EMPLOYEES where LOWER(LAST_NAME) = LOWER(:last_name)
)
select LAST_NAME, HIRE_DATE, DEPARTMENT_ID from EMPLOYEES
where DEPARTMENT_ID = (select DEPARTMENT_ID from t) and LAST_NAME != (select LAST_NAME from t);

-- 2
with T as (
    select AVG(SALARY) AVG_SALARY from EMPLOYEES
)
select EMPLOYEE_ID, LAST_NAME, SALARY from EMPLOYEES where SALARY > (select AVG_SALARY from t);

-- 3
with T as (
    select * from EMPLOYEES where LAST_NAME like '%u%'
)
select EMPLOYEE_ID, LAST_NAME from EMPLOYEES where DEPARTMENT_ID in (select DEPARTMENT_ID from t);

-- 4
with T as (
    select * from DEPARTMENTS where LOCATION_ID = 1700
)
select LAST_NAME, DEPARTMENT_ID, JOB_ID from EMPLOYEES where DEPARTMENT_ID in (select DEPARTMENT_ID from t);

-- 4.1
with T as (
    select * from DEPARTMENTS where LOCATION_ID = :dep_location
)
select  DEPARTMENT_ID, LAST_NAME, JOB_ID from EMPLOYEES where DEPARTMENT_ID in (select DEPARTMENT_ID from t);

-- 5
with T as (
    select DEPARTMENT_ID from EMPLOYEES where lower(LAST_NAME) = 'king' fetch first row only
)
select LAST_NAME, SALARY from EMPLOYEES where DEPARTMENT_ID = (select DEPARTMENT_ID from t);

-- 6
with T as (
    select DEPARTMENT_ID from DEPARTMENTS where lower(DEPARTMENT_NAME) = 'executive'
)
select * from EMPLOYEES where DEPARTMENT_ID = (select DEPARTMENT_ID from T fetch first row only);

-- 7
with T as (
    select DEPARTMENT_ID from EMPLOYEES where lower(LAST_NAME) like '%u%'
)
select EMPLOYEE_ID, LAST_NAME, SALARY from EMPLOYEES
where SALARY > (select avg(SALARY) from EMPLOYEES) and DEPARTMENT_ID in (select DEPARTMENT_ID from T);
