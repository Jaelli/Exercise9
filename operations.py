
var = input("Please enter a value: ")

print(var.upper())

print(len(var))

print(var.isnumeric())

containsNumbers = any(var.isdecimal()for var in var)
print("Does the input contain any numeric characters?", containsNumbers)
