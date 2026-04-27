valid = "loop"

while (valid != "exit"):
    a = input("Enter score:")

    try :
        a = float(a)
        valid = True
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if a>=90:
    print("Grade: A")
elif a>=80:
    print("Grade: B")
elif a>=70:
    print("Grade: C")
elif a>=60:
    print("Grade: D")
else:    print("Grade: F")

