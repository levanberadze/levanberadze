year = int(input("enter year: "))

if year % 2 == 1:
    print("year is odd")
else:
    print("year is even")

# Prompt the user for a year
year_to_search = int(input("Enter the year: "))

# Open the file in read mode
with open('oscars.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into fields using commas as separators
        fields = line.strip().split(',')

        # Extract information from the fields
        current_year = int(fields[0])
        actor_gender = fields[1]
        actor_first_name = fields[3]
        actor_last_name = fields[4]

        # Check if the current line corresponds to the entered year
        if current_year == year_to_search:
            # Print the first and last names of the Oscar winners for the entered year
            print(f"Oscar winners in {year_to_search}: {actor_first_name} {actor_last_name}")
            break  # Stop searching once a match is found
    else:
        # If no match is found
        print(f"No Oscar winners found for the year {year_to_search}")


























