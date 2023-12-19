select * from city
inner join country
on city.country_id = country.country_id;

select city.city, country.country from city
inner join country
on city.country_id = country.country_id;

select customer.first_name, last_name, email, address_id from customer
inner join address
on customer.address_id = address.address_id
