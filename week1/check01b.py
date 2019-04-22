firstname = input("Please enter your name: ")
currentAge = input("Please enter your age: ")

print("\nHello %s, you are %s years old." % (firstname, currentAge))
print("On your next birthday, you will be %d." % (int(currentAge) + 1))