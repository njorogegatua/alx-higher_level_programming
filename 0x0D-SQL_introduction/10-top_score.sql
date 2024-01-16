-- lists all records of the table second_table
-- results should display both the score and the name
-- records should be ordered by score(top first)
SELECT DISTINCT score, name 
	FROM second_table
	ORDER BY score DESC, name;
