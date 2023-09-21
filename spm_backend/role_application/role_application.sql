-- Create the role_application table
CREATE TABLE role_application (
    id INT AUTO_INCREMENT PRIMARY KEY,
    application_date DATE NOT NULL,
    role_listing_id INT NOT NULL,
    staff_id INT NOT NULL,
    FOREIGN KEY (role_listing_id) REFERENCES role_listing(id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
);

-- Insert data into the role_application table
INSERT INTO role_application (application_date, role_listing_id, staff_id)
VALUES
    ('2023-09-15', 2, 2),
    ('2023-09-16', 3, 3),
    ('2023-09-16', 2, 1);