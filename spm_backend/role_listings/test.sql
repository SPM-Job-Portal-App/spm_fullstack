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
    ('John', 'Doe', 'Management', 'USA', 'john.doe@example.com', 'Manager'),
    ('Alice', 'Smith', 'IT', 'Canada', 'alice.smith@example.com', 'Developer'),
    ('Emma', 'Wilson', 'Design', 'UK', 'emma.wilson@example.com', 'Designer');

-- Create the role_listing table
CREATE TABLE role_listing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255) NOT NULL,
    skills VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    dept VARCHAR(255) NOT NULL,
    is_open BOOLEAN NOT NULL,
    reporting_manager INT,
    FOREIGN KEY (reporting_manager) REFERENCES staff(id) ON DELETE CASCADE
);

-- Insert data into the role_listing table
INSERT INTO role_listing (role_name, skills, country, dept, is_open, reporting_manager)
VALUES
    ('Manager', 'Leadership, Communication', 'USA', 'Management', true, NULL),
    ('Developer', 'Programming, Web Development', 'Canada', 'IT', false, 1),
    ('Designer', 'Graphic Design, UI/UX', 'UK', 'Design', true, 1);

-- Create the role_application table
CREATE TABLE role_application (
    id INT AUTO_INCREMENT PRIMARY KEY,
    application_date DATE NOT NULL,
    role_listing_id INT NOT NULL,
    staff_id INT NOT NULL,
    FOREIGN KEY (role_listing_id) REFERENCES role_listing(id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
);

-- Insert data into the role_application table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-09-15', 2, 2),
    ('2023-09-16', 3, 3),
    ('2023-09-16', 2, 1);