-- displays the top 3 of cities temperature during July
-- and August ordered by temperature (descending)
SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
WHERE `month` BETWEEN 7 AND 8
ORDER BY AVG(`value`) DESC
LIMIT 3;
