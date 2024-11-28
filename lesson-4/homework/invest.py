# task 2

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"Year {year}: ${amount:.2f}")


def main():
    principal = float(input("Enter the initial amount: "))
    rate = float(input("Enter the annual rate of return (as a decimal): "))
    years = int(input("Enter the number of years: "))

    print("\nInvestment growth:")
    invest(principal, rate, years)


if __name__ == "__main__":
    main()
