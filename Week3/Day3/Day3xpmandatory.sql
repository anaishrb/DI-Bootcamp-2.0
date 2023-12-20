-- 1 select * from language
-- 2 SELECT film.title, film.description, language.name AS language_name
-- FROM film
--JOIN language ON film.language_id = language.language_id;


-- 3SELECT film.title, film.description, language.name AS language_name
--FROM language
-- LEFT JOIN film ON language.language_id = film.language_id;
 -- 4create table new_film(
--	 id serial PRIMARY KEY,
--	 name varchar(100)
 --);
 -- 5INSERT INTO new_film (name)VALUES
 --('Titanic'),
-- ('Point break'),
 -- ('La vie de Adele');
 
 -- 6create table customer_review(
--	 review_id serial primary key,
--	 film_id INT not null,
--	 language_id INT not null,
--	 review_title varchar(100),
--	 score INT CHECK (score >= 1 AND score <= 10),
--     review_text TEXT,
--     last_update TIMESTAMP,
 --    FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
 --    FOREIGN KEY (language_id) REFERENCES language(language_id)
--);

-- Insert into customer_review (film_id, language_id, review_title, score, review_text, last_update)
--values (1, 1, 'Good movie', 9, 'This movie was amazing', current_timestamp);

--Insert into customer_review (film_id, language_id, review_title, score, review_text, last_update)
--values (2, 2, 'Bad movie', 2, 'This movie was not good', current_timestamp);

--Exercice 2

--UPDATE film
--SET language_id = 3
--WHERE language_id = 1;
-- to drop the table we need to make sure we drop the right table cause once its done all the data is deleted
-- drop table if exists customer_review;
--SELECT COUNT(*) AS outstanding_rentals
--FROM rental
--WHERE return_date IS NULL;
--SELECT f.title AS movie_title, f.rental_rate AS movie_rental_rate
--FROM rental r
--JOIN inventory i ON r.inventory_id = i.inventory_id
--JOIN film f ON i.film_id = f.film_id
--WHERE r.return_date IS NULL
--ORDER BY f.rental_rate DESC
--LIMIT 30;

--SELECT f.*
--FROM film f
--JOIN film_actor fa ON f.film_id = fa.film_id
--JOIN actor a ON fa.actor_id = a.actor_id
--WHERE f.description ILIKE '%sumo wrestler%'
--AND (a.first_name ILIKE '%Penelope%' AND a.last_name ILIKE '%Monroe%');

SELECT *
FROM film
WHERE (title ILIKE '%boat%' OR description ILIKE '%boat%')
AND replacement_cost > 20.00; -- 
