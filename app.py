# from crypt import methods
# from json.tool import main
# from urllib import request
from cmath import phase
import model
from flask import Flask, render_template, request


# from passlib.hash import md5_crypt as md5
# from passlib.hash import sha256_crypt as sha256
# from passlib.hash import sha512_crypt as sha512

# md5_passwd = md5.encrypt(passwd, rounds=5000, implicit_rounds=True)
# sha256_passwd = sha256.encrypt(passwd, rounds=5000, implicit_rounds=True)
# sha512_passwd = sha512.encrypt(passwd, rounds=5000, implicit_rounds=True)

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def hello():
    y=''
    if request.method=="POST":
        Age= request.form['name']
        chol= request.form['chol']
        BMI= request.form['BMI']
        mental = request.form['Mental']
        physical= request.form['physical']
        smoke = request.form['smoke']
        BP= request.form['BP']
        physical_active= request.form['phyactive']
        alchol= request.form['alchol']
        walk= request.form['walk']
        gender= request.form['gen']

        uv=[int(BP), int(chol), int(BMI), int(smoke), int(physical_active), int(alchol), int(mental), int(mental), int(walk), int(gender), int(Age)]
        y= model.prob_dia(uv)
        

    
    return render_template('index.html', predict=y)

if __name__== "__main__":
    app.run(debug=True)
