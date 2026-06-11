print(10 > 5)     # greater than      → True
print(3 < 2)      # less than         → False
print(7 == 7)     # equal to          → True
print(7 != 4)     # not equal to      → True
print(5 >= 5)     # greater or equal  → True
print(8 <= 3)     # less or equal     → False

temperature = 35

if temperature > 30:
    print("It's hot today!")
    print("Drink water.")

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("Too young to vote.")

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


print("--- Grade Calculator ---")

marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: " + grade)

print("--- Even or Odd ---")

number = int(input("Enter a whole number: "))

if number % 2 == 0:
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")
