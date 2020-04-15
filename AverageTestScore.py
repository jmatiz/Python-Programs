import math
import turtle

count = 0
NEWCASE = 'y'
test = []
total_testscore = 0
count_category2 = 0
test_category2 = []
total_testscore_category2 = 0

while NEWCASE == 'y':
    
    test_input = float(input('Enter a test score : '))

    if test_input < 0 or test_input > 100:
        print("That is not a valid test score, please try again")

    else:
        if test_input > 80 and test_input < 90:
            count_category2 = count_category2 + 1
            test_category2.append(test_input)
        
        test.append(test_input)
        
        count = count + 1
    
        NEWCASE = input('Would you like to input another test score? y for yes, n for no: ')


for x in test:
    total_testscore = total_testscore + x


average_testscore = total_testscore/count

print('Your test score average is ', average_testscore)

for x in test:
    turtle.write(x)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()





