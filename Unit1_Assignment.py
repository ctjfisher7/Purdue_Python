''' Connor Fisher IT244 Python Programming
	Unit 1 Assignment Created 20220204
'''
#First primary way of completing the assignment.
string1 = " Python was created in the 1890's by Guido van Rossum. "
string2 = " Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "
string3 = " He is affectionately known as Python's \"Benevolent Dictator for Life\". "
print(string1.replace("1890", "1990").strip(), string3.strip(), string2.strip())


#Secondary way of completing assignment
string4 = string1.replace("1890", "1990").lstrip() + string3.strip() + string2.rstrip()
print(string4)
#Could also leave string1 & string2 with no strip to get "same results" (if not counting the index/spaces)
#Question for professor - In C++ you can put an array or vector inside another vector/array to make a matrix, can you do the same in python with lists and Arrays?
