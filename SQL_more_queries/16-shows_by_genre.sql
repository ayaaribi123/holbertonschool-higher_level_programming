-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_shows.title AS "title", tv_genres.name AS "name"
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY title, name