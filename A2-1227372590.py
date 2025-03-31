@AUTHOR: [Saloni Bansal]
@EMAIL: [sbansa46@asu.edu]

# Answer to Question 1
for num in range(2, 27, 2): 
    print (f "Generated number: {num}")

# Answer to Question 2
for i in range(3, 0, -1):
    for j in range(1001, 1006):
        print(f "{i};{j}")

# Answer to Question 3
input1 = int(input('Enter an integer number: '))
if input1 < 0:
    print("Input1 is negative")
elif input1 == 0:
    print("Input1 is zero")
elif input1 <= 20:
    print("Input1 is positive but less than or equal to 20")
else:
    print("Input1 is greater than 20")

# Answer to Question 4
j = 0
sum11 = 0
while j < 10:
    sum11 = j * 11 + sum11
    print(f"j: {j} sum11: {sum11}")
    j += 1
print('')
print('Total sum11 is:', sum11)

# Answer to Question 5
historical = (3, 5, 1, 9, 0, 3, 9, 2, 4, 7)
predictiona = (1, 5, 4, 1, 7, 7, 1, 0, 3, 9)
predictionb = (6, 0, 4, 3, 4, 4, 8, 4, 3, 7)
print('')
print('historical:', historical)
print('predictiona:', predictiona)
print('predictionb:', predictionb)
print('')
topresults = zip(historical, predictiona, predictionb)
for h, p1, p2 in topresults:
    print(f'historical: {h} prediction a: {p1} prediction b: {p2}')

# Answer to Question 6
btcdec1 = [11234, 12475]
btcdec1.append(14560)
btcdec2 = []
btcdec2.append(15630)
btcdec2.append(12475)
btcdec2.append(14972)
btcdec1.extend(btcdec2)
btcdec1.sort()
print(btcdec1)

# Answer to Question 7
list1 = [-4, 2, 7, -6, 3, -5, 8, 10, 4, -10]
list2 = [1, 7, 8, -10, 2, 6, -1, 10, -3, -8]
cnt = 0
for item in list1:
    if item in list2:
        cnt += 1
print('Number of common items between list1 and list2 is:', cnt)

# Answer to Question 8
numbers = [0.1, 0.2, 0.3, 0.4, 0.5]
# Arithmetic Mean
arithmetic_mean = sum(numbers) / len(numbers)
# Geometric Mean
from math import prod
geometric_mean = prod([1 + x for x in numbers]) ** (1/len(numbers)) - 1
print(f"Arithmetic Mean: {arithmetic_mean}")
print(f"Geometric Mean: {geometric_mean}")
