# program to convert words to piglatin
# not complete yet

def main():
    userinput = input("Type a word: ")
    
    for word in userinput.split():
        vowels = "aeiou" 
        
        if word.startswith(vowels): 
            print(f"{word}hay")
        
        # elif word[0] not in n:
        #     print(f"{word[1:]}{word[0]}ay ", end="")
        
        elif word[0:2] not in vowels:
            print(f"{word[2:]}{word[:2]}ay ", end="")
            # print(word[0:2])
            
        elif word[0] not in vowels:
            print(f"{word[1:]}{word[:1]}ay ", end="")
            
            
    
main()
