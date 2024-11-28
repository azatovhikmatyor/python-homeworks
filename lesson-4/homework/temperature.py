# task 1

def convert_cel_to_far(celsius):
    return round(celsius * 9 / 5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)

def main():
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius_converted = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius_converted} degrees C")

    celsius = float(input("\nEnter a temperature in degrees C: "))
    fahrenheit_converted = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit_converted} degrees F")

if __name__ == "__main__":
    main()
