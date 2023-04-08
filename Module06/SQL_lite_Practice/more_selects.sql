--Посчиттает кол-во полей в которых заполнено поле ТЕЛЕФОН таблице contacts
SELECT COUNT(phone)
FROM contacts;

--Минимальный возраст пользователей в таблице users
SELECT COUNT(*)
FROM contacts;

--Минимальный возраст пользователей в таблице users
SELECT min(age) as minAge
FROM users

--Максимальный возраст пользователей в таблице users
SELECT max(age) as maxAge
FROM users

--Средний возраст пользователей в таблице users
SELECT avg(age) as averageAge
FROM users

SELECT COUNT(user_id) as total_contacts, user_id
FROM contacts
GROUP BY user_id

--Перший запит — показати id та name користувачів молодше або дорівнює 26 років
SELECT name, id
FROM users
WHERE age <= 26

SELECT *
FROM contacts
WHERE user_id IN (SELECT id
    FROM users
    WHERE age >26);
    
 SELECT id
    FROM users
    WHERE age < 11;