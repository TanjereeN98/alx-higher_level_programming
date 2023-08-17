-- list all genres not linked to the show Dexter
SELECT tg.name AS name
FROM tv_genres AS tg
LEFT JOIN (
    SELECT tsg.genre_id
    FROM tv_show_genres AS tsg
    JOIN tv_shows AS ts ON ts.id = tsg.show_id
    WHERE ts.name = 'Dexter'
) ON tg.id = tsg.genre_id
WHERE tsg.genre_id IS NULL
ORDER BY tg.name;
