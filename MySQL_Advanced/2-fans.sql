-- Script to rank country origins of bands by the total number of non-unique fans
-- and handle different cases for entries

SELECT origin AS origin, 
       SUM(nb_fans) AS total_fans,

       -- Use CASE to classify the number of fans into different categories
       CASE 
           WHEN SUM(nb_fans) = 0 THEN 'Case with 0 entries'
           WHEN SUM(nb_fans) = 10 THEN 'Case with 10 unique entries'
           WHEN SUM(nb_fans) = 1000 THEN 'Case with 1000 entries'
           WHEN SUM(nb_fans) > 1000 THEN 'Case with more than 1000 entries'
           ELSE 'Other cases'
       END AS fan_category

FROM metal_bands 
GROUP BY origin 
ORDER BY total_fans DESC;
