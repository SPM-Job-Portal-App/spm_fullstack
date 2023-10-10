CREATE TABLE staff_skill (
    staff_id INT NOT NULL,
    skill_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (staff_id, skill_name),
    FOREIGN KEY (staff_id) REFERENCES staff (id),
    FOREIGN KEY (skill_name) REFERENCES skill (skill_name)
);

