-- Script to create database hbtn_0d_2 and user user_0d_2
-- Create user if not exists
-- Grant SELECT privilege to the user on the database
CREATE DATABASE IF NOT EXISTS @database_name;
CREATE USER IF NOT EXISTS @username@'%' IDENTIFIED BY @password;
GRANT SELECT ON @database_name.* TO @username@'%';