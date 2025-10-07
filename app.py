from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle')
def area_of_a_circle():
    return render_template('areaofacircle.html')

@app.route('/areaOfTriangle')
def area_of_a_triangle():
    return render_template('areaofatriangle.html')

if __name__ == "__main__":
    app.run(debug=True)
