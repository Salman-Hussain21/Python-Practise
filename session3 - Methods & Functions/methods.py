#in built functions
# print('Hi there!')  # Print
# print(input('Your Name: '))

#Methods
# print('Salman'.upper()) #uppercase
# print('Salman'.lower()) #lowercase
# print('Salman'.capitalize()) #capitalize
# print('Salman'.replace('S', 'P')) #replace
# print('Salman'.count('a')) #count
# print(len('Salman')) #length using built in function

#other functions
# print(abs(-10)) #absolute value
# print(round(12.56)) #rounding
# print(max(10, 20, 5, 30)) #maximum
# print(min(10, 20, 5, 30)) #minimum
# print(pow(2, 3)) #power
# print(sum([80, 20, 30])) #sum of iterable
# print(sorted([5, 2, 9, 1])) #sorting


#pthagroras theorem function
side_a = int(input('Width: '))
side_b = int(input('Height: '))
hyp = (pow(side_a, 2) + pow(side_b, 2) ) ** 1/2

print('Hypotenuse is: ', hyp)