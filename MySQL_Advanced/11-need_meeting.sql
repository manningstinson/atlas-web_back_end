-- Drop table if it already exists
DROP TABLE IF EXISTS students;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT DEFAULT 0,
    last_meeting DATE NULL
);

-- Insert initial data into the table
INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);
