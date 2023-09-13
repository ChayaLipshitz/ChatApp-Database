USE db;


CREATE TABLE IF NOT EXISTS users (
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (name, password)
);


CREATE TABLE IF NOT EXISTS rooms (
  name VARCHAR(255) NOT NULL,
  creation_date DATETIME NOT NULL,
  creative_name VARCHAR(255),
  PRIMARY KEY (name),
  FOREIGN KEY (creative_name) REFERENCES users (name)
);


CREATE TABLE IF NOT EXISTS messages (
  room VARCHAR(255) NOT NULL,
  date DATETIME NOT NULL,
  user VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL,
  PRIMARY KEY (date, user),
  FOREIGN KEY (room) REFERENCES rooms (name)
);

INSERT INTO users(name, password) VALUES ('user111', 1234);