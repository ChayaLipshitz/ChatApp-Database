from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
import base64
from datetime import datetime
server = Flask(__name__)

os.environ["ROOM_PATH"] = "./rooms"
server.secret_key="chatApp@Chaya_Lipshitz"


@server.route("/", methods=['GET','POST'])
def index(): 
    return redirect('/register')

@server.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(checkUserExist(username, password)):
            return "username and pass already exist"
        else:
            encrypted_password = encode_password(password)
            my_query = "INSERT INTO users(name, password) VALUES ('"+ str(username) + "', '" + str(encrypted_password) + "');"
            result = query(my_query)
            return redirect('login')
    return render_template('register.html')

@server.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(checkUserExist(username, password)):
            session['username'] = username
            return redirect('lobby')
        else:      
            return "wrong usernaname or password"       
    return render_template('login.html')

@server.route('/lobby', methods = ['POST','GET'])
def lobby():
   my_query = "SELECT name from rooms"
   result = query(my_query)
   rooms = []
   for room in result:
        room_name,  = room
        rooms.append(room_name)
   if request.method == 'POST':
        new_room = request.form['new_room']
        if (str(new_room)) in rooms:
            return "exist"
        else:
            now = datetime.now()
            username= session.get('username')
            my_query = "INSERT INTO rooms(name, creation_date, creator_name) VALUES ('" + new_room + "', '" + str(now) + "', '" + username + "');"
            query(my_query)
            rooms.append(new_room)
   return render_template("lobby.html", all_rooms = rooms) 

@server.route('/logout', methods = ['POST','GET'])
def logout():
    session.pop('username', None)
    return redirect('register')

@server.route("/chat/<room>")
def chat(room):
    return render_template('chat.html', room=room)

@server.route('/api/chat/<room>', methods = ['GET','POST'])
def manage_chat(room):
    user= session.get('username')
    if user==None:
        # user="guest"
        return "Please register first: localhost:5000/register"
    if request.method == 'POST':
        user_mssage= request.form['msg']
        now = datetime.now()
        my_query= "INSERT INTO messages (room, date, user, content) VALUES ('" + room + "', '" + str(now) + "', '" + user + "', '" + user_mssage + "'); "
        query(my_query)
    my_query = "SELECT date, user, content from messages where room='" + room + "';"
    all_messages = query(my_query)
    content = ""
    if all_messages == []:
        content = str(user) + ", No messages yet"
    else:
        for message in all_messages:
            dateM, userM, contentM = message
            #message in format:  [2023-08-21 11:00:11] yuval: hello
            content += "[" + str(dateM) + "]" + str(userM) + ": " + str(contentM) + "\n"
    return content

#encode password
def encode_password(user_pass):
    pass_bytes = user_pass.encode('ascii')
    base64_bytes = base64.b64encode(pass_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

#decode password
def decode_password(user_pass):
    base64_bytes = user_pass.encode('ascii')
    pass_bytes = base64.b64decode(base64_bytes)
    user_pass = pass_bytes.decode('ascii')
    return user_pass

def checkUserExist(username,password):
    my_query = "Select name, password from users;"
    users = query(my_query)
    if users == []:
        return False
    for user in users:
        sql_name, sql_password = user
        if(sql_name == username and decode_password(sql_password) == password):
            return True
    return False

def query(my_query):
    connection = mysql.connector.connect(
      user='root',
      password='test',
      host='mysql',
      port="3306",
      database='chat-app-db')
    print("chat-app-db connected")
    cursor = connection.cursor()
    cursor.execute(my_query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result
    
if __name__ == "__main__":
    server.run(host='0.0.0.0')