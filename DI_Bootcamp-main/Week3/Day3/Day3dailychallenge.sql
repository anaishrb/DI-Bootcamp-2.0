--CREATE TABLE Customer (
--    id SERIAL PRIMARY KEY,
--    first_name VARCHAR(50) NOT NULL,
--    last_name VARCHAR(50) NOT NULL
--);

--CREATE TABLE Customer_profile (
--    id SERIAL PRIMARY KEY,
--    isLoggedIn BOOLEAN DEFAULT false,
--    customer_id INTEGER UNIQUE,
--    FOREIGN KEY (customer_id) REFERENCES Customer(id)
--);
INSERT INTO Customer (first_name, last_name) VALUES
    ('John', 'Doe'),
    ('Jerome', 'Lalu'),
    ('Lea', 'Rive');