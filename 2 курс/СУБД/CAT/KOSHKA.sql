DROP TABLE STAFF_TO_TRIP;
DROP TABLE TICKETS;
DROP TABLE SCHEDULE;
DROP TABLE TRIPS;
DROP TABLE CUSTOMERS;
DROP TABLE STAFF;
DROP TABLE SALARY;
DROP TABLE TRAINS;
ALTER TABLE STATIONS DROP CONSTRAINT stations_next_fk;
DROP TABLE STATIONS;

CREATE TABLE  STATIONS (
    station_name VARCHAR2(35) NOT NULL,
    next_station VARCHAR2(35) NOT NULL CONSTRAINT stations_next_fk REFERENCES stations(station_name),
    CONSTRAINT stations_pk PRIMARY KEY (station_name)
);

CREATE TABLE  TRAINS (
    ID NUMBER,
    "type" VARCHAR2(35) NOT NULL,
    "year" DATE NOT NULL,
    number_of_seats NUMBER NOT NULL,
    inspection VARCHAR2(35) NOT NULL,
	CONSTRAINT trains_pk PRIMARY KEY (ID)
);

CREATE TABLE  SALARY (
    work_position VARCHAR2(35) NOT NULL,
    salary NUMBER NOT NULL CONSTRAINT salary_salary_len CHECK (salary > 0),
    CONSTRAINT salary_pk PRIMARY KEY (work_position)
);

CREATE TABLE  STAFF (
    passport_ID NUMBER NOT NULL CONSTRAINT staff_passport_ID_len CHECK (passport_ID = 10),
    surname VARCHAR2(35) NOT NULL,
    "name" VARCHAR2(35) NOT NULL,
    patronymic VARCHAR2(35),
    date_of_birth DATE NOT NULL,
    phone_number NUMBER NOT NULL CONSTRAINT staff_phone_len CHECK (phone_number = 11),
    certificat NUMBER NOT NULL,
    presence_of_a_medical_book NUMBER NOT NULL,
    education_document VARCHAR2(35) NOT NULL,
    work_position VARCHAR2(35) NOT NULL CONSTRAINT staff_workpos_fk REFERENCES salary(work_position),
    CONSTRAINT staff_pk PRIMARY KEY (passport_ID)
);

CREATE TABLE  CUSTOMERS (
    passport_ID NUMBER CONSTRAINT customers_passport_ID_len CHECK (passport_ID = 10),
    surname VARCHAR2(35) NOT NULL,
    "name" VARCHAR2(35) NOT NULL,
    patronymic VARCHAR2(35),
    date_of_birth DATE NOT NULL,
    phone_number NUMBER NOT NULL CONSTRAINT customers_phone_len CHECK (phone_number = 11),
    CONSTRAINT customers_pk PRIMARY KEY (passport_ID)
);

CREATE TABLE  TRIPS (
    ID NUMBER NOT NULL,
    departure_station VARCHAR2(35) NOT NULL CONSTRAINT tickets_departure_fk REFERENCES stations(station_name),
    destination_station VARCHAR2(35) NOT NULL CONSTRAINT tickets_destination_fk REFERENCES stations(station_name),
    CONSTRAINT trips_pk PRIMARY KEY (ID)
);

CREATE TABLE  SCHEDULE (
    ID NUMBER NOT NULL,
    trip_ID NUMBER NOT NULL CONSTRAINT schedule_trip_fk REFERENCES trips(ID),
    railway_station VARCHAR2(35) NOT NULL,
    "date" DATE NOT NULL,
    "time" DATE NOT NULL,
    train NUMBER NOT NULL CONSTRAINT schedule_train_fk REFERENCES trains(ID),
    platform NUMBER,
    CONSTRAINT schedule_pk PRIMARY KEY (ID)
);

CREATE TABLE  TICKETS (
    price NUMBER NOT NULL,
    railway_carriage NUMBER NOT NULL,
    place NUMBER NOT NULL,
    departure_station VARCHAR2(35) NOT NULL CONSTRAINT ticket_departure_fk REFERENCES stations(station_name),
    destination_station VARCHAR2(35) NOT NULL CONSTRAINT ticket_destination_fk REFERENCES stations(station_name),
    passport_ID1 NUMBER CONSTRAINT ticket_passport_ID1_fk REFERENCES customers(passport_ID),
    passport_ID2 NUMBER CONSTRAINT ticket_passport_ID2_fk REFERENCES staff(passport_ID),
    schedule NUMBER NOT NULL CONSTRAINT ticket_schedule_fk REFERENCES schedule(ID),
    CONSTRAINT ticket_pk PRIMARY KEY (passport_ID1, passport_ID2, schedule)
);

CREATE TABLE  STAFF_TO_TRIP (
    work_position VARCHAR2(35) NOT NULL CONSTRAINT staff2trip_workpos_fk REFERENCES salary(work_position),
    place NUMBER,
    schedule NUMBER NOT NULL CONSTRAINT staff2trip_schedule_fk REFERENCES schedule(ID),
    ID_number NUMBER NOT NULL CONSTRAINT staff2trip_ID_number_fk REFERENCES staff(passport_ID),
    CONSTRAINT staff_to_trip_pk PRIMARY KEY (ID_number, schedule)
);