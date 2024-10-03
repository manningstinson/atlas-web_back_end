-- Drop the students table if it already exists
DROP TABLE IF EXISTS students;

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT DEFAULT 0,
    last_meeting DATE NULL
);

-- Insert initial data
INSERT INTO students (name, score, last_meeting) VALUES ("Bob", 80, NULL);
INSERT INTO students (name, score, last_meeting) VALUES ("Sylvia", 120, NULL);
INSERT INTO students (name, score, last_meeting) VALUES ("Jean", 60, NULL);
INSERT INTO students (name, score, last_meeting) VALUES ("Steeve", 50, NULL);
INSERT INTO students (name, score, last_meeting) VALUES ("Camilia", 80, NULL);
INSERT INTO students (name, score, last_meeting) VALUES ("Alexa", 130, NULL);

-- Drop the view if it already exists
DROP VIEW IF EXISTS need_meeting;

-- Create the view need_meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE 
    score < 80
    AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);

-- Test Case 1: Nobody needs a meeting (initial state)
SELECT * FROM need_meeting;

SELECT "--";

-- Test Case 2: 1 student low score and not meeting yet (update Bob's score)
UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT * FROM need_meeting;

SELECT "--";

-- Test Case 3: 1 student low score and already had a meeting (set last meeting today for Bob)
UPDATE students SET last_meeting = CURDATE() WHERE name = 'Bob';
SELECT * FROM need_meeting;

SELECT "--";

-- Test Case 4: 1 student low score and meeting was overdue (set Bob's last meeting more than 1 month ago)
UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Bob';
SELECT * FROM need_meeting;

SELECT "--";

-- Show the structure of the need_meeting view
SHOW CREATE VIEW need_meeting;

-- Show the structure of the students table
SHOW CREATE TABLE students;
