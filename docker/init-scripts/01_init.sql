CREATE SCHEMA IF NOT EXISTS vc;

CREATE SEQUENCE dog_sequence START 1;

CREATE TABLE IF NOT EXISTS vc.dogs (
    dog_id INTEGER PRIMARY KEY DEFAULT NEXTVAL('dog_sequence'),
    name_ VARCHAR,
    kind_ VARCHAR
);

CREATE SEQUENCE post_sequence START 100;

CREATE TABLE IF NOT EXISTS vc.registration (
    post_id INTEGER PRIMARY KEY DEFAULT NEXTVAL('post_sequence'),
    dog_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dog_id) REFERENCES vc.dogs(dog_id)
);



