from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('first.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
