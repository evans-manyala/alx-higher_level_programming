
SELECT city, AVG(value) AS avg_temperatures
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temperatures DESC
LIMIT 3;