-- init_db.sql
-- Use this to set up your Tables for Lab 1

CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    GPA REAL DEFAULT 0.0
);

-- Sample Data
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('John', 'Doe', 3.8);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('Jane', 'Smith', 3.9);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('Alice', 'Brown', 3.4);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('Bob', 'White', 3.1);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('Charlie', 'Black', 3.6);
