-- displays the average temperature
SELECT city, AVG(value) as temperature
FROM temperature
GROUP BY city
ORDER BY temperature DESC