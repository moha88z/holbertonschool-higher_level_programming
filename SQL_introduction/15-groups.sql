-- Task 15: Count records grouped by score
-- This script lists each score and the number of records with that score, ordered by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

