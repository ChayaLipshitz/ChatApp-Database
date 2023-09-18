USE chat-app-db;


CREATE TABLE IF NOT EXISTS users (
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (name, password)
);


CREATE TABLE IF NOT EXISTS rooms (
  name VARCHAR(255) NOT NULL,
  creation_date DATETIME NOT NULL,
  creator_name VARCHAR(255),
  PRIMARY KEY (name),
  FOREIGN KEY (creator_name) REFERENCES users (name)
);


CREATE TABLE IF NOT EXISTS messages (
  room VARCHAR(255) NOT NULL,
  date DATETIME NOT NULL,
  user VARCHAR(255) NOT NULL,
  content VARCHAR(255) NOT NULL,
  PRIMARY KEY (date, user),
  FOREIGN KEY (room) REFERENCES rooms (name),
  FOREIGN KEY (user) REFERENCES users (name)
);

INSERT INTO users(name, password) VALUES ('user111', "1234");
INSERT INTO users(name, password) VALUES ('user222', "12345");
INSERT INTO rooms(name, creation_date, creator_name) VALUES ('my room', "2015-12-20 10:01:01", "user222");
INSERT INTO messages (room, date, user, content)
VALUES ('my room', '2023-09-18 18:01:08', 'user222', 'helllllllo');