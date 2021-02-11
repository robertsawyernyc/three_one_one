DROP TABLE IF EXISTS incidents;
DROP TABLE IF EXISTS complaints;
DROP TABLE IF EXISTS locations;


CREATE TABLE IF NOT EXISTS complaints (
    id serial PRIMARY KEY,
    agency VARCHAR(255),
    agency_name VARCHAR(255),
    complaint_type VARCHAR(255),
    descriptor VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS locations (
    id serial PRIMARY KEY,
    setting VARCHAR(255),
    incident_address VARCHAR(255),
    zip_code INTEGER,
    city VARCHAR(255),
    borough VARCHAR(255),
    latitude DECIMAL,
    longitude DECIMAL
);

CREATE TABLE IF NOT EXISTS incidents (
    id serial PRIMARY KEY,
    open_data_id INTEGER  UNIQUE,
    created_date TIMESTAMP,
    closed_date TIMESTAMP,
    location_id INTEGER,
    complaint_id INTEGER,
    CONSTRAINT fk_location
        FOREIGN KEY (location_id)
            REFERENCES locations (id),
    CONSTRAINT fk_complaint
        FOREIGN KEY (complaint_id)
            REFERENCES complaints (id)
);