from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the homepage!'

@app.route('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2000)
    with app.test_request_context():
        print(url_for('index'))  # Output: /
        print(url_for('user_profile', username='Alice'))  # Output: /user/Alice
