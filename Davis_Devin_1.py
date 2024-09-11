# Devin Davis
# COT5480
# PID 3921337
# 8/31/2024
# de545945@ucf.edu
# For this week's assignment, I was to print dictionary statements and run them with the correct codes using the lists keys and values.

keys = ['GOOGL', 'META', 'MSFT']

values = [109, 157, 263]

# Prints out the dictionary that is converted from those two lists above.
# Comment: This code was used to print and convert keys and values together resulting in {'GOOGL': 109, 'META': 157, 'MSFT': 263}.
dictionary = dict(zip(keys, values))
print(dictionary)

# Prints out the length of the dictionary.
# Comment: The goal was to find the length of the dictionary that was created which is 3.
print(len(dictionary))

# Prints out all the keys.
# Comment: This code was created to only print keys and not include values ['GOOGL', 'META', 'MSFT'].
print(keys)

# Prints out the dictionary after deleting the key GOOGL.
# Comment: This code the dictionary after deleting GOOGL from it resulting in {'META': 157, 'MSFT': 263}.
del dictionary['GOOGL']
print(dictionary)

# Prints True or False if META is in the dictionary.
# Comment: Because META is in the dictionary, the code was created to show as True in the results.
print('META' in dictionary)

# Prints the dictionary after adding another value. "AAPL": 158.
# Comment: AAPL and 158 as new keys and values in dictionary were added in the code resulting with {'META': 157, 'MSFT': 263, 'AAPL': 158}.
dictionary['AAPL'] = 158
print(dictionary)

# Prints the minimum value from the dictionary (Hint: use built-in min() function).
# Comment: The built-in min() function code was used to find the minimum value from the dictionary resulting with 157.
print(min(dictionary.values()))