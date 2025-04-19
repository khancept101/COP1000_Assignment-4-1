"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.0
# Number of characters.
numChars = int(input("Enter the number of characters: "))
# Color of characters.
color = input("Enter the color of the characters: ")
# Type of wood.
woodType = input("Enter the type of wood: ")

# Write assignment and if statements here as appropriate.
if numChars > 5:
    extra = numChars - 5
    charge += extra * 4.0

if woodType.lower() == "oak":
    charge += 20.0

if color.lower() == "gold":
    charge += 15.0
    
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
