import sqlite3

conn = sqlite3.connect('homes.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE homes
          (
          id                  INTEGER PRIMARY KEY ASC,
          home_type           VARCHAR(20) NOT NULL,
          home_id             INTEGER NOT NULL,
          square_footage      INTEGER NOT NULL,
          year_built          INTEGER NOT NULL,
          number_of_rooms     INTEGER NOT NULL,
          number_of_bathrooms INTEGER NOT NULL,
          city                VARCHAR(100) NOT NULL,
          selling_agent       VARCHAR(100) NOT NULL,
          yearly_property_tax FLOAT NOT NULL,
          
          monthly_strata_fee  INTEGER,
          pets_allowed        INTEGER,
          number_of_floors    INTEGER,
          has_rental_suite    INTEGER
          )
          ''')

conn.commit()
conn.close()
