-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN p_user_id INT  -- Use a different name for the parameter to avoid confusion
)
BEGIN
    DECLARE avg_score FLOAT DEFAULT 0;
    DECLARE score_count INT DEFAULT 0;

    -- Calculate the average score for the given p_user_id
    SELECT AVG(score), COUNT(score) INTO avg_score, score_count
    FROM corrections
    WHERE user_id = p_user_id;  -- Reference the parameter correctly

    -- Check if the user has any corrections (projects)
    IF score_count > 0 THEN
        -- Update the average_score in the users table
        UPDATE users
        SET average_score = avg_score
        WHERE id = p_user_id;  -- Reference the parameter correctly
    ELSE
        -- If the user has no scores, set the average_score to 0
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;  -- Reference the parameter correctly
    END IF;
END //

DELIMITER ;
