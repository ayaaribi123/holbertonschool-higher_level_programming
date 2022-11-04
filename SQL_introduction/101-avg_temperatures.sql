-- displays the average temperature
SELECT city, AVG(value)
FROM hbtn_0c_0.temperature
GROUP BY city
ORDER BY temperature DESC