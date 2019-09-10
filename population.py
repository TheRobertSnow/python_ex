years=float(input("Years: "))
people = 307357870.0
new_people = 0.0
sec_year = 31536000.0
if years >= 0: #Make sure the input is valid
    born = sec_year/7 # Calculate how many people are born every year
    dead = sec_year/13 # Calculate how many people die every year
    immigrant = sec_year/35 # Calculate how many immigrate every year
    new_people = ((born + immigrant - dead)* years)+ people # Multiply added population by number of years and add current population
    print("New population after",int(years),"years is", int(new_people))
else: #If input is invalid then print('Invadlid input!')
    print("Invalid input!")
