-- Задание 1
select * from exam_marks where EXAM_DATE between '1999-01-10' and '1999-01-20';

-- Задание 2
select * from subject s join exam_marks em on s.SUBJ_ID = em.SUBJ_ID
where STUDENT_ID in (12, 32);

-- Задание 3
select SUBJ_NAME from subject where SUBJ_NAME like 'И%';

-- Задание 4
select * from student where NAME like 'И%' or NAME like 'С%';

-- Задание 5
select * from exam_marks where MARK is null;

-- Задание 6
select * from exam_marks where MARK is not null;