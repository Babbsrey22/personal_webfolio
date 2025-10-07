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

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_of_a_circle():
    area = None
    if request.method == "POST":
        try:
            radius = float(request.form['radius'])
            area = 3.14159 * (radius ** 2)
        except:
            area = "Invalid input. Please enter a valid number ~"
    return render_template('areaofacircle.html', area=area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def area_of_a_triangle():
    area = None
    if request.method == "POST":
        try:
            base = float(request.form['base'])
            height = float(request.form['height'])
            area = 1/2 * base * height
        except:
            area = "Invalid input. Please enter a valid number ~"
    return render_template('areaofatriangle.html', area=area)

if __name__ == "__main__":
    app.run(debug=True)
