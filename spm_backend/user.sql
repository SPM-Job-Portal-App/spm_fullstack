-- Create the 'user' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS user;

-- Use the 'user' database
USE user;

-- Create a 'User' table
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Insert dummy data into the 'User' table
INSERT INTO user (username, email)
VALUES
    ('john_doe', 'john.doe@example.com'),
    ('jane_smith', 'jane.smith@example.com'),
    ('alice_wonderland', 'alice.wonderland@example.com');
