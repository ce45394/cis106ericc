def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total = total * 0.90
    return total

sum_total = 0

while True:
    answer = input("Do you want to enter data (Yes or No)? ").lower()
    if answer != "yes":
        break

    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = compute_total(qty, price)
    sum_total += total

    print("Quantity:", qty)
    print("Price:", price)
    print("Total:", format(total, ".2f"))
    print()

print("Sum of all totals:", format(sum_total, ".2f"))