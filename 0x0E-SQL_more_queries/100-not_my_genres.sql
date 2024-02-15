--  Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter The tv_shows table contains only one record
--  where title = Dexter (but the id can be different) Each record should display: tv_genres.name Results must be sorted in ascending order by the genre name.
--  You can use a maximum of two SELECT statements.
--  The database name will be passed as an argument of the mysql command

SELECT tv_genres.name
FROM tv_genres AS genre
WHERE genre.id NOT IN
        (SELECT sg.genre_id
         FROM tv_genres.tv_show_genres AS sg
         JOIN tv_genres.tv_shows AS t ON sg.show_id = t.id
         WHERE t.title = 'Dexter')
ORDER BY genre.name ASC;