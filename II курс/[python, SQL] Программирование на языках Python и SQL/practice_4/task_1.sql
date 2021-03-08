set lc_time_names = 'ru_RU';  -- отображение даты на русском языке

-- 1
select concat_ws(
    ';',
    STUDENT_ID,
    ucase(SURNAME),
    ucase(NAME),
    STIPEND,
    KURS,
    ucase(CITY),
    date_format(BIRTHDAY, '%d/%m/%Y'),
    UNIV_ID
) as "RESULT" from student;

-- 2
select concat_ws(
    '; ',
    concat(substr(ucase(NAME), 1, 1), '.', ucase(SURNAME)),
    concat('место жительства-', ucase(CITY)),
    concat('родился - ', date_format(BIRTHDAY, '%d.%m.%y'), '.')
) as "RESULT" from student;

-- 3
select lcase(concat_ws(
    '; ',
    concat(substr(NAME, 1, 1), '.', SURNAME),
    concat('место жительства-', CITY),
    concat('родился: ', date_format(BIRTHDAY, '%d-%b-%Y'), '.')
)) as "RESULT" from student;

-- 4
select concat(
    ucase(left(NAME, 1)), substr(lcase(NAME), 2),
    ' ',
    ucase(left(SURNAME, 1)), substr(lcase(SURNAME), 2),
    ' родился в ',
    year(BIRTHDAY),
    ' году.'
) as "RESULT" from student;

-- 5
select SURNAME, NAME, STIPEND * 100 as "DREAM_STIPEND" from student;

-- 6
select concat(
    ucase(NAME),
    ' ',
    ucase(SURNAME),
    ' родился в ',
    year(BIRTHDAY),
    ' году.'
) as "RESULT" from student where KURS in (1, 2, 4);

-- 7
select concat_ws(
    '; ',
    concat('Код-', UNIV_ID),
    concat(ucase(UNIV_NAME), '-г.', ucase(CITY)),
    concat('Рейтиг=', RATING, '.')
) as "RESULT" from university;

-- 8
select concat_ws(
    '; ',
    concat('Код-', UNIV_ID),
    concat(ucase(UNIV_NAME), '-г.', ucase(CITY)),
    concat('Рейтиг=', round(RATING, -length(RATING) + 1), '.')
) as "RESULT" from university;
