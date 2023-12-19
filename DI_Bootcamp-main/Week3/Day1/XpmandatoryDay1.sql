--CREATE TABLE item(
--	id serial PRIMARY KEY,
--	item_name varchar(50),
--	price numeric,
--	customers serial
-- );

INSERT INTO item (item_name, price) VALUES
    ('Small Desk', 100),
    ('Large Desk', 300),
    ('Fan', 80);

-- CREATE TABLE customers (
--    id serial PRIMARY KEY,
--    first_name varchar(50),
--    last_name varchar(50)
--);

INSERT INTO customers (first_name, last_name) VALUES
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson');
	
-- SELECT * FROM item;
-- SELECT * FROM item WHERE price > 80;
-- SELECT * FROM item WHERE price < 300;
-- SELECT * FROM customers WHERE last_name = 'Smith';
-- SELECT FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE first_name <> 'Scott';


