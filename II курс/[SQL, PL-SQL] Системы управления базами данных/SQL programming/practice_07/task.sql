-- 1
select JOB_ID from JOB_HISTORY
where (END_DATE - START_DATE) > 100
group by JOB_ID having count(EMPLOYEE_ID) > 3;

-- 2
select row_number() over (order by DEPARTMENT_ID), DEPARTMENT_ID, count(EMPLOYEE_ID)
from EMPLOYEES group by DEPARTMENT_ID;

-- 3
-- Создаем сотрудника с ID 115
insert into EMPLOYEES (
   EMPLOYEE_ID, FIRST_NAME, LAST_NAME,
   EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID,
   SALARY, COMMISSION_PCT, MANAGER_ID,
   DEPARTMENT_ID, BONUS
) select 115, FIRST_NAME, LAST_NAME,
   '115@email.com', PHONE_NUMBER, HIRE_DATE, JOB_ID,
   SALARY, COMMISSION_PCT, MANAGER_ID,
   DEPARTMENT_ID, BONUS from EMPLOYEES where SALARY < 6000 fetch next 1 row only;
select * from EMPLOYEES where EMPLOYEE_ID = 115;

update EMPLOYEES set SALARY = 8000 where EMPLOYEE_ID = 115 and SALARY < 6000;

delete from EMPLOYEES where EMPLOYEE_ID = 115 and SALARY = 8000;

-- 4
select * from ALL_CONSTRAINTS where TABLE_NAME like '%EMPLOYEE%';
select TABLE_NAME from ALL_CONSTRAINTS where CONSTRAINT_TYPE = 'R' and R_CONSTRAINT_NAME = 'DEPT_ID_PK';
select DEPARTMENT_ID from DEPARTMENTS order by DBMS_RANDOM.VALUE fetch first 2 row only;

update EMPLOYEES set DEPARTMENT_ID = (select DEPARTMENT_ID from DEPARTMENTS
    order by DBMS_RANDOM.VALUE fetch first row only)
where DEPARTMENT_ID = 20;
update JOB_HISTORY set DEPARTMENT_ID = null where DEPARTMENT_ID = 20;

-- 5
update EMPLOYEES set JOB_ID = (select JOB_ID from JOBS where upper(JOBS.JOB_ID) = 'IT_PROG')
where EMPLOYEE_ID = 110 and DEPARTMENT_ID = 10 and JOB_ID not like 'IT%';

-- 6

