--1 select * from customer
--2 SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;
--3 select distinct create_date from customer 
--4 select * from customer order by first_name desc;
--5 select film_id, title, description, release_year 
--from film
-- ORDER BY rental_rate ASC;
-- 6 SELECT address.address, address.phone
--FROM customer
--JOIN address ON customer.address_id = address.address_id
--WHERE address.district = 'Texas';

--7 select * from film where film_id in (15, 150);

--10 select * from film 
-- order by rental_rate ASC
-- limit 10;

-- 11SELECT * FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10 ROWS
-- FETCH NEXT 10 ROWS ONLY;

-- 12 SELECT c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer c
-- JOIN payment p ON c.customer_id = p.customer_id
-- ORDER BY c.customer_id;

--13SELECT film.*
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id
-- WHERE inventory.film_id IS NULL;

-- 14 SELECT city.city, country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id;