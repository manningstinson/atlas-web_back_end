-- This SQL script retrieves a list of metal bands that primarily fall under the "Glam rock" genre.
-- It calculates their lifespan based on the years they were formed and their split years.
-- If a band has no split year, the current year is used for the calculation.
-- If a band has no formed year, it defaults to 0.
-- The results are ordered by longevity (lifespan) in descending order.

SELECT 
    band_name, 
    -- Calculate lifespan
    IFNULL(split, YEAR(CURDATE())) - IFNULL(formed, 0) AS lifespan
FROM 
    metal_bands -- Specify the table to select from
WHERE 
    style LIKE '%Glam rock%' -- Filter to include only bands with 'Glam rock' in their style
ORDER BY 
    lifespan DESC; -- Order the results by lifespan in descending order
