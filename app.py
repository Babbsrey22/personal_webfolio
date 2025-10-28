from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uppercase', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areacircle', methods=['GET', 'POST'])
def area_of_a_circle():
    area = None
    if request.method == "POST":
        try:
            radius = float(request.form['radius'])
            area = 3.14159 * (radius ** 2)
        except:
            area = "Invalid input. Please enter a valid number ~"
    return render_template('areaofacircle.html', area=area)

@app.route('/areatriangle', methods=['GET', 'POST'])
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

# -------------INFIX-POSTFIX CONVERTERRRR
def infix_converter(exp):  
    exp = re.sub(r"([+\-*/^()])", r" \1 ", exp)
    exp = exp.strip()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    result = []

    for ch in exp.split():
        if ch.isalnum(): # operator
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                result.append(stack.pop())
            stack.append(ch)
    
    while stack:
        result.append(stack.pop())
    return ' '.join(result)

@app.route('/infixtopostfix', methods=['GET', 'POST'])
def infix_to_postfix():
    postfix = None
    if request.method == "POST":
        try:
            infix = request.form.get('infix', '')
            postfix = infix_converter(infix)
        except:
            postfix = "Invalid expression."
    return render_template('infixtopostfix.html', postfix=postfix)

if __name__ == "__main__":
    app.run(debug=True)
