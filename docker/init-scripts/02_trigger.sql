CREATE OR REPLACE FUNCTION fill_registration()
 RETURNS trigger AS
 $$
 BEGIN
     INSERT INTO vc.registration(dog_id)
     VALUES(NEW.dog_id);
     RETURN NEW;
 END;
 $$
 LANGUAGE 'plpgsql';

CREATE TRIGGER fill_dog_id
 AFTER INSERT
 ON vc.dogs
 FOR EACH ROW
 EXECUTE PROCEDURE fill_registration();

