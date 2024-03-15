height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/(height ** 2)
print("Your Body Mass index is: ", bmi)

if (bmi > 0):
    if (bmi < 18.5):
        print("You are Underweight.")
    elif (18.5 < bmi < 25):
        print("You are Healthy.")
    elif (25 <= bmi < 30):
        print("You are Overweight.")
    else:
        print("You are obese.")
else:
    print("Please enter valid details.")