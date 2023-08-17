-- list all genres not linked to the show Dexter
SELECT tg.name AS name
FROM tv_genres AS tg
JOIN tv_show.genres AS tsg ON tsg.genre_id = tg.id
JOIN tv_shows AS ts ON ts.id = tsg.show_id
WHERE ts.name != 'Dexter'
ORDER BY tg.name;
