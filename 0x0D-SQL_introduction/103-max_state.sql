-- Script to display the max temperature of each state in hbtn_0c_0 database
SELECT state, MAX(temperature) AS max_temperature
FROM Temperatures
GROUP BY state
ORDER BY state;