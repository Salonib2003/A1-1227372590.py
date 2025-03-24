@author: SALONI BANSAL
@email: sbansa46@asu.edu

# Answer to Question 1 
int1 = 10
int2 = 20
float1 = 30.5

results1 = int1 + int2 + float1

print(results1)  
print(type(results1))  

# Answer to Question 2
string1 = """This is a longer string
that spans multiple lines"""

count_s = string1.count('s')
print(count_s) 

# Answer to Question 3
import math
var1 = math.pi
rounded_var1 = round(var1, 3)
print(rounded_var1)  

# Answer to Question 4
var1 = int(input('Enter a var1 number: '))
var2 = int(input('Enter a var2 number: '))
var3 = var1 * var2

print('')
print('The result of multiplying var1 and var2 is:', var3)

# Answer to Question 5
numerator1 = '32000'
denominator1 = '1000'

float_result = float(int(numerator1) / int(denominator1))
print(float_result) 

# Answer to Question 6
year = 1991
author = 'Guido van Rossum'
text1 = f"Python is a general-purpose programming language released in {year} by {author}"
print(text1)

# Answer to Question 7
sunny = True
warm = False

print('Is it True or False that I should go out for ice cream?:', (sunny and warm))

# Answer to Question 8
from datetime import datetime, timedelta

dt = datetime(2021, 9, 6, 18, 51, 17)
dt2 = dt - timedelta(weeks=4)

dt2_str = dt2.strftime('%m/%d/%Y')
print('dt2_str date is:', dt2_str) 
