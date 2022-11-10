-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tv_genres.name AS name,
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id= tv_show.id
WHERE tv_show.title = Dexter
ORDER BY name