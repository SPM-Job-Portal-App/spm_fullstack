-- Create the role_listing table
CREATE TABLE role_listing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    dept VARCHAR(255) NOT NULL,
    is_open BOOLEAN NOT NULL,
    opening_date DATE,
    closing_date DATE,
    reporting_manager INT,
    FOREIGN KEY (role_name) REFERENCES role (role_name) ON DELETE CASCADE,
    FOREIGN KEY (reporting_manager) REFERENCES staff(id) ON DELETE CASCADE
);

-- Insert data into the role_listing table
INSERT INTO role_listing (role_name, country, dept, is_open, opening_date, closing_date, reporting_manager)
VALUES
    ('Consultant', 'USA', 'Sales', True, '2023-10-01', '2023-10-15', NULL),
    ('Developer', 'Canada', 'IT', False, '2023-10-01', '2023-10-15', 130001),
    ('Sales Manager', 'UK', 'Solutioning', True, '2023-10-01', '2023-10-15', 130001);
    
    