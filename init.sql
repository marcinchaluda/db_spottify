DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

create table Country
(
    country_id serial not null
    constraint country_pkey primary key,
    name   varchar(100) not null
);

create table City
(
    city_id serial not null
    constraint city_pkey primary key,
    name   varchar(100) not null
);


INSERT INTO public.Country (name) VALUES ('Poland');
INSERT INTO public.Country (name) VALUES ('Russia');
INSERT INTO public.Country (name) VALUES ('Germany');


INSERT INTO public.City (name) VALUES ('Cracov');
INSERT INTO public.City (name) VALUES ('Warsaw');
INSERT INTO public.City (name) VALUES ('Kuzmice');