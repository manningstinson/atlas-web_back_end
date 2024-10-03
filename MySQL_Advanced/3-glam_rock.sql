SELECT 
    band_name, 
    IFNULL(split, YEAR(CURDATE())) - IFNULL(formed, 0) AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
