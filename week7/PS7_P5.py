def compute_tuition(credits, code):
    if code == "I":
        return credits * 250
    else:
        return credits * 550

total_tuition = 0

while True:
    answer = input("Do you want to enter a student (Yes or No)? ").lower()
    if answer != "yes":
        break

    name = input("Enter last name: ")
    credits = int(input("Enter credit hours: "))
    code = input("Enter district code (I/O): ").upper()

    tuition = compute_tuition(credits, code)
    total_tuition += tuition

    print("Student:", name)
    print("Tuition Owed:", format(tuition, ".2f"))
    print()

print("Total Tuition Owed:", format(total_tuition, ".2f"))