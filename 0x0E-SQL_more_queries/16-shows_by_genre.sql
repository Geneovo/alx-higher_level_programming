-- Lists all shows and genres linked to that show on server, from database
SELECT tv_shows.title, tv_genres.name
  FROM tv_shows
  LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres
  ON tv_show_genres.genres_id = tv_genres.id
  ORDER BY tv_shows.title, tv_genres.name;