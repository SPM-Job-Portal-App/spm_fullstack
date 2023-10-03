-- Create the role table
CREATE TABLE role (
    role_name VARCHAR(50) PRIMARY KEY,
    role_desc LONGTEXT,
);

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

    