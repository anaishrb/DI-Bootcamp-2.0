-- CREATE TABLE students (
--    id serial PRIMARY KEY,
--    last_name varchar(50),
--    first_name varchar(50),
--    birth_date date
--);

INSERT INTO students (id, first_name, last_name, birth_date) VALUES
    (1, 'Marc', 'Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')),
    (2, 'Yoan', 'Cohen', TO_DATE('03/12/2010', 'DD/MM/YYYY')),
    (3, 'Lea', 'Benichou', TO_DATE('27/07/1987', 'DD/MM/YYYY')),
    (4, 'Amelia', 'Dux', TO_DATE('07/04/1996', 'DD/MM/YYYY')),
    (5, 'David', 'Grez', TO_DATE('14/06/2003', 'DD/MM/YYYY')),
    (6, 'Omer', 'Simpson', TO_DATE('03/10/1980', 'DD/MM/YYYY')),
	
SELECT first_name, last_name FROM students;



