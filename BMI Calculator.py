#BMI = (weight in pounds *703) / (height in inches **)
name = input("Enter your name: ").capitalize()
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
BMI = (weight * 703) / (height ** 2)
print(BMI)
if BMI > 0:
    if (BMI<=18.5):
        print(name + " You are underweight.")
    elif (BMI<=24.9):
        print(name +" You are normal weight.")
    elif (BMI<=29.9):
        print(name +" You are overweight.")
    elif (BMI<=34.9):
        print(name +" You are obese.")
    elif (BMI<=39.9):
        print(name +" You are severely obese.")
    else:
        print(name + " You are morbidly obese.")
else:
    print("Enter valid input")


