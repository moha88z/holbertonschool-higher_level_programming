-- Task 16: List records with a valid name
-- This script selects score and name from second_table where name is not empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

