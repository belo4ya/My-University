-- Задание 1
select SUBJ_ID, SUBJ_NAME, SEMESTER, HOUR from subject;

-- Задание 2
select * from exam_marks where SUBJ_ID = 12;

-- Задание 3
select KURS, SURNAME, NAME, STIPEND from student;

-- Задание 4
select SUBJ_NAME, HOUR from subject where SEMESTER = 4;

-- Задание 5
select distinct MARK descibe from exam_marks;

-- Задание 6
select SURNAME from student where KURS >= 3;

-- Задание 7
select SURNAME, NAME, KURS from student where STIPEND > 140;

-- Задание 8
select SUBJ_NAME from subject where HOUR > 30;

-- Задание 9
select * from university where RATING > 300;

-- Задание 10
select SURNAME, NAME, KURS from student
where STIPEND >= 100 and CITY like 'Воронеж';

-- Задание 11
SELECT *
FROM STUDENT
WHERE (STIPEND < 100 OR NOT
    (DATE_FORMAT(BIRTHDAY, '%d/%m/%y') >= '10/03/1980' AND
     STUDENT_ID > 1003));

-- Задание 12
SELECT *
FROM STUDENT
WHERE NOT ((DATE_FORMAT(BIRTHDAY, '%d/%m/%y') = '10/03/1980' OR
            STIPEND > 100) AND STUDENT_ID >= 1003);
