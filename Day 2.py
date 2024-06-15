print("Welcome to the tip calculator")
total = float(input("What was the total bill??\n"))
tip = int(input("How much tip would you like to give?? 10%, 15% or 20%??\n"))
people = float(input("How many people to split the bill?\n"))

split = total / people

tip_percentage = tip/100

total_tip =  total * tip_percentage

total_bill = total_tip + total_tip

cut = split + total_tip/people

print(f"Each person should pay :")
print(f"{cut:.2f}")