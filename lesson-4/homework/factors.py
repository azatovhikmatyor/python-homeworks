# task 3

def find_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    for factor in factors:
        print(f"{factor} is a factor of {number}")

def main():
    number = int(input("Enter a positive integer: "))
    find_factors(number)

if __name__ == "__main__":
    main()
