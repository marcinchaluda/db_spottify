CREATE OR REPLACE VIEW user_view AS
    SELECT p.name playlist, s.name song , a.name album, b.name band
    FROM playlist p
    INNER JOIN user_playlist up on p.playlist_id = up.playlist_id
    INNER JOIN user_account ua on up.user_id = ua.user_id AND ua.user_id = 974
    INNER JOIN song_playlist sp on p.playlist_id = sp.playlist_id
    INNER JOIN song s on sp.song_id = s.song_id
    INNER JOIN album a on s.album_id = a.album_id
    INNER JOIN band b on a.band_id = b.band_id
    ORDER BY 1, 2;