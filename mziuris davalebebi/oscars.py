user_input = input("shemoiyvane weli: ")
with open("oscars.txt", "r") as file:
    for line in file:
        a = line.split(",")

        year = int(a[0])
        gender = a[1]
        name_surname = a[2]
        film = a[3]

        if year == user_input:
            print()





