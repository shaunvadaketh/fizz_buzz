import sys

if len(sys.argv) > 1:
    n = sys.argv[1]
else:
    n = input("Please enter a number: ")
    
while True:
    try:
        int(n)
        break
    except ValueError:
        n = input("You didn't enter an integer. Please enter an integer for the upper limit. ")

n = int(n)
print("Fizz Buzz counting up to {}".format(n))
for number in range(1, n+1):
    if number % 3 == 0 and number % 5 == 0: 
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)