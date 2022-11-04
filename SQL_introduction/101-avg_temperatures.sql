-- displays the average temperature
SELECT city, AVG(value) as avg_temperature
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC