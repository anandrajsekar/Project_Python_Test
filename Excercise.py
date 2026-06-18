# BMI Calculator 
# BMI = weight/(height^2)

# The BMI Should be classified as follows:
# Underweight - BMI under or equal to 18.5
# Normal - BMI Between 18.5 and 25 (not included 18.5 but included 25)
# Overweight - BMI between 25 and 30 ( not included 25 but included 30)
# Obese - BMI greater than 30

# Output: Your BMI is '{BMI Value}'. You are '{classified}'

Weight = int(input("Emter Your Weight in Kg : "))
Height = float(input("Enter Your Height in Cm : "))/100
BMI = float(Weight/(Height**2))

if BMI <= 18.5:

    print(f"Your Weight (Kg) is : '{Weight}', Your Height (m) is : '{Height}' and Your BMI is : '{BMI}'. You are in Underweight")

elif 18.5 < BMI <= 25:

    print(f"Your Weight (Kg) is : '{Weight}', Your Height (m) is : '{Height}' and Your BMI is : '{BMI}'. You are in Normal")

elif 25 < BMI <= 30:
    
    print(f"Your Weight (Kg) is : '{Weight}', Your Height (m) is : '{Height}' and Your BMI is : '{BMI}'. You are in Overweight")

else:

    print(f"Your Weight (Kg) is : '{Weight}', Your Height (m) is : '{Height}' and Your BMI is : '{BMI}'. You are in Obese")