def main():
    print("Enter 1 to convert from Celsius to Fahrenheit")
    print("Enter 2 to convert from Fahrenheit to Celsius")
    choice = int(input("Select 1 or 2: "))

    # while statement before if else statement
    while choice == 1 or choice == 2:
        if choice == 1:
            temp_c = float(input("Enter temperature in Celcius: "))
            temp_f = celsius_to_fahrenheit(temp_c)
            print("%.2f Celsius = %.2f Fahrenheit" % (temp_c, temp_f))
        else:
            temp_f = float(input("Enter temperature in Fahrenheit: "))
            temp_c = fahrenheit_to_celsius(temp_f)
            print("%.2f Fahrenheit = %.2f Celsius" % (temp_f, temp_c))

        print("\nEnter 1 to convert from Celsius to Fahrenheit")
        print("Enter 2 to convert from Fahrenheit to Celsius")
        choice = int(input("Select 1 or 2: "))
    print("STOP!!")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

main()