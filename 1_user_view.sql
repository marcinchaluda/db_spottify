CREATE VIEW user_view AS
    SELECT p.name playlist, s.name song , a.name album, b.name band
    FROM playlist p
    LEFT JOIN user_playlist up on p.playlist_id = up.playlist_id
    LEFT JOIN user_account ua on up.user_id = ua.user_id
    LEFT JOIN song_playlist sp on p.playlist_id = sp.playlist_id
    LEFT JOIN song s on sp.song_id = s.song_id
    LEFT JOIN album a on s.album_id = a.album_id
    LEFT JOIN band b on a.band_id = b.band_id
    WHERE ua.user_id = 3
    ORDER BY 1, 2;