-- 7-1

-- 1
select *
from d_play_list_items,
     d_track_listings;

-- 2
SELECT *
FROM d_play_list_items d1,
     d_track_listings d2
WHERE d1.song_id = d2.song_id;

-- 3
SELECT d_songs.type_code, d_songs.title, d_types.description
FROM d_songs,
     d_types
WHERE d_songs.type_code = d_types.code;

-- 4
SELECT d_songs.type_code, d_songs.title, d_types.description
FROM d_songs,
     d_types
WHERE d_songs.type_code = d_types.code
  AND d_songs.id in (47, 48);

-- 5
SELECT *
FROM d_clients,
     d_events,
     d_job_assignments
WHERE d_clients.client_number = d_events.client_number
  AND d_events.id = d_job_assignments.event_id;

-- 6
SELECT d_track_listings.song_id, d_cds.title
FROM d_track_listings,
     d_cds
WHERE d_track_listings.cd_number = d_cds.cd_number;

-- 7-2
-- 1
SELECT ev.name, pck.code
FROM d_events ev,
     d_packages pck
WHERE (ev.cost BETWEEN pck.low_range AND pck.high_range);

-- 2
SELECT emp.last_name, emp.salary, jg.grade_level
FROM employees emp,
     job_grades jg
WHERE emp.salary BETWEEN jg.lowest_sal AND jg.highest_sal;

-- 7
SELECT cust.first_name || ' ' || cust.last_name "Customer Name", od.order_number, od.order_total, od.order_date
FROM f_customers cust
         LEFT JOIN f_orders od ON cust.id = od.cust_id;

-- 8
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees
         LEFT JOIN departments ON employees.department_id = departments.department_id;

-- 9
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees,
     departments
WHERE employees.department_id(+) = departments.department_id;

-- 10
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees,
     departments
WHERE employees.department_id = departments.department_id(+)
UNION
SELECT employees.last_name, employees.department_id, departments.department_name
FROM employees,
     departments
WHERE employees.department_id(+) = departments.department_id;

-- 11
SELECT d_cds.title, d_track_listings.song_id
FROM d_cds,
     d_track_listings
WHERE d_cds.cd_number = d_track_listings.cd_number(+);