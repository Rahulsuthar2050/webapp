from flask import Flask, render_template, request
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
dbuser=os.getenv('DB_user')
dbpass=os.getenv('DB_pass')
sd = os.path.abspath('./HTML')
HTML_dir = os.path.abspath('./HTML/HTMLS')
app = Flask(__name__,static_folder=sd,template_folder=HTML_dir)

@app.route('/')
def index():
    return render_template('index.html')

def getdbconn():
    conn=psycopg2.connect(host="db",database="webapp",user=dbuser,password=dbpass,port="5432")
    return conn

@app.route('/login_page',methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username_input= request.form.get('uname')
        password_input= request.form.get('psw')
        conn = getdbconn()
        cur=conn.cursor()

        cur.execute("SELECT name,password from users where name = %s", (username_input,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            stored_n =user[0]
            stored_p = user[1]
            if password_input == stored_p:
                return f"Welcome {stored_n} verfication successfull!"
            else:
                return f"invalid username or pass"
        else:
            return f"User not found"
    return render_template('login.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)