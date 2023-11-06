-- Insert dummy data into the RoleListing table
INSERT INTO role_listing (role_name, country, dept, is_open, opening_date, closing_date, reporting_manager) VALUES
    ('Consultant', 'USA', 'Sales', true, '2023-10-01', '2023-10-15', null),
    ('Developer', 'Canada', 'IT', false, '2023-10-01', '2023-10-15', 130001),
    ('Sales Manager', 'UK', 'Solutioning', true, '2023-10-01', '2023-10-15', 130001),
    ('Call Centre', 'UK', 'CEO', false, '2023-11-08', '2023-11-11', 140001),
    ('Admin Executive', 'Canada', 'Chairman', true, '2023-11-06', '2023-11-06', 190037);

-- Insert dummy data into the RoleApplication table
INSERT INTO role_application (application_date, role_listing_id, staff_id) VALUES
    ('2023-09-15', 2, 2),
    ('2023-09-16', 3, 3),
    ('2023-09-16', 2, 1);
