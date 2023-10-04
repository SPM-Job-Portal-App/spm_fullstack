-- Create the staff table
CREATE TABLE staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_first_name VARCHAR(255) NOT NULL,
    staff_last_name VARCHAR(255) NOT NULL,
    dept VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

-- Insert data into the staff table
INSERT INTO staff (staff_first_name, staff_last_name, dept, country, email, role)
VALUES
    ('John', 'Doe', 'Sales', 'USA', 'john.doe@example.com', 'Manager'),
    ('Alice', 'Smith', 'Engineering', 'Canada', 'alice.smith@example.com', 'Developer'),
    ('Emma', 'Wilson', 'Solutioning', 'UK', 'emma.wilson@example.com', 'Designer');