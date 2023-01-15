DROP DATABASE user_db_ex1;
CREATE DATABASE user_db_ex1;
\c user_db_ex1;

CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   first_name VARCHAR(15) NOT NULL,
   last_name VARCHAR(15) NOT NULL,
   img_url VARCHAR
);

INSERT INTO users (first_name, last_name, img_url)
   VALUES
      ('Steven', 'Jones', 'https://cdn.britannica.com/63/12863-050-D12BEABD/Quahog.jpg?w=400&h=300&c=crop'),
      ('Clam', 'Stevenson', 'https://cdn.britannica.com/63/12863-050-D12BEABD/Quahog.jpg?w=400&h=300&c=crop'),
      ('Test', 'McElhaney', NULL);