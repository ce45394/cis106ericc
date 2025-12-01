def batting_average(hits, at_bats):
    return hits / at_bats

count = 0

while True:
    answer = input("Do you want to enter a player (Yes or No)? ").lower()
    if answer != "yes":
        break

    name = input("Enter last name: ")
    hits = int(input("Enter hits: "))
    at_bats = int(input("Enter at bats: "))

    avg = batting_average(hits, at_bats)
    count += 1

    print("Player:", name)
    print("Batting Average:", format(avg, ".3f"))
    print()

print("Number of players entered:", count)