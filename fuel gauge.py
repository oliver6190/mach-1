def main():
    final_fuel = get_percentage()
    final_fuel = round(final_fuel * 100)
    if final_fuel <= 1:
        print("E")
    elif final_fuel >= 99:
        print("F")
    else:
        print(f"{final_fuel}%")


def get_percentage():
    try:
        while True:
            fraction = input("enter fuel :  ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            fuel_in_the_tank = x / y
            if fuel_in_the_tank <= 1:
                return fuel_in_the_tank
    except ValueError and ZeroDivisionError:
        print("enter a fraction:  ")


main()
