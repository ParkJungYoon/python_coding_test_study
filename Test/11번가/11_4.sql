-- write your code in PostgreSQL 9.4
SELECT p.name
FROM phones as p
INNER JOIN calls as c
ON p.phone_number  = c.caller or p.phone_number = c.callee
GROUP BY p.name
having sum(c.duration) >= 10
ORDER BY p.name