-- 10-1

-- 3
select * from D_PLAY_LIST_ITEMS
where EVENT_ID = (select EVENT_ID from D_PLAY_LIST_ITEMS where SONG_ID = 45 fetch first row only);

-- 4
select * from D_EVENTS
where COST > (select COST from D_EVENTS where ID = 100 fetch first row only);

-- 5
select * from D_SONGS
where ID = (select CD_NUMBER from D_CDS where upper(TITLE) = upper('Party Music for All Occasions'));

-- 6
select * from D_EVENTS where THEME_CODE = (select CODE from D_THEMES where D_THEMES.DESCRIPTION = 'Tropical');

-- 7
select FIRST_NAME, LAST_NAME from F_STAFFS where SALARY > (select SALARY from F_STAFFS where ID = 12);

-- 8
select * from F_STAFFS
where STAFF_TYPE != (select STAFF_TYPE from F_STAFFS where FIRST_NAME = 'Bob' and LAST_NAME = 'Miller');

-- 9
select * from EMPLOYEES
where DEPARTMENT_ID = (select DEPARTMENT_ID from DEPARTMENTS where DEPARTMENT_NAME = 'IT');

-- 10
select * from DEPARTMENTS where LOCATION_ID = (select LOCATION_ID from LOCATIONS where CITY = 'Seattle');


-- 10-2

-- 1
select * from EMPLOYEES
where SALARY > (select SALARY from EMPLOYEES where LAST_NAME = 'Lorentz') and
      DEPARTMENT_ID = (select DEPARTMENT_ID from EMPLOYEES where LAST_NAME = 'Abel');

-- 2
select * from EMPLOYEES
where JOB_ID = (select JOB_ID from EMPLOYEES where LAST_NAME = 'Rajs') and
      HIRE_DATE > (select START_DATE from JOB_HISTORY
      where JOB_HISTORY.EMPLOYEE_ID = (select EMPLOYEE_ID from EMPLOYEES where LAST_NAME = 'Davies'));

-- 3
select * from D_EVENTS where THEME_CODE = (select THEME_CODE from D_EVENTS where ID = 100);

-- 4
select STAFF_TYPE from F_STAFFS
where SALARY < (select min(SALARY) from F_STAFFS where STAFF_TYPE = 'Cook' group by STAFF_TYPE);

-- 5
select DEPARTMENT_ID, avg(SALARY) from EMPLOYEES
group by DEPARTMENT_ID
having avg(SALARY) > (select SALARY from EMPLOYEES where LAST_NAME = 'Ernst');

-- 6
select DEPARTMENT_ID, min(SALARY) from EMPLOYEES
group by DEPARTMENT_ID
having min(SALARY) > (select min(SALARY) from EMPLOYEES where DEPARTMENT_ID != 50);

-- 10-3

-- 2
select * from D_SONGS where TYPE_CODE in (select CODE from D_TYPES where DESCRIPTION in ('Jazz', 'Pop'));

-- 3
select LAST_NAME from EMPLOYEES where SALARY in (select min(SALARY) from EMPLOYEES group by DEPARTMENT_ID);

-- 4
select * from F_STAFFS where SALARY = (select min(SALARY) from F_STAFFS);

-- 7
select DEPARTMENT_ID from EMPLOYEES
group by DEPARTMENT_ID
HAVING min(SALARY) >  (select min(SALARY) from EMPLOYEES where DEPARTMENT_ID < 50);

-- 8
select EMPLOYEE_ID, LAST_NAME from EMPLOYEES
where SALARY in (select min(SALARY) from EMPLOYEES group by DEPARTMENT_ID);

-- 9

with t as (
    select DEPARTMENT_ID, MANAGER_ID from EMPLOYEES where EMPLOYEE_ID = 41
)
select LAST_NAME, FIRST_NAME, DEPARTMENT_ID, MANAGER_ID from EMPLOYEES
where (DEPARTMENT_ID, MANAGER_ID) in (select t.DEPARTMENT_ID, t.MANAGER_ID from t);

-- 10
with t as (
    select DEPARTMENT_ID, MANAGER_ID from EMPLOYEES where EMPLOYEE_ID = 41
)
select LAST_NAME, FIRST_NAME, DEPARTMENT_ID, MANAGER_ID from EMPLOYEES
where DEPARTMENT_ID = (select DEPARTMENT_ID from t) and MANAGER_ID = (select MANAGER_ID from t);
