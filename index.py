print ("hello world")
print ("we are learning git")

def fahrenheit_to_celsius(fahrenheit):
     celsius = (fahrenheit - 32) * 5/9
     return celsius

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
