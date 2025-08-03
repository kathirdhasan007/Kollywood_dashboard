CREATE DATABASE IF NOT EXISTS Dashboard;
USE Dashboard;

CREATE TABLE Genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50)
);

CREATE TABLE Movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year INT,
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE Actors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    actor_name VARCHAR(100)
);

CREATE TABLE Movie_cast (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);

INSERT INTO Genres (genre_name)
VALUES 
('Action'), ('Comedy'), ('Drama'), ('Thriller'), ('Romance'), ('Horror'),
('Sci-Fi'), ('Fantasy'), ('Adventure'), ('Mystery'), ('Crime'), ('Biography'),
('Animation'), ('Family'), ('Musical'), ('Sports'), ('War'), ('History'),
('Western'), ('Supernatural'), ('Political'), ('Documentary'), ('Short'),
('Experimental'), ('Mythology'), ('Psychological'), ('Surreal'), ('Silent'),
('Period'), ('Satire');

INSERT INTO Movies (title, release_year, genre_id)
VALUES
('Vikram', 2022, 1), ('Doctor', 2021, 2), ('Kaithi', 2019, 4),
('Jai Bhim', 2021, 3), ('Love Today', 2022, 5), ('Ponniyin Selvan', 2023, 19),
('Master', 2021, 1), ('3', 2012, 5), ('I', 2015, 6), ('Robot', 2010, 7),
('Enthiran', 2010, 7), ('Ratsasan', 2018, 4), ('Bigil', 2019, 16),
('Mersal', 2017, 1), ('Maanaadu', 2021, 4), ('Asuran', 2019, 3),
('Vada Chennai', 2018, 3), ('Indian', 1996, 19), ('Anniyan', 2005, 6),
('Thuppakki', 2012, 1), ('Theri', 2016, 1), ('96', 2018, 5),
('Don', 2022, 2), ('Etharkkum Thunindhavan', 2022, 1),
('Dasavatharam', 2008, 25), ('Karnan', 2021, 3), ('Soorarai Pottru', 2020, 12),
('Pizza', 2012, 6), ('Irumbu Thirai', 2018, 4), ('Vedalam', 2015, 1);


INSERT INTO Actors (actor_name)
VALUES 
('Kamal Haasan'), ('Rajinikanth'), ('Vijay'), ('Ajith Kumar'), ('Dhanush'),
('Suriya'), ('Vikram'), ('Sivakarthikeyan'), ('Jayam Ravi'), ('Karthi'),
('Nayanthara'), ('Trisha'), ('Samantha'), ('Keerthy Suresh'), ('Anushka'),
('Aishwarya Rai'), ('Prakash Raj'), ('Vadivelu'), ('Yogi Babu'), ('SJ Suryah'),
('Vijay Sethupathi'), ('Santhanam'), ('Arvind Swamy'), ('Sarath Kumar'),
('Parthiban'), ('Narain'), ('Ritika Singh'), ('Natraj'), ('Manju Warrier'), ('Kangana Ranaut');

INSERT INTO Movie_cast (movie_id, actor_id)
VALUES
(1, 1), (2, 8), (3, 5), (4, 6), (5, 8), (6, 10), (7, 3), (8, 5), (9, 7), (10, 2),
(11, 2), (12, 18), (13, 3), (14, 3), (15, 20), (16, 5), (17, 5), (18, 1), (19, 7),
(20, 3), (21, 3), (22, 8), (23, 6), (24, 1), (25, 5), (26, 6), (27, 18), (28, 7),
(29, 3), (30, 4);

INSERT INTO Reviews (movie_id, user_id, rating, review_text)
VALUES
(1, 1, 5, 'Outstanding action and visuals!'),
(2, 2, 4, 'Great comedic timing by Sivakarthikeyan.'),
(3, 3, 5, 'Kaithi is a masterclass in tension-building.'),
(4, 4, 5, 'Jai Bhim moved me to tears.'),
(5, 5, 4, 'Fresh and funny take on modern love.'),
(6, 6, 3, 'Visually epic but a bit lengthy.'),
(7, 7, 4, 'Mass scenes with great music.'),
(8, 8, 5, 'Love story with deep emotions.'),
(9, 9, 3, 'Impressive makeup and effects.'),
(10, 10, 4, 'Rajini in full form!'),
(11, 11, 3, 'Same vibes as Enthiran, but less punch.'),
(12, 12, 5, 'Thrilling from start to finish.'),
(13, 13, 4, 'Bigil blends sports and sentiment well.'),
(14, 14, 5, 'Vijay’s best performance yet.'),
(15, 15, 4, 'SJ Suryah steals the show.'),
(16, 16, 5, 'Raw and emotional rural drama.'),
(17, 17, 4, 'A gritty portrayal of Chennai underworld.'),
(18, 18, 3, 'Aged well, iconic Kamal movie.'),
(19, 19, 5, 'Psychological thriller with style.'),
(20, 20, 4, 'Packed with punch dialogues.'),
(21, 21, 3, 'Feel-good romance, slow pace though.'),
(22, 22, 5, 'Don makes learning fun.'),
(23, 23, 4, 'Solid performance, but predictable.'),
(24, 24, 3, 'Too much happening, hard to follow.'),
(25, 25, 5, 'Powerful social message with emotion.'),
(26, 26, 4, 'Uplifting and well-acted.'),
(27, 27, 5, 'Pizza is a horror gem.'),
(28, 28, 3, 'Decent cyber thriller.'),
(29, 29, 4, 'Vedalam delivers fan service.'),
(30, 30, 3, 'Not bad, but could’ve been tighter.');

