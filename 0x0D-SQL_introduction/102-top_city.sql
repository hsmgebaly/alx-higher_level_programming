-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, temperature
FROM Temperatures WHERE (MONTH(date) = 7 OR MONTH(date) = 8)
ORDER BY temperature DESC
LIMIT 3;
