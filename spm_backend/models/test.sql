-- Insert data into the role table
INSERT INTO role (role_name, role_desc)
VALUES
    ('Manager', "Lead the time all day everyday. Lead the time all day everyday. Lead the time all day everyday."),
    ('Developer', "Write code all day everyday. Write code all day everyday. Write code all day everyday."),
    ('Account Manager',	"The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. "),
    ('Admin Executive',	"Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries."),
    ('Call Centre',	"Call Centre Executive is responsible for providing assistance to customers by addressing their queries and requests. "),
    ('Consultant', "The Consultant is responsible for providing Sales technical expertise to the sales team and clients during the sales process. He/She delivers presentations and technical demonstrations of the organisation's products to prospective clients. "),
    ('Finance Director', "The Finance Director is the business partner for all the business units in an organisation.");   

-- Insert data into the role_application table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-09-15', 2, 2),
    ('2023-09-16', 3, 3),
    ('2023-09-16', 2, 1);

-- Insert data into the role_listing table
INSERT INTO role_listing (role_name, country, dept, is_open, opening_date, closing_date, reporting_manager)
VALUES
    ('Consultant', 'USA', 'Sales', True, '2023-10-01', '2023-10-15', NULL),
    ('Developer', 'Canada', 'IT', False, '2023-10-01', '2023-10-15', 1),
    ('Manager', 'UK', 'Solutioning', True, '2023-10-01', '2023-10-15', 1);

-- Insert data into the role_listing table
INSERT INTO role_skill (role_name, skill_name)
VALUES
    ('Developer', 'Applications Development'),
    ('Developer', 'Application Integration'),
    ('Consultant', 'Account Management'),
    ('Finance Director', 'Accounting and Tax Systems');

-- Insert data into the role_listing table
INSERT INTO skill (skill_name, skill_desc)
VALUES
    ('Account Management', "Manage, maintain and grow the sales and relationships with a specific customer or set of accounts. This includes in-depth customer engagement, relationship-building and provision of quality solutions and service to address customers' needs efficiently and generate revenue."),
    ('Applications Development', "Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components."),
    ('Application Integration', "Integrate data or functions from one application program with that of another application program - involves development of an integration plan, programming and the identification and utilisation of appropriate middleware to optimise the connectivity and performance of disparate applications across target environments"),
    ('Accounting and Tax Systems', "Implement accounting or tax software systems in the organisation");

-- Insert data into the staff table
INSERT INTO staff (staff_first_name, staff_last_name, dept, country, email, role)
VALUES
    ('John', 'Doe', 'Sales', 'USA', 'john.doe@example.com', 'Manager'),
    ('Alice', 'Smith', 'Engineering', 'Canada', 'alice.smith@example.com', 'Developer'),
    ('Emma', 'Wilson', 'Solutioning', 'UK', 'emma.wilson@example.com', 'Designer');