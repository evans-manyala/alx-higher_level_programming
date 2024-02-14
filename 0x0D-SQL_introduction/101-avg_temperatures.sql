-- SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
SELECT city, AVG(temperature)  AS average_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_fahrenheit DESC;

