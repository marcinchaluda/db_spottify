DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

create table Country
(
    country_id serial not null
    constraint country_pkey primary key,
    name varchar(100) not null
);

create table City
(
    city_id serial not null
    constraint city_pkey primary key,
    name varchar(100) not null
);

create table Address
(
    address_id serial not null
    constraint address_pkey primary key,
    street varchar(100) not null,
    local_number integer not null,
    city_id integer not null
        constraint fk_city
            references City,
    country_id integer not null
        constraint fk_country
            references Country
);

create table Studio
(
    studio_id serial not null
    constraint studio_pkey primary key,
    name varchar(100) not null,
    address_id integer not null
    constraint fk_address
            references Address
);

create table Artist
(
    artist_id serial not null
    constraint artist_pkey primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    gender varchar(100) not null,
    instrument varchar(100) not null
);

create table Band
(
    band_id serial not null
    constraint band_pkey primary key,
    name varchar(100) not null,
    band_establishment timestamp default now()
);

create table Album
(
    album_id serial not null
    constraint album_pkey primary key,
    name varchar(100) not null,
    date timestamp default now(),
    studio_id integer not null
        constraint fk_studio
            references Studio,
    band_id integer not null
        constraint fk_band
            references Band
);

create table Artist_band
(
    artist_band_id serial not null
    constraint artist_band_pkey primary key,
    artist_id integer not null
        constraint fk_artist
            references Artist,
    band_id integer not null
        constraint fk_band
            references Band
);

create table Genre
(
    genre_id serial not null
    constraint genre_pkey primary key,
    type varchar(100) not null
);

create table Song
(
    song_id serial not null
    constraint song_pkey primary key,
    name varchar(100) not null,
    length varchar(10) not null,
    views integer not null,
    album_id integer not null
        constraint fk_album
            references Album,
    genre_id integer not null
        constraint fk_genre
            references Genre
);

create table Playlist
(
    playlist_id serial not null
    constraint playlist_pkey primary key,
    name varchar(100) not null,
    date timestamp default now()
);

create table Song_playlist
(
    song_playlist_id serial not null
    constraint song_playlist_pkey primary key,
    song_id integer not null
        constraint fk_song
            references Song,
    playlist_id integer not null
        constraint fk_playlist
            references Playlist
);

INSERT INTO public.Country (name) VALUES ('Poland');
INSERT INTO public.Country (name) VALUES ('Russia');
INSERT INTO public.Country (name) VALUES ('Germany');

INSERT INTO public.City (name) VALUES ('Cracov');
INSERT INTO public.City (name) VALUES ('Warsaw');
INSERT INTO public.City (name) VALUES ('Kuzmice');

INSERT INTO public.Address VALUES (1,'Lwowska', 56, 2, 3);

INSERT INTO public.Studio VALUES (1,'Janusze', 1);

INSERT INTO public.Artist (first_name, last_name, gender, instrument) VALUES ('Bob', 'Cat', 'male', 'guitar');

INSERT INTO public.Band (name) VALUES ('Suchy chleb dla konia');

INSERT INTO public.Album (name, studio_id, band_id) VALUES ('Pod ksiezycem', 1, 1);

INSERT INTO public.artist_band (artist_id, band_id) VALUES (1, 1);

INSERT INTO public.genre (type) VALUES ('rock');
INSERT INTO public.genre (type) VALUES ('disco-polo');

INSERT INTO public.song (name, length, views, album_id, genre_id) VALUES ('oh now', '4:32', 2, 1, 2);

INSERT INTO public.playlist (name) VALUES ('my-playlist');

INSERT INTO public.song_playlist (song_id, playlist_id) VALUES (1, 1);

