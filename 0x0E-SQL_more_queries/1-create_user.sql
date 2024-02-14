-- Script that creates the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS @username@'%' IDENTIFIED BY @password;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO @username@'%' WITH GRANT OPTION;