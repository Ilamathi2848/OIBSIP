# BMI Calculator

def calculate_bmi(weight, height):
    """Calculate the BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Prompt user for weight and height
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    category = classify_bmi(bmi)
    
    # Display result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
