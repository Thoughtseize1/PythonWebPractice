SELECT id, name, email FROM contacts
WHERE name == 'Chaim Lewis';

SELECT id, name, email FROM contacts ORDER BY id DESC

SELECT name, email, favorite 
FROM contacts
WHERE favorite = NOT TRUE
ORDER BY name;

SELECT name, age, email
FROM users
WHERE age BETWEEN 10 AND 28
ORDER BY name;

SELECT name, email
FROM users
WHERE name LIKE '%k%'
ORDER BY name;