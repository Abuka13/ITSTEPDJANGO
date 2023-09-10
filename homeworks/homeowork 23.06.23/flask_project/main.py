from flask import Flask, render_template

app = Flask(__name__)

data = {
    'name': 'Abuka',
    'Surname': '13',
    'hobby': 'football',
    'number': '+77777777777',
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)