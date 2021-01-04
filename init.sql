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
    street varchar(100) not null,
    address_id integer not null
    constraint fk_address
            references Address
);

INSERT INTO public.Country (name) VALUES ('Poland');
INSERT INTO public.Country (name) VALUES ('Russia');
INSERT INTO public.Country (name) VALUES ('Germany');

INSERT INTO public.City (name) VALUES ('Cracov');
INSERT INTO public.City (name) VALUES ('Warsaw');
INSERT INTO public.City (name) VALUES ('Kuzmice');

INSERT INTO public.Address VALUES (1,'Lwowska', 56, 2, 3);