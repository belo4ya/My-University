-- 21
select STUDENT_ID, SURNAME, STIPEND * 1.2 from student order by STIPEND desc;
select STUDENT_ID, SURNAME, STIPEND * 1.2 from student order by SURNAME;

-- 22
select STUDENT_ID, max(MARK), min(MARK) from exam_marks group by STUDENT_ID;

-- 23
select SEMESTER, SUBJ_NAME, SUBJ_ID from subject order by SEMESTER desc;
select SEMESTER, SUBJ_NAME, SUBJ_ID, HOUR from subject order by HOUR;

-- 24
select sum(MARK) as SUM_MARK from exam_marks group by EXAM_DATE order by SUM_MARK desc;

-- 25
select max(MARK) MAX_MARK from exam_marks
group by EXAM_DATE order by MAX_MARK desc;

select avg(MARK) AVG_MARK from exam_marks
group by EXAM_DATE order by AVG_MARK desc;

select min(MARK) MIN_MARK from exam_marks
group by EXAM_DATE order by MIN_MARK desc;

-- 26
select * from exam_marks
where STUDENT_ID = (select STUDENT_ID from student where lower(SURNAME) = 'иванов' limit 1);

-- 27
with t as (
    select STUDENT_ID from exam_marks
    where SUBJ_ID = 101 and MARK > (select avg(MARK) from exam_marks where SUBJ_ID = 101)
)
select NAME, SURNAME from student where STUDENT_ID in (select STUDENT_ID from t);

-- 28
with t as (
    select STUDENT_ID from exam_marks
    where SUBJ_ID = 102 and MARK < (select avg(MARK) from exam_marks where SUBJ_ID = 102)
)
select NAME, SURNAME from student where STUDENT_ID in (select STUDENT_ID from t);

-- 29
select count(*) from exam_marks group by STUDENT_ID having count(*) > 20;

-- 30
select STUDENT_ID, SURNAME from student s1
where STIPEND = (select max(STIPEND) from student s2 where s2.CITY = S1.CITY);

-- 31
select STUDENT_ID, SURNAME from student
where CITY not in (select distinct CITY from university);

-- 32
select * from student s left join university u on s.UNIV_ID = u.UNIV_ID
where s.CITY != u.CITY;

-- 33
select * from student s
where exists(select UNIV_ID from university u where s.UNIV_ID = u.UNIV_ID and u.RATING > 300);

-- 34
select s.* from student s join university u on s.UNIV_ID = u.UNIV_ID where RATING > 300;

-- 35
select * from student s
where exists(select u.UNIV_ID from university u where s.UNIV_ID != u.UNIV_ID and s.CITY = u.CITY);

-- 36
select SUBJ_NAME from subject subj
where exists(select EXAM_ID from exam_marks em1
             where subj.SUBJ_ID = em1.SUBJ_ID and em1.MARK > 2 and
                   (select count(*) from exam_marks em2
                    where em2.SUBJ_ID = subj.SUBJ_ID and
                          em1.MARK > 2 and
                          em2.STUDENT_ID != em1.STUDENT_ID)
                       > 1);

-- 37
select * from university
where RATING >= any (select RATING from university where upper(UNIV_NAME) = 'ВГУ')
  and upper(UNIV_NAME) != 'ВГУ';

-- 38
select * from student where CITY != all (select CITY from university);

select * from student where not (CITY = any (select CITY from university));

-- 39
select SUBJ_ID from exam_marks
where MARK > all (select MARK from exam_marks where SUBJ_ID = 105);

-- 40
select SUBJ_ID from exam_marks
where MARK > (select max(MARK) from exam_marks where SUBJ_ID = 105);
