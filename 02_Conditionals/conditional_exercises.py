# Exercise one.
# Write a code that asks for input between 1 and 5, the code will take the integer value and print out the string value. 

# user_input = int(input('please input a selection between 1 and 5 >> '))

# if user_input == 1:
#     print("One")
# elif user_input == 2:
#     print("Two")
# elif user_input == 3:
#     print("Three")
# elif user_input == 4:
#     print("Four")
# elif user_input == 5:
#     print("Five")
# else:
#     print("selection out of range, Try again between 1 and 5")


# Exercise two.
# Repeat the previous task but this time the user will input a string and the 
# code will ouput the integer value. Convert the string to lowercase first.

# user_input_2 = str(input('Please input selection between one and five in words, please!>>  ')).lower()

# if user_input_2 == 'one':
#     print(1)
# elif user_input_2 == 'two':
#     print(2)
# elif user_input_2 == 'three':
#     print(3)
# elif user_input_2 == 'four':
#     print(4)
# elif user_input_2 == 'five':
#     print(5)
# else:
#     print('Out of range, try again!')


# Exercise three.
# Create a variable containing an integer between 1 and 10, ask user to guess and if too low, they lost, if too high they won.

secret_number = 5

guess_number = int(input('Please enter a selection between 1 and 10 >>  '))

if guess_number == secret_number:
    print("You guessed the correct number!")
elif guess_number > secret_number and guess_number <=10:
    print("Number too high, try again")
elif guess_number < secret_number and guess_number >=1:
    print("Entry too low, try again")
else:
    print("Out of range")


# Exercise Four.
