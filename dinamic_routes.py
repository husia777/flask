from flask import Flask, render_template

app = Flask(__name__)

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


if __name__ == '__main__':
    app.run()