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

create table Album
(
    album_id serial not null
    constraint album_pkey primary key,
    name varchar(100) not null,
    date timestamp default now(),
    studio_id integer not null
        constraint fk_studio
            references Studio
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


INSERT INTO public.Country (name) VALUES ('Poland');
INSERT INTO public.Country (name) VALUES ('Russia');
INSERT INTO public.Country (name) VALUES ('Germany');

INSERT INTO public.City (name) VALUES ('Cracov');
INSERT INTO public.City (name) VALUES ('Warsaw');
INSERT INTO public.City (name) VALUES ('Kuzmice');

INSERT INTO public.Address VALUES (1,'Lwowska', 56, 2, 3);

INSERT INTO public.Studio VALUES (1,'Janusze', 1);

INSERT INTO public.Album (name, studio_id) VALUES ('Pod ksiezycem', 1);

INSERT INTO public.Artist (first_name, last_name, gender, instrument) VALUES ('Bob', 'Cat', 'male', 'guitar');

INSERT INTO public.Band (name) VALUES ('Suchy chleb dla konia');

