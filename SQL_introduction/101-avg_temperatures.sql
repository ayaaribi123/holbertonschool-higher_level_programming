-- displays the average temperature
SELECT city, AVG(value)
FROM temperature
GROUP BY city
ORDER BY temperature DESC