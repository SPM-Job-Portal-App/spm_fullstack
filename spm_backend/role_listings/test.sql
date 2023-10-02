-- Insert data into the staff table
INSERT INTO staff (staff_first_name, staff_last_name, dept, country, email, role)
VALUES
    ('John', 'Doe', 'Sales', 'USA', 'john.doe@example.com', 'Manager'),
    ('Alice', 'Smith', 'Engineering', 'Canada', 'alice.smith@example.com', 'Developer'),
    ('Emma', 'Wilson', 'Solutioning', 'UK', 'emma.wilson@example.com', 'Designer');

-- Insert data into the role_listing table
INSERT INTO role_listing (role_name, skills, country, dept, is_open, reporting_manager)
VALUES
    ('Manager', 'Leadership, Communication', 'USA', 'Sales', True, NULL),
    ('Developer', 'Programming, Web Development', 'Canada', 'IT', False, 1),
    ('Designer', 'Graphic Design, UI/UX', 'UK', 'Solutioning', True, 1);

-- Insert data into the role_application table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-09-15', 2, 2),
    ('2023-09-16', 3, 3),
    ('2023-09-16', 2, 1);