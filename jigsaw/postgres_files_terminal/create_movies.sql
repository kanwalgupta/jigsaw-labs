CREATE TABLE IF NOT EXISTS movies (
    id serial PRIMARY KEY,
    title varchar(255) UNIQUE NOT NULL,
    genre varchar(255),
    budget bigint,
    runtime decimal,
    year integer,
    month integer,
    revenue bigint,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);