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
        if passlen <= 12:
            # print(passlen)
            s="abcdefghjkmnpqrstuvwxyz23456789!#$%&-=+?ABCDEFGHJKMNPQRSTUVWXYZ!#$%&-=+?"
            p = "".join(random.sample(s,passlen ))
            return render_template('home.html', gen_pas = f'Temporary ITS password generated:     {p}')


        else:

            s="abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
            p = "".join(random.sample(s,passlen ))
            return render_template('home.html', gen_pas = f'Temporary ITS password generated:     {p}')


        # print(p)


    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True)