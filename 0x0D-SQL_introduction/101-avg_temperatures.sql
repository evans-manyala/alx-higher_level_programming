-- SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
SELECT city, AVG(value)  AS average_temp
FROM temperatures
GROUP BY city
ORDER BY average_temp DESC;