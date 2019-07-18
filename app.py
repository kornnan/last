#!flask/bin/python
from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route('/VIP21/Kornilova_Anna_Valerevna', methods=['GET'])
def os():
    return render_template("words.html")

if __name__ == '__main__':
    app.run(debug=True)
