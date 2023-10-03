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
    ('Developer', 'Applications Development'),
    ('Developer', 'Application Integration'),
    ('Consultant', 'Account Management'),
    ('Finance Director', 'Accounting and Tax Systems')

