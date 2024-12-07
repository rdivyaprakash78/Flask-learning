from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder= "Templates")

counter = 1
@app.route('/')
def home():
    global counter
    if counter > 1 :
        counter = 1
        return redirect(url_for("form"))
    counter += 1
    return render_template('home.html')
        

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET' :
        return render_template('form.html')
    else :
        name = request.form["nm"]
        age = request.form["age"]
        return redirect(url_for("handling_form_values", name = name, age = age))

@app.route('/name : <name> age : <age>')    
def handling_form_values(name, age):
    return f"<h1> You are Mr. {name} and your age is {age} </h1>"

if __name__ == '__main__':
    app.run(debug=True)
