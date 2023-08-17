-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name AS name, SUM(tsr.rating) AS rating
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id
JOIN tv_shows AS ts ON ts.id = tsg.show_id
JOIN tv_show_ratings AS tsr ON tsr.show_id = ts.id
GROUP BY tg.name
ORDER BY rating DESC;