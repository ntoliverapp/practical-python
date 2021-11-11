age = int((input("How old are you?\n")))
decade = age//10
years = age % 10
response = "You are " + str(decade) + " decades and " + str(years) + " years old."
print(response)