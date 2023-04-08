INSERT INTO genders (name)
VALUES ('PIDOR1');
--VACUUM;
--
INSERT INTO users (name, email, password, age, gender_id)
VALUES ('Nikita', 'boris@test.com', 'QWERTY123', 29, 1),
('Katya', 'alina@test.com', 'qwer126567', 26, 2),
('Sofa', 'maksim@test.com', '12376098', 10, 2);

DELETE FROM users 
WHERE name in ('Nikita','Katya','Sofa');

VACUUM;

DELETE FROM sqlite_sequence WHERE name='users';

INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);
