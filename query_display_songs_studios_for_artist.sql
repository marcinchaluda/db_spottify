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
        LEFT JOIN artist_band ab ON a.artist_id = ab.artist_id
        LEFT JOIN band b ON ab.band_id = b.band_id
        LEFT JOIN album al ON b.band_id = al.band_id
        LEFT JOIN song s ON al.album_id = s.album_id
        LEFT JOIN studio st ON al.studio_id = st.studio_id
        WHERE a.artist_id = p_artist_id;
END artist_func;
$artist_songs$ LANGUAGE plpgsql;

SELECT * FROM artist_discography(13);