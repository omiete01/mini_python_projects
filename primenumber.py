# this program finds the next prime number till user stops the program
# a prime number is a number that cannot be divided by any whole number except by itself
# still in progress......

def main():
    
    input("Hey there, I can find the next prime number. Try me......")
    
    while True:
        
        user_ask = input("Would you like to know the next prime number? Type 'y' for yes and 'n' for no.... ").lower()
        
        if user_ask == "y":
    
            for num in range(1, 101):
                
                for x in range(2,num):
                    
                    
                        if(num % x == 0 and num != 1):
                            break
                        else:
                            print(num,"is a prime number")
        elif user_ask == "n":
            break
                        
        
        
main()
