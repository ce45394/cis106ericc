def trip_info(miles, gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost

total_miles = 0
total_cost = 0
count = 0

while True:
    answer = input("Do you want to enter a trip (Yes or No)? ").lower()
    if answer != "yes":
        break

    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg, cost = trip_info(miles, gallons)

    total_miles += miles
    total_cost += cost
    count += 1

    print("City:", city)
    print("Miles:", miles)
    print("MPG:", format(mpg, ".2f"))
    print("Gas Cost:", format(cost, ".2f"))
    print()

print("Number of trips:", count)
print("Total miles:", total_miles)
print("Total gas cost:", format(total_cost, ".2f"))