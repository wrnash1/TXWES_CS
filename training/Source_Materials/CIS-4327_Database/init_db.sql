-- Database setup
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    GPA REAL DEFAULT 0.0
);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('John', 'Doe', 3.8);
INSERT INTO Students (FirstName, LastName, GPA) VALUES ('Jane', 'Smith', 3.9);
