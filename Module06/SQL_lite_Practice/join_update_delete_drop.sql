SELECT *
FROM contacts c
JOIN users u ON u.id = c.user_id
WHERE u.age <30;

SELECT u.id, u.name, u.email, g.name AS gender
FROM users AS u
INNER JOIN genders AS g ON g.id = u.gender_id;

SELECT c.id, c.name, c.phone, u.name as 'username'
FROM contacts c
JOIN users u ON u.id = c.user_id
WHERE u.age <30;

SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
JOIN users AS u ON u.id = c.user_id;

UPDATE contacts SET user_id = 3 WHERE id = 3;
--Меняем Софе почту 
UPDATE users SET email = 'sofa_bla_bla@gmail.com' WHERE id = 1;

-- Меняем Никите почту на клевую.У Никиты поле name = Nikita
UPDATE users SET email = 'nikita55_LIKE@gmail.com' WHERE name = 'Nikita';

--Меняем Никите возраст на правильный. У Никиты id = 1
UPDATE users SET age = 28 WHERE id = 1;

--Этот запрос удаляет из таблицы contacts того, у кого id = 4. ВАЖНО - Нельзя удалять без условия: 
DELETE FROM contacts WHERE id = 4;

--Якщо ми хочемо видалити всі дані з таблиці, але при цьому саму таблицю залишити, 
-- слід використовувати команду TRUNCATE:
TRUNCATE TABLE contacts;

--У випадку, якщо ми хочемо видалити саме саму таблицю, то нам слід використати команду DROP:
DROP TABLE contacts;