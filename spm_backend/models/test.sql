-- Insert dummy data into the Access_control table
INSERT INTO access_control (access_id, access_control_name) VALUES
    (1, 'Admin'),
    (2, 'User'),
    (3, 'Manager'),
    (4, 'HR');

-- Insert dummy data into the Role table
INSERT INTO role (role_name, role_description) VALUES
    ('Admin', 'Administrator role'),
    ('Manager', 'Manager role'),
    ('Employee', 'Employee role');

-- Insert dummy data into the Skill table
INSERT INTO skill (skill_name, skill_desc) VALUES
    ('Programming', 'Programming skills'),
    ('Database Management', 'Database management skills'),
    ('Project Management', 'Project management skills');

-- Insert dummy data into the RoleSkill table
INSERT INTO role_skill (role_name, skill_name) VALUES
    ('Admin', 'Programming'),
    ('Manager', 'Project Management'),
    ('Employee', 'Database Management');

-- Insert dummy data into the Staff table
INSERT INTO staff (staff_first_name, staff_last_name, dept, country, email, role) VALUES
    ('John', 'Doe', 'IT', 'USA', 'john.doe@example.com', 1),
    ('Jane', 'Smith', 'HR', 'Canada', 'jane.smith@example.com', 2),
    ('Robert', 'Johnson', 'Sales', 'UK', 'robert.johnson@example.com', 3);

INSERT INTO staff_skill (staff_id, skill_name )
VALUES
    (2, "Project Management");

-- Insert dummy data into the RoleListing table
INSERT INTO role_listing (role_name, country, dept, is_open, opening_date, closing_date, reporting_manager) VALUES
    ('Admin', 'USA', 'IT', true, '2023-10-01', '2023-11-01', 1),
    ('Manager', 'Canada', 'HR', false, '2023-09-15', '2023-10-15', 2),
    ('Employee', 'UK', 'Sales', true, '2023-10-05', '2023-11-05', 3);

-- Insert dummy data into the RoleApplication table
INSERT INTO role_application (application_date, role_listing_id, staff_id) VALUES
    ('2023-10-02', 1, 1),
    ('2023-09-20', 2, 2),
    ('2023-10-06', 3, 3);
