from flask import Flask, render_template
app = Flask(__name__)

users = [{'uid': 1, 'name': 'Bob'}]

@app.route('/api/userinfo')
def userinfo():
    return {'data': users},200

@app.route('/')
def hello_world():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)
