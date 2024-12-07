from flask import Flask, render_template

app = Flask(__name__, template_folder="Templates")

@app.route('/')
def home():
    return render_template('child.html')

if __name__ == '__main__':
    app.run(debug=True)