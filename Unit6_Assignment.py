'''Connor Fisher IT244 Python Programming Purdue
    Unit 6 Assignment created 20220310'''
#Program that calculates the temperature in Celsius or Fahrenheit.
#Here is the functions that calcuates the temperatures.
#Added the round function due to some temperatures being repeating.
def converTemp(tempScale, temps):
    if(tempScale.upper() == 'F'): 
        temps[1] = round(((temps[0] - 32) * 5/9),1)
    elif(tempScale.upper()== 'C'):
        temps[0]= round(((temps[1] * 9/5) + 32),1)
    return(temps)
#Initial input variables and list.
tempValue = float(input('\n\nEnter a temperature value: '))
tempScale = input('\nEnter a letter to indicate the temperature scale (C or F): ')
temps = [0,0]
#Portion where input temp assigned to the list at designated index.
if(tempScale.upper()== 'F'):
    temps[0] = tempValue
elif(tempScale.upper() == 'C'):
    temps[1] = tempValue
#Calling of the function.
converTemp(tempScale, temps)
#Print statements for the temperatures.
print('\n\nYou entered', tempValue, 'degrees', tempScale.upper()+'.')
print('\nThe temperature in Celsius is: ',temps[1])
print('\nThe temperature in Fahrenheit is: ', temps[0],'\n')
#Additional notes - had to use trial and error to find the right position to use the round func.
#Attempted this at the if/elif statement variable declaration *round(temps[],1)*
#Could have made tempScale redeclared with .upper() rather than continuiously using .upper()
#Tried to build the program different w/ having the func append to list but wasnt able to get it to work. 
