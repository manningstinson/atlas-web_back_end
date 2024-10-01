-- Select the origin of the bands and sum the number of fans,
-- ensuring to exclude NULL values in the nb_fans column
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
WHERE nb_fans IS NOT NULL  -- Filter out any NULL fan counts
GROUP BY origin
ORDER BY nb_fans DESC;  -- Order the results by the number of fans in descending order
