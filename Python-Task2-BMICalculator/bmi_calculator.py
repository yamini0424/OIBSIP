try:
 Weight=float(input("Enter Your Weight(kg):"))
 Height=float(input("Enter Your Height(m):"))
 if (Weight <= 0 or Height <= 0.5):
    print("Weight should be greater than 0 and Height should be grater than 0.5")
 else:
    bmi=Weight/(Height**2)
    print(f"Your bmi is {bmi:.2f}")
    if (bmi < 18.5):
      print("Underweight")
    elif (bmi < 25):
      print("Normal Weight")
    elif (bmi < 30):
      print("Overweight")
    else:
      print("Obese")
except ValueError:
  print("Invalid input! Please enter numeric values only.")
