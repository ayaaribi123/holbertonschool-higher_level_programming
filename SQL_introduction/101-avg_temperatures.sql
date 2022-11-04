-- displays the average temperature
SELECT city, AVG(value) as "hbtn_0c_0.temperature"
FROM temperature
GROUP BY city
ORDER BY temperature DESC