-- Create the role_listing table
CREATE TABLE role_listing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL,
    skills VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    dept VARCHAR(255) NOT NULL,
    is_open BOOLEAN NOT NULL,
    reporting_manager INT,
    FOREIGN KEY (role_name) REFERENCES role (role_name) ON DELETE CASCADE,
    FOREIGN KEY (reporting_manager) REFERENCES staff(id) ON DELETE CASCADE
);

-- Insert data into the role_listing table
INSERT INTO role_listing (role_name, skills, country, dept, is_open, reporting_manager)
VALUES
    ('Manager', 'Leadership, Communication', 'USA', 'Sales', True, NULL),
    ('Developer', 'Programming, Web Development', 'Canada', 'IT', False, 1),
    ('Designer', 'Graphic Design, UI/UX', 'UK', 'Solutioning', True, 1);