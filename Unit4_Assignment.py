''' Connor Fisher IT244 Python Programming
	Unit 4 Assignment Created 20220224
'''
#Program for selecting ice cream choices with gone size and price.
#Inital variables,lists, dictionary set up.
flavorList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]
conePrices = {"S":"$1:50", "M":"$2.50", "L": "$3.50"}
coneSizes= {"S":"smallish", "M":"more for me", "L":"lotta lickin"}

#This section is where I changed the one of the list index variables and added an additional index variable.
flavorList[3] = "Peach"
flavorList.append("Cookies and Cream")
flavorList.sort()
flavorNum = len(flavorList)

#This section is the introduction to the program and provides the basic information.
print("\nWelcome to The Ice Creamery!\n")
print("We have a total of", flavorNum, "flavors we are serving today at The Ice Creamery.\n")

#Here prints a list of flavors and the number of flavors.
#I had an slight issue here, I forgot how you printed the number then the flavor.
#I looked up solutions to include the one you demonstrated on the planet demonstration.
#Second solution I found was for index, flavor in enumerate(flavorList): print(index + 1, flavor)
for flavor in flavorList:
    print(flavorList.index(flavor) + 1, flavor)

#Input of customers choices comes in here. 
#Used the upper function to makes sure the choice would be recognized during the print statement if they input a lowercase.
#Implemented range in the second if to simplify the statement. 
customerSize = input("\nPlease enter a cone size you would like (S, M, L): ")
customerSize = customerSize.upper()
if customerSize == "S" or customerSize == "M" or customerSize == "L":
    customerFlavor = input("\nPlease enter your flavor number: ")
    try:
        customerFlavor = int(customerFlavor)
    except:
        print()
#Added the try/except to kick out any input that wasnt an integer. I used a print() instead of having two error messages appear. 
    if customerFlavor in range(1,8):
        print("\nYour total is:", conePrices[customerSize])
        print("\nYour", coneSizes[customerSize], "sized cone of The Ice Creamary's", flavorList[customerFlavor - 1 ], "will arrive shortly.")
    else:
        print("\nYou did not enter a valid flavor number. Please try again.")
else:
    print("\nYou entered an invalid cone size. Please try again.")
print("\nThank you for visiting The Ice Creamery!")
