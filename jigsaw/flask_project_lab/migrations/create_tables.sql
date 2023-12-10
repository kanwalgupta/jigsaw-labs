DROP TABLE IF EXISTS parks;
DROP TABLE IF EXISTS species;

CREATE TABLE IF NOT EXISTS parks (
  park_code TEXT PRIMARY KEY NOT NULL,
  park_name TEXT UNIQUE,
  state TEXT,
  acres INTEGER,
  latitude DECIMAL,
  longitude DECIMAL
);

CREATE TABLE IF NOT EXISTS species (
  species_id TEXT PRIMARY KEY NOT NULL,
  park_name TEXT,
  category TEXT,
  "order" TEXT,
  family TEXT,
  scientific_name TEXT,
  common_names TEXT,
  record_status TEXT,
  occurrence TEXT,
  nativeness TEXT,
  abundance TEXT,
  seasonality TEXT,
  conservation_status TEXT
);

