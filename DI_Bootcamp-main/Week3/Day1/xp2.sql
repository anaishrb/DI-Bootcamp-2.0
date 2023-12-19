-- CREATE TABLE students (
--    id serial PRIMARY KEY,
--    last_name varchar(50),
--    first_name varchar(50),
--    birth_date date
--);

--INSERT INTO students (id, first_name, last_name, birth_date) VALUES
--    (1, 'Marc', 'Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')),
--    (2, 'Yoan', 'Cohen', TO_DATE('03/12/2010', 'DD/MM/YYYY')),
--    (3, 'Lea', 'Benichou', TO_DATE('27/07/1987', 'DD/MM/YYYY')),
--    (4, 'Amelia', 'Dux', TO_DATE('07/04/1996', 'DD/MM/YYYY')),
--    (5, 'David', 'Grez', TO_DATE('14/06/2003', 'DD/MM/YYYY')),
--    (6, 'Omer', 'Simpson', TO_DATE('03/10/1980', 'DD/MM/YYYY')),
	
SELECT first_name, last_name FROM students;
SELECT first_name, last_name FROM students WHERE id = 2;
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE SUBSTRING(first_name, LENGTH(first_name) - 1, 1) = 'a';
SELECT first_name, last_name FROM students WHERE id IN (1, 3);



