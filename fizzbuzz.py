# this program prints numbers from 1 to user input number
# prints "Fizz" for multiples of 3, "Buzz" for multiples of 5 and "FizzBuzz" for multiples of both 5 and 3

def main():
    
    userinput = int(input("Enter a number: "))
    
    for number in range(1, userinput + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{number} ", end="")
        
main()
