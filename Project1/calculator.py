def calculate():
    operation = input('''
Please type in the math operation you would like to complete:  
+ for addition
- for subtraction
* for multiplication
/ for division
''') #This allows the user to specify which operation they would like to use for their calcuation
            
    score_1 = int(input('Please enter the first Score: '))  #User input for their first score
    score_2 = int(input('Please enter the second Score: ')) #User input for their second score

    if operation == '+':
        print('{} + {} = '.format(score_1, score_2))   # First operation - addition - adds the two inputs
        print(score_1 + score_2)

    elif operation == '-':
        print('{} - {} = '.format(score_1, score_2))  # Second operation - subtraction - subtracts the two inputs
        print(score_1 - score_2)

    elif operation == '*':
        print('{} * {} = '.format(score_1, score_2))  # Third operation - multiplication - multiplies the two scores
        print(score_1 * score_2)

    elif operation == '/':
        print('{} / {} = '.format(score_1, score_2))  # Fourth operation - division - divides the two inputs
        print(score_1 / score_2)

    else:
        print('You have not typed a valid operator, please run the program again.')  #This is an error message that displays if the user does not specify a valid operation (+, -, *, /)

    # Add again function to calculate function
    again()

def again():
    calc_again = input('''
Do you want to calculate another score again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Thanks for using my score calculator!')  #Allows the user to choose whether they would like to make another calculation
    else:
        again()

calculate()

####### CODE CITATION ######
    #This is Python based Score Calculator 
    # Credit for this code - https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
    # I have changed the function of this calculator - it is now meant to be used as a scoring calculator -- Have a game that you need to keep score in?  Use this calculator to quickly calculate your score from your game!
    #Comments are created by Ryan McConnell
