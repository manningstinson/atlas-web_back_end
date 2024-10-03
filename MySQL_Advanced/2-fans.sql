-- Ensure that nb_fans contains only valid numeric values, handle potential null or empty entries
SELECT origin AS origin, 
       SUM(CAST(nb_fans AS UNSIGNED)) AS total_fans
FROM metal_bands
-- Filter out entries where nb_fans is null, empty, or non-numeric
WHERE nb_fans IS NOT NULL AND nb_fans != '' AND nb_fans REGEXP '^[0-9]+$'
GROUP BY origin
ORDER BY total_fans DESC;
