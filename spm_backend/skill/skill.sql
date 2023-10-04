-- Create the role_skill table
CREATE TABLE skill (
    skill_name VARCHAR(50) PRIMARY KEY,
    skill_desc LONGTEXT
);

-- Insert data into the role_listing table
INSERT INTO skill (skill_name, skill_desc)
VALUES
    ('Account Management', "Manage, maintain and grow the sales and relationships with a specific customer or set of accounts. This includes in-depth customer engagement, relationship-building and provision of quality solutions and service to address customers' needs efficiently and generate revenue."),
    ('Applications Development', "Develop applications based on the design specifications; encompassing coding, testing, debugging, documenting and reviewing and/or refining it across the application development stages in accordance with defined standards for development and security. The complexity of the application may range from a basic application to a context-aware and/or augmented reality application that incorporates predictive behaviour analytics, geo-spatial capabilities and other appropriate algorithms. The technical skill includes the analysis and possibly the reuse, improvement, reconfiguration, addition or integration of existing and/or new application components."),
    ('Application Integration', "Integrate data or functions from one application program with that of another application program - involves development of an integration plan, programming and the identification and utilisation of appropriate middleware to optimise the connectivity and performance of disparate applications across target environments"),
    ('Accounting and Tax Systems', "Implement accounting or tax software systems in the organisation")