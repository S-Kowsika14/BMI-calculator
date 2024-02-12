def calculate_bmi(weight, height, unit_system):
    if unit_system == 'metric':
        bmi = weight / (height ** 2)
    elif unit_system == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    return bmi

def get_health_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'

def main():
    try:
        unit_system = input("Choose unit system (metric/imperial): ").lower()
        if unit_system not in ['metric', 'imperial']:
            raise ValueError("Invalid unit system. Please choose either 'metric' or 'imperial'.")

        weight = float(input("Enter your weight in {} units: ".format('kg' if unit_system == 'metric' else 'lbs')))
        height = float(input("Enter your height in {} units: ".format('meters' if unit_system == 'metric' else 'inches')))

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height, unit_system)
        health_category = get_health_category(bmi)

        print("Your BMI is: {:.2f}".format(bmi))
        print("Health Category: {}".format(health_category))

    except ValueError as ve:
        print("Error:", ve)

if_name_ == "_main_":
    main()
