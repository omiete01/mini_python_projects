
def main():
    
    # reverse words input by a user
    userinput = input("Type a word: ").lower()
    count = userinput[::-1]
    print(count)
    
main()   

''' Slice notation takes the form [start:stop:step]. In this case, we omit the start and stop positions 
since we want the whole string. We also use step = -1, which means, "repeatedly step from right to left by 1 character".'''