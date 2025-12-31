from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['nm']
    return f"Selamat Datang, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
