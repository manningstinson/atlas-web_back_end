-- Import the metal_bands.sql data
-- Note: The actual import command should be run in your terminal, not in the SQL file.

-- Use this command in the terminal:
-- cat metal_bands.sql | mysql -uroot -p holberton

-- Once the data is imported, run the following query to rank the origins by the number of fans.

-- Select the origin of the bands and sum the number of fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands  -- Assuming the data was imported into a table named 'metal_bands'
GROUP BY origin   -- Group by the country of origin
ORDER BY nb_fans DESC;  -- Order the results by the number of fans in descending order
