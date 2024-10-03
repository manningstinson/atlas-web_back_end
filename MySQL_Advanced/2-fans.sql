-- Select the origin of the bands and sum the number of fans,
-- ensuring to exclude NULL values in the nb_fans column
SELECT origin, AS origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;  -- Order the results by the number of fans in descending order