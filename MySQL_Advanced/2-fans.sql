-- Create the 'users' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    -- 'id' is an integer that auto-increments, cannot be null, and is the primary key
    id INT NOT NULL AUTO_INCREMENT,

    -- 'email' is a string with a maximum length of 255 characters
    -- It must be unique and cannot be null
    email VARCHAR(255) NOT NULL UNIQUE,

    -- 'name' is a string with a maximum length of 255 characters, can be null
    name VARCHAR(255),

    -- 'country' is an enumerated type with allowed values 'US', 'CO', and 'TN'
    -- It cannot be null, and defaults to 'US' if no value is provided
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',

    -- Define 'id' as the primary key for the table
    PRIMARY KEY (id)
);
