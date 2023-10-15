-- Insert data into the AccessControl table
INSERT INTO access_control (access_id, access_control_name)
VALUES
    (1, 'Admin'),
    (2, 'User'),
    (3, 'Guest');

-- Insert data into the RoleApplication table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-10-14', 1, 1),
    ('2023-10-15', 2, 2),
    ('2023-10-16', 3, 3);

-- Insert data into the RoleListing table
INSERT INTO role_listing (role_name, country, dept, is_open, opening_date, closing_date, reporting_manager)
VALUES
    ('Manager', 'USA', 'HR', true, '2023-10-14', '2023-10-21', 1),
    ('Developer', 'Canada', 'IT', true, '2023-10-14', '2023-10-20', 2),
    ('Designer', 'UK', 'Creative', true, '2023-10-14', '2023-10-19', 3);

-- Insert data into the Role table
INSERT INTO role (role_name, role_description)
VALUES
    ('Manager', 'Manages the HR department.'),
    ('Developer', 'Develops software applications.'),
    ('Designer', 'Designs creative assets.');

-- Insert data into the Skill table
INSERT INTO skill (skill_name, skill_desc)
VALUES
    ('Management', 'Skills related to management and leadership.'),
    ('Programming', 'Programming languages and development tools.'),
    ('Design', 'Graphic design and creative skills.');

-- Insert data into the RoleSkill table
INSERT INTO role_skill (role_name, skill_name)
VALUES
    ('Manager', 'Management'),
    ('Developer', 'Programming'),
    ('Designer', 'Design');

-- Insert data into the Staff table
INSERT INTO staff (id, staff_first_name, staff_last_name, dept, country, email, role)
VALUES
    (1, 'John', 'Doe', 'HR', 'USA', 'john@example.com', 1),
    (2, 'Alice', 'Smith', 'IT', 'Canada', 'alice@example.com', 2),
    (3, 'Bob', 'Johnson', 'Creative', 'UK', 'bob@example.com', 3);

-- Insert data into the StaffSkill table
INSERT INTO staff_skill (staff_id, skill_name)
VALUES
    (1, 'Management'),
    (2, 'Programming'),
    (3, 'Design');