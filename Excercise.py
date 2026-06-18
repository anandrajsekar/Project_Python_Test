# BMI Calculator 
# BMI = weight/(height^2)

# The BMI Should be classified as follows:

# Underweight - BMI under or equal to 18.5

# Output : Your Weight (Kg) is : '72', Your Height (m) is : '2.0' and Your BMI is : '18.0'. You are in Underweight

# Normal - BMI Between 18.5 and 25 (not included 18.5 but included 25)

# Output : Your Weight (Kg) is : '72', Your Height (m) is : '1.9' and Your BMI is : '19.94459833795014'. You are in Normal

# Overweight - BMI between 25 and 30 ( not included 25 but included 30)

# Output : Your Weight (Kg) is : '72', Your Height (m) is : '1.6' and Your BMI is : '28.124999999999993'. You are in Overweight

# Obese - BMI greater than 30

# Output : Your Weight (Kg) is : '72', Your Height (m) is : '1.5' and Your BMI is : '32.0'. You are in Obese

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