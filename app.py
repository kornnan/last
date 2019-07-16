Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, jsonify, render_template


app = Flask(__name__)


tasks = [

    {
        'rating': 'exelent',

        'subject': 'Operation sistem'  # операционные системы
    },


    {
        'rating': 'exelent',

        'subject': 'electrical engineering',  # электротехника
    },


    {
        'rating': 'good',

        'subject': 'computational mathematics',  # вычислительная математика
    },


    {
        'rating': 'exelent',

        'subject': 'computers and peripherals',  # эвм и периферийные устройства
    }

]


@app.route('/VIP21/Kornilova_Anna_Valerevna', methods=['GET'])

def get_tasks():

    return jsonify({'tasks': tasks})


if __name__ == '__main__':

app.run(debug=True)
