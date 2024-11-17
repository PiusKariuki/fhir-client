-- Initialize a patient table
CREATE TABLE IF NOT EXISTS patient (
    id  SERIAL PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    birth_date DATE
);