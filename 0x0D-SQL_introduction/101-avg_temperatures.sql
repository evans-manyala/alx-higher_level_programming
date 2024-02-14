-- SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
SELECT city, ROUND(AVG(temperature * 9/5 + 32), 2) AS average_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY average_fahrenheit DESC;

