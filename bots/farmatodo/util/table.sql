drop table if exists product;
create table product(
id serial primary key,
name varchar,
price float,
image varchar,
address varchar,
origin varchar
);