INSERT INTO Users (id, username, email, password)
VALUES
(1, 'arun_k', 'arun.k@email.com', 'pass01'),
(2, 'divya_r', 'divya.r@email.com', 'pass02'),
(3, 'karthik_m', 'karthik.m@email.com', 'pass03'),
(4, 'meena_s', 'meena.s@email.com', 'pass04'),
(5, 'vijay_d', 'vijay.d@email.com', 'pass05'),
(6, 'anitha_j', 'anitha.j@email.com', 'pass06'),
(7, 'sathish_v', 'sathish.v@email.com', 'pass07'),
(8, 'revathi_n', 'revathi.n@email.com', 'pass08'),
(9, 'pradeep_t', 'pradeep.t@email.com', 'pass09'),
(10, 'lakshmi_b', 'lakshmi.b@email.com', 'pass10'),
(11, 'ramesh_p', 'ramesh.p@email.com', 'pass11'),
(12, 'keerthi_a', 'keerthi.a@email.com', 'pass12'),
(13, 'ganesh_r', 'ganesh.r@email.com', 'pass13'),
(14, 'nandhini_k', 'nandhini.k@email.com', 'pass14'),
(15, 'suresh_m', 'suresh.m@email.com', 'pass15'),
(16, 'deepa_s', 'deepa.s@email.com', 'pass16'),
(17, 'manoj_v', 'manoj.v@email.com', 'pass17'),
(18, 'sandhya_d', 'sandhya.d@email.com', 'pass18'),
(19, 'aravind_j', 'aravind.j@email.com', 'pass19'),
(20, 'shruti_n', 'shruti.n@email.com', 'pass20'),
(21, 'balaji_k', 'balaji.k@email.com', 'pass21'),
(22, 'pooja_r', 'pooja.r@email.com', 'pass22'),
(23, 'vikram_s', 'vikram.s@email.com', 'pass23'),
(24, 'isha_m', 'isha.m@email.com', 'pass24'),
(25, 'dinesh_t', 'dinesh.t@email.com', 'pass25'),
(26, 'radhika_b', 'radhika.b@email.com', 'pass26'),
(27, 'kavin_p', 'kavin.p@email.com', 'pass27'),
(28, 'swathi_a', 'swathi.a@email.com', 'pass28'),
(29, 'mohan_r', 'mohan.r@email.com', 'pass29'),
(30, 'janani_s', 'janani.s@email.com', 'pass30');

SELECT * FROM Movies;
SELECT title, release_year FROM Movies WHERE release_year > 2020;
SELECT username, email FROM Users WHERE email LIKE '%.com';
SELECT genre_name FROM Genres;
SELECT actor_name FROM Actors ORDER BY actor_name ASC;

SELECT * FROM Reviews WHERE rating = 5;
SELECT COUNT(*) FROM Users;
SELECT AVG(rating) FROM Reviews;
SELECT genre_id, COUNT(*) AS movie_count FROM Movies GROUP BY genre_id;
SELECT release_year, COUNT(*) FROM Movies GROUP BY release_year ORDER BY release_year DESC;

SELECT m.title, g.genre_name 
FROM Movies m
JOIN Genres g ON m.genre_id = g.id;

SELECT r.review_text, u.username 
FROM Reviews r
JOIN Users u ON r.user_id = u.id;

SELECT m.title, a.actor_name 
FROM Movie_cast mc
JOIN Movies m ON mc.movie_id = m.id
JOIN Actors a ON mc.actor_id = a.id;

SELECT m.title, COUNT(r.id) AS total_reviews 
FROM Movies m
LEFT JOIN Reviews r ON m.id = r.movie_id
GROUP BY m.title;

SELECT m.title, ROUND(AVG(r.rating),2) AS avg_rating 
FROM Movies m
JOIN Reviews r ON m.id = r.movie_id
GROUP BY m.title;

SELECT actor_name 
FROM Actors 
WHERE id IN (
  SELECT actor_id FROM Movie_cast 
  WHERE movie_id = (SELECT id FROM Movies WHERE title = 'Vikram')
);

SELECT * FROM Movies WHERE id IN (SELECT movie_id FROM Reviews WHERE rating = 5);

SELECT actor_name 
FROM Actors 
WHERE id IN (
  SELECT actor_id FROM Movie_cast 
  WHERE movie_id = (SELECT id FROM Movies WHERE title = 'Vikram')
);

SELECT * FROM Users WHERE id IN (SELECT user_id FROM Reviews WHERE rating < 3);
SELECT title FROM Movies WHERE genre_id = (SELECT id FROM Genres WHERE genre_name = 'Thriller');
SELECT username FROM Users WHERE id IN (SELECT user_id FROM Reviews WHERE review_text LIKE '%mass%');

UPDATE Movies SET release_year = 2024 WHERE title = 'Leo';
DELETE FROM Reviews WHERE rating < 2;
DELETE FROM Movies WHERE release_year < 2000;
UPDATE Genres SET genre_name = 'Action Drama' WHERE genre_name = 'Drama';

SELECT g.genre_name, ROUND(AVG(r.rating), 2) AS avg_genre_rating
FROM Genres g
JOIN Movies m ON g.id = m.genre_id
JOIN Reviews r ON m.id = r.movie_id
GROUP BY g.genre_name;

SELECT m.title, COUNT(DISTINCT mc.actor_id) AS total_cast 
FROM Movies m
JOIN Movie_cast mc ON m.id = mc.movie_id
GROUP BY m.title;

SELECT username, COUNT(*) AS review_count 
FROM Reviews r
JOIN Users u ON r.user_id = u.id
GROUP BY username
ORDER BY review_count DESC;

SELECT release_year, MAX(rating) FROM Movies m JOIN Reviews r ON m.id = r.movie_id GROUP BY release_year;
SELECT genre_name FROM Genres WHERE id NOT IN (SELECT genre_id FROM Movies);
