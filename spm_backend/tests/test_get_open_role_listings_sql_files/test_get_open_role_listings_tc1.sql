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
    ('Alice', 'Smith', 'Engineering', 'Canada', 'alice.smith@example.com', 'Developer');

-- Create the role_skill table
CREATE TABLE skill (
    skill_name VARCHAR(50) PRIMARY KEY,
    skill_desc LONGTEXT
);

-- Insert data into the role_listing table
INSERT INTO skill (skill_name, skill_desc)
VALUES
    ('Applications Development', "Develop applications based on the design specifications");

-- Create the role table
CREATE TABLE role (
    role_name VARCHAR(50) PRIMARY KEY,
    role_desc LONGTEXT
);

-- Insert data into the role table
INSERT INTO role (role_name, role_desc)
VALUES
    ('Developer', "Write code all day everyday. Write code all day everyday. Write code all day everyday.");

-- Create the role_skill table
CREATE TABLE role_skill (
    role_name VARCHAR(50),
    skill_name VARCHAR(50),
    PRIMARY KEY (role_name, skill_name),
    FOREIGN KEY (role_name) REFERENCES role (role_name) ON DELETE CASCADE,
    FOREIGN KEY (skill_name) REFERENCES skill(skill_name) ON DELETE CASCADE
);

-- Insert data into the role_listing table
INSERT INTO role_skill (role_name, skill_name)
VALUES
    ('Developer', 'Applications Development');

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
    ('Developer', 'Canada', 'IT', True, '2023-10-01', '2023-10-15', 1);
    
