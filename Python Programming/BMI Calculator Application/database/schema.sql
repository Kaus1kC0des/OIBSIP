-- User details
CREATE TABLE user (
    userid TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
);

-- Login Database
CREATE TABLE login (
    userid TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    FOREIGN KEY(userid) REFERENCES user(userid)
);

-- BMI Database
CREATE TABLE bmi (
    userid TEXT PRIMARY KEY,
    bmi REAL NOT NULL,
    prev_bmi REAL,
    date TEXT NOT NULL,
    FOREIGN KEY(userid) REFERENCES user(userid)
);