#variables are passed through functions

def hello():
    print("Hello World!")

hello()

def user_name(name):
    print(f'Hello, {name}')

user_name('ugo')

# Key word argument
def user_name_2(name = 'input name, please!'):
    print(f'Hello, {name}')

user_name_2()

# Fibonacci sequence in a function
def fib(n):
    """Calculates and returns the nth fibonacci number"""
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
    return a
fib_num = fib(20)
print(fib_num)

for i in range(20):
    print(fib(i))


# Function to calculate average of numbers

def calc_mean(first, *remainder):
    """This calculates the mean of numbers"""
    mean = (first + sum(remainder))/(1+len(remainder)) 
    return mean


print(calc_mean(23,344, 34, 1, 22, 65, 76, 344, 677, 555))



# Step 1: Define the calculate_mean function
def calculate_mean(first, *remainder):
  if first is None and not remainder:
    print('No values provided')
    return
  mean = (first + sum(remainder))/(1+len(remainder))
  return mean
  
# Step 2: Test the function
mean = calculate_mean(10, 20, 30)
print("The mean of 10, 20, 30 is:", mean)

mean = calculate_mean(5, 15, 25, 35, 45)
print("The mean of 5, 15, 25, 35, 45 is:",mean)