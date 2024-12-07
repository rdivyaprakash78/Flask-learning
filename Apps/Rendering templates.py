from flask import Flask, render_template

app = Flask(__name__, template_folder= "Templates")

@app.route('/')
def init():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)