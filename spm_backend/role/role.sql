CREATE TABLE role (
   role_name  VARCHAR(20) NOT NULL,
   skill_name VARCHAR(50) NOT NULL,
   description VARCHAR(50) NOT NULL,
   department VARCHAR(50) NOT NULL,
   PRIMARY KEY (role_name, skill_name)
);