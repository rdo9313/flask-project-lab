DROP TABLE IF EXISTS restaurants;

CREATE TABLE IF NOT EXISTS restaurants (
  id serial PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(255),
  category VARCHAR(255),
  rating DECIMAL,
  url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);