-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows AS ts
LEFT JOIN (
    SELECT tsg.show_id
    FROM tv_show_genres AS tsg
    JOIN tv_genres AS tg ON tg.id = tsg.genre_id
    WHERE tg.name = 'Comedy'
) AS comedy_shows ON ts.id = comedy_shows.show_id
WHERE comedy_shows.show_id IS NULL
ORDER BY ts.title;
