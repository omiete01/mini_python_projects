# reverse words in a text file and stores it in a new file
 
import sys

def main():    
    
    if len(sys.argv) < 3:
        sys.exit("Too few commandline arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many commandline arguments")
    
    if not(sys.argv[1].endswith(".txt")):
        sys.exit("Please use a text file.")
        
    reverse_file(sys.argv[1], sys.argv[2])
 
    
def reverse_file(file1, file2):   
    
    try:
        list = []
        
        with open (file1, "r") as file:
        
            read = file.readlines()
            
            for lines in read:
                reverse = "".join(lines[::-1])
                list.append(reverse)
                
        with open (file2, "w") as file:
            for line in list:
                file.writelines(f"{line}")
                
    except FileNotFoundError:
        sys.exit(f"Can't find {file1}")              
    
    
main()