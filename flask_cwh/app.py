from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form['name']
        print(name)

    return render_template('index.html',name = name)

@app.route('/products')
def products():
    return 'This is a product page'

if __name__ == "__main__":
    app.run(debug=True, port=8080)