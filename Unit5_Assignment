''' Connor Fisher IT244 Python Programming
	Unit 5 Assignment Created 20220305
'''
#Program that processes pormotional credits for customers.
#Defining of the variables.
recordCount = 0
recordsList = []
# Defining of the file handle.
#Spent more time trying to figure out why this portion wasn't working than the entire program. 
#Wasnt working with just IT244_U5_Data.txt even though both program and file were in the same folder. 
infoFile = open('/home/cfish/Documents/Purdue/Python/IT244_U5_Data.txt', 'r')
#Loop to access each record and closing of file
for info in infoFile:
	recordsList.append(info.strip())

infoFile.close()
#Added the new customer to the infoFile
recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")
#Creating and writing to the .csv file. 
#Added the header for the record. (DONT FORGET THE w !!!)
infoFile = open("IT244_U5_PromoCredit.csv", 'w')
infoFile.write("Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n")
#Working through the records list with a loop and adding the promo credit.
for record in recordsList:
	infoFile.write(record)
	infoFile.write(", $500\n")
	recordCount = recordCount + 1

infoFile.close()
#Print statement of the records counts
print("\n\nThere are ", recordCount," written to the promo credits.\n" )
