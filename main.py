# Function to input height in feet
def height_feet_input():
    height_feet = float(input('Enter your height in feet.\n'))
    return height_feet

# Function to input height in inches
def height_inches_input():
    height_inches = float(input('Enter your height in inches.\n'))
    return height_inches

# Function to input weight
def weight_input():
    weight = float(input('Enter your weight.\n'))
    return weight

# Function to calculate BMI and determine BMI
def bmi_calc(height_feet, height_inches, weight):
    # BMI calculation formula
    bmi = (weight * 0.45) / ((((height_feet * 12) + height_inches) * 0.025) * (((height_feet * 12) + height_inches) * 0.025))
    
    type = "NULL"
    
    # Checking BMI and printing result
    if round(bmi, 1) < 18.5:
        print("You are underweight. BMI:", round(bmi, 1))
        type = "Underweight"
    elif 18.4 <= round(bmi, 1) <= 24.9:
        print("You are normal weight. BMI:", round(bmi, 1))
        type = "Normal"
    elif 25.0 <= round(bmi, 1) <= 29.9:
        print("You are overweight. BMI:", round(bmi, 1))
        type = "Overweight"
    elif round(bmi, 1) >= 30.0:
        print("You are obese. BMI:", round(bmi, 1))
        type = "Obese"
    
    return type

def main():

    height_feet = height_feet_input()
    height_inches = height_inches_input()
    weight = weight_input()
    
    # Calling BMI calculation function
    bmi_category = bmi_calc(height_feet, height_inches, weight)

if __name__ == "__main__":
    main()
  
