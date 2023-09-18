# ChatApp-Database

Chat App
This is a simple chat app built with HTML, Python-Flask, and Docker. The app allows users to register, log in, and chat with other users in rooms.

Requirements
Docker
Docker Compose
Python 3.8+
Setup
Clone the repository:
git clone https://github.com/bardia/chat-app.git
Install the dependencies:
cd chat-app
pip install -r requirements.txt
Build the Docker images:
docker-compose build
Start the app:
docker-compose up
The app will be available at http://localhost:5000.

Usage
To register, visit http://localhost:5000/register. Enter a username and password, and click "Register".
To log in, visit http://localhost:5000/login. Enter your username and password, and click "Login".
To create a room, visit http://localhost:5000/rooms. Click "Create Room", enter a name for your room, and click "Create".
To join a room, visit http://localhost:5000/rooms. Click the name of the room you want to join.
To chat, enter a message in the input field and click "Send".
Best Practices
The app is built using the following best practices:

Use of Docker containers to isolate the app's dependencies and environment.
Use of Docker Compose to simplify the deployment and management of the app.
Use of Python's best practices for code organization, testing, and deployment.
Use of a database to store user data and chat messages.
Further Development
The app could be improved in the following ways:

Add additional features, such as the ability to send files, add users to a room, and block users.
Improve the performance of the app by using a more efficient database and caching mechanism.
Add security features, such as password hashing and rate limiting.
License
The app is licensed under the MIT License.
