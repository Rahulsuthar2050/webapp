from flask import Flask, render_template
import os
sd = os.path.abspath('./HTML')
HTML_dir = os.path.abspath('./HTML/HTMLS')
app = Flask(__name__,static_folder=sd,template_folder=HTML_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)