def compute_pay(job_code, hours):
    if job_code == "L":
        rate = 25
    elif job_code == "A":
        rate = 30
    elif job_code == "J":
        rate = 50
    else:
        rate = 0

    if hours > 40:
        gross = 40 * rate + (hours - 40) * (rate * 1.5)
    else:
        gross = hours * rate

    return rate, gross

total_gross = 0

while True:
    answer = input("Enter employee (Yes or No)? ").lower()
    if answer != "yes":
        break

    name = input("Enter last name: ")
    code = input("Enter job code (L/A/J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate, gross = compute_pay(code, hours)
    total_gross += gross

    print("Name:", name)
    print("Hours:", hours)
    print("Rate:", rate)
    print("Gross Pay:", format(gross, ".2f"))
    print()

print("Total of all gross pay:", format(total_gross, ".2f"))