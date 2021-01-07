DROP FUNCTION IF EXISTS artist_discography;

CREATE OR REPLACE FUNCTION artist_discography(p_artist_id INTEGER)
RETURNS TABLE (
    song_name VARCHAR(200),
    studio_name VARCHAR(100)
)
AS $artist_songs$
<<artist_func>>
BEGIN
    RETURN QUERY
        SELECT s.name, st.name FROM artist a
        INNER JOIN artist_band ab ON a.artist_id = ab.artist_id AND a.artist_id = p_artist_id
        INNER JOIN band b ON ab.band_id = b.band_id
        INNER JOIN album al ON b.band_id = al.band_id
        INNER JOIN song s ON al.album_id = s.album_id
        INNER JOIN studio st ON al.studio_id = st.studio_id;
END artist_func;
$artist_songs$ LANGUAGE plpgsql;

SELECT * FROM artist_discography(13);