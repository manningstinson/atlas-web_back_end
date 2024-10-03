-- Script to rank country origins of bands by the total number of non-unique fans

SELECT origin AS origin, 
       SUM(nb_fans) AS nb_fans 
FROM metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;
