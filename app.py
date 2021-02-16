from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')

@app.route("/password", methods = ['POST', 'GET'])
def password():

    if request.method == 'POST':

        passlen = int(request.form['password_length'])
        # print(passlen)
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&-=+?"
        p = "".join(random.sample(s,passlen ))
        # print(p)

        return render_template('home.html', gen_pas = f'Temporary ITS password generated:     {p}')

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True)