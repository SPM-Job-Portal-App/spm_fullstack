-- Insert data into the Staff table
INSERT INTO staff (staff_first_name, staff_last_name, dept, country, email, role)
VALUES
    ('John', 'Doe', 'HR', 'USA', 'john@example.com', 'Manager'),
    ('Jane', 'Smith', 'IT', 'Canada', 'jane@example.com', 'Engineer'),
    ('Alice', 'Johnson', 'Finance', 'UK', 'alice@example.com', 'Accountant');

-- Insert data into the RoleListing table
INSERT INTO role_listing (role_name, skills, country, dept, is_open, opening_date, closing_date, reporting_manager)
VALUES
    ('HR Manager', 'HR skills', 'USA', 'HR', 1, '2023-10-01', '2023-10-15', 1),
    ('IT Engineer', 'IT skills', 'Canada', 'IT', 1, '2023-10-01', '2023-10-15', 2),
    ('Finance Accountant', 'Finance skills', 'UK', 'Finance', 1, '2023-10-01', '2023-10-15', 3);

-- Insert data into the RoleApplication table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-10-05', 1, 1),
    ('2023-10-06', 2, 2),
    ('2023-10-07', 3, 3);
