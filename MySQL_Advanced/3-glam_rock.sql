-- Select bands with Glam rock as main style, computing their lifespan and ranking them by longevity
SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed
        ELSE split - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
