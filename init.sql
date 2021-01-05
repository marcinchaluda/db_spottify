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

create table Street
(
    street_id serial not null
    constraint street_pkey primary key,
    name varchar(100) not null
);

create table Address
(
    address_id serial not null
    constraint address_pkey primary key,
    street_id integer not null
            constraint fk_street
            references Street,
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
    name varchar(200) not null,
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

create table User_account
(
    user_id serial not null
    constraint user_pkey primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(100) not null,
    address_id integer not null
        constraint fk_address
            references Address
);

create table User_playlist
(
    user_playlist_id serial not null
    constraint user_playlist_pkey primary key,
    user_id integer not null
    constraint fk_user
        references User_account,
    playlist_id integer not null
    constraint fk_playlist
        references Playlist
);

create table Subscription
(
    subscription_id serial not null
    constraint subscription_pkey primary key,
    date timestamp default now(),
    user_id integer not null
    constraint fk_user
        references User_account,
    band_id integer not null
    constraint fk_band
        references Band
);
