CREATE TABLE staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    staff_first_name VARCHAR(255) NOT NULL,
    staff_last_name VARCHAR(255) NOT NULL,
    dept VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    `role` INT NOT NULL,  -- Change data type to INT to match access_id
    FOREIGN KEY (`role`) REFERENCES access_control (access_id) ON DELETE CASCADE
);

