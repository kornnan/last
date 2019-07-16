#!flask/bin/python
from flask import Flask, jsonify


app = Flask(__name__)


tasks = [

    {
        'rating': 'exelent:5',

        'subject': 'Operation sistem.'  # операционные системы
    },


    {
        'rating': 'exelent:5',

        'subject': 'electrical engineering.',  # электротехника
    },


    {
        'rating': 'good:4',

        'subject': 'computational mathematics.',  # вычислительная математика
    },


    {
        'rating': 'exelent:5',

        'subject': 'computers and peripherals.',  # эвм и периферийные устройства
    }

]


@app.route('/VIP21/Kornilova_Anna_Valerevna', methods=['GET'])

def get_tasks():

    return jsonify({'tasks': tasks})


if __name__ == '__main__':

	app.run(debug=True)
