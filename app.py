from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height_feet = float(request.form['height_feet'])
    height_inches = float(request.form['height_inches'])
    weight = float(request.form['weight'])
    bmi_value, bmi_category = bmi_calc(height_feet, height_inches, weight)
    return render_template('result.html', bmi_value=round(bmi_value, 2), bmi_category=bmi_category)

def bmi_calc(height_feet, height_inches, weight):
    bmi = (weight * 0.45) / ((((height_feet * 12) + height_inches) * 0.025) * (((height_feet * 12) + height_inches) * 0.025))
    if round(bmi, 1) < 18.5:
        category = "Underweight"
    elif 18.5 <= round(bmi, 1) <= 24.9:
        category = "Normal"
    elif 25.0 <= round(bmi, 1) <= 29.9:
        category = "Overweight"
    elif round(bmi, 1) >= 30.0:
        category = "Obese"
    return bmi, category

if __name__ == "__main__":
    app.run(debug=True)
