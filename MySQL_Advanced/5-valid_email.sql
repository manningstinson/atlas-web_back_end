-- Drop the trigger if it already exists to avoid duplication
DROP TRIGGER IF EXISTS email_change_trigger;

-- Create a new trigger that fires BEFORE an update on the users table
CREATE TRIGGER email_change_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email is being changed
    IF NEW.email <> OLD.email THEN
        -- Reset valid_email to 0 if the email is changed
        SET NEW.valid_email = 0;
    END IF;
END;
