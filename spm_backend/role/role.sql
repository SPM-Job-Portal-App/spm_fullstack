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
    ('Account Manager',	"The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analysing, and summarising sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organisation's products and services, as well as trends, developments and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused and persistent individual, who takes rejection as a personal challenge to succeed when given opportunity. He appreciates the value of long lasting relationships and prioritises efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily."),
    ('Admin Executive',	"Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, we’d like to meet you."),
    ('Call Centre',	"Call Centre Executive is responsible for providing assistance to customers by addressing their queries and requests. He/She advises customers on appropriate products and services based on their needs. He is responsible for the preparation of customer documentation. In the case of complex customer requests, he escalates them to senior officers. He is able to abide by safety and/or security standards in the workplace. The Call Centre Executive  pays strong attention to details to verify and process documentation. He also shows initiative and quick decision-making skills to provide excellent personalised customer services and support. He is comfortable with various stakeholder interactions whilst working in shifts and possesses adequate computer literacy to process customer documentation.");

    