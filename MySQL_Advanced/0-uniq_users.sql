-- Create the 'users' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    -- 'id' is an integer that cannot be null and will auto-increment with each new record
    id INT NOT NULL AUTO_INCREMENT,

    -- 'email' is a string with a maximum length of 255 characters
    -- It cannot be null and must be unique across the table
    email VARCHAR(255) NOT NULL UNIQUE,

    -- 'name' is a string with a maximum length of 255 characters
    -- It is allowed to be null
    name VARCHAR(255),

    -- Define 'id' as the primary key for the table
    PRIMARY KEY (id)
);
