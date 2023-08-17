-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- Write a script that displays the max temperature of each state (ordered by State name).
SELECT State, MAX(temperature) AS max_temperature
FROM Temperatures
GROUP BY State
ORDER BY State;
