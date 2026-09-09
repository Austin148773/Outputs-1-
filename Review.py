#ask the user for name 
name = input("whats your name")

# greet user by name
print(f"Hello {name}!")

#ask what year they where born 
birth_year = int(input("what year where you born in?"))

#give the user their apporment age in dog years 

age = 2026 - birth_year
print (f"you are {age} years old in human years")
dog_years = age * 7 
print (f"you are {dog_years} in dog years")