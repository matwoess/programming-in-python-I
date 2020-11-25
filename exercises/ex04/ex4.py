"""
ex4.py
Author: Mathias Wöß
Matr.Nr.: K11709064
Exercise 4
"""

#
# Start of code block that should not be modified.
#

# The next 3 lines will ask the user for input through the console and set the variables var1 and var2
# to the input the user typed in the console. These values will be of datatype string, so if you want to do
# numerical computations  with them, you will need to convert them to the datatype int or float. See the assignment
# sheet for more details.
datatype = input('Select a datatype (type "int", "float" or "string" and hit enter) for var1:')
var1 = input('Enter var1:')
var2 = input('Enter var2:')
result = None  # This variable should be overwritten with the result of your operation later.

#
# End of code block that should not be modified.
#

# Place your code here. Store the result in the variable "result".
if datatype == 'int':
    result = int(var1) * int(var2)
elif datatype == 'float':
    result = float(var1) * int(var2)
elif datatype == 'string':
    result = var1 * int(var2)
else:
    raise TypeError(f'unsupported data type "{datatype}"')

#
# Do not modify the code below this line.
#

# This will print the result to the console.
print(f"Result: {result}")